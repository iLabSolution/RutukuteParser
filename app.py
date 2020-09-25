from flask import Flask, render_template, request
from functions import parser
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# start url
urlr = "https://www.obozrevatel.com/googlenews.xml"

app = Flask(__name__)


# Url input class
class urlForm(FlaskForm):
    url = StringField('url')
    parse = SubmitField('parse')


# Parser
@app.route("/", methods=["GET", "POST"])
def template():
    form = urlForm()
    if form.is_submitted() and validators:
        url = request.form.get("url")
        # try open url (check is input == url)
        try:
            return render_template("template.html", form=form, newsList=parser.getXMLNews(url))
        except:
            print("Error")
    # start page
    return render_template('template.html', form=form, newsList=parser.getXMLNews(urlr))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request,  url_for, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask("__name__")
app.config["SECRET_KEY"] == "Hima"

@app.route("/", methods = ['GET', 'POST'])
def reverse():
    if request.method == 'POST':
        s = request.form['string']
        reversed_s = reverse_string(s)
        return '''
                <h1>Reverse String</h1>
                <p>Original string: {}</p>
                <p>Reversed string: {}</p>
            '''.format(s, reversed_s)
    else:
        return '''
                <form method="post">
                    <label for="string">Enter a string:</label>
                    <input type="text" id="string" name="string">
                    <input type="submit" value="Reverse">
                </form>
            '''

def reverse_string(s):
    return s[::-1]



if __name__ == '__main__':
    app.run(debug=True)
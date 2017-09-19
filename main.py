from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form_html="""
<!DOCTYPE html>
<html>

    <head>
        <title>Web Caesar</title>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>

    <body>
        <form action="/caesar" method="POST">
            <p> Rotate by: <input type="text" name="rot" value="0"></p>
            <textarea name="text"></textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>

</html>

"""

new_caesar = """
<!DOCTYPE html>
<html>

    <head>
        <title>Web Caesar</title>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0; 
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>

    <body>
        <form action="/caesar" method="POST">
            <p> Rotate by: <input type="text" name="rot" value="0"></p>
            <textarea name="text">{new_text:s}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>

</html>

"""

response_html = """
<!DOCTYPE html>
<html>

<head>
<title></title>
</head>

<body>
    <h1>Code {new_text:s}</h1>
</body>

</html>

"""

@app.route("/caesar", methods=['POST'])
def caesar():
    text = request.form['text']
    rot = int(request.form['rot'])

    new_text = rotate_string(text,rot)

    return new_caesar.format(new_text=new_text)

    

@app.route("/")
def index():
    
    return form_html

app.run()
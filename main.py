from flask import Flask, request
from caesar import rotate_string 


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
        <!DOCTYPE html>
            <html>
                <head>
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
                <form action="/" method="post">
                    <label for="rot" >
                        Rotate by:
                    </label>
                    <input type="text" name="rot" id="" input="0">
                    <textarea name="text" id="" cols="30" rows="10">{0}</textarea>
                    <button type="submit">
                        Submit Query
                    </button>
                </form>
                </body>
            </html>
        """
@app.route("/")
def index():
    content = form
    return content


@app.route("/", methods=['POST','GET'])
def encrypt():
    if request.method == 'POST':
        text = request.form['text']
        rot = int(request.form['rot'])
        return form.format(rotate_string(text, rot))
    return form.format("")
    

app.run()    


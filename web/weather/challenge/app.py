from flask import Flask
from flask import request
from flask import render_template
from flask import render_template_string


app = Flask(__name__)

@app.route('/')
def index():
   return render_template("flag.html")


@app.route("/degree", methods=["POST"])
def degree():
    if request.method == "POST":
        print(request.form)
        dd = request.form['degree']
        template = f''' 
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
                        <title>Weather App</title>
                    </head>

                    <body class="bg-blue-300 h-screen flex flex-col justify-center items-center text-blue-800">
                        <h1 class="text-3xl font-bold mb-5">Woooow, is it really {dd}?</h1>

                        <a href="/" class="bg-blue-800 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline-blue">Go Back</a>

                    </body>

                    </html>
                '''
        return render_template_string(template)



if __name__ == '__main__':
    app.run(debug = True)
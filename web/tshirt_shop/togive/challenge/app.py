import os
from flask import Flask, render_template, request
from lxml import etree
app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/create', methods=['GET','POST'])
def upload_svg():

    if  request.method == 'GET':
            return render_template('create.html')


    elif  request.method == 'POST':

        file = request.files['xml']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
 
        parser = etree.XMLParser(no_network=False)
 
        doc = etree.parse(f, parser=parser)
        parsed_xml = etree.tostring(doc, pretty_print=True,encoding=str) 
        rep = repr(parsed_xml)

        return f''' 

                     <!DOCTYPE html>
            <html lang="en" class="h-full">
            <head>
                <meta charset="UTF-8">
                <title>Result Page</title>
                <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
            </head>
            <body class="m-0 h-full bg-gradient-to-br from-gray-800 to-blue-700 text-white font-sans relative overflow-hidden">
                <div class="min-h-screen flex items-center justify-center">
                    <div class="border border-gray-700 p-8 rounded shadow-md bg-gray-100 w-3/4 md:w-2/3 lg:w-1/2">
                        {rep}
                    </div>
                </div>
            </body>
            </html>
            '''
    
if __name__ == '__main__':
    app.run(debug = True)

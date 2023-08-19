import subprocess
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        fileName = request.form.get('fileName')

        command = f"grep {keyword} files/{fileName}"
        if not keyword or not fileName:
            return render_template('index.html', result='Please Enter Keywords and select the file')
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                result = result.stdout
            else:
                result = "No result"
        except subprocess.TimeoutExpired:
            result = "Command execution timed out"  

        if not result:
            result = "No result"
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result='Please Enter Keywords and select the file')

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template

app = Flask(__name__)

FLAG = 'ingeniums{thAT$_TOO_muCh_$sRF_4nD_S3SS1oN_f0RGe}'

@app.route('/')
def index():
    return render_template('admin.html', flag=FLAG)
    
    

if __name__ == '__main__':
	app.run(host="0.0.0.0", port = 5001)


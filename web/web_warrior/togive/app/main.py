from flask import Flask, render_template, request, session
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import Image
import io
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = '<REDACTED>'

@app.route('/')
def index():
    session['internal'] = False
    return render_template('index.html')


@app.route('/screenshot', methods=['POST'])
def capture_screenshot():
    url = request.form.get('url')
    internal = session.get('internal', False)

    if not url:
        return render_template('error.html', error="No URL was provided.")

    if not internal:
        return render_template('error.html', error="Unauthorized. Only internal users can capture screenshots.")

    if len(url) < 10 or not url.startswith(('http://', 'https://')):
        return render_template('error.html', error="Please enter a valid URL.")

    for hostname in ['localhost', '127.0.0.1', '0.0.0.0', '0x0.0x0.0x0.0x0']:
        if hostname in url:
            return render_template('error.html', error="Host not allowed.")

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)

        screenshot = driver.get_screenshot_as_png()

        driver.quit()

        image = Image.open(io.BytesIO(screenshot))

        image_stream = io.BytesIO()
        image.save(image_stream, format='PNG')
        image_stream.seek(0)

        image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

        return render_template('result.html', image_data=image_base64)
    except Exception as e:
        return render_template('error.html', error="An error occurred while capturing the screenshot.")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

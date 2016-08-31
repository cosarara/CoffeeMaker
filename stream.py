#!/usr/bin/env python
from flask import Flask, render_template, Response
from PIL import Image
import time
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(path):
    last_image = None
    while True:
        try:
            image = Image.open(path)
        except:
            continue
        if image == last_image:
            time.sleep(1)
            continue

        with io.BytesIO() as output:
            try:
                image.save(output, format="JPEG")
            except:
                continue
            frame = output.getvalue()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen("/var/www/images/pic_centres.png"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

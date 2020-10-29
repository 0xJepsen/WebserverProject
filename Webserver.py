from flask import Flask, render_template, url_for
from flask_wtf import Form
import os

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES

@app.route("/")
def main():
    cat1 = os.path.join(app.config['UPLOAD_FOLDER'], 'smallCat.jpg')
    #cat2 = os.path.join(app.config['UPLOAD_FOLDER'], 'OrangeCat.jpg')
    return render_template('index.html', user_image = cat1)
    #return render_template('index.html', user_image = cat2)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 10001)

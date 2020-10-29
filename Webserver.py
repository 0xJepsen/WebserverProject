from flask import Flask, render_template, request
from flask_wtf import Form
import os

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES

votes = [0, 0]

@app.route("/", methods=['GET', 'POST'])
def main():
    print(request.method)
    if request.method=='POST':
        if request.form.get('voteCat1') == 'voteCat1':
            print("Vote for cat 1")
            votes[0] += 1
            print(votes[0])
        elif request.form.get('voteCat2') == 'voteCat2':
            print("Vote fore cat 2")
            votes[1] += 1
            print(votes[1])
        else: 
            return render_template("index.html")
    elif request.method=='GET':
        print("Not Cat")

    cat1 = os.path.join(app.config['UPLOAD_FOLDER'], 'smallCat.jpg')
    cat2 = os.path.join(app.config['UPLOAD_FOLDER'], 'standingCat.pg.jpg')
    return render_template('index.html', user_image = cat1, user_image2 = cat2)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 10001)

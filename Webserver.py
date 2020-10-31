from flask import Flask, render_template, request, jsonify
from flask_wtf import Form
import os

IMAGES = os.path.join('static', 'images')

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = IMAGES

votes = [0, 0]

#@app.route('/foo', methods=['POST'])
#def foo():
#    print(request.headers)
#    data = request.json
#    return jsonify(data)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method=='POST':
        print(request.get_data())
        if request.form.get('voteCat1') == 'voteCat1':
            votes[0] += 1
            print("Number of cat 1: ", votes[0])
        elif request.form.get('voteCat2') == 'voteCat2':
            votes[1] += 1
            print("Number of cat 2: ", votes[1])
        else: 
            return render_template("index.html")
    elif request.method=='GET':
        print("Not Cat")

    cat1 = os.path.join(app.config['UPLOAD_FOLDER'], 'smallCat.jpg')
    cat2 = os.path.join(app.config['UPLOAD_FOLDER'], 'standingCat.pg.jpg')
    return render_template('index.html', user_image = cat1, user_image2 = cat2)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 10001)

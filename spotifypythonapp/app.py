
from flask import Flask, render_template,request
from main import main
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST", "GET"])
def result():
    output = request.form.to_dict()
    username = output["username"]
    playlist_link1 = output["playlist_link1"]
    playlist_link2 = output["playlist_link2"]
    main(username,playlist_link1,playlist_link2)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
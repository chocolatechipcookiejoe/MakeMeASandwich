from flask import Flask
import mandrill

app = Flask(__name__)

@app.route("/")
def homepage():
    return app.send_static_file("index.html")

@app.route("/sendemail", methods=['POST'])
def send():
    pass

if __name__=="__main__":
    app.run(debug=True)

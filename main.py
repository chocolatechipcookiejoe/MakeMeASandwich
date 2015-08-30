from flask import Flask
import mandrill

app = Flask(__name__)

@app.route("/")
def homepage():
    app.send_static_file("index.html")

@app.route("/sendemail", methods=['POST'])
def send():

if __name__=="__main__":
    app.run()

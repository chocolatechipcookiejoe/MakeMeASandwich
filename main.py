from flask import Flask
import mandrill

app = Flask(__name__)
mandrill_client = mandrill.Mandrill("6bm0PZ5ilOTJ6tTMJowdxg")

@app.route("/")
def homepage():
    return app.send_static_file("index.html")

@app.route("/sendemail", methods=["POST"])
def send():
    pass

if __name__=="__main__":
    app.run(debug=True)

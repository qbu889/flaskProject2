from flask import Flask
import config

app = Flask(__name__)
app.config["SECRET_KEY"] = "skhrek349Lx!@#"
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'Hello World! '


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

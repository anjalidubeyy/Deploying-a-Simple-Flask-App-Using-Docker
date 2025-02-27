from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Anjali and Saaz! Welome to Essentials of Cloud and Devops."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make Flask accessible to all IPs

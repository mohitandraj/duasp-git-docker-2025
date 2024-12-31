from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "WWELCOME_MESSAGE", "Happy New Year 2025!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
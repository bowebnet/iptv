from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "IPTV API'ye hoş geldin!", "status": "online"})

@app.route('/test')
def test():
    return jsonify({"test": "API çalışıyor"})

if __name__ == '__main__':
    app.run(debug=True)

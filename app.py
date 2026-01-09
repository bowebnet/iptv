from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Android/web'den erişim için

# Temel yapılandırma
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'iptv-proje-guvenlik-anahtari')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///iptv.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Veritabanı (sonra aktif edeceğiz)
# db = SQLAlchemy(app)

# Ana sayfa
@app.route('/')
def home():
    return jsonify({
        "message": "IPTV Projesi API'si çalışıyor.",
        "version": "1.0",
        "endpoints": {
            "ana_sayfa": "/",
            "iptv_listesi": "/api/iptv (GET)",
            "iptv_ekle": "/api/iptv (POST)",
            "iptv_test": "/api/iptv/test (POST)"
        }
    })

# Test endpoint
@app.route('/test')
def test():
    return jsonify({"status": "başarılı", "api": "çalışıyor"})

# IPTV listesi (geçici)
@app.route('/api/iptv', methods=['GET'])
def iptv_listesi():
    # Şimdilik boş liste, sonra veritabanından çekeceğiz
    return jsonify({"iptv_list": []})

if __name__ == '__main__':
    app.run(debug=True)

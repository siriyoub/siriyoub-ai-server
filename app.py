from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "✅ Siriyoub AI Server is ready to receive images!"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "❌ No image part in request."}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "❌ No selected image."}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # رد تجريبي فقط - هنا يتم عادة تحويل الصورة إلى فيديو
    return jsonify({"message": "✔️ Image received successfully!", "filename": filename}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)


---

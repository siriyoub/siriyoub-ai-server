from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "🎉 Siriyoub AI Server is running!"

@app.route("/animate", methods=["POST"])
def animate():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    filename = "uploaded_image.jpg"
    image.save(filename)

    # ❗ بدل هذا لاحقًا بتوليد الفيديو الفعلي
    fake_video = "sample_result.mp4"
    if not os.path.exists(fake_video):
        return jsonify({"error": "Video not found"}), 404

    return send_file(fake_video, mimetype="video/mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

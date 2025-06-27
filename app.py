
from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

@app.route('/animate', methods=['POST'])
def animate():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image = request.files['image']
    save_path = 'input.jpg'
    image.save(save_path)

    # فيديو تجريبي فقط (لاحقًا نضيف الذكاء الاصطناعي)
    result_video = 'sample_result.mp4'
    if os.path.exists(result_video):
        return send_file(result_video, mimetype='video/mp4')
    else:
        return 'Video not found', 404

@app.route('/')
def index():
    return "🎉 Siriyoub AI Server is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

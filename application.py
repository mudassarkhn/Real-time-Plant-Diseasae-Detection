from flask import Flask, render_template, Response, request, jsonify
import cv2
import torch
import numpy as np
from ultralytics import YOLO
import base64
from PIL import Image
import io

app = Flask(__name__)

# Global variables
camera = None
model = YOLO('model.pt')
model.to('cuda' if torch.cuda.is_available() else 'cpu')
camera_active = False

def detect_objects(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)
    annotated_frame = results[0].plot()
    return cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

def generate_frames():
    global camera, camera_active
    camera = cv2.VideoCapture(0)
    
    while camera_active:
        success, frame = camera.read()
        if not success:
            break
        
        frame_with_detections = detect_objects(frame)
        ret, buffer = cv2.imencode('.jpg', frame_with_detections)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_video')
def start_video():
    global camera_active
    camera_active = True
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_camera')
def stop_camera():
    global camera, camera_active
    camera_active = False
    if camera:
        camera.release()
    return "Camera stopped"

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        file = request.files['file']
        img = Image.open(file.stream)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
        result_frame = detect_objects(img_cv)
        
        _, buffer = cv2.imencode('.jpg', result_frame)
        img_str = base64.b64encode(buffer).decode()
        
        return jsonify({'status': 'success', 'image': f'data:image/jpeg;base64,{img_str}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
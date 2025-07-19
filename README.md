# 🌿 Real-time Plants Disease Detection System 🌿


![]('screenshot1.png')
![]('screenshot2.png')
## 🚀 Overview

This project is a real-time plants disease detection system built with Flask and powered by a YOLO (You Only Look Once) object detection model. It allows users to detect plant diseases either through a live webcam feed or by uploading images. The system processes video frames or images to identify and highlight diseased areas in real-time.

The web interface features a clean and user-friendly design with a background image and favicon for branding.

## ✨ Features

- 🎥 Real-time object detection using webcam video stream.
- 📷 Image upload for disease detection on static images.
- 🖼️ Annotated video frames and images showing detected diseases.
- 💻 Responsive and intuitive web interface.
- 🤖 Uses a pre-trained YOLO model (`model.pt`) for detection.
- 🎨 Background image and favicon for enhanced UI experience.

## 📁 Project Structure

```
.
├── application.py          # Main Flask application
├── requirements.txt       # Python dependencies
├── model.pt               # Pre-trained YOLO model file
├── static/
│   ├── background.jpg     # Background image for the web UI
│   └── favicon.ico        # Favicon icon for the web UI
└── templates/
    └── index.html         # HTML template for the web interface
```

## 🛠️ Installation

1. Clone the repository or download the project files.

2. It is recommended to create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🎬 Usage

1. Ensure your webcam is connected if you want to use the live video detection.

2. Run the Flask application:

```bash
python application.py
```

3. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

4. Use the buttons on the web page to:

- ▶️ **Start Webcam**: Begin real-time detection using your webcam.
- 📤 **Upload Image**: Upload an image file to detect diseases in the image.

5. To stop the webcam feed, click the ⏹️ **Stop Webcam** button.

## ⚙️ How It Works

- The backend uses OpenCV to capture video frames from the webcam.
- Each frame is processed by the YOLO model to detect plant diseases.
- The processed frames are sent back to the frontend as a video stream.
- For image uploads, the image is sent to the backend, processed, and the annotated image is returned and displayed.
- The frontend is built with HTML, CSS, and JavaScript to provide a smooth user experience.

## 🎨 Icons and UI

- The favicon (`favicon.ico`) is used as the browser tab icon.
- The background image (`background.jpg`) is used as a semi-transparent background for the web page to enhance visual appeal.

## 📦 Dependencies

- Flask==2.3.2
- torch==2.0.1
- ultralytics==8.3.52
- supervision==0.1.0
- numpy==1.23.5

## 📝 Notes

- The YOLO model file `model.pt` should be present in the project root directory.
- The application automatically uses GPU if available, otherwise falls back to CPU.

## 📄 License

This project is provided as-is without any warranty. Feel free to modify and use it for your own purposes.

---
Created for real-time plants disease detection using deep learning and computer vision.

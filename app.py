from flask import Flask, render_template, request, jsonify, send_from_directory
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model("model.h5")
model.summary()  # Optional: to check the model architecture

# Function to process the uploaded image and perform analysis
def process_image(file):
    img = Image.open(file)
    img = img.resize((224, 224))  # Ensure the image size matches the model's input shape
    img = np.array(img) / 255.0  # Normalize the image pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension for the model
    return img

# Route for the home page
@app.route("/")
def index():
    return render_template("upload.html")

# Route for image upload and analysis
@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        try:
            image = process_image(file)
            prediction = model.predict(image)
            # Perform any post-processing on the prediction if needed

            return jsonify({"result": "Prediction: " + str(prediction)})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Route for serving static files (js, css, etc.)
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)
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
@app.route("/", method=['GET'])
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
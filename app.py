from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Route for the home page
@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images" + imagefile.filename
    imagefile.save(image_path)

    fruit_classes = ['apple_bad', 'apple_good', 'test']

    target_size= (256,256)
    img = tf.keras.preprocessing.image.load_img(image_path, target_size= target_size)
    model = tf.keras.models.load_model("model.h5")
    model.summary()
    # takes an image as an input
    # And gives us the confidence score of the prediction
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    predicted_class = fruit_classes[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    print(predicted_class)
    print(confidence)

    return render_template('index.html', predictclass = predicted_class)

if __name__ == "__main__":
    app.run(debug=True)
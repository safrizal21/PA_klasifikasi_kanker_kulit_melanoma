'''
	Contoh Deloyment untuk Domain Computer Vision (CV)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.JPG']
app.config['UPLOAD_PATH'] = './static/img/uploads/'

model = None
labels = ['benign', 'malignant']

def load_model():
    global model
    model = make_model()  # Memanggil fungsi make_model()
    model.load_weights('model121_1.h5')
    model.summary()

def make_model():
    pretrained_model = tf.keras.applications.densenet.DenseNet121(
        input_shape=(170, 170, 3),
        include_top=False,
        weights='imagenet',
        pooling='avg'
    )
    pretrained_model.trainable = False
    input = pretrained_model.input
    x = tf.keras.layers.Dense(128, activation='relu')(pretrained_model.output)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dense(32, activation='relu')(x)                        
    output = tf.keras.layers.Dense(2, activation='softmax')(x)
    model = tf.keras.models.Model(input, output)
    return model

@app.route("/")
def beranda():
    return render_template('index.html')

@app.route("/api/deteksi", methods=['POST'])
def apiDeteksi():
    hasil_prediksi = '(none)'
    prediksi_submit = '(none)'

    input_gambar = request.files['file']
    filename = secure_filename(input_gambar.filename)

    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        prediksi_submit = '/static/img/uploads/' + filename

        if file_ext in app.config['UPLOAD_EXTENSIONS']:
            input_gambar.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            test_image = Image.open('.' + prediksi_submit)
            test_image_resized = test_image.resize((170, 170))
            image_array = img_to_array(test_image_resized)
            test_image_x = (image_array / 255) - 0.5
            test_image_x = tf.expand_dims(test_image_x, axis=0)
            pred = model.predict(test_image_x)
            y_pred_test_classes_single = tf.argmax(pred, axis=1).numpy()
            hasil_prediksi = labels[y_pred_test_classes_single[0]]

            return jsonify({
                "prediksi": hasil_prediksi,
                "prediksi_submit": prediksi_submit
            })
        else:
            return jsonify({
                "prediksi": hasil_prediksi,
                "prediksi_submit": prediksi_submit
            })

if __name__ == '__main__':
    # Load model yang telah ditraining
    model = make_model()
    model.load_weights("model121_1.h5")

    # Run Flask di localhost
    app.run(host="localhost", port=5000, debug=True)
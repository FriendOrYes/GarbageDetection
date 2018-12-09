from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.models import model_from_json
from tensorflow.python.keras.preprocessing import image
import numpy as np
from tensorflow.python.keras import utils
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import Model
from keras.preprocessing.image import img_to_array
from scipy.misc import toimage
from keras.applications.vgg16 import preprocess_input

img_width, img_height = 256, 256
input_shape = (img_width, img_height, 3)
classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic']


    # backend Tensorflow, channels_last
print("Загружаю сеть из файлов")
json_file = open("../mnist_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель
loaded_model = model_from_json(loaded_model_json)
#Загружаем сохраненные веса в модель
loaded_model.load_weights("../mnist_model.h5")
print("Загрузка сети завершена")
# Компилируем загруженную модель
loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

def getImageInfo(img):
    if img == None:
        return ""

    # image_file_name = '../paper1.jpg'
    # img = image.load_img(image_file_name, input_shape=input_shape)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array /= 255.

    x = preprocess_input(img_array)

    prediction = loaded_model.predict(x)
    print(classes[np.argmax(prediction)])

    return classes[np.argmax(prediction)]



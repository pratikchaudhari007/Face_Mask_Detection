from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
#import detect_mask_image
model = load_model("mask_detector.model")
print(model.summary())
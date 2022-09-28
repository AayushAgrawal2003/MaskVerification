import matplotlib.pyplot as plt 
import tensorflow as tf 
from tensorflow import keras 
import numpy as np


from fastapi import FastAPI,UploadFile , File
from io import BytesIO
import nest_asyncio
from pyngrok import ngrok
from PIL import Image
import numpy as np
import uvicorn
MODEL = tf.keras.models.load_model("../my_h5_model.h5")

app = FastAPI()
CLASS_NAMES =["with_mask" , "without_mask"] 
@app.get('/index')
async def home():
  return "Hello World"

@app.get("/ping")
async def ping():
  return "I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    image = tf.image.resize(image , [256,256] ).numpy()
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

  image = read_file_as_image(await file.read())
  img_batch = np.expand_dims(image, 0)
  predictions = MODEL.predict(img_batch)

  predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
  print(CLASS_NAMES[np.argmax(predictions[0])])
  confidence = np.max(predictions[0])
  return {
      'class': predicted_class,
      'confidence': float(confidence)
  }




ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)


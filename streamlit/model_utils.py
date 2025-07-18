import tensorflow as tf
import numpy as np
import requests
import json
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


# Hard
def llama_guard_check(text):
    fast_keywords = [
        "kill", "rape", "suicide", "molest", "terror", "child porn",
        "fuck", "shoot", "abuse", "murder", "explode"
    ]
    lowered_text = text.lower()
    if any(kw in lowered_text for kw in fast_keywords):
        return "unsafe"

    headers = {
        "Authorization": "Bearer <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>",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", 
        "X-Title": "<YOUR_SITE_NAME>", 
    }

    data = {
        "model": "meta-llama/llama-guard-3-8b",
        "messages": [{"role": "user", "content": text}]
    }

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        response.raise_for_status()
        result = response.json()

        model_reply = result["choices"][0]["message"]["content"].lower()
        if "safe" in model_reply:
            return "safe"
        else:
            return "unsafe"

    except Exception as e:
        print(f"Error in llama_guard_check: {e}")
        return "error"
#=================================
model = tf.keras.models.load_model("my_LSTM.h5") 
vectorizer = tf.keras.models.load_model("vectorizer_model").layers[0]

class_names = ['Non-Violent Crimes', 'Safe', 'Unknown S-Type', 'Violent Crimes',
       'other', 'unsafe']
#================================= 
# Soft 
def soft_classify(text):
    processed = vectorizer(np.expand_dims(text,0))
    pred = model.predict(processed)
    pred_class = np.argmax(pred, axis=1)[0]
    return class_names[pred_class], pred[0]
#=============================
def generate_caption_from_image(image):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
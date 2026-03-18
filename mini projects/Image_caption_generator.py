# Image Caption Generator using AI

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Step 1: Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Step 2: Load image
image = Image.open("image.jpg")  # Put your image file here

# Step 3: Process image
inputs = processor(images=image, return_tensors="pt")

# Step 4: Generate caption
output = model.generate(**inputs)

# Step 5: Decode result
caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:", caption)
import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration


# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load image
img_path = "C:/Users/Ishwari kafle/Desktop/home/project1/man_dog.jpg"


# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')

#  pre-processed image is passed through the processor to generate inputs in the required format
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)
import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

#load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

#defining image captioning function
def caption_image(input_image : np.ndarray) -> str:
    # Convert the input image to RGB format
    image = Image.fromarray(input_image).convert('RGB')
    
    # Pre-process the image and text
    text = "a photo of"
    inputs = processor(images=image, text=text, return_tensors="pt")
    
    # Generate a caption for the image
    outputs = model.generate(**inputs, max_length=50)
    
    # Decode the generated tokens to text
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

# Create a Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    title  ="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model.",
    outputs="text"
)

# Launch the Gradio app
iface.launch()
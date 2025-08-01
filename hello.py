import gradio as gr

def greet(name):
    return "Hello, How are you " + name + "?"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Hardcoded to localhost + port 7860
demo.launch(server_name="127.0.0.1", server_port=7860, share=False, inbrowser=True)
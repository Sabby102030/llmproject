from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import requests
from huggingface_hub import login

app = Flask(__name__)

# Set your Hugging Face API token here
hf_api_token = "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"

# Login to Hugging Face
login(hf_api_token)

# Load the model and tokenizer from Hugging Face
model_name = "HuggingFaceTB/SmolLM-360M"
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=hf_api_token)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_api_token)

@app.route('/')
def home():
    return render_template("chat.html")

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.json["input"]
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

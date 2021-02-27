import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def predict(input):
	inputs = tokenizer.encode(input, return_tensor='pt')
	outputs = model.generate(inputs, max_length=200, do_sample=True)
	return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(predict("Hello, "))

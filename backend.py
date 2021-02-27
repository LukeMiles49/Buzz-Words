import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def predict(input):
	inputs = tokenizer.encode(input, return_tensors='pt')
	outputs = model.generate(inputs, max_length=400, do_sample=True)
	return tokenizer.decode(outputs[0], skip_special_tokens=True)

#print(predict("""Let me tell you a story:"""))

class Blockchain():
    def __init__(self):
        self.blocks=["initial block"]
        self.setup_next()
    def next_block(self):
        m = max(self.votesto)
        nx = [i for i in range(3) if self.votesto[i]==max]
        self.blocks.append(self.opts[random.choice(nx)])
        self.setup_next()

    def setup_next(self):
        last = self.blocks[-1]
        self.opts=[]
        for i in range(3):
            self.opts.append(predict(last))
        self.votesby={}
        self.votesto=[0,0,0]

    def vote(self, name, target):
        """Submit a vote. Returns false if invalid"""
        if target not in [0,1,2]:
            return False
        if name not in self.votesby:
            self.votesby[name]=target
            self.votesto[target]
            return True
        return False
    def getOpts(self):
        return [x for x in self.opts]

        

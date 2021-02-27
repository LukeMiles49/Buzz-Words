import random
import time

try:
    #assert False
    import torch
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    def predict(input):
        inputs = tokenizer.encode(input, return_tensors='pt')
        outputs = model.generate(inputs, max_length=200, do_sample=True)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
except Exception as e:
    def predict(input):
        return (input + "GPT2 is sorry, but does not want to say any more today."+str(random.random()) )

#print(predict("""Let me tell you a story:"""))

class Blockchain():
    def __init__(self):
        print("creating blockchain")
        self.blocks=["initial block"]
        self.setup_next()
    def next_block(self):
        m = max(self.votesto)
        nx = [i for i in range(3) if self.votesto[i]==m]
        #print(nx)
        self.blocks.append(self.opts[random.choice(nx)])
        self.setup_next()

    def setup_next(self):
        self.blocktime=time.time()
        last = self.blocks[-1]
        self.opts=[]
        for i in range(3):
            p = predict(last+"\n"+"\n")
            p = p[len(last):]
            while p[0]=="\n":
                p=p[1:]
            l = p.find("\n")
            if l>0:
                p=p[:l]
            self.opts.append(p)

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
    def history(self, since):
        if time.time()-self.blocktime > 100:
            self.next_block()
        return list(self.blocks[since:])
    def __len__(self):
        return len(self.blocks)

        

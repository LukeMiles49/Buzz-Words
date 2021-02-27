from flask import Blueprint
from flask import request
from app.blockchain import Blockchain
import json


BLOCKCHAIN = Blueprint('BLOCKCHAIN', __name__)

chain = Blockchain()

@BLOCKCHAIN.route('/api/options', methods=['GET'])
def options():
    return json.dumps({
          "options" : chain.getOpts()
        , "round" : len(chain)+1
    })
@BLOCKCHAIN.route('/api/history', methods=['GET'])
def history():
    since = request.args.get('since', type=int)
    return json.dumps(chain.history(since))
@BLOCKCHAIN.route('/api/vote', methods=['POST'])
def vote():
    id = request.args.get('id')
    opt = request.args.get('opt', type=int)
    round = request.args.get('round', type=int)
    if(len(chain)!=round+1):
        return "failed"
    if chain.vote(id,opt):
        return "success"
    else:
        return "failed"

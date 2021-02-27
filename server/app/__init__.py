from flask import Flask
import hashlib
import uuid
from .index import INDEX
from .api import BLOCKCHAIN

app = Flask(__name__)

app.config['SECRET_KEY'] = hashlib.sha256(
    str(uuid.uuid4()).encode()
).hexdigest()

# Register Blueprints
app.register_blueprint(
    INDEX, url_prefix='')
app.register_blueprint(
    BLOCKCHAIN, url_prefix='')

app.config.from_object(__name__)

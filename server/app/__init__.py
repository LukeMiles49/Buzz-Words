from flask import Flask
import hashlib
import uuid

app = Flask(__name__)

app.config['SECRET_KEY'] = hashlib.sha256(
    str(uuid.uuid4()).encode()
).hexdigest()

app.config.from_object(__name__)

from app import views
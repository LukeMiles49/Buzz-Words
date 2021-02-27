from flask import Blueprint
from flask import render_template

# Define the INDEX global variable
INDEX = Blueprint('INDEX', __name__)

@INDEX.route('/', defaults={'path': ''})
@INDEX.route('/<path:path>')
def index(path):
    """
    The additional route "/<path:path" is to redirect all.
    routes to index.html

    Args:
        None

    Returns:
        (html): index.html render
    
    """
    return render_template('index.html')

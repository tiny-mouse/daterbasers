from __future__ import absolute_import

from clay import app

@app.route('/', methods=['GET'])
def index():
    return "Heddo Whirled!"


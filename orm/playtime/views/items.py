from __future__ import absolute_import

from clay import app
from flask import render_template

from playtime.util.data import ITEMS
# Uncomment to use the db
#from playtime.models import db_session
#from playtime.models.item import Item

@app.route('/', methods=['GET'])
def index():
    return "Heddo Whirled!"

@app.route('/items', methods=['GET'])
def items():
    all_items = ITEMS
    # Uncomment to use the db
    #all_items = db_session.query(Item).all()
    # Uncomment to use the db and sort items.
    #all_items = db_session.query(Item).order_by(Item.name).all()
    return render_template('items.html', items=all_items)

from __future__ import absolute_import

from clay import app, config
from flask import redirect, render_template, request

from playtime.util.data import ITEMS
from playtime.models import db_session
from playtime.models.item import Item
from playtime.models.hex_color import HexColor
from playtime.models.item_type import ItemType
from playtime.models.storage_location import StorageLocation

bg_color = config.get('bg_color', 'white')

@app.route('/', methods=['GET'])
def items():
    # Uncomment to use static data
    all_items = ITEMS
    return render_template('static_items.html', items=all_items, bg_color=bg_color)
    # Uncomment to use the db
    #all_items = db_session.query(Item).all()
    # Uncomment to use the db and sort items.
    all_items = db_session.query(Item).order_by(Item.name).all()
    return render_template('items.html', items=all_items, bg_color=bg_color)

@app.route('/new', methods=['GET'])
def create_item_form():
    colors = db_session.query(HexColor).order_by(HexColor.hex_value).all()
    locations = db_session.query(StorageLocation).order_by(StorageLocation.name).all()
    types = db_session.query(ItemType).order_by(ItemType.name).all()
    return render_template(
        'create_item.html', hex_colors=colors, locations=locations,
        types=types, bg_color=bg_color)

@app.route('/items/create', methods=['POST'])
def create_item():
    form_data = request.form
    name = form_data.get('name')
    type_id = form_data.get('type_id')
    item_type = db_session.query(ItemType).get(type_id)
    location_id = form_data.get('location_id')
    location = db_session.query(StorageLocation).get(location_id)
    hex_id = form_data.get('hex_id')
    hex_color = db_session.query(HexColor).get(hex_id)
    new_item = Item(name=name, item_type=item_type, storage_location=location, hex_color=hex_color)

    db_session.add(new_item)
    db_session.commit()

    return redirect('/')

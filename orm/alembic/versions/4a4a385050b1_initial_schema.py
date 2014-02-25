"""initial schema

Revision ID: 4a4a385050b1
Revises: None
Create Date: 2014-02-22 16:14:51.802262

"""

# revision identifiers, used by Alembic.
revision = '4a4a385050b1'
down_revision = None

import random

from alembic import op
import sqlalchemy as sa

from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column

# This isn't the most efficent way of doing this, but unless you're a wizard
# these hex colors don't make a ton of sense. Intentionally suboptimal.
# ALSO: please excuse this migration. It's not great.
ALL_COLORS = {
    "red": [ "FF0000", "8E2323", "EE2C2C", "8C1717", "EE0000", "E3170D", "FC1501" ],
    "orange": [ "E04006", "EE4000", "FF7F24", "FF6103", "EE8833", "FF4500", "FF6600" ],
    "yellow": [ "FFFF00", "EEAD0E", "CDAB2D", "FFCC11", "FFC125", "FCDC3B", "FFD700" ],
    "green": [ "00FF00", "7FFF00", "3F6826", "55AE3A", "228B22", "0AC92B", "43CD80" ],
    "blues": [ "0000FF", "388E8E", "37FDFC", "0D4F8B", "5D7B93", "0276FD", "000080" ],
    "purple": [ "7F00FF", "2E0854", "A020F0", "68228B", "9932CC", "AA00FF", "CC99CC" ],
    "pink": [ "FF33CC", "FF1CAE", "CD1076", "FF00AA", "FF6EB4", "FF0066", "CD6889" ],
}

ALL_TYPES = [ "books", "shirts", "pants", "shoes", "bags", "dishes", "electronics" ]
STORAGE_LOCATIONS = [ "kitchen", "living room", "den", "office", "bathroom", "room" ]

def get_rando_name():
    names = ["my", "joe", "jane", "jesse", "bob", "mom", "brophia", "nicola", "marfa"]
    modifiers = ["favorite", "newest", "oldest", "borrowed", "found"]
    items = ["t-shirt", "book", "plate", "blanket", "skirt", "shoes", "dress", "camera", "laptop", "comfy socks", "pjs"]
    owner = random.choice(names)
    ownership = "'s" if owner != "my" else ""
    item = random.choice(items)
    return "{0}{1} {2} {3}".format(owner, ownership, random.choice(modifiers), item)

def upgrade():
    from playtime.models import db_session
    from playtime.models.color_family import ColorFamily
    from playtime.models.hex_color import HexColor
    from playtime.models.item_type import ItemType
    from playtime.models.storage_location import StorageLocation

    op.create_table(
        'color_families',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True)
    )
    op.create_table(
        'hex_colors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('hex_value', sa.String(50), nullable=False, unique=True),
        sa.Column('color_family_id', sa.Integer, nullable=False)
    )
    op.create_table(
        'item_types',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True)
    )
    op.create_table(
        'storage_locations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True)
    )
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('item_type_id', sa.Integer, nullable=False),
        sa.Column('hex_color_id', sa.Integer, nullable=False),
        sa.Column('storage_location_id', sa.Integer, nullable=False),
    )

    color_families_table = table('color_families', column('name', String))
    hex_colors_table = table('hex_colors', column('hex_value', String), column('color_family_id', Integer))
    item_types_table = table('item_types', column('name', String))
    items_table = table('items', column('name', String), column('hex_color_id', Integer), column('storage_location_id', Integer), column('item_type_id', Integer))
    storage_locations_table = table('storage_locations', column('name', String))

    location_rows = [{'name':value} for value in STORAGE_LOCATIONS]
    op.bulk_insert(storage_locations_table, location_rows)


    for family, values in ALL_COLORS.iteritems():
        op.execute(color_families_table.insert().values(name=family))
        color_family = db_session.query(ColorFamily).filter(ColorFamily.name == family).first()
        hex_rows = [{'hex_value':value, 'color_family_id':color_family.id} for value in values]
        op.bulk_insert(hex_colors_table, hex_rows)

    type_rows = [{'name':value} for value in ALL_TYPES]
    op.bulk_insert(item_types_table, type_rows)

    item_types = db_session.query(ItemType).all()
    colors = db_session.query(HexColor).all()
    storage_locations = db_session.query(StorageLocation).all()

    items = []
    for i in range(1000):
        # Pick a random type
        item_type = random.choice(item_types)
        # Pick a random hex color
        hexvalue = random.choice(colors)
        # Pick a random storage location
        storage_location = random.choice(storage_locations)
        #Add it
        hexcolor = db_session.query(HexColor).filter(
            HexColor.hex_value == hexvalue.hex_value).first()
        item_name = get_rando_name()
        items.append({
            'name': item_name,
            'item_type_id':item_type.id,
            'hex_color_id':hexcolor.id,
            'storage_location_id':storage_location.id,

        })
    op.bulk_insert(items_table, items)


def downgrade():
    op.drop_table('items')
    op.drop_table('item_types')
    op.drop_table('color_families')
    op.drop_table('hex_colors')
    op.drop_table('storage_locations')

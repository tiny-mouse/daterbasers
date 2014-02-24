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

from sqlalchemy import String
from sqlalchemy.sql import table, column

# This isn't the most efficent way of doing this, but unless you're a wizard
# these hex colors don't make a ton of sense. Intentionally suboptimal.
ALL_COLORS = {
    "red": [ "FF0000", "8E2323", "EE2C2C", "8C1717", "EE0000", "E3170D", "FC1501" ],
    "orange": [ "E04006", "EE4000", "FF7F24", "FF6103", "EE8833", "FF4500", "FF6600" ],
    "yellow": [ "0000FF", "EEAD0E", "CDAB2D", "FFCC11", "FFC125", "FCDC3B", "FFD700" ],
    "green": [ "00FF00", "7FFF00", "3F6826", "55AE3A", "228B22", "0AC92B", "43CD80" ],
    "blues": [ "0000FF", "388E8E", "37FDFC", "0D4F8B", "5D7B93", "0276FD", "000080" ],
    "purple": [ "7F00FF", "2E0854", "A020F0", "68228B", "9932CC", "AA00FF", "CC99CC" ],
    "pink": [ "FF33CC", "FF1CAE", "CD1076", "FF00AA", "FF6EB4", "FF0066", "CD6889" ],
}

ALL_TYPES = [ "books", "shirts", "pants", "shoes", "bags", "dishes", "electronics" ]

def get_rando_name():
    names = ["my", "joe", "jane", "jesse", "bob", "mom", "brophia", "nicola", "marfa"]
    modifiers = ["favorite", "newest", "oldest", "borrowed", "found"]
    return "{0}'s {1}".format(random.choice(names), random.choice(modifiers))

def upgrade():
    from playtime.models import db_session
    from playtime.models.color_family import ColorFamily
    from playtime.models.hex_color import HexColor
    from playtime.models.item_type import ItemType

    op.create_table(
        'color_families',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True)
    )
    op.create_unique_constraint("uq_color_family_name", "color_families", ["name"])
    op.create_table(
        'hex_colors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('hexvalue', sa.String(50), nullable=False)
    )
    op.create_unique_constraint("uq_hexvalue", "hex_colors", ["hexvalue"])
    op.create_table(
        'item_types',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    color_families_table = table('color_families', column('name', String))
    hex_colors_table = table('hex_colors', column('hexvalue', String))
    item_types_table = table('item_types', column('name', String))
    items_table = table('items', column('name', String))

    for family, values in ALL_COLORS.iteritems():
        op.execute(color_families_table.insert().values(name=family))
        colorfamily = db_session.query(ColorFamily).filter(ColorFamily.name == family).first()
        hex_rows = [{'hexvalue':value} for value in values]
        op.bulk_insert(hex_colors_table, hex_rows)

    type_rows = [{'name':value} for value in ALL_TYPES]
    op.bulk_insert(item_types_table, type_rows)

    item_types = db_session.query(ItemType).all()
    colors = db_session.query(HexColor).all()

    items = []
    for i in range(1000):
        # Pick a random type
        item_type = random.choice(item_types)
        # Pick a random hex color
        hexvalue = random.choice(colors)
        #Add it
        hexcolor = db_session.query(HexColor).filter(
            HexColor.hexvalue == hexvalue).first()
        item_name = get_rando_name()
        items.append({
            'name': item_name,
            'item_type_id':item_type.id,
            'hex_color_id':hexcolor.id
        })
    op.bulk_insert(items_table, items)


def downgrade():
    op.drop_table('items')
    op.drop_table('item_types')
    op.drop_table('color_families')
    op.drop_table('hex_colors')

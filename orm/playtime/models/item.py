from __future__ import absolute_import

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base


class Item(Base):
    ''' A physical item. '''

    __tablename__ = 'items'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode, unique=True)
    item_type_id = Column('item_type_id', Integer, ForeignKey('item_types.id'), nullable=False, index=True)
    hex_color_id = Column('hex_color_id', Integer, ForeignKey('hex_colors.id'), nullable=False, index=True)

    item_type = relationship('ItemType', primaryjoin="ItemType.id == Item.item_type_id")
    hex_color = relationship('HexColor', primaryjoin="HexColor.id == Item.hex_color_id")


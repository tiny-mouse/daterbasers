from __future__ import absolute_import

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base
from playtime.models.hex_color import HexColor
from playtime.models.item_type import ItemType
from playtime.models.storage_location import StorageLocation


class Item(Base):
    ''' A physical item. '''

    __tablename__ = 'items'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode, unique=True)
    item_type_id = Column(Integer, ForeignKey('item_types.id'), nullable=False, index=True)
    hex_color_id = Column(Integer, ForeignKey('hex_colors.id'), nullable=False, index=True)
    storage_location_id = Column(Integer, ForeignKey('storage_locations.id'), nullable=False, index=True)

    item_type = relationship(ItemType, primaryjoin="ItemType.id == Item.item_type_id")
    hex_color = relationship(HexColor, primaryjoin="HexColor.id == Item.hex_color_id")
    storage_location = relationship(StorageLocation, primaryjoin="StorageLocation.id == Item.storage_location_id")


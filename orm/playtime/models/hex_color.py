from __future__ import absolute_import

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base
from playtime.models.color_family import ColorFamily


class HexColor(Base):
    ''' A color in hex value 000000 - FFFFFF '''

    __tablename__ = 'hex_colors'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    hex_value = Column(Unicode, unique=True)
    color_family_id = Column(Integer, ForeignKey('color_families.id'), nullable=False, index=True)

    color_family = relationship(ColorFamily, primaryjoin="ColorFamily.id == HexColor.color_family_id")

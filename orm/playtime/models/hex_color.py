from __future__ import absolute_import

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base


class HexColor(Base):
    ''' A color in hex value 000000 - FFFFFF '''

    __tablename__ = 'hex_colors'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    hexcolor = Column(Unicode, unique=True)

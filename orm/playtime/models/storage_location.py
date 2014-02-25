from __future__ import absolute_import

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base


class StorageLocation(Base):
    ''' Where something goes. '''

    __tablename__ = 'storage_locations'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode, unique=True)

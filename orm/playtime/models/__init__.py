from __future__ import absolute_import

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_session = scoped_session(sessionmaker())
Base = declarative_base()
Base.query = db_session.query_property()

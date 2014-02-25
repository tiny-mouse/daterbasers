from __future__ import absolute_import

import sqlalchemy

from clay import config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# This isn't great, but it's just an example app
engine = sqlalchemy.engine_from_config(config.get('database'))
db_session = scoped_session(sessionmaker())
db_session.configure(bind=engine)
Base = declarative_base()
Base.query = db_session.query_property()

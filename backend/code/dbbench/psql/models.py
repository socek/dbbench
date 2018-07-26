from datetime import datetime
from datetime import timezone

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

metadata = MetaData()


class Base(object):
    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).timestamp(),
            'updated_at': self.updated_at.replace(tzinfo=timezone.utc).timestamp(),
        }


Model = declarative_base(metadata=metadata, cls=Base)


class First(Model):
    __tablename__ = 'first'

    name = Column(String(100), nullable=True)

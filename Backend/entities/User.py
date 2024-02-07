from main_config import db
from sqlalchemy import Column, Integer, String, DateTime

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(1024), nullable=False, unique=True)
    password = Column(String(1024), nullable=False)

    def __repr__(self):
        return f'<user {self.id}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

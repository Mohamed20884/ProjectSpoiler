from app.models.model import Model
from app.models.user import User

from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, DateTime, ScrolledText


class Client(Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)

    first_name = Column(Text, nullable=False, index=True)

    last_name = Column(Text, nullable=False, index=True)

    date_of_birth = Column(Date, nullable=False)

    nation_insurance_number = Column(Text, unique=True)


    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'data_of_birth': self.date_of_birth,
            'national_insurance_number': self.nation_insurance_number
        }

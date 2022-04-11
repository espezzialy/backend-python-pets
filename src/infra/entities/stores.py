import enum 
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class StoresTypes(enum.Enum):
    """ Defining in this file the types of Stores that we gonna have"""

    MALL = "mall"
    INDEPENDENT = "independent"
    ONLINE   = "online"



class Stores(Base):
    """ Stores Entity """

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False,unique=False)
    address = Column(String(60), nullable=False, unique=True)
    type = Column(Enum(StoresTypes), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


    def __repr__(self):
        return f"Store [name={self.name}, address={self.address}, type = {self.type}. user_id={self.user_id}]""

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == self.name
            and self.address == other.address
            and self.type == other.type
            and self.user_id == other.user_id
        ):
            return True
        return False


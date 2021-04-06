import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """ Defining the  Anymal Types"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    RAT = "rat"
    TURTLE = "turtle"


class Pets(Base):
    """ Pets Entity """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet [name={self.name}, specie={self.specie}, user_id={self.user_id}]"

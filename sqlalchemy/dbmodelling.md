# Database Modelling using sqlalchemy
When creating table objects using sqlalchemy ,the object inherits from
an inbuild class called *declarative_base*.
We import data types such as Integer,String and Text from the sqlalchemy datatypes library.
+ Code snippet below for demo purposes

```from sqlachemy.ext.declarative import declarative_base
from sqlachemy import Column
from sqlachemy.types import Integer,String,Text,ForeignKey


Base = declarative_base

class User(Base):
    """user account"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)

    def __repr__():
        return "<User %r>" % self.username```
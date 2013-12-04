#!/usr/bin/python2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Creates the SQLite database example.db in the current directory
# echo=True is to print out the SQL statements when you run the program
engine = create_engine("sqlite:///example.db", echo=True)


"""
Valid SQLite URL forms are:
     sqlite:///:memory: (or, sqlite://)
      sqlite:///relative/path/to/file.db
       sqlite:////absolute/path/to/file.d
"""

# Create a sessionmaker with the engine
Session = sessionmaker(bind=engine)

# Create a session with the sessionmaker
session = Session()

# The Base from which the User class inherits from
Base = declarative_base()

# A User class, that we can use with the database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    # The initializing method of the class
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    # This method is called when printing out instances of this class
    def __repr__(self):
       return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

# Create the User table
Base.metadata.create_all(engine)


# Create two users
u1 = User("trauzti", "Trausti Saemundsson", "holysecret")
u2 = User("knuth", "Donald E. Knuth", "moresecret")

# Add them to the session
session.add(u1)
session.add(u2)

# Save them to the database
session.commit()

# Print all Users
print session.query(User).all()

# Get Trauzti from the database
u = session.query(User).filter(User.name == "trauzti").first()

#Change the name and save it
u.name = "Trausti"
session.merge(u)
session.commit()

# Print all Users
print session.query(User).all()

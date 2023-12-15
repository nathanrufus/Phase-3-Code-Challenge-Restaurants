from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db='mysql+mysqlconnector://root:6131a21A?@localhost/Restaurants'
engine =create_engine(db, echo=True)
Session =sessionmaker(bind=engine)
session = Session()
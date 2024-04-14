from databases.database import Base, engine
from models.model import User, Order

Base.metadata.create_all(bind=engine)
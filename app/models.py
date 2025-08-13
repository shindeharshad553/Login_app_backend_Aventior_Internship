from .database import Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey,Text
from datetime import datetime
from sqlalchemy.orm import relationship

# creating the models that is the python classes that will be mapped to the database tables
class User(Base):
    __tablename__ = "LoginData"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)

    # Relationship to Token
    tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")


class Token(Base):
    __tablename__ = "TokenInformation"
    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(Text, nullable=False)
    refresh_token = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Correct ForeignKey reference
    user_id = Column(Integer, ForeignKey("LoginData.id"), nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="tokens")

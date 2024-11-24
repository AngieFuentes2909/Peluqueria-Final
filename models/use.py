from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base


# Modelo de SQLAlchemy para la tabla 'usuarios'
class UserModel(Base):
    __tablename__ = "usuarios"

    UserId = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50), nullable=False)
    Apellido = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Telefono = Column(String(15), nullable=False)
    Password = Column(String(100), nullable=False)

# Modelo de Pydantic para validación de datos
class User(BaseModel):
    Nombre: str
    Apellido: str
    Email: str
    Telefono: str
    Password: str



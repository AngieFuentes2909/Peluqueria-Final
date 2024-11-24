from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from models.use import User, UserModel
from auth import create_access_token, decode_access_token, verify_password, hash_password
from core.database import get_db
from models.loginp import LoginRequest
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import SecurityScheme
from fastapi.security import OAuth2
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")




@app.get('/')
def root():
    return {"message": "¡Hola, bienvenido!"}


@app.get('/users')
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


# Ruta para crear un usuario
@app.post("/user")
def create_user(user: User, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.Password)
    user_db = UserModel(
        Nombre=user.Nombre,
        Apellido=user.Apellido,
        Email=user.Email,
        Telefono=user.Telefono,
        Password=hashed_password
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return {"message": "Usuario creado correctamente"}


# Endpoint para actualizar un usuario
@app.put('/user/{user_id}')
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    user_db = db.query(UserModel).filter(UserModel.UserId == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user_db.Nombre = user.Nombre
    user_db.Apellido = user.Apellido
    user_db.Email = user.Email
    user_db.Telefono = user.Telefono
    if user.Password:
        user_db.Password = hash_password(user.Password)

    db.commit()
    db.refresh(user_db)
    return {"message": "Usuario actualizado correctamente", "user": user_db}


# Endpoint para eliminar un usuario
@app.delete('/user/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserModel).filter(UserModel.UserId == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user_db)
    db.commit()
    return {"message": "Usuario eliminado correctamente"}

@app.post("/login")
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.Email == login_data.Email).first()
    if not user or not verify_password(login_data.Password, user.Password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": user.Email})
    return {"access_token": access_token, "token_type": "bearer"}







@app.get("/protected", summary="Ruta protegida")
def protected_route(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    user_email = payload.get("sub")
    if not user_email:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = db.query(UserModel).filter(UserModel.Email == user_email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    return {"message": "Acceso permitido", "user": user.Nombre}
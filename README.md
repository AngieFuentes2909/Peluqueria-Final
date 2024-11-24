---

# Sistema de Gestión de Citas para Peluquería

## Descripción
Este proyecto es un sistema diseñado para gestionar de manera eficiente las citas de una peluquería. El sistema permite a los clientes reservar, modificar y cancelar citas, mientras que los administradores pueden gestionar horarios, supervisar pagos y organizar los servicios ofrecidos.  
El propósito principal es mejorar la experiencia de usuario y optimizar las operaciones internas de la peluquería.

---

## Instalación y Ejecución

### Requisitos Previos
1. *Python* (versión 3.9 o superior).
2. *Node.js* (versión 16 o superior).
3. *MySQL* como base de datos relacional.
4. Un navegador web moderno para el frontend.

---

### Backend

1. Clona este repositorio y accede al directorio del proyecto:
   ```bash
   git clone https://github.com/AngieFuentes2909/Peluqueria-Final
   cd sistema-citas-peluqueria/backend

2. Instala las dependencias de Python:

pip install -r requirements.txt


3. Configura las variables de entorno en un archivo .env dentro del directorio backend:




4. Ejecuta el servidor:

python manage.py runserver




---

Frontend

1. Ve al directorio del frontend:

cd ../frontend


2. Instala las dependencias de React:

npm install


3. Inicia el servidor de desarrollo:

npm start



El frontend estará disponible en: http://localhost:8000


---

Base de Datos

1. Asegúrate de tener MySQL instalado y configurado en tu máquina.


2. Crea la base de datos utilizando el siguiente comando en MySQL:

CREATE DATABASE nombre_base_datos;


3. Importa las tablas iniciales utilizando el script proporcionado en el archivo schema.sql:

mysql -u ROOT -p pelubd




---

Tecnologías Utilizadas

Backend: Python, Flask/Django.

Frontend: React.js.

Base de Datos: MySQL.

Control de Versiones: Git y GitHub.



---

Integrantes del Equipo y Roles

Angie Fuentes - Desarrollo del Backend: Responsable de implementar la lógica del servidor, las rutas de la API y la conexión con la base de datos.

Marta Domínguez - Administración de la Base de Datos: Encargada del diseño, creación y mantenimiento de las tablas en MySQL.

Wildherman Betancourt - Desarrollo del Frontend: Diseñador y desarrollador de la interfaz gráfica de usuario con React.js.




---



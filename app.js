// URL base del backend
const BASE_URL = "http://127.0.0.1:8000";

// Referencias a elementos del DOM
const loginForm = document.getElementById("loginForm");
const protectedButton = document.getElementById("accessProtected");
const messageDiv = document.getElementById("message");

// Evento para el formulario de login
loginForm.addEventListener("submit", async (event) => {
    event.preventDefault(); // Evitar que la página se recargue al enviar el formulario

    // Obtener valores del formulario
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        // Hacer la solicitud al endpoint de login
        const response = await axios.post(`${BASE_URL}/login`, {
            Email: email,  // Cambiar 'username' a 'Email' para que coincida con el backend
            Password: password,
        });

        // Obtener el token de acceso de la respuesta
        const { access_token } = response.data;

        // Guardar el token en el almacenamiento local
        localStorage.setItem("access_token", access_token);

        // Mostrar un mensaje de éxito
        messageDiv.textContent = "Inicio de sesión exitoso. Token guardado.";
        messageDiv.style.color = "green";
    } catch (error) {
        // Manejo de errores
        if (error.response && error.response.status === 401) {
            messageDiv.textContent = "Credenciales incorrectas.";
        } else {
            messageDiv.textContent = "Error al conectar con el servidor.";
        }
        messageDiv.style.color = "red";
    }
});

// Evento para acceder a la ruta protegida
protectedButton.addEventListener("click", async () => {
    // Obtener el token del almacenamiento local
    const token = localStorage.getItem("access_token");

    if (!token) {
        messageDiv.textContent = "Por favor, inicia sesión primero.";
        messageDiv.style.color = "red";
        return;
    }

    try {
        // Hacer la solicitud a la ruta protegida
        const response = await axios.get(`${BASE_URL}/protected`, {
            headers: {
                Authorization: `Bearer ${token}`, // Incluir el token en el encabezado
            },
        });

        // Mostrar el resultado de la ruta protegida
        const { user, message } = response.data;
        messageDiv.textContent = `${message}. Bienvenido, ${user}`;
        messageDiv.style.color = "green";
    } catch (error) {
        // Manejo de errores
        if (error.response && error.response.status === 401) {
            messageDiv.textContent = "Acceso denegado. Token inválido o expirado.";
        } else {
            messageDiv.textContent = "Error al conectar con el servidor.";
        }
        messageDiv.style.color = "red";
    }
});

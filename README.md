🧪 Framework de Automatización de Pruebas – Proyecto Final

Este proyecto es un framework completo de automatización de pruebas desarrollado como Trabajo Final Integrador.
Incluye:

✔ Pruebas de UI con Selenium WebDriver
✔ Pruebas de API con Requests
✔ Framework basado en Pytest
✔ Organización con Page Object Model (POM)
✔ Captura automática de screenshots en fallos
✔ Parametrización y lectura de datos desde JSON
✔ Reportes HTML con Pytest
✔ Logging detallado
✔ Preparado para integrarse con GitHub Actions (CI/CD)

📌 Tecnologías utilizadas

Python 3

Selenium WebDriver

Pytest

Requests

Pytest-HTML

Git & GitHub

GitHub Actions


✔️ Funcionalidades Implementadas
1️⃣ Pruebas de UI (Selenium)

Pruebas automatizadas sobre https://www.saucedemo.com
, incluyendo:

Login exitoso (parametrizado)

Login negativo

Agregar productos al carrito

Navegación dentro del sistema

Flujo completo de checkout

Tecnologías aplicadas:

Page Object Model

Selenium WebDriver

Parametrización

Datos externos JSON

Capturas automáticas cuando un test falla

2️⃣ Pruebas de API (Requests)

Tests sobre la API pública ReqRes:
https://reqres.in/

Incluye:

GET users

POST create user

DELETE user

Validación de códigos de estado

Validación de contenido JSON

3️⃣ Generación de Reportes HTML

Pytest genera un archivo:

report.html


Este incluye:

Lista de tests ejecutados

Resultados (Passed / Failed)

Tiempo de ejecución

Screenshots anexados en caso de fallos

Activado mediante:

pytest.ini

4️⃣ Logging

El archivo:

execution.log


Registra:

Fecha y hora

Pasos clave de ejecución

Errores y fallos

Screenshots generados

5️⃣ Captura de Screenshots Automática

Cuando un test falla, automáticamente se genera un screenshot en:

/screenshots/


El archivo contiene:

screenshot_nombredeltest_fecha.png


Esto es manejado desde:

tests/conftest.py


📊 Cómo ver los reportes

Después de ejecutar los tests, abre:

report.html


Incluye:

Resultados

Logs

Screenshots de fallos


Proyecto desarrollado como entrega final del curso de Automatización de Pruebas con Python.

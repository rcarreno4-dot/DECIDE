# 🚀 Guía de Despliegue en Render (Render.com)

Esta guía te explica cómo subir y publicar tu aplicación **DECIDE v2.0** en **Render** de forma gratuita en 3 pasos sencillos.

---

## 🛠️ Configuración que ya fue preparada en el proyecto

Tu proyecto ya tiene todos los archivos que Render necesita para detectar y desplegar la aplicación automáticamente:

1. **[`requirements.txt`](file:///c:/Users/Fabian/OneDrive/Desktop/AppCarlos/requirements.txt)**: Incluye `flask` y el servidor de producción `gunicorn`.
2. **[`Procfile`](file:///c:/Users/Fabian/OneDrive/Desktop/AppCarlos/Procfile)**: Indica a Render el comando de inicio `web: gunicorn app_web:app`.
3. **[`render.yaml`](file:///c:/Users/Fabian/OneDrive/Desktop/AppCarlos/render.yaml)**: Configuración como código (Blueprint) para Render.
4. **[`app_web.py`](file:///c:/Users/Fabian/OneDrive/Desktop/AppCarlos/app_web.py)**: Lee automáticamente la variable de entorno `$PORT` asignada por Render y sirve la interfaz web con React + Tailwind + Bootstrap.

---

## 📋 Pasos para Desplegar

### Paso 1: Subir tu código a GitHub

1. Abre tu terminal en la carpeta del proyecto `AppCarlos` e inicializa Git (si aún no lo tienes):
   ```bash
   git init
   git add .
   git commit -m "DECIDE v2.0 con soporte Web y Render"
   ```

2. Crea un nuevo repositorio en [GitHub.com](https://github.com/new) (puede ser público o privado, por ejemplo llamado `decide-app`).

3. Conecta y sube tus cambios:
   ```bash
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/decide-app.git
   git push -u origin main
   ```

---

### Paso 2: Crear el servicio en Render

1. Entra a tu cuenta en **[Render.com](https://dashboard.render.com/)**.
2. Haz clic en el botón azul **"New +"** (arriba a la derecha) y selecciona **"Web Service"**.
3. Selecciona **"Build and deploy from a Git repository"** y haz clic en **"Next"**.
4. Conecta tu cuenta de GitHub y elige tu repositorio `decide-app`.

---

### Paso 3: Confirmar los Parámetros en Render

Render detectará automáticamente la configuración, pero asegúrate de que estos campos coincidan:

| Campo | Valor |
| :--- | :--- |
| **Name** | `decide-emocional` (o el nombre que prefieras) |
| **Language** | `Python` |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app_web:app` |
| **Instance Type** | `Free` |

5. Haz clic en **"Deploy Web Service"** (o "Create Web Service").

---

### ⏱️ ¡Listo!

Render descargará las dependencias (`flask` y `gunicorn`), iniciará el servicio y en menos de 1 minuto te dará una URL pública con HTTPS gratuita:

🌐 **`https://decide-emocional.onrender.com`**

Cualquier persona desde cualquier celular, tablet o computadora podrá ingresar, registrarse, hacer las evaluaciones emocionales y ver sus resultados interactivos.

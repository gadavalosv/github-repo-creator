import os
import subprocess
from github import Github
from github.GithubException import BadCredentialsException
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import sha256

# Función para generar una clave basada en una contraseña
def generate_key(password):
    return urlsafe_b64encode(sha256(password.encode()).digest())

# Función para encriptar el token
def encrypt_token(token, key):
    fernet = Fernet(key)
    return fernet.encrypt(token.encode())

# Función para desencriptar el token
def decrypt_token(encrypted_token, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_token).decode()

# Función para leer el token encriptado desde un archivo local
def read_encrypted_token(password, token_file='github_token.enc'):
    # Obtener la ruta absoluta del directorio donde se encuentra el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(script_dir, token_file)
    if os.path.exists(token_path):
        try:
            with open(token_path, 'rb') as file:
                encrypted_token = file.read()
                key = generate_key(password)
                return decrypt_token(encrypted_token, key)
        except Exception as e:
            print("Error al desencriptar el token: ", e)
            return None
    return None

# Función para guardar el token encriptado en un archivo local
def save_encrypted_token(token, password, token_file='github_token.enc'):
    # Obtener la ruta absoluta del directorio donde se encuentra el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(script_dir, token_file)
    key = generate_key(password)
    encrypted_token = encrypt_token(token, key)
    with open(token_path, 'wb') as file:
        file.write(encrypted_token)
    print(f"Token encriptado y guardado con éxito en {token_path}.")

# Función para crear el repositorio en GitHub con opción de privacidad
def create_github_repo(repo_name, token):
    # Preguntar si el repositorio debe ser público o privado
    is_private = input(
        "¿Quieres que el repositorio sea privado? (s/n): ").lower().strip() == 's'

    try:
        g = Github(token)
        user = g.get_user()
        # Crear el repositorio con la opción de privacidad
        repo = user.create_repo(repo_name, private=is_private)
        print(
            f"Repositorio {repo_name} creado {'privado' if is_private else 'público'} en GitHub con éxito.")
        return repo.clone_url
    except BadCredentialsException:
        print("El token de acceso es inválido o ha expirado.")
        print("Por favor, genera un nuevo token en este enlace: https://github.com/settings/tokens")
        return None


# Preguntar el nombre del proyecto
project_name = input("Introduce el nombre del proyecto: ")

# Preguntar la contraseña para encriptar/desencriptar el token
password = input(
    "Introduce una contraseña para encriptar/desencriptar el token: ")

# Ruta donde se ejecutará el programa
current_path = os.getcwd()
project_path = os.path.join(current_path, project_name)

# Crear la carpeta del proyecto
if not os.path.exists(project_path):
    os.mkdir(project_path)
    print(f"Carpeta {project_name} creada con éxito.")
else:
    print(f"La carpeta {project_name} ya existe.")

# Inicializar Git localmente
os.chdir(project_path)
subprocess.run(["git", "init"])

# Crear archivo README.md
with open("README.md", "w") as readme:
    readme.write(f"# {project_name}")

# Hacer commit inicial
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])

# Leer token encriptado desde el archivo local
github_token = read_encrypted_token(password)

# Si no se encuentra un token válido, pedir uno nuevo
if not github_token:
    print("No se encontró un token de GitHub válido.")
    github_token = input("Por favor, introduce un nuevo token de GitHub: ")
    save_encrypted_token(github_token, password)

# Crear repositorio en GitHub y obtener la URL de clonación
remote_url = create_github_repo(project_name, github_token)

# Si no se pudo crear el repositorio, pedir un nuevo token
if not remote_url:
    github_token = input("Introduce el nuevo token de GitHub: ")
    save_encrypted_token(github_token, password)
    remote_url = create_github_repo(project_name, github_token)

# Añadir el remoto y hacer push si el repositorio fue creado
if remote_url:
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
    print(f"Repositorio subido a GitHub con éxito: {remote_url}")

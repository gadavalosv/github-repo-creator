# GitHub Repo Creator - Automate Local and Remote Repo Setup

Este script automatiza la creación de repositorios locales y remotos en GitHub. Te permite crear un repositorio localmente, agregar un commit inicial y subirlo automáticamente a tu cuenta de GitHub, con la opción de encriptar el token de autenticación para mayor seguridad.

## Características

- Crea un repositorio localmente con un commit inicial.
- Crea automáticamente un repositorio remoto en GitHub.
- Soporta la opción de crear repositorios públicos o privados.
- Encripta y almacena de manera segura el token de GitHub en un archivo.
- Detecta si el token ha expirado y te proporciona un enlace para generar uno nuevo.
- El token se puede actualizar sin necesidad de modificar el archivo de configuración manualmente.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- [PyGithub](https://pypi.org/project/PyGithub/) - Para interactuar con la API de GitHub.
- [cryptography](https://pypi.org/project/cryptography/) - Para la encriptación del token de GitHub.

### Instalación de dependencias

```bash
pip install PyGithub cryptography
```

## Uso

1. Clona el repositorio o descarga el script a tu máquina local.
   
2. Asegúrate de tener un **token de acceso personal** de GitHub. Puedes generarlo desde el siguiente enlace:
   - [Generar un nuevo token](https://github.com/settings/tokens)

3. Ejecuta el script:
   
   ```bash
   python github_repo_creator.py
   ```

4. Sigue las instrucciones en pantalla:
   - Introduce el nombre de tu proyecto.
   - Indica si el repositorio será público o privado.
   - Introduce tu **token de GitHub** la primera vez. El token se almacenará encriptado para futuras ejecuciones.

5. El script creará un repositorio localmente y lo subirá automáticamente a GitHub.

### Encriptación del Token

El token de GitHub se encripta utilizando una contraseña proporcionada por el usuario para mayor seguridad. Cada vez que ejecutes el script, deberás ingresar la misma contraseña para desencriptar el token.

Si el token caduca o no es válido, el script te pedirá que ingreses uno nuevo y actualizará el archivo encriptado.

## Opciones del Script

- **Privacidad del repositorio**: Se te preguntará si deseas que el repositorio sea público o privado.
- **Manejo de tokens**: Si el token almacenado es inválido o ha expirado, se te proporcionará un enlace para generar uno nuevo y actualizar el archivo.

## Licencia

Este proyecto está licenciado bajo la Licencia GPL v3. Para más detalles, consulta el archivo [LICENSE](LICENSE).

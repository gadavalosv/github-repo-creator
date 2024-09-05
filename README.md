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

## ¡Haz Fork y Contribuye!

Si encuentras útil este proyecto, ¡te invito a hacer un fork! Siéntete libre de mejorar el código, agregar funcionalidades o adaptarlo a tus necesidades. Todas las contribuciones son bienvenidas.

Para hacer un fork, simplemente haz clic en el botón de "Fork" en la parte superior de esta página y comienza a trabajar en tu versión del proyecto. ¡Espero ver tus aportaciones!

## Cómo Contribuir

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/tu-feature`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agregar nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/tu-feature`).
5. Abre un Pull Request.

Si tienes ideas, dudas o mejoras, no dudes en abrir un Issue. ¡La comunidad está aquí para apoyarte!

## Licencia

Este proyecto está licenciado bajo la Licencia Pública General de GNU v3, lo que significa que cualquier versión derivada debe ser de código abierto. Lee más en [LICENSE](./LICENSE).

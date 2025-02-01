
# Api para probar competencias tecnicas ?

 Este proyecto presenta una api desarrollada en django rest framework. Utiliza uv como herramienta de gestión de dependencias y entornos virtuales. Se incluye una bd sqlite que ha sido utilizada para probar la funcionalidad y cuenta con unos pocos datos de prueba.


 # Usando UV

 - uv se puede instalar desde el siguiente enlace https://docs.astral.sh/uv/getting-started/installation/
 - una vez instalado, ejecutar dependencias del proyecto con ```uv init```. Esto genera entornos automaticos e instala lo que contenga uv.lock.

 # Ejecutando Django

- Crear migraciones ```uv run python manage.py makemigrations```
- Ejecutar migraciones ```uv run python manage.py migrate```
- Terminado lo anterior, ejecutar ```uv run python manage.py runserver``` para levantar la app django.

# Bot de Telegram

- Una vez el servidor de django este levantado, ejecutar command ```uv run python manage.py telegram_bot``` para levantar el script que se comunica con la app de telegram, con el fin de listar los platos disponibles en la API.
- Dirigirse a la app de telegram y buscar el bot ```https://t.me/CapitalizarmeBot``` o ```@CapitalizarmeBot```. Una vez encontrado, iniciar la interaccion con el.
- El bot tiene disponibles 2 comandos ```/start``` y ```/platos``` que lista los platos disponibles en la API.


# Tests
- Ejecutar test unitarios con ```pytest -vv```
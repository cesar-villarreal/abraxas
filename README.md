ABRAXAS

La API fue desarrollada en Django, el framework de Python. Para su realización se utilizó la librería djangorestframework. Esta aplicación utiliza Green Unicorn como servidor HTTP WSGI. Su código se encuentra en Github y fue almacenada en un contenedor de Docker. Los datos de las tareas son almacenados en una base de datos MySql que está alojada en un servidor de GoDaddy y es administrada por el propio Django.




REGLAS DE NEGOCIO

Los campos en la base de datos son:
id: entero de incremento automático
task_id: Valor de identificación de la tarea de incremento automático considerando el valor más grande antes de la creación de una nueva tarea.
description: Cadena de caracteres definida por el usuario.
duration: Duración de la tarea en minutos especificada por el usuario.
created_at: Fecha y hora de la creación de la tarea.
updated_at: Fecha y hora de actualización de la tarea.
status: Cadena de caracteres con el estado de la tarea con valor predeterminado “pendiente”.
timespan: Valor determinado por la diferencia de tiempo entre la fecha y hora de actualización y la fecha y hora en que el estado de la tarea cambia a “completada”. Corresponde a el tiempo que el usuario utilizó para completar la tarea.

Tarea Completada:
Cuando se actualiza una tarea que ya tiene el status igual a “completada” se obtiene como respuesta el mensaje “Task already completed”. En este momento se calcula el timespan y se actualiza su valor en la base de datos.




ESPECIFICACIONES TÉCNICAS

El código de la aplicación junto con los requerimientos de librerías y el archivo para crear la imagen de Docker se encuentran en el repositorio https://github.com/cesar-villarreal/abraxas.git.

Debido a que se trabaja con Docker para poder desplegar la aplicación se considera que no es necesario realizar scripts para administrar el ciclo de vida de la aplicación ya que se cuenta con los comando de Docker para ello. Estos son:
Para ejecutar la aplicación a través del contenedor en segundo plano y redirigiendo el puerto 5001 al host:
docker run -dp 5001:5001 <app_name>

Para pausar el contenedor con la aplicación:
docker pause <app_name>

Para que el contenedor con su aplicación continúe con su tarea:
docker unpause <app_name>

Para detener el contenedor:
docker stop <app_name>

Para reiniciar el contenedor:
docker restart <app_name>

La aplicación se desplegó en un droplet de DigitalOcean con GNU/Linux Debian 10.
Para poder desplegar la aplicación es suficiente con ejecutar los siguientes comandos en el droplet y con permisos de superusuario:

# apt-get update
# apt-get -y upgrade
# apt-get -y install git docker.io
# git clone https://github.com/cesar-villarreal/abraxas.git
# cd abraxas
# docker build -t abraxas .
# docker run -dp 5001:5001 abraxas

La aplicación pública tiene el endpoint astrobits.xyz:5001/api/ Está en el puerto 5001 para mantener un poco de congruencia con el ambiente local en esta prueba técnica.




Referencias de la API

· Listas todas las tareas: GET task-list/
· Crea una tarea: POST task-create/
  Payload: JSON con los campos “description” y “duration”
· Actualizar una tarea: PUT task-update/<id>/
  Payload: JSON con los campos a actualizar
· Borrar una tarea: DEL task-delete/<id>/
· Listar tareas por status: GET task-status/<status>/
· Buscar tareas por palabra: GET tasks/search?q=<foo>
· Generar cincuenta tareas aleatorias: POST task-random/

Las credenciales de la base de datos y la secret key creada por Django se mantuvieron en el archivo settings.py en el repositorio de Github.




ToDo:

· Validación del campo status para admitir únicamente las cadenas “completada” o “pendiente”.
· Formatos de salida JSON y XML sin que sean cadenas de caracteres.

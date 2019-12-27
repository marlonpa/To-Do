# To-Do
To-do, creacion de tareas, asignacion, cambio de estado y lista de tareas, creacion de usuarios y lista.


# Paso para correr el la aplicacion
# Se instala python y agregamos las variables de entorno de python 
# Creacion de entorno virtual
  $ mkdir entorno
  $ cd entorno
  $ python -m venv "nombre entorno"

# Activar entorno
  $source "nombre entorno"/bin/activate

# Instalar pip en el entorno
  $python -m pip install --upgrade pip
  
# Instalar dependencias
  $pip install -r requirements.txt
  
# Clonamos el proyecto
 $git clone 'https://github.com/marlonpa/To-Do.git'
 
# Se crea base de datos en mysql
  mysql -u root -p
  create database todo;
 
# Corremos el proyecto
 $python manager.py makemigrations users agenda
 $python manager.py migrate
 $python manager.py createsuperuser
 $python manager.py runserver
 
# Abrimos navegador
  localhost:8000



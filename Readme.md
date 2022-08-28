#Recetario

##Descripción
Esta aplicación es un sencillo sistema de almacenamiento de recetas. Dicho programa está realizado con el framework Flask de python, con el framework de css Bootstrap4 y con el gestor de base de datos MySQL.

##Requisitos
- Versión de python3.7 o superior.
- Apache2 o Nginx.
- Paquete wsgi de Apache2.
- Gestor de base de datos, en este caso MySQL versión 8 o superior.

##Instrucciones
- En el archivo requirement.txt están las librerias necesarias para que la apliación funcione correctamente. Una vez instalado el paquete pip de python3 solo es necesario colocarse dentro del directorio que contiene la aplicación y ejecutar el siguiente comando "pip install -r requirement.txt.
- Esta instalación se puede ejecutar tanto en el sistema operativo como en un entorno virtual, de esta forma está programada la aplicación.
- Instalación del paquete wsgi => sudo apt-get install libapache2-mod-wsgi-py3.
- Si se usa un entorno virtual, hay que instalarlo previamente y crearlo. Para instalarlo => sudo pip3 install virtualenv. Para crearlo => virtualenv Recetario --python=python3.7

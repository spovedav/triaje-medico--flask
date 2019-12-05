# Triaje Medico > Python(Flask)  
### Autor: Stevyn Poveda
### Fecha: 02-11-2019
Este proyecto fue echo el en flask
python vs 3.8.0

#### Dependencia

cmd > pip install flask

cmd > pip install flask-socketio

cmd > pip install pymySQL

#### Conexion a la Base de datos
Como gestor de base de datos se uso MySQL(4.8.5) en el apache XAMPP(v3.2.3)
https://github.com/spovedav/triaje-medico--flask/tree/master/bd

#### Socket io
Unas partes trabaja con socket para enviar informacion en tiempo real 

Server: esta en el index.py

Cliente: esta en template/admision.html , template/panel_principal.html

###### cuando las chicas de admision hacen admisionan a un nuevo paciente para ese dia la informcion del pacinete se le envia al panel de todas las chicas de admision
Me falata la parte de los doctores, para que ellos puedan revisar y evolucionar al paciente. �

##### Usuario    Contrasena 
({"usuario":"admision","pass":"admision"},{"usuario":"doctor1","pass":"doctor1"},{"usuario":"doctor2","pass":"doctor2"},{"usuario":"doctor3","pass":"doctor3"})

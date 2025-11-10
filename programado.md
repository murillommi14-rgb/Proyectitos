# NUAM – Mantenedor de Calificaciones Tributarias

## entorno y estructura
- instalamos python, virtualenv y django  
- creamos el proyecto nuam_mantenedor con las apps core, calificaciones y auditoria  
- dejamos listas las carpetas templates y static  

## configuracion (settings.py)
- registramos nuestras apps en INSTALLED_APPS  
- idioma chileno y base de datos sqlite  
- activamos templates y static  
- agregamos el middleware para capturar usuario e ip  

## core (portada)
- hicimos la vista HomeView en core/views.py  
- creamos el template home.html en templates/core  
- la portada tiene links a admin y calificaciones  

## urls principales
- en urls conectamos las rutas:  
  - /admin es el panel de administracion  
  - / es la portada  
  - /calificaciones es el modulo calificaciones  

## calificaciones (modulo principal)
- armamos el modelo Calificacion con campos basicos: corredor, instrumento, año, monto, factores f8 a f19, estado y timestamps  
- pusimos la validacion de negocio: la suma de f8 a f19 no puede pasar de 1  
- registramos el modelo en el admin  
- creamos formularios y vistas para listar y crear  
- hicimos templates simples para la lista y para crear  
- corrimos las migraciones y probamos la validacion  

## auditoria (bitacora)
- armamos el modelo Auditoria para registrar cambios  
- guarda accion (creado, actualizado, eliminado), modelo, id del objeto, detalle, usuario, ip y navegador  
- agregamos middleware para capturar el request  
- hicimos señales para que cada vez que se guarde o borre una calificacion quede en la bitacora  
- registramos la auditoria en el admin y probamos que funciona  

## estado actual
- home funcionando en /  
- se pueden crear y listar calificaciones en /calificaciones/  
- la validacion de factores funciona (si la suma pasa de 1 tira error)  
- la auditoria registra usuario, ip y navegador en el admin  
- todo probado y corriendo bien  

## lo que falta por hacer
- filtros por año o corredor en la lista de calificaciones  
- exportar datos a excel o pdf  
- carga masiva desde csv o xlsx  
- roles y permisos (admin, analista, auditor)  
- mejorar la interfaz y el diseño  


## RECORDAR QUE TODO ESTA SUJETO A CAMBIOS, SI TIENEN MÁS IDEAS O ALGO PARA MEJORAR/CAMBIAR ALGO YA HECHO USTEDES HAGANLO PERO DOCUMENTEN O AVISEN EN ALGUN TEXTO NUEVO YA QUE ES NECESARIO Y NOS AYUDARA A TODOS A ENTENDER EL QUE ESTA PASANDO CON EL PROYECTO!!!
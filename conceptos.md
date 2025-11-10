# notas para entender mejor el proyecto (esto lo saque más facil de chatgpt pero es más que nada para una ayuda al momento de entender lo que estamos haciendo (para el grupo))

## que es una vista?
una vista es una función o clase en django que decide qué se muestra cuando alguien entra a una ruta (ejemplo: cuando entramos a "/" se muestra la portada) 
nosotros usamos **HomeView** (para la portada) y vistas de lista/crear para las calificaciones

## que son los templates?
los templates son los archivos .html donde ponemos el contenido que se va a ver en pantalla  
ejemplo: `home.html` es la portada, `lista.html` muestra las calificaciones, `crear.html` muestra el formulario

## que es un modelo?
un modelo es como una tabla en la base de datos, pero escrito en python
cada modelo se convierte en una tabla cuando corremos las migraciones
ejemplo: el modelo **Calificacion** se guarda en la base con todos sus campos

## que son las migraciones?
son archivos que django genera para crear o cambiar tablas en la base de datos 
cada vez que hacemos cambios en un modelo, corremos `makemigrations` y `migrate` para aplicar esos cambios en la base

## que es el admin?
es un panel que ya trae django por defecto para manejar los datos sin tener que programar nada extra 
nosotros lo usamos para crear, ver o borrar registros de Calificaciones y para revisar la Auditoria

## que son las señales?
las señales son como "ganchos" que se disparan cuando pasa algo en la base de datos  
por ejemplo: si se guarda o borra una Calificacion, se ejecuta automáticamente nuestro código que crea un registro en la Auditoria
gracias a esto, no necesitamos acordarnos de llamar a la bitácora, django lo hace solo con las señales

## que es el middleware?
es como un "filtro" que corre en cada request y respuesta  
nosotros hicimos uno para guardar temporalmente el request actual y así saber qué usuario hizo la acción, cuál es su ip y navegador
esto es lo que nos permitió dejar esos datos en la Auditoria

## que es la validacion de negocio?
es una regla que nos inventamos y que el sistema debe respetar siempre
en este caso: la suma de los factores f8 a f19 no puede ser mayor que 1 
si alguien intenta guardar algo que rompe esta regla, django muestra un error y no lo guarda


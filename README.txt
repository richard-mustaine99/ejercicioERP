======================================INTRODUCCIÓN====================================
El siguiente proyecto corresponde a Richard Castro y ha sido realizado utilizando python 3.8.7 y la base de datos SqlLite.
Las tablas utilizadas para este proyecto corresponden a Empresa, Contacto y Relaciones. Esta ultima se utiliza para guardar la relacion existente entre la id de la empresa y la id de contacto. (Revisar archivo models.py para ver detalle)
*Se asume que el usuario ya sabe como prender el server e iniciar el sistema, por ende no se agregan instrucciones de como hacerlo

======================================FUNCIONALIDADES==================================
Este proyecto cuenta con las siguientes funcionalidades:

-Login de usuario. Si este no posee cuenta tiene la opción para crearse una cuenta.

-Vista para ver todas las empresas registradas en una tabla.

-Vista para ver todos los contactos registrados en una tabla.

-Posee las opciones para editar y eliminar tanto una empresa como un contacto por medio de los botones que se encuentran en la tabla.

-Para ser mas especifico en cuanto a la dirección, mediante un archivo json se recuperan todas las regiones, provincias y comunas de Chile. De esta forma, el usuario al seleccionar una región, desplegará un select de provincias correspondientes a la seleccionada. Lo mismo ocurre con la comuna, al seleccionar una provincia, se desplegará un nuevo select con las comunas correspondientes.

-El sistema está hecho de tal forma que, para asignar un nuevo contacto a una empresa debe:
-Primero, debe estar creada la empresa.
-Segundo, el contacto debe estar registrado en el sistema
-Una vez se cumplen los dos pasos anteriores, al editar una empresa, aparece un navtab en la parte superior llamada "Contactos". Al pinchar alli, se desplegaran en una tabla todos los contactos que tiene asignada la empresa, en caso de no existir, se despleiga un mensaje. Para agregar uno nuevo, debe apretar el botón de "Agregar contacto". Esto abrirá una ventana modal con un select en donde apareceran todos los contactos registrados en el sistema.

======================================VALIDACIONES====================================
-Todos los campos son obligatorios.
-Formateo automatico de rut
-Validaciones de campos (Por ejemplo, deja ingresar solo numeros en telefono o solo letras en nombre)
-Si el rut de un contacto ya existe, mostrará mensaje de error y no se creará.
-Si el rut de una empresa ya existe, mostrará mensaje de error y no se creará.
-Si al asignar un nuevo contacto, este ya se encuentra asignado, mostrará mensaje de error y no se asignará nuevamente.
-Si un usuario no está autenticado e intenta ingresar a alguna sección del sistema, arrojará mensaje de "Usuario no autenticado", no mostrará nada de información de la página y redirigirá al login.

======================================CREDENCIALES====================================
*******SUPERADMIN*********
Username: ecos
email: superadminecos@gmail.com
pass: ecospass123
*******USUARIO************
Username: ecosuser
email: userecos@gmail.com
Pass: userpass321



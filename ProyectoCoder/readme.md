##  Pre-entrega proyecto final: Coderhouse / Python
### Alumno: Nahuel Zeballos

#### Acceso al admin:
- Usuario: Tutor
- Contraseña: coder1234

	####  URL principal:
- http://127.0.0.1:8000/AppCoder/inicio/
- Desde allí mediante herencias se accede a todo el resto de URLs, las cuales contienen los diversos formularios de carga y busqueda, que cuentan con sus respectivas clases y modelos.
#### Funcionalidades:
- Partiendo de la template inicio, se dara acceso al resto de templates mediante una barra de navegación, esta template  cuenta con un condicional if, que dependiendo el número de página (ingresado mediante un contexto en las views) definira el titulo a mostrarse.
- Cada sección cuenta con un formulario, ya sea para cargar estudiantes, profesores, cursos y entregables, cada form está realizado con las api´s de Django.
- Por otra parte, en la sección busqueda, se encuentra un form de tipo GET, el cual sirve especificamente para realizar una busqueda por cursos, está sección cuenta tambien con un link volver para realizar una nueva busqueda.
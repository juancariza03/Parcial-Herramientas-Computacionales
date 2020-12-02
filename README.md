# Parcial Final Herramientas Computacionales
### Definición

El algoritmo permite al usuario de la universidad adquirir un descuento en cafetería al comprar artículos
dependiendo de su rol en esta.

Para la solución del problema trabajado en el algoritmo, se implementaron funciones que contenían métodos,
condiciones, variables, arreglos e impresiones de texto. Aparte también se dio uso a la recursividad.

### Contrato

1. **Entradas**: 
	- Cedula del cliente
	- Rol del cliente
	- Artículos que va a comprar el cliente
2. **Salidas**: 
	- Precio cada artículo
	- Precio total
	- Texto compra realiza con cédula
	- Rol
	- Productos comprados

### Funciones:

- inicializarDiccionario(): Tiene el arreglo que contiene los artículos de la cafetería
- inicializarRoles(): Tiene el arreglo que contiene los roles de la universidad
- comprarProducto(): Tiene todo el proceso para hacer el registro de que se va a comprar y en cuanta cantidad
- obtenerPrecio(): Tiene como entrada los artículos, el rol del usuario y su cédula, retorna estos mismos,
junto con sus artículos comprados, el precio de cada artículo y el precio total de su compra.
- main(): La parte central del código que se encarga de ejecutar cada una de las funciones implementadas y de hacer
la verificación inicial de que todas las entradas estén correctas, antes de ejecutar las funciones.	

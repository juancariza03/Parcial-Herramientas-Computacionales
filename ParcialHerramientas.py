def main():
    global productos,roles
    inicializarRoles()
    while(True):
        try:
            cedula=int(input("Ingrese su cedula "))
            if(cedula<1):
                raise ValueError
            break
        except ValueError:
            print("Eso no es un numero valido")
    while(True):
        rol=str(input("Ingrese su rol en la universidad "))
        rol= rol.capitalize()
        if rol in roles:
            break
        else:
            print("Este rol no existe")
    productos= dict()
    inicializarDiccionario()
    articulos=comprarProducto()
    obtenerPrecio(articulos, rol, cedula)
    
def inicializarDiccionario():
    global productos
    productos["Papas"]=[1, 2500]
    productos["Gaseosa"]=[2, 2000]
    productos["Perro"]=[3, 5000]
    productos["Pizza"]=[4, 6000]
    productos["Galletas"]=[5, 1200]
    productos["Chicle"]=[6, 200]
    productos["Paleta"]=[7, 1500]
def inicializarRoles():
    global roles
    roles=["Profesor", "Estudiante"]

def comprarProducto():
    global productos, roles
    for i in productos:
        print(i,"......",productos[i])
    
    while(True):
        try:
            cantidadArticulos=int(input("Cuantos articulos desea comprar? "))
            if(cantidadArticulos<1):
                raise ValueError
            break
        except ValueError:
            print("Eso no es un numero valido")
    articulosAComprar=[]
    for i in range(cantidadArticulos):
        articulo=str(input("Ingrese el nombre del articulo que desea comprar: "))
        articulo= articulo.capitalize()
        while(True):            
            if articulo in productos:
                try:
                    cantidadDeArticulo=int(input("Ingrese la cantidad de " + articulo + " desea comprar "))
                    if(cantidadDeArticulo<1):
                        raise ValueError
                    articulosAComprar.append([cantidadDeArticulo, articulo])
                    break
                except ValueError:
                    print("Eso no es un numero valido")
            else:
                print("Este articulo no existe")
                articulo=str(input("Ingrese el nombre del articulo que desea comprar: "))
    return articulosAComprar
def obtenerPrecio(articulos, rol, cedula):
    global productos
    if(rol=="Estudiante"):
        descuento=0.5
    elif(rol=="Profesor"):
        descuento=0.8
    total=0
    for i in articulos:
        codigo=productos[i[1]][0]
        precioArticulo=productos[i[1]][1] * descuento
        cantidadDeArticulo=i[0]
        precio= precioArticulo*cantidadDeArticulo
        print("El", rol, "con cedula", cedula,", debe pagar", precioArticulo, "por el producto", codigo, "y son", cantidadDeArticulo, "unidades, para un total de", precio)
        total+=precio
    print("El precio total es:", total)
main()

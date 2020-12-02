def main():
    global productos,roles
    inicializarRoles()
    cedula=int(input("Ingrese su cedula "))
    while(True):
        rol=str(input("Ingrese su rol en la universidad "))
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
    cantidadArticulos=int(input("Cuantos articulos desea comprar? "))
    articulosAComprar=[]
    for i in range(cantidadArticulos):
        articulo=str(input("Ingrese el nombre del articulo que desea comprar: "))
        while(True):            
            if articulo in productos:
                cantidadDeArticulo=int(input("Ingrese la cantidad de " + articulo + " desea comprar "))
                articulosAComprar.append([cantidadDeArticulo, articulo])
                break
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

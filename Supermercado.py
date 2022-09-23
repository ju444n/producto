print(*** MENU ***)
print("1. Recibir info de un producto")
print("2. Mostrar todos los productos registrados")
print("3. Buscar producto por codigo y editar el precio")
print("4. Buscar por codigo un producto y eliminarlo")
print("5. Cerrar programa")
opcion=100

compras=[]

while(opcion!=6):
    compras={}
    opcion = int(input("Elija una opcion"))

    if(opcion==1):
        compra={}
            compra['nombre']=input("Digite el nombre del producto: ")
            compra['codigo']=input("Digite el codigo del producto: ")
            compra['precio']=input("Digite el precio del producto: ")
            compras.append(compra)
    
    elif(opcion==2):

        if len(compras)>0:
            for compra in compras:
                print(f"El producto: {producto['nombre']} de código: {producto['codigo']} Cuesta: {producto['precio']}")

        else:
            print("El carrito esta vacio")
    
    elif(opcion==3):
        if len(compras)>0
            codigo=input("Digite el codigo del producto para cambiar de precio: ")
            valornuevo=input("Digite el nuevo valor del producto: ")
            for c in compras:
                if c['codigo']==codigo:
                    c['precio']==valornuevo:
                        print(f"El producto: {c['nombre']} ahora cuesta : {valornuevo}")

    else:
        print("Este codigo del producto no existe")

    elif(opcion==4):
        if len(compras)>0:
            codigo=input("Digite el codigo del producto para ELIMINAR: ")
            i=0
            for c in compras:
                if c['codigo']==codigo:
                    e=int(input(f"Desea eliminar el producto {c['nombre']} SI= 1 o NO= 0"))
                    if e==1:
                        productos.pop(i)
                        print("Producto eliminado")
                    else:
                        print("NO se ha eliminado el producto")
                i+=1
        else:
            print("Este codigo de producto no existe")
    
    elif(opcion==5)
        print("Cerrando programa...")
        opcion=0

    else:
        print("Digite una opcion valida" )

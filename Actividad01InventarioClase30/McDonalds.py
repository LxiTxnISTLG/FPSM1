inventario = [{"Nombre":"McFlurry", "precio":2.50, "stock":10}]

def menu_principal():
    """
    Muestra el menú principal 
    """
    while True:
        print(" Menú Principal ")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender Producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":    
            vender_producto()
        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente otra vez por favor ")

def agregar_producto():
    """
    Agregar un nuevo producto al inventario
    """
    
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de producto: "))
    
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    
    inventario.append(producto)
    
    print(f"Producto {nombre} agregado al inventario")
    print(inventario)

def mostrar_inventario():
    """
    Muestra todos los productos del inventario
    """
    
    if len(inventario) == 0:
        print("El inventario está vacío")
    else:
        print("Presentando inventario")
        
        for producto in inventario:
            print(f"Nombre:{producto["nombre"]}, Precio: {producto['precio']:.2f}, cantidad: {producto['stock']}")

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta 
    """
    
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    
    for producto in inventario:
        if producto['nombre'].lower() == nombre.lower():
           cantidad = int(input(f"¿Cuantas unidades de {nombre} desea vender?: "))
           if cantidad <= producto["stock"]:
               producto["stock"] -= cantidad
               total = cantidad * producto["precio"]
               print(f"Venta realizada. Total: ${total:.2f}")
               
               if producto["stock"] == 0:
                   print(f"El producto {nombre} se ha agotado. ")
                   
               return
           else:
               print("No hay suficiente stock en inventario")
               return
           
    print("Producto no encontrado en el inventario")

menu_principal()
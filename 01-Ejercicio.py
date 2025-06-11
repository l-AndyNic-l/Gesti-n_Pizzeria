# Sistema de Gestión de Pedidos para una Pizzería.

# Menu con las siguientes opciones: 
# Registrar nuevos productos: precio unitario, stock disponibles, INGREDIENTES
# Tomar pedidos: Descontar del  stock, calcular compra | nombre cliente, pizza comprada, cantidad y el total pagado
# Calcular totales: calcular compra y ventas del dia.
# Registro de ventas realizadas: mostrar que pizzas se vendieron, cuuantas y el total.

import os, msvcrt

menu = """------------------------- M E N Ú -------------------------
1) Registrar nuevas pizzas disponibles para la venta.
2) Ver el cátalogo de pizzas.
3) Ingresar el pedido.
4) Ver los pedidos realizados.
5) Salir.
-----------------------------------------------------------
"""

tipos_masas = """*** Tipos de masas ***
1) Napolitana.
2) Americana.
3) Romana.
4) Italiana.
"""

masas = ( "Napolitana", "Romana", "Italiana", "Americana" )

pizzas = [
    {
        "codigo": 7811,
        "nombre": "Pepperoni",
        "ingredientes": [ "Salsa De Tomate", "Queso Parmesano", "Pepperoni" ],
        "tipo_masa": "Napolitana",
        "precio": 13900,
        "stock": 20
    },
        {
        "codigo": 7812,
        "nombre": "Canadian Bacon",
        "ingredientes": [ "Salsa De Tomate", "Queso Mozzarella", "Lomito Canadiense", "Tocino", "Queso Parmesano", "Queso Romano" ],
        "tipo_masa": "Romana",
        "precio": 15990,
        "stock": 15
    },
        {
        "codigo": 7813,
        "nombre": "Margarita",
        "ingredientes": [ "Salsa De Tomate", "Queso Mozzarella", "Albahaca", "Pimienta Negra", "Aceite Oliva" ],
        "tipo_masa": "Italiana",
        "precio": 19990,
        "stock": 10
    },
]

while True:
    os.system( "cls" )
    print( menu )

    opcion = input( "Ingrese una opción: " )

    if opcion == "1":
        os.system( "cls" )
        print( "----- Registrar Nueva Pizza -----" )

        codigo = int( input( "Ingrese el codigo: " ) )
        nombre = input( "Ingrese el nombre: " )

        print( tipos_masas )
        tipo_masa = int( input( "Ingrese el número de la masa: " ) )
        masa = masas[ tipo_masa - 1 ]

        precio = int( input( "Ingrese el precio unitario: " ) )
        stock = int( input( "Ingrese el stock disponible" ) )

        pizza = {
            "codigo": codigo,
            "nombre": nombre,
            "tipo_masa": masa,
            "precio": precio,
            "stock": stock
        }

        pizzas.append( pizza )

        print( "Pizza registrada exitosamente!" )

    elif opcion == "2":
        pass

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        print( "Gracias, hasta pronto!" )
        break

    else:
        print( "ERROR! Ingrese una opción válida." )

    print( "Precione una tecla para continuar." )
    msvcrt.getch()
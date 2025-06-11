# Sistema de Gestión de Pedidos para una Pizzería.

# Menu con las siguientes opciones: 
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
2) Americana.
4) Italiana.
1) Napolitana.
3) Romana.
"""

masas = ( "Americana",  "Italiana", "Napolitana", "Romana" )

pizzas = [
    {
        "codigo": 7811,
        "nombre": "Pepperoni",
        "tipo_masa": "Napolitana",
        "precio": 13900,
        "stock": 20
    },
        {
        "codigo": 7812,
        "nombre": "Canadian Bacon",
        "tipo_masa": "Romana",
        "precio": 15990,
        "stock": 15
    },
        {
        "codigo": 7813,
        "nombre": "Margarita",
        "tipo_masa": "Italiana",
        "precio": 19990,
        "stock": 10
    },
]

ventas_dia = []

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
        stock = int( input( "Ingrese el stock disponible: " ) )

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
        os.system( "cls" )
        print( "----- Cátalogo de Pizzas -----" )

        contador_catalogo = 0
        
        for p in pizzas:

            contador_catalogo = contador_catalogo + 1
            print( f"{ contador_catalogo }) Nombre: { p[ "nombre" ] } | T.Masa: { p[ "tipo_masa" ] } | Precio: ${ p[ "precio" ] } | Stock: { p[ "stock" ] }" )

    elif opcion == "3":
        os.system( "cls" )
        print( "----- Realizar Pedido -----" )

        nombre_user = input( "Ingrese el nombre del cliente: " )
        nombre_pizza = input( "Ingrese el nombre de la pizza: " )

        for p in pizzas:

            if p[ "nombre" ] == nombre_pizza:

                cantidad_comprar = int( input( "Ingrese la cantidad de pizzas que comprara: " ) )

                if p[ "stock" ] >= cantidad_comprar:

                    p["stock"] = p["stock"] - cantidad_comprar

                    total = p["precio"] * cantidad_comprar

                    print( f"El total del pedido de pizzas de { p['nombre'] } es de ${ total }." )

                    venta = {
                        "nombre": nombre_user,
                        "pizza": p[ "nombre" ],
                        "cantidad": cantidad_comprar,
                        "total": total
                    }

                    ventas_dia.append( venta )

                    print( "Compra realizada con exito!" )

                    break

                else:
                    print( "La cantidad que desea comprar supera al stock." )  

    elif opcion == "4":
        os.system( "cls" )
        print( "----- Ver los Pedidos Realizados -----" )

        if len( ventas_dia ) == 0:
            print( "No se han realizado ventas." )

        else:

            contador_ventas = 0
            acumulador = 0
        
            for v in ventas_dia:

                acumulador = acumulador + v[ "total" ]
                contador_ventas = contador_ventas + 1
                print( f"{ contador_catalogo }) Usuario: { v[ "nombre" ] } | Pedido: { v[ "cantidad" ] } pizzas de { v[ "pizza" ] } | Total: ${ v[ "total" ] }")

            print( f"Ventas totales: ${ acumulador }." )

    elif opcion == "5":
        print( "Gracias, hasta pronto!" )
        break

    else:
        print( "ERROR! Ingrese una opción válida." )

    print( "Precione una tecla para continuar." )
    msvcrt.getch()
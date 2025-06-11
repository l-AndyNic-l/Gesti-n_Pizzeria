# Sistema de Gestión de Pedidos para una Pizzería.

import os, msvcrt

menu = """------------------------- M E N Ú -------------------------
1) Registrar nuevas pizzas disponibles para la venta.
2) Ver el cátalogo de pizzas.
3) Ingresar el pedido.
4) Ver los pedidos realizados.
5) Salir.
-----------------------------------------------------------
"""

tipos_masas = """\n*** Tipos de masas ***
2) Americana.
4) Italiana.
1) Napolitana.
3) Romana."""

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

    opcion = input( "* Ingrese una opción: " )

    if opcion == "1":
        os.system( "cls" )
        print( "----- Registrar Nueva Pizza -----" )

        while True:
            try:
                codigo = int( input( "\n* Ingrese el codigo: " ) )
                codigo_existe = False

                if codigo > 0:

                    for p in pizzas:

                        if p[ "codigo" ] == codigo:

                            codigo_existe = True
                            print( "ERROR! Este código ya esta registrado." )
                            break
                
                if codigo_existe == False:
                    break
            
            except:
                print( "ERROR! Ingrese un código válido." )

        while True:
            try:
                nombre = input( "\n* Ingrese el nombre: " ).strip().title()
                nombre_existe = False

                if len( nombre ) >= 4:

                    for p in pizzas:

                        if p[ "nombre" ] == nombre:

                            nombre_existe = True
                            print( "ERROR! Este nombre ya esta registrado." )
                            break
                
                else:
                    print( "ERROR! El nombre de la pizza debe ser mayor a 3 caracteres." )
                
                if nombre_existe == False:
                    break
            
            except:
                print( "ERROR! Ingrese un nombre válido." )

        print( tipos_masas )

        while True:
            try:
                tipo_masa = int( input( "\n* Ingrese el número de la masa: " ) )

                if tipo_masa >= 0 and tipo_masa <= 3:

                    masa = masas[ tipo_masa - 1 ]
                    break

                else:
                    print( "ERROR! Ingrese una opción dentro del rango." )

            except:
                print( "ERROR! Ingrese una opción válida." )

        while True:
            try:
                precio = int( input( "\n* Ingrese el precio unitario: " ) )

                if precio >= 3000:
                    break

                else:
                    print( "ERROR! Debe ingresar un precio como minimo de $3000." )

            except:
                print( "ERROR! Ingrese un precio válido." )

        while True:
            try:
                stock = int( input( "\n* Ingrese el stock disponible: " ) )

                if stock >= 1:
                    break

                else:
                    print( "ERROR! Debe ingresar un stock mayor a 0." )

            except:
                print( "ERROR! Ingrese un stock válido." )

        pizza = {
            "codigo": codigo,
            "nombre": nombre,
            "tipo_masa": masa,
            "precio": precio,
            "stock": stock
        }

        pizzas.append( pizza )

        print( "\n|-- Pizza registrada exitosamente! --|" )

    elif opcion == "2":
        os.system( "cls" )
        print( "----- Cátalogo de Pizzas -----\n" )

        contador_catalogo = 0
        
        for p in pizzas:

            contador_catalogo = contador_catalogo + 1
            print( f"{ contador_catalogo }) Nombre: { p[ "nombre" ] } | T.Masa: { p[ "tipo_masa" ] } | Precio: ${ p[ "precio" ] } | Stock: { p[ "stock" ] }" )

    elif opcion == "3":
        os.system( "cls" )
        print( "----- Realizar Pedido -----" )

        while True:
            try:
                nombre_user = input( "\n* Ingrese el nombre del cliente: " )

                if len( nombre_user ) >= 3:
                    break

                else:
                    print( "ERROR! El nombre debe ser mayor a 2 caracteres." )

            except:
                print( "ERROR! Ingrese un nombre válido." )

        while True:
            try:
                nombre_pizza = input( "\n* Ingrese el nombre de la pizza: " ).strip().title()
                pizza_existe = False


                if len( nombre_pizza ) >= 4:

                    for p in pizzas:

                        if p[ "nombre" ] == nombre_pizza:

                            pizza_existe = True
                            
                            while True:
                                try:
                                    cantidad_comprar = int( input( "\n* Ingrese la cantidad de pizzas que comprara: " ) )

                                    if cantidad_comprar >= 1:
                                        break
                                
                                except:
                                    print( "ERROR! Ingrese una cantidad válida." )

                            if p[ "stock" ] >= cantidad_comprar:

                                p["stock"] = p["stock"] - cantidad_comprar

                                total = p["precio"] * cantidad_comprar

                                print( f"\nEl total del pedido de pizzas de { p['nombre'] } es de ${ total }." )

                                venta = {
                                    "nombre": nombre_user,
                                    "pizza": p[ "nombre" ],
                                    "cantidad": cantidad_comprar,
                                    "total": total
                                }

                                ventas_dia.append( venta )

                                print( "\n|-- Compra realizada con exito! --|" )

                                break

                            else:
                                print( "ERROR! La cantidad que desea comprar supera al stock." )  

                        if pizza_existe == False:
                            print( "ERROR! La pizza no existe." )
                            break

                        else:
                            print( "ERROR! El nombre de la pizza debe ser mayor a 3 caracteres." )

            except:
                print( "ERROR! Ingrese un nombre de pizza válido." )


    elif opcion == "4":
        os.system( "cls" )
        print( "----- Ver los Pedidos Realizados -----\n" )

        if len( ventas_dia ) == 0:
            print( "|-- No se han realizado ventas --|" )

        else:

            contador_ventas = 0
            acumulador = 0
        
            for v in ventas_dia:

                acumulador = acumulador + v[ "total" ]
                contador_ventas = contador_ventas + 1
                print( f"{ contador_ventas }) Usuario: { v[ "nombre" ] } | Pedido: { v[ "cantidad" ] } pizzas de { v[ "pizza" ] } | Total: ${ v[ "total" ] }")

            print( f"Ventas totales: ${ acumulador }." )

    elif opcion == "5":
        print( "\n|-- Gracias, hasta pronto! --|" )
        break

    else:
        print( "ERROR! Ingrese una opción válida.\n" )

    print( "\n\n***** Presione una tecla para continuar *****" )
    msvcrt.getch()
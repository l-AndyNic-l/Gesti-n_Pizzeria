# Sistema de Gestión de Pedidos para una Pizzería.

# Menu con las siguientes opciones: 
# Registrar nuevos productos: Codigo, Nombre, Tipo de Masa, precio unitario, stock disponibles, INGREDIENTES
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

while True:
    os.system( "cls" )
    print( menu )

    opcion = input( "Ingrese una opción: " )

    if opcion == "1":
        pass

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
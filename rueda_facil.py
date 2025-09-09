#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Facturación para Tienda de Llantas "Rueda Fácil"
Autor: Sistema de Facturación
Fecha: 2025
"""

def calcular_precio_unitario(cantidad_llantas):
    """
    Calcula el precio unitario según la cantidad de llantas compradas.
    
    Args:
        cantidad_llantas (int): Número de llantas a comprar
    
    Returns:
        int: Precio unitario en pesos
    """
    if cantidad_llantas < 5:
        return 35000
    elif cantidad_llantas <= 10:  # Entre 5 y 10 (inclusive)
        return 40000
    else:  # Más de 10 llantas
        return 45000

def procesar_cliente(numero_cliente):
    """
    Procesa la compra de un cliente individual.
    
    Args:
        numero_cliente (int): Número del cliente
    
    Returns:
        dict: Información del cliente y su compra
    """
    print(f"\n--- CLIENTE #{numero_cliente} ---")
    
    # Solicitar cantidad de llantas con validación
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido")
    
    # Calcular precios
    precio_unitario = calcular_precio_unitario(cantidad)
    total_pagar = cantidad * precio_unitario
    
    # Mostrar factura del cliente
    print(f"\n{'='*40}")
    print(f"FACTURA - CLIENTE #{numero_cliente}")
    print(f"{'='*40}")
    print(f"Cantidad de llantas: {cantidad}")
    print(f"Precio unitario: ${precio_unitario:,}")
    print(f"Total a pagar: ${total_pagar:,}")
    print(f"{'='*40}")
    
    return {
        'cliente': numero_cliente,
        'cantidad': cantidad,
        'precio_unitario': precio_unitario,
        'total': total_pagar
    }

def mostrar_resumen_ventas(ventas):
    """
    Muestra un resumen general de todas las ventas del día.
    
    Args:
        ventas (list): Lista con información de todas las ventas
    """
    print(f"\n{'='*50}")
    print("RESUMEN DE VENTAS DEL DÍA - RUEDA FÁCIL")
    print(f"{'='*50}")
    
    total_llantas = sum(venta['cantidad'] for venta in ventas)
    total_ingresos = sum(venta['total'] for venta in ventas)
    
    print(f"Total de clientes atendidos: {len(ventas)}")
    print(f"Total de llantas vendidas: {total_llantas}")
    print(f"Total de ingresos: ${total_ingresos:,}")
    print(f"Promedio por cliente: ${total_ingresos // len(ventas):,}")
    print(f"{'='*50}")

def main():
    """
    Función principal del programa de facturación.
    """
    print("=" * 50)
    print("SISTEMA DE FACTURACIÓN - RUEDA FÁCIL")
    print("=" * 50)
    
    # Solicitar número de clientes con validación
    while True:
        try:
            num_clientes = int(input("Ingrese el número de clientes a atender: "))
            if num_clientes <= 0:
                print("Error: Debe atender al menos 1 cliente")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido")
    
    # Lista para almacenar información de ventas
    ventas_del_dia = []
    
    # Procesar cada cliente usando un bucle for
    for cliente in range(1, num_clientes + 1):
        venta = procesar_cliente(cliente)
        ventas_del_dia.append(venta)
        
        # Preguntar si desea continuar (excepto en el último cliente)
        if cliente < num_clientes:
            continuar = input("\n¿Presione ENTER para continuar con el siguiente cliente...").strip()
    
    # Mostrar resumen final
    mostrar_resumen_ventas(ventas_del_dia)
    
    print("\n¡Gracias por usar el Sistema de Facturación Rueda Fácil!")

# Ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()

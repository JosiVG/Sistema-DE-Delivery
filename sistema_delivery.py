total_pedidos = 0
pedidos_entregados = 0
pedidos_pendientes = 0
recaudacion_total = 0.0

pedidos_zona_norte = 0
pedidos_zona_sur = 0
pedidos_zona_centro = 0

def validar_monto():
    """Valida que el importe sea un número positivo."""
    continuar_validacion = True
    while continuar_validacion:
        monto_input = input("Ingrese el importe del pedido: $")
        
        # Validación: verifica si el texto ingresado es numérico
        if monto_input.replace('.', '', 1).isdigit():
            monto = float(monto_input)
            if monto > 0:
                return monto
            else:
                print("? Error: El monto debe ser mayor a cero. Intente de nuevo.")
        else:
            print("? Error: Entrada inválida. Ingrese solo números (ej: 1450 o 350.50).")
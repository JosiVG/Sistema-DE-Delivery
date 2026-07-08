# TRABAJO FINAL INTEGRADOR - SISTEMA DE DELIVERY
# INTEGRANTES: Guinea Josias Vicente, Herrmann Benasayag Mateo, Romero Pasetto Alejo | COMISION: D - K1.4

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

        if monto_input.replace('.', '', 1).isdigit():
            monto = float(monto_input)
            if monto > 0:
                return monto
            else:
                print(" Error: El monto debe ser mayor a cero. Intente de nuevo.")
        else:
            print(" Error: Entrada inválida. Ingrese solo números (ej: 1450 o 350.50).")

def validar_zona():
    """Valida que la zona ingresada sea correcta."""
    continuar_validacion = True
    while continuar_validacion:
        print("Zonas de reparto: [N]orte | [S]ur | [C]entro")
        zona = input("Seleccione la zona (N/S/C): ").upper().strip()        
        if zona == "N" or zona == "S" or zona == "C":
            return zona
        else:
            print("Error: Zona no válida. Debe ingresar N, S o C.")

def registrar_pedido():
    """Registra el pedido aumentando los contadores y acumuladores correspondientes."""
    global total_pedidos, pedidos_pendientes, recaudacion_total
    global pedidos_zona_norte, pedidos_zona_sur, pedidos_zona_centro

    print("--- REGISTRAR NUEVO PEDIDO ---")
    
    monto = validar_monto()
    zona = validar_zona()
    
    total_pedidos = total_pedidos + 1
    pedidos_pendientes = pedidos_pendientes + 1
    recaudacion_total = recaudacion_total + monto
    
    if zona == "N":
        pedidos_zona_norte = pedidos_zona_norte + 1
        zona_texto = "Norte"
    elif zona == "S":
        pedidos_zona_sur = pedidos_zona_sur + 1
        zona_texto = "Sur"
    else:
        pedidos_zona_centro = pedidos_zona_centro + 1
        zona_texto = "Centro"
        
    print(f"¡Pedido #{total_pedidos} registrado exitosamente!")
    print(f"Importe: ${monto:.2f} | Zona asignada: {zona_texto} | Estado: Pendiente")


def controlar_entregas():
    """Gestiona el cambio de estado de los pedidos pendientes."""
    global pedidos_pendientes, pedidos_entregados
    
    print("--- CONTROL DE ENTREGAS ---")
    
    if pedidos_pendientes == 0:
        print(" No hay pedidos pendientes de entrega en este momento.")
        return

    print(f"Estado logístico: Hay {pedidos_pendientes} pedido(s) pendientes 'En camino'.")
    
    while True:
        confirmar = input("¿Desea despachar y marcar como 'ENTREGADO' el próximo pedido? (S/N): ").upper().strip()
        
        if confirmar == "S":
            pedidos_pendientes = pedidos_pendientes - 1
            pedidos_entregados = pedidos_entregados + 1
            print("[Simulación] El cadete fue al domicilio...")
            print("¡Éxito! El pedido ha cambiado al estado de: ENTREGADO.")
            break
        elif confirmar == "N":
            print("Operación cancelada. El pedido sigue marcado como 'Pendiente'.")
            break
        else:
            print("Entrada incorrecta. Ingrese S para confirmar o N para cancelar.")


def mostrar_estadisticas():
    """Muestra el reporte detallado usando los contadores y acumuladores."""
    print("---  ESTADÍSTICAS Y REPORTES DE VENTAS ---")
    
    if total_pedidos == 0:
        print(" Sin datos. Registre pedidos primero para ver las estadísticas.")
        return
        
    print(f" Total de pedidos registrados históricamente: {total_pedidos}")
    print(f" Pedidos entregados exitosamente: {pedidos_entregados}")
    print(f" Pedidos pendientes de entrega: {pedidos_pendientes}")
    print(f" Recaudación total acumulada: ${recaudacion_total:.2f}")
    
    promedio_ventas = recaudacion_total / total_pedidos
    print(f"Importe promedio por pedido: ${promedio_ventas:.2f}")
    
    print("Cantidad de pedidos por zonas de reparto:")
    print(f"- Zona Norte: {pedidos_zona_norte} pedido(s)")
    print(f"- Zona Sur: {pedidos_zona_sur} pedido(s)")
    print(f"- Zona Centro: {pedidos_zona_centro} pedido(s)")


def mostrar_menu():
    """Imprime las opciones en la consola."""
    print("-"*30)
    print("       SISTEMA DE DELIVERY")
    print("-"*30)
    print("1. Registrar nuevo pedido")
    print("2. Control de entregas realizadas")
    print("3. Ver estadísticas de ventas")
    print("4. Salir del programa")

def main():
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            controlar_entregas()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            print("¡Gracias por utilizar el Sistema de Delivery! Cerrando...")
            ejecutando = False
        else:
            print("Error: Opción inválida. Digite un número válido del 1 al 4.")

if __name__ == "__main__":
    main()
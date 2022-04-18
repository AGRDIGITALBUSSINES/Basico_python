import control

def estadistica(lista_tuplas_asignado, lista_tuplas_registrado):

    tamaño = len(lista_tuplas_asignado)
    for x in range(tamaño):
        asignadas = lista_tuplas_asignado[x][1]
        entragadas = lista_tuplas_registrado[x][1]
        print("Diferencia de cajas: = ", asignadas - entregadas)
    for y in range(tamaño):
        t_asignado = lista_tuplas_asignado[y][2]
        t_entregado = lista_tuplas_registrado[y][2]
        print("Diferencia de tiempos = ", t_asignado - t_entregado)
        print("Eficiencia = ", (t_asignado - t_entregado)/t_asignado)

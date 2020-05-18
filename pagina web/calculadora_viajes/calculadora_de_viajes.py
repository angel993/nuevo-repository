
# varriable para controlar mi while (caso quiera rodar el programa nuevamente)
run = True
while run:
    print()
    print('==== Calculadora de custos de viajes - Vehiculo/Avion ===')
    print()

    # lista con los precios del combustible(orden: gasolina, etanol, gnv, diesel)
    listas_precio_combustible = [4.29, 2.15, 3.24, 3.35]

    opcion = True
    while opcion:
        tipo_viajes = int(input(' # Medio de transporte (Digite: 1-Vehiculo, 2-Avion): '))
        if tipo_viajes == 1 or tipo_viajes == 2:
            opcion = False
        else:
            print('Opcion: ' + str(tipo_viajes) + ' invalido - Opciones validas solamente 1-Vehiculo, 2-Avion')
            print('Por favor intente nuevamente')
            opcion = True

    # variables que el usuario dara entrada
    cantidad_trechos = int(input(' # cuantos trechos? (1-solamente ida, 2- ida y vuelta) '))
    cuantas_personas = int(input(' # cuantas personas? '))
    dias_viaje = int(input(' # cuantas dias en total (con o sin hospedaje)? '))
    dias_hospedaje = int(input(' # cuantas dias de hospedaje? '))

    # Si no se va a hospedar no tiene porque pedir el costo del diario\
    if dias_hospedaje != 0:
        costo_diario_hospedaje = float(input(' # cuanto cuesta el dia de hospedaje? '))
    else:
        costo_diario_hospedaje = 0
    comidas_por_dia = int(input(' # cuantas comidas por dia? '))
    limite_gasto_por_comida =int(input(' # cual es el limite de gasto/comida/persona/dia? '))

    # calculo por categoria que es comun para viaje en Vehiculo o Avion
    costos_hospedaje = dias_hospedaje * costo_diario_hospedaje
    costos_alimentacion = cuantas_personas * limite_gasto_por_comida * comidas_por_dia * dias_viaje

    # se fuera un viaje tipo 1:
    if tipo_viajes == 1:
        #colecta del usuario - variables para viaje tipo vehiculo
        distancia_en_km = int(input(' # cuantos kilometros hay hasta su destino? '))
        autonomia_vehiculo = float(input(' # cuantos KM/L su carro recorre? '))
        costo_peaje  = float(input(' # cuanto cuesta el peaje? '))
        numero_peajes =float(input(' # cuantos peajes hay hasta su destino? '))
        otras_despensas = float(input(' # cualquier otra despenza? '))
        # lista de costos de los combustibles (g,e,g,d)
        costos_combustibles = []
        for precio in listas_precio_combustible:
            costos_combustibles.append(distancia_en_km / autonomia_vehiculo * precio)

        costo_peaje_total = numero_peajes * costo_peaje * cantidad_trechos

        # listas de costos de viaje por combustible(g,e,g,d)
        costos_viaje_por_combustible = []
        for costo_combustible in costos_combustibles:
            costos_viaje_por_combustible.append(
                costo_combustible + costo_peaje_total + costos_hospedaje + costos_alimentacion + otras_despensas
            )

        # Redondeando para 2 casa decimales el costo total por combustible
        costos_viaje_por_combustible = ['%.2f' % round(elem, 2) for elem in costos_viaje_por_combustible]

        # Mostrando en pantalla los precios de cada combustible por categoria
        print()
        print('==================== RESULTADO PARA VIAJE EN VEHICULO=============')
        print()
        print(
            'Costos GASOLINA - (TRANSPORTE + PEAJE): \\tR$ ' + str('%.2f' % round(costos_combustibles[0] + costo_peaje_total, 2)))
        print(
        'Costos ETANOL - (TRANSPORTE + PEAJE): \\tR$ ' + str('%.2f' % round(costos_combustibles[1] + costo_peaje_total, 2))
        )
        print(
            'Costos GNV - (TRANSPORTE + PEAJE): \\tR$ ' + str('%.2f' % round(costos_combustibles[2] + costo_peaje_total, 2))
        )
        print(
            'Costos DIESEL - (TRANSPORTE + PEAJE): \\tR$ ' + str('%.2f' % round(costos_combustibles[3] + costo_peaje_total, 2))
        )

        print()
        print('Costo total con HOSPEDAJE: \\tR$ ' + str('%.2f' % round(costos_hospedaje, 2)))
        print('Costo total con ALIMENTACION: \\tR$ ' + str('%.2f' % round(costos_alimentacion, 2)))
        print('Costo total con OTRA DESPEZA: \\tR$ ' + str('%.2f' % round(otras_despensas, 2)))

        print()
        print('Costo total de su viaje -  GASOLINA: \\tR$ ' + str(costos_viaje_por_combustible[0]))
        print('Costo total de su viaje -  ETANOL: \\tR$ ' +  str(costos_viaje_por_combustible[1]))
        print('Costo total de su viaje -  GNV: \\tR$ ' + str(costos_viaje_por_combustible[2]))
        print('Costo total de su viaje -  DIESEL: \\tR$ ' + str(costos_viaje_por_combustible[3]))

    # si  fuera tipo avion
    elif tipo_viajes == 2:
        precio_pasaje_persona = float(input('Cual es el precio del pasaje/persona/trecho? '))
        despensa_uber = float(input('Cual es el precio del uber/taxi hasta el aeropuerto? '))
        # no tiene que pedir precio por dias de utilizar uber si no lo utilizara
        dias_utilizando_uber = int(input('Cuantos dias utilizara uber? '))
        if dias_utilizando_uber != 0:
            utilizar_uber = float(input('Cual es el precio de utilizar uber/dia? '))
        else:
            utilizar_uber = 0
        otras_despensas = float(input(' # cualquier otra despenza? '))
        costos_pasajes = cuantas_personas * precio_pasaje_persona * cantidad_trechos
        costos_uber = despensa_uber * cantidad_trechos
        costos_utilizar_uber = utilizar_uber * dias_utilizando_uber

        costo_avion_total = costos_pasajes + costos_uber + costos_utilizar_uber + costos_alimentacion + costos_hospedaje
        # Mostrar en pantalla los resultados
        print()
        print('==================== RESULTADO PARA VIAJE EN AVION=============')
        print()
        print('Costo del PASAJE + UBER: \\tR$ ' + str('%.2f' % round(costos_pasajes + costos_uber, 2)))
        print('Costo total con HOSPEDAJE: \\tR$ ' + str('%.2f' % round(costos_hospedaje, 2)))
        print('Costo total con ALIMENTACION: \\tR$ ' + str('%.2f' % round(costos_alimentacion, 2)))
        print('Costo total con OTRA DESPEZA: \\tR$ ' + str('%.2f' % round(otras_despensas, 2)))

        print()
        print('costo total de su VIAJE: \\tR$ ' + str(costo_avion_total))

    # aqui pedimos al usuario si quiere rodar nuevamente
    print()
    ejecutar_nuevamente = input(' Quiere ejecutar nuevamente el programa? (s = si, cualquier otra tecla = no')
    run = True if ejecutar_nuevamente.lower() == 's' else False

print()
print('Hasta el proximo viaje')
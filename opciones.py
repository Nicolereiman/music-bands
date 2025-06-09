from banda import Banda
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

folder_path = os.path.dirname(__file__) #Dirección absoluta de la carpeta donde está ubicado este archivo py

with open(folder_path + '/bandas-inscriptas.csv', 'r', encoding='latin1') as csvfile: #UTF-8 tiene problemas con algunos caracteres, así que usamos LATIN1
    reader = csv.DictReader(csvfile, delimiter=";")
    for linea in reader:
        Banda(*linea.values())


def grabar_txt(nombre_archivo: str, encabezados: list, filas: list):
    """Grabar datos en un archivo txt
    
    Parameters
    ----------
        nombre_archivo: str 
            Nombre que se le dará al archivo para guardar (no usar caracteres prohibidos)
        encabezados: list
            Lista con el nombre de los encabezados
        filas: list(dict)
            Una lista de diccionarios con los encabezados como clave y los valores correspondientes a cada registro (records)
    """
    try:
        with open(folder_path + '/' + nombre_archivo + '.txt', 'w', encoding = 'latin1', newline = '') as txtfile:
            writer = csv.DictWriter(txtfile, fieldnames = encabezados, delimiter = "\t")
            writer.writeheader()
            writer.writerows(filas)
    except OSError: #Si se ingresa un caracter no apto para nombrar archivos, como " o ?, saltan errores
        print("El nombre de archivo no es válido")


def opcion1(barrio_input):
    cantidad_bandas = sum(1 for banda in Banda.lista_bandas if banda.barrio == barrio_input)
    bandas = ";".join(banda.nombre for banda in Banda.lista_bandas if banda.barrio == barrio_input)
    records = [{"CANTIDAD_BANDAS": cantidad_bandas, "BANDAS": bandas}] #Guardamos los datos en el formato aceptado por la función grabar_txt (formato records)
    grabar_txt(nombre_archivo = "Opcion1. bandas_solistas_por_barrio", encabezados = ["CANTIDAD_BANDAS", "BANDAS"], filas = records)
    
    #Creamos una lista de listas (al estilo de una matriz con 2 columnas) que va a ser input de la ventana en la GUI que contiene la tabla para mostrar los datos de forma tabular
    data_encabezados = [[f"Cantidad de bandas de {barrio_input}: {cantidad_bandas}"], ["Bandas"]]
    data = [[banda] for dicc in records for banda in dicc["BANDAS"].split(";")]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente las bandas para mejor visualización
    return data_encabezados + data


def opcion2(fecha):
    recuento_bandas = Counter(banda.barrio for banda in Banda.lista_bandas if banda.fecha_inscripcion <= fecha)
    # Tenemos un diccionario con barrios como clave y la cantidad de bandas como valor. El método writerows de csv.DictWriter admite
    # una lista de diccionarios así que reconvertimos el diccionario anterior a la forma adecuada para grabar el txt
    suma_bandas = sum(recuento_bandas.values())
    cantidad_barrios = len(recuento_bandas)
    
    records = [{"FECHA_LIMITE_SUPERIOR": fecha, "PROMEDIO_BANDAS": round(suma_bandas/cantidad_barrios, 2)}]
    grabar_txt(nombre_archivo = "Opcion2. promedio_bandas_por_barrio_hasta_fecha", encabezados = ["FECHA_LIMITE_SUPERIOR", "PROMEDIO_BANDAS"], filas = records)
    
    texto_promedios = "\n".join(str(dicc["PROMEDIO_BANDAS"]) for dicc in records)
    return f"El promedio de bandas hasta el {fecha.day}/{fecha.month}/{fecha.year} es: {texto_promedios}"


def opcion3():
    recuento_generos = defaultdict(lambda: defaultdict(int)) #Hay diccionarios anidados hasta el 2do nivel, por eso se usa esta función lambda
    for banda in Banda.lista_bandas:
        recuento_generos[banda.barrio][banda.genero] += 1 #defauldict nos va permitir ir generando las claves (barrio y genero) a medida que entran datos previamente no leídos
    
    # Filtramos por el género más escuchado en cada barrio
    genero_mas_escuchado = {barrio: max(recuento_generos[barrio], key = recuento_generos[barrio].get) for barrio in recuento_generos}
    personalidad_predominante = {barrio: Banda.genero_personalidad[genero] for barrio, genero in genero_mas_escuchado.items()}
    
    data_encabezados = [["Barrio", "Personalidad"]]
    data = [[barrio, personalidad] for barrio, personalidad in personalidad_predominante.items()]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente por barrio
    return data_encabezados + data


def opcion4(nombre_banda):
    for banda in Banda.lista_bandas:
        if banda.nombre == nombre_banda:
            return banda.__str__() #Rescatamos la cadena del método str para devolverlo y mostrarlo en el GUI
    else:
        print(f"El nombre del solista o banda {nombre_banda} no se encuentra en la base de datos")
        

def opcion5():
    recuento_bandas = Counter(banda.barrio for banda in Banda.lista_bandas)
    data_encabezados = [["Barrio", "Cantidad de bandas"]]
    data = [[tupla[0], tupla[1]] for tupla in sorted(recuento_bandas.items(), key = lambda kv: kv[1], reverse = True)]
    return data_encabezados + data


def opcion6():
    recuento_bandas = Counter(banda.barrio for banda in Banda.lista_bandas)
    data_encabezados = [["Barrio", "Cantidad de bandas"]]
    data = [[tupla[0], tupla[1]] for tupla in sorted(recuento_bandas.items(), key = lambda kv: kv[0])]
    return data_encabezados + data

    
def opcion7():
    dicc_generos = {genero: [0, 0, 0] for genero in Banda.genero_personalidad}
    for banda in Banda.lista_bandas:
        dicc_generos[banda.genero][0] += 1 #Cantidad de bandas
        dicc_generos[banda.genero][1] += len(banda.discos)
        dicc_generos[banda.genero][2] += banda.cantidad_integrantes
    
    data_encabezados = [["Genero", "Cantidad de bandas", "Cantidad de discos", "Cantidad de integrantes"]]
    data = [[genero, cant_bandas, cant_discos, cant_integrantes] for genero, (cant_bandas, cant_discos, cant_integrantes) in dicc_generos.items()]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente por género
    return data_encabezados + data


def opcion8():
    recuento_generos = {genero: [0, 0] for genero in Banda.genero_personalidad} 
    for banda in Banda.lista_bandas:
        recuento_generos[banda.genero][0] += banda.cantidad_integrantes #Suma integrantes
        recuento_generos[banda.genero][1] += 1 #Cantidad bandas
    
    records = [{"GENERO": genero, "PROMEDIO_INTEGRANTES": round(cant_integrantes/cant_bandas,2)} for genero, (cant_integrantes, cant_bandas) in recuento_generos.items()]
    grabar_txt(nombre_archivo = "Opcion8. promedio_integrantes_por_genero", encabezados = ["GENERO", "PROMEDIO_INTEGRANTES"], filas = records)
    
    data_encabezados = [["Genero", "Promedio integrantes"]]
    data = [[dicc["GENERO"], dicc["PROMEDIO_INTEGRANTES"]] for dicc in records]
    data = sorted(data, key = lambda x: x[1]) #Ordenamos en orden ascendente por promedio
    return data_encabezados + data
    

def opcion9():
    presencia_redes = {banda.nombre: banda.cantidad_redes for banda in Banda.lista_bandas}
    #En esta ocasión el Counter de la librería collections nos va a servir para filtrar el top10 de las bandas con mayor presencia en redes sociales
    top10 = Counter(presencia_redes).most_common(10)
    
    x, y = zip(*top10)
    plt.figure(figsize=(8, 5))
    plt.barh(x, y, color='#DF7861')
    plt.xlabel("Cantidad de links a redes sociales", size=12, weight="demibold")
    plt.tight_layout() #Necesario para que no se vean cortadas los etiquetas del eje y
    plt.show()


def opcion10():
    recuento_generos = defaultdict(lambda: defaultdict(int))
    for banda in Banda.lista_bandas:
        recuento_generos[banda.barrio][banda.genero] += 1
    
    #Filtramos por el género más tocado en cada barrio
    genero_mas_tocado = {barrio: max(recuento_generos[barrio], key=recuento_generos[barrio].get) for barrio in recuento_generos}
    records = [{"BARRIO": barrio, "GENERO_PREDOMINANTE": genero} for barrio, genero in genero_mas_tocado.items()]
    grabar_txt(nombre_archivo = "Opcion10. genero_mas_tocado_por_barrio", encabezados = ["BARRIO", "GENERO_PREDOMINANTE"], filas = records)
    
    data_encabezados = [["Barrio", "Genero predominante"]]
    data = [[dicc["BARRIO"], dicc["GENERO_PREDOMINANTE"]] for dicc in records]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente por género
    return data_encabezados + data


def opcion11(anio):
    bandas_por_mes = Counter(banda.fecha_inscripcion.month for banda in Banda.lista_bandas if banda.fecha_inscripcion.year == anio)
    nombre_mes = {1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun", 
                  7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12 :"Dic"}
    num_mes, cant_bandas = zip(*bandas_por_mes.items())
    
    # Un contador nos va a facilitar contar los generos por mes y extraer para cada mes calculado el predominante, a través del método most_common
    genero_predominante_por_mes = {mes: Counter(banda.genero for banda in Banda.lista_bandas if banda.fecha_inscripcion.year == anio and 
                                                banda.fecha_inscripcion.month == mes).most_common(1)[0][0] for mes in num_mes}
    
    fig, ax = plt.subplots()
    containers = ax.bar(num_mes, cant_bandas, color='#DF7861') #Obtenemos el objeto BarContainer para poder colocarle etiquetas después a través del método ax.bar_label
    x_ticks = np.arange(min(num_mes), max(num_mes)+1)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(nombre_mes[num] for num in x_ticks) #Cambiamos los números por el nombre del mes
    ax.bar_label(containers, [genero for _, genero in sorted(genero_predominante_por_mes.items(), key = lambda kv: kv[0])])
    plt.show()


def opcion12(fecha_inicial, fecha_final):
    recuento_generos = Counter(banda.genero for banda in Banda.lista_bandas if (banda.fecha_inscripcion >= fecha_inicial) and (banda.fecha_inscripcion <= fecha_final))
    return f"El género más común entre las fechas {fecha_inicial.day}/{fecha_inicial.month}/{fecha_inicial.year} " \
          f"y {fecha_final.day}/{fecha_final.month}/{fecha_final.year} es {recuento_generos.most_common(1)[0][0]}"


def opcion13():
    estilos_por_genero = {genero: len(estilos) for genero, estilos in Banda.genero_estilo.items()}
    genero_con_mas_estilos = max(estilos_por_genero, key = estilos_por_genero.get)
    
    data_encabezados = [[f"El género con más estilos es {genero_con_mas_estilos} con un total de {estilos_por_genero[genero_con_mas_estilos]} estilos"], ["Genero", "Estilos"]]
    data = [[genero, str(estilos)] for genero, estilos in Banda.genero_estilo.items()]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente por género
    return data_encabezados + data


def opcion14(fecha):
    bandas_discos = {banda.nombre: ";".join(banda.discos) for banda in Banda.lista_bandas if banda.fecha_inscripcion <= fecha and banda.discos}
    records = [{"BANDA": banda, "DISCOS": discos} for banda, discos in bandas_discos.items()]
    grabar_txt(nombre_archivo = "Opcion14. bandas_que_grabaron_discos_hasta_fecha", encabezados = ["BANDA", "DISCOS"], filas = records)
    
    data_encabezados = [["Banda", "Discos"]]
    data = [[dicc["BANDA"], dicc["DISCOS"]] for dicc in records]
    data = sorted(data, key = lambda x: x[0]) #Ordenamos alfabéticamente por banda
    return data_encabezados + data
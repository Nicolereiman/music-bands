from datetime import datetime

class Banda:
    lista_bandas = list() #Lista de instancias que pasan la condición de no repetir el nombre de la banda / solista
    nombre_bandas = set()
    genero_personalidad = dict() #Mapa o diccionario de los pares genero-personalidad (la relación es 1 a 1)
    genero_estilo = dict() #Diccionario con clave género y valores estilo que va a ser una lista, dado que pueden haber 0, 1 o más estilos por género
    barrios = set() #Set de los barrios en el dataset
    fechas = set() #Fechas registradas. Van a servir para el calendario que usemos en el GUI
    
    def __init__(self, nombre: str, genero: str, estilo: str, fecha_inscripcion: datetime, link_facebook: str,
                 link_twitter: str, otras_redes: list, discos: list, link_videoclip: str, video_en_vivo: str,
                 barrio: str, cantidad_integrantes: int):
        self.nombre = nombre
        self.genero = genero
        
        if estilo: #Check cadena vacía
            self.estilo = estilo
        else:
            self.estilo = "indefinido"
        
        self.fecha_inscripcion = datetime.strptime(fecha_inscripcion, "%d/%m/%Y")
        self.fechas.add(self.fecha_inscripcion)
        
        if link_facebook: #Check cadena vacía
            self.link_facebook = link_facebook
        else:
            self.link_facebook = "indefinido"
        
        if link_twitter: #Check cadena vacía
            self.link_twitter = link_twitter
        else:
            self.link_twitter = "indefinido"
        
        if otras_redes: #Check cadena vacía
            self.otras_redes = otras_redes.split(" ; ") #Otras redes es un string que dentro de sí tiene un delimitador que es espacio;espacio. Las pasamos a una lista para poder manejarlas
        else:
            self.otras_redes = ["indefinido"]
        
        self.total_redes = [self.link_facebook, self.link_twitter] + self.otras_redes #Útil para el punto 9
        self.cantidad_redes = sum(1 for red in self.total_redes if red != "indefinido")
        
        if discos: #Check cadena vacía
            self.discos = discos.split(" ; ")
        else:
            self.discos = ["indefinido"]
        
        if link_videoclip: #Check cadena vacía
            self.link_videoclip = link_videoclip
        else:
            self.link_videoclip = "indefinido"
        
        if video_en_vivo: #Check cadena vacía
            self.video_en_vivo = video_en_vivo
        else:
            self.video_en_vivo = "indefinido"
        
        #Hay barrios nombrados con / o -, como por ejemplo AVELLANEDA / CABALLITO y SAN JUSTO-LANUS-LOMAS DEL MIRADOR, por lo cual se decide tomar
        # el primer barrio de esa lista de barrios separado por los delimitadores
        if barrio:
            self.barrio = barrio.split("/")[0].split("-")[0].strip() #Se usa el strip para casos donde antes y después del delimitador hay espacios
        else:
            self.barrio = "indefinido"
        
        self.cantidad_integrantes = int(cantidad_integrantes)
        
        # Si bien la personalidad no es un atributo de la banda, cada personalidad se vincula a un tipo de género, y cada banda tiene solo un género, así que se puede
        # mapear la personalidad a los valores de género dentro de la banda y construimos las personalidades al iniciar el script del GUI para no tener que hacerlo después
        if self.genero in ["BLUES", "JAZZ", "SOUL", "HIP HOP / RAP", "OPERA"]:
            self.personalidad = "Alta autoestima - Creativo - Amable - Extravertido"
        elif self.genero == "COUNTRY":
            self.personalidad = "Trabajador - Extravertido"
        elif self.genero == "SKA / REGGAE":
            self.personalidad = "Algo vago - Creativo - Amable - Extravertido - Alta autoestima"
        elif self.genero == "ELECTRO / DANCE":
            self.personalidad = "Creativo - Extravertido - Poco amable"
        elif self.genero == "INDIE":
            self.personalidad = "Baja autoestima - Creativo - Poco amable - Poco trabajador"
        elif self.genero in ["ROCK", "METAL / HEAVY"]:
            self.personalidad = "Baja autoestima - Creativo - Poco trabajador - Introvertido - Amable"
        else:
            self.personalidad = "Sin descripcion" #La nota de psicología no considera todos los géneros. El género no mencionado tiene entonces una personalidad "Sin descripción"
        
        self.genero_personalidad.setdefault(self.genero, self.personalidad)
        
        #Buscamos el nombre de la banda en los registros (NO ES ÚNICO). Si no coincide con ninguno de los registros se guarda la 
        # instancia en una lista y el nombre de la banda en un set. Prestar atención que solo va a permanecer la primera aparición de ese nombre de banda
        if self.nombre not in self.nombre_bandas:
            self.nombre_bandas.add(self.nombre)
            self.lista_bandas.append(self)
        
        if self.genero in self.genero_estilo:
            self.genero_estilo[genero].add(self.estilo) #El estilo lo llamamos desde el self ya que lo modificamos en las cadenas vacías
        else:
            #Ponemos el estilo en una lista para que el set no separe las letras, sino que inicialmente se conforme por un solo elemento
            self.genero_estilo.update({genero: set([self.estilo])})
        
        self.barrios.add(self.barrio)
    
    
    def __str__(self):
        return f"""Nombre: {self.nombre}
Genero: {self.genero}
Estilo: {self.estilo}
Fecha inscripcion: {self.fecha_inscripcion.day}/{self.fecha_inscripcion.month}/{self.fecha_inscripcion.year}
Link Facebook: {self.link_facebook}
Link Twitter: {self.link_twitter}
Otras Redes: {self.otras_redes}
Discos: {self.discos}
Barrio: {self.barrio}
Cantidad Integrantes: {self.cantidad_integrantes}"""
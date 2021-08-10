class Player:

    def __init__(self, usuario):
        """
            Inicialización de las variables de instancia
        Args:
            usuario: Dict, información del jugador
        """
        self._nick = usuario["nombre"]
        self._edad = usuario["edad"]
        self._genero = usuario["genero"]
        self._nivel_actual = str(usuario["configuracion"]["nivel_actual"])
        self._nivel = usuario["configuracion"]["level" + self._nivel_actual]
        self._msj_victoria = usuario["configuracion"]["msj_victoria"]
        self._msj_derrota = usuario["configuracion"]["msj_derrota"]
        self._msj_tiempo = usuario["configuracion"]["msj_tiempo"]
        self._tema = usuario["configuracion"]["tema"]
        self._puntaje = 0

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nuevo_nick):
        self._nick = nuevo_nick

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero):
        self._genero = nuevo_genero

    @property
    def nivel_actual(self):
        return self._nivel_actual

    @nivel_actual.setter
    def nivel_actual(self, nuevo_nivel_actual):
        self._nivel_actual = str(nuevo_nivel_actual)

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nuevo_nivel, usuario):
        self._nivel = usuario["configuracion"]["level" + self.nuevo_nivel]


    @property
    def msj_victoria(self):
        return self._msj_victoria

    @msj_victoria.setter
    def msj_victoria(self, nuevo_msj_victoria):
        self._msj_victoria = nuevo_msj_victoria

    @property
    def msj_derrota(self):
        return self._msj_derrota

    @msj_derrota.setter
    def msj_derrota(self, nuevo_msj_derrota):
        self._msj_derrota = nuevo_msj_derrota

    @property
    def msj_tiempo(self):
        return self._msj_tiempo

    @msj_tiempo.setter
    def msj_tiempo(self, nuevo_msj_tiempo):
        self._msj_tiempo = nuevo_msj_tiempo

    @property
    def tema(self):
        return self._tema

    @tema.setter
    def tema(self, nuevo_tema):
        self._tema = nuevo_tema

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, nuevo_puntaje):
        self._puntaje = self._puntaje + nuevo_puntaje

    @puntaje.setter 
    def puntaje_0(self, nuevo_puntaje):
        self._puntaje = nuevo_puntaje   


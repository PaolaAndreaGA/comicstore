class Autor():
    def __init__(self, id, apellidos, nombres, pais = None):
      self.id = id
      self.apellidos = apellidos
      self.nombres = nombres
      self.pais = pais

    def nombre_completo(self):
      return "{0},{1}".format(self.apellidos, self.nombres)

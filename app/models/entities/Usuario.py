from re import I


class Usuario():
  def __init__(self, id, usuario, password, tipousuario):
    self.id = id
    self.usuario = usuario
    self.password = password
    self.tipodeusuario = tipousuario
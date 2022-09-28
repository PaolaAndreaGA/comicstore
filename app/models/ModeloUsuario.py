class ModeloUsuario():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario, password FROM usuario WHERE usuario = '{0}'".format(
                usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)
            return True
        except Exception as ex:
            raise Exception(ex)

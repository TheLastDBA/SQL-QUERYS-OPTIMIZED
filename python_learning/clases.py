class Coche:
    def __init__(self,modelo,marca,descuento):
        self.modelo = modelo
        self.marca = marca
        self.movimiento = False
        self.descuento = descuento

        pass

    def precio_2_ano(self):
        return self.descuento * 0.10
  
    


class prestamo:
    def __init__(self,monto,tasa,cant_anos,usuario):
            self.monto = monto 
            self.tasa = tasa
            self.cant_anos = cant_anos
            self.descuento = 0.03
            self.usuario = usuario
    
    def print_solicitud_prestamo(self,banco_name):
         return f'El usuario {self.usuario}, solicito un prestamo de {self.monto} a {self.cant_anos} años en banco: {banco_name}. la tasa valida para el es de: {self.tasa} y con un descuento de {self.descuento}%'
    


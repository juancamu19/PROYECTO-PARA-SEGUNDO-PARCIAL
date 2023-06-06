class Empresa():
    def __init__(self):
        self.cuenta = 0
        self.fecinicio = None 
    def objeto_a_lista(self):
        obj_list = []
        for attr, value in self.__dict__.items():
            obj_list.append(value)
        return obj_list
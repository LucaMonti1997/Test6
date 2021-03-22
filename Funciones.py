# Restringe un numero entre un minimo y un maximo
def clamp(numero, minimo=0, maximo=100):
    return max(min(numero, maximo), minimo)


# CAJÓN DE FUNCIONES SIN UTILIZAR, PERO UTILES QUIZÁS
# Rutina que busca todo los atributos de tipo Torre
# for a in dir(self):
#     if hasattr(self, a):
#         if type(getattr(self, a)) == Torre:
#             b = getattr(self, a)
#             b.ancho = int(b.ancho_base * self.mult_ancho)
#             b.alto = int(b.alto_base * self.mult_alto)

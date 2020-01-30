class FormaGeometrica:
    def calc_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self,base):
        self.base = base 
    
    def calc_area(self):
        return self.base*self.base #no quadrado(base = altura)

class Circulo(FormaGeometrica):
    def __init__(self,raio):
        self.raio = raio
    
    def calc_area(self):
        return self.raio* self.raio* 3.14

quadrado1=Quadrado(10) #defini o valor de 10 para a base do quadrado1 por meio da
                        #classe Quadrado
print(quadrado1.base)
area = quadrado1.calc_area()
print(area)
circulo1 = Circulo(5)#defini um objeto com o valor de raio 5 usando a classe Circulo
print(circulo1.raio)
area2 = circulo1.calc_area()
print(area2)


formas1 = [quadrado1,circulo1]

soma = 0
for i in formas1:#no lugar do nome 'i' poderia ser 'listaformas'
    soma = soma + i.calc_area() #consigo agora pegar o metodo geral e aplicar no for e fazer a soma
                                # o i nesse caso é uma variavel (objeto) com poliformismo
print('A area é: {}'.format(soma))

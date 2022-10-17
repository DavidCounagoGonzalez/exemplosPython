

def nomeFunction(parametro1,parametro2):
    '''Nesta parte
    facemos a descripción-documentación da función
    '''
    print(parametro1)

def funcion2 (parametro1 = 2, parametro2 = "Manuel"):
    '''En esta funcion imos darlle valor os parámetros por defecto'''

    print(parametro1)
    print(parametro2)

funcion2(parametro2= "Ana", parametro1= 4)

def funcionNumeroParametrosVariable (parametro1,parametro2, *outros):
    '''Función con número de parametros variables'''

    print(parametro1)
    print(parametro2)
    for parametro in outros:
        print(parametro)

funcionNumeroParametrosVariable(1,2,3,4,5)

def funcionNumeroParametroVariableConIdentificador(nome, dni, **outros):
    print("Nome: " + nome)
    print("DNI: " + dni)
    for clave in outros.keys():
        print(clave + " " + str(outros[clave]))

funcionNumeroParametroVariableConIdentificador("Manuel", "33333333H", Edade=34, Sexo=": Home")

def funcionRetornaVariosValores(x, y):
    '''As funcions en python poden retornar máis dun valor'''
    return x*2, y*2, 2

a, b, c = funcionRetornaVariosValores(5, 3)
print(a)
print(b)
print(c)

def saudar  (lingua):
    def saudar_gl ():
        print("Ola")
    def saudar_es():
        print("Hola")
    def saudar_en():
        print("Hello")
    def saudar_it():
        print("Ciao")
    lingua_function = {"es" : saudar_es(),
                       "gl" : saudar_gl(),
                       "it" : saudar_it(),
                       "en" : saudar_en()
                      }
    return lingua_function[lingua]

    """if lingua == "es": 
        return saudar_es """

f = saudar("it")


'''Funcións Lambda'''

def numero_par (n):
    return n % 2 == 0

print(numero_par(5))

l = [-3,4,5,-6,7]

l2 = filter(numero_par, l)
print("Pares:")
for elemento in l2:
    print(elemento)

l3 = filter (lambda n : n % 2 == 0, l)
l4 = filter (lambda  n : n > 0, l)
print("Maiores que cero:")
for elemento in l4:
    print(elemento)

l5 = map (lambda  n: n**2, l)
l5_2 = [n**2 for n in l]
l6 = [n for n in l if n % 2 == 0]

x = [0,1,2,3]
y = ['a','b','c','d']

z = [ c*n for n in x
          for c in y
          if n > 1]

print(z)

z =[]
for n in x:
    for c in y:
        if n > 1:
            z.append(n * c)

'''Xeradores'''

x=(n**2 for n in l)

print(type(l5_2))
print(type(x))
print(l5)
print(x)
lista = list(x)
print(lista)
'''for elemento in x:
    print(elemento)
'''
'''Decoraciones'''

def meu_decorador (funcion):
    def nova (*args):
        print("Chamada a funcion ", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nova
def saudar2():
    print('Ola')
meu_decorador(saudar2())

'''Excepcións'''

def división (a , b):
    try:
        d=a/b
    except ZeroDivisionError as error:
        print("Ollo, estás dividindo entre cero" + str(error))
        d = None
    except:
        print("Para calquera outra execución")
    else:
        print("Todo vai, ben non hai excepcións")
    finally:
        print("Executase sempre con ou sin excepción")
        return d

división(3, 1)
def asteriscos(func):
    def envoltura():
        print('**********')
        func()
        print('**********')
        
    return envoltura

@asteriscos
def saludo():
    print('Hola mundo')

if __name__ == '__main__':
    # saludo_decorado = asteriscos(saludo)
    # saludo_decorado()
    saludo()
    
class Usuario:
    #variables protegidas
    __email= "rosa@gmail.com"
    __password= "123456"
    
    def __init__(self):
        pass
    
    def login(self, email, password):
        if(self.__email == email and self.__password == password):
            print("Bienvenido")
        else:
            print("Datos incorrectos")
            
    def set_password(self, password):
        self.__password = password
        
        
print("Login de Usuario")
email = input("Ingrese su email: ")
password = input("Ingrese su password: ")

usuario = Usuario()
usuario.set_password(password)
usuario.login(email, password)
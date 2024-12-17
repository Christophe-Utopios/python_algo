class WrongLoginException(BaseException):
    pass

class WrongPasswordException(BaseException):
    pass

def input_login():
    try:
        login = input("Saisir votre Login : ")
        if not login.isalpha() or not login.islower(): # not (login.isalpha() and login.islower())
            raise WrongLoginException("Login invalide")
    except WrongLoginException as wl: 
        print(wl)
        return ""
    else:
        print("Login valide !")
        return login

def input_password(): 
    try:
        password = input("Saisir votre Password : ")
        if not password.isdigit():
            raise WrongPasswordException("Password invalide")
    except WrongPasswordException as wl: 
        print(wl)
        return ""
    else:
        print("Password valide !")
        return password

if __name__ == '__main__':
    login = ""
    password = ""
    while login == "" and password == "": # password == "" est équivalent à not password car une chaine vide correspond à un False
        login = input_login()
        password = input_password()

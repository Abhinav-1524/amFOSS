import re

passwd = input("enter a password: ")

def password():

    passwd_check=re.compile(r'(\s{8,})')
    uppercase=re.compile(r'[A-Z]')
    lowercase=re.compile(r'[a-z]')
    number=re.compile(r'[1-9]')
    character=re.compile(r'\W|_')
    try:
        mo=passwd_check.search(passwd)
    except:
        return ("please enter another password")
    
        

    if uppercase.search(passwd):
        if lowercase.search(passwd):
            if number.search(passwd):
                if character.search(passwd):
                    return ("the password is valid")
                else:
                    return ("the password doesn't contain any characters.")
            else:
                return("the password doesn't contain any numbers.")
        else:
            return("the password doesn't contain any lowercase character.")
    else:
        return("the password doesn't contain any uppercase character.")
    


    

print(password())

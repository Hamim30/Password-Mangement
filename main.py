from cryptography.fernet import Fernet

def load_key():
    file= open("key.key","rb")
    key=file.read()
    file.close()
    return key



# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()

key= load_key()
fer=Fernet(key)
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data= (line.rstrip())
            user,password=data.split()
            print("User: ",user , "Password: ",str(fer.decrypt(password.encode()).decode()))

def add():
    name =input("Account name")
    password=input("Password:")
    with open("passwords.txt","a") as f:
        f.write(name+" "+ fer.encrypt(password.encode()).decode()+"\n")


while True:
    mode =input("Add password(add) or view password(view)?").lower().strip()
    if mode=="q":
        break
    if mode =="add":
        add()
        pass
    elif mode =="view":
        view()
        pass
    else:
        print("invalid mode")
        continue
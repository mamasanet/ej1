from clasemail import email
import csv

if __name__ == '__main__':
    conta = 0
    x = input("ingrese el id: ")
    y = input("ingrese el dominio: ")
    z = input("ingrese el tipo de dominio: ")
    contra = input("ingrese la contraseña: ")
    nom = input("ingrese el nombre: ")
    mail = email(x, y, z, contra)
    print("estimado {} le enviaremos un mensaje a la direccion: ".format(nom), mail.retornamail())
    contra = input("ingrese la contraseña actual: ")
    if contra == mail.retornacontra():
        newpass = input("ingrese su nueva contraseña: ")
        mail.setpass(newpass)



    else:
        print("contraseña incorrecta")
obj2 = input("ingrese una mail: ")
pass2 = input("ingrese una contraseña")
mail2 = email()
mail2.crearCuenta(obj2, pass2)
archivo = open('mails.csv')
reader = csv.reader(archivo, delimiter=',')
dom = input("ingrese un dominio: ")
lista = []
#test
for fila in reader:
    mail3=email()
    mail3.crearCuenta(fila[0])
    lista.append(mail3)

print(lista[0].getdom()) # para ver si funcionaba
for i in range(len(lista)):
    if lista[i].getdom()==dom:
        conta+=1
print(conta)

import re 

opcion = 0

while opcion !=10:
    print ("\nSeleccione una opcón")
    print ("1. Palabras que tengan una longitud de 7 o más letras\n2. Expresiones que NO finalicen con una vocal\n3. Palabras que inicien con “M” donde la segunda letra no sea vocal\n4. Expresiones encerradas entre comillas\n5. Ip’s")
    print ("6. Horas\n7. Telefonos\n8. Correos electrónicos\n9. Url’s\n10. Código postal\n11. Salir")
    opcion = int (input("Ingrese una opción:  "))

    if opcion ==1:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==2:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[(b-d)|(f-h)|(j-nñ)|(p-t)|(v-z)]$"
            for elemento in lista:
                if re.search(regex, elemento):
                    print(elemento)
        textfile.close()
    elif opcion ==3:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[M][(b-d)|(f-h)|(j-nñ)|(p-t)|(v-z)][a-z]+"
            for elemento in lista:
                if re.search(regex, elemento):
                    print(elemento)
        textfile.close()
    elif opcion ==4:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "(\"[\w\*\s-]+\")"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==5:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==6:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "\d\d[:]\d\d"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==7:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "\+[0-9]{2}\s[0-9]{10}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==8:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "\w+[\@]+\w+[.]+\w+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==9:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[Ww]+\w[.]\w+[.]\w+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion ==10:
        filename = "txtPrueba.txt"
        textfile = open(filename, "r")
        regex = "[0-9]{5}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 11:
        print("Cerrando programa...\nPrograma finalizado")
        break
    else:
        print("La opción seleccionada es incorrecta!")
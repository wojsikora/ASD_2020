""" 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв. """

def zad():
    fl=input()
    sl=input()
    print("The place of the first letter in the alfabet is",ord(fl)-96)
    print("The place of the first letter in the alfabet is",ord(sl)-96)
    print("Between them there are",abs(ord(sl)-ord(fl)-1),"letter(s)")
zad()
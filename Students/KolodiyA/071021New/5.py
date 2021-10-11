print("Введи кол-во бутылок меньше 1л и больше 1л:")
less1l= int(input())
more1l =int(input())
print("Еслт ты сдашь всю эту посуду, то получишь:" + str(round(less1l*0.1 + more1l*0.25,2))+"₽" )
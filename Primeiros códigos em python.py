a = int (input ("Digite o valor do coeficiente a: "))
b = int (input ("Digite o valor do coeficiente b: "))
c = int (input ("Digite o valor do coeficiente c: "))
 #delta = b^2 - 4ac
 Delta = b**2 - 4*a*c
 print(" O valor de delta é : ", Delta)

 # x = (-b +- raiz (delta)) /2a
 x1 = (-b - Delta**0.5)/(2*a)
 x1 = (-b + Delta**0.5)/(2*a)
 print (" O valor de x1 é: ",x1)
 print (" O valor de x2 é: ", x2)
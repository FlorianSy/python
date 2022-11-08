print('Lotto')
number1 = int(input('Zahl Zwischen 1-50'))
number2 = int(input('Zahl Zwischen 1-50'))
number3 = int(input('Zahl Zwischen 1-50'))
# Gewinnzahl 1 : 2
# Gewinnzahl 2 : 1
# Gewinnzahl 3 : 49


if number1 == 2 and number2 == 1 and number3 == 49:
    print('Gewonnen')
else:
    print('Verloren')


input('Versuchen sie es nocheinmal % ')
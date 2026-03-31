#4 CALCULADORA
n1 = float(input("selecione um número: ")) # Variavel "n1" solicitara um numero
n2 = float(input("selecione outro numero: "))  # Variavel "n2" solicitara outro numero
operação = input("escolha uma opração [soma, subtração, multiplicação ou divisão]: ") # Variavel "operação" solicitora como sera a operação
if operação == "soma": # se escolher "soma" realizara a soma
    print( n1 + n2)
elif operação == "subtração":# se escolher "subtração" realizara a subtração
    print( n1 - n2)
elif operação == "multiplicação":# se escolher "multiplicação" realizara a multiplicação
    print( n1 * n2)
elif operação == "divisão":# se escolher "divisão" realizara a divisão
    print( n1 / n2)
else:
    print("essa operação não existe")# se não escolher uma operação ou escolher uma operação que não existe exemplo raiz aparecera que a operação não esxiste

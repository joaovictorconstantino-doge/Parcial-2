#6 tempo
print("Escolha uma opção:")
print("1 - Converter segundos para horas, minutos e segundos")
print("2 - Converter horas para horas, minutos e segundos")

opcao = int(input("Digite 1 ou 2: ")) # variavel "opcao" pedira os numeros 1 ou 2 como opções de converção de tempo

if opcao == 1: # se escolher opção 1
    segundos = int(input("Digite o número de segundos: ")) # variavel segundos solicita os segundos do tempo 
    
    horas = segundos // 3600 # variavel horas é igual a segundos dividido inteiro por 3600
    resto = segundos % 3600 # variavel resto sera igual asegundos e vai retornar a sobra da divisão inteira 
    minutos = resto // 60 # variavel minutos sera igual a resto dividido inteiro pro 60
    segundos_restantes = resto % 60 # variavel "segundos_restantes" sera igual a "resto" retornando a sobra para divisão inteira 

    print(print(horas, "hora(s),", minutos, "minuto(s) e", segundos_restantes, "segundo(s)")) # mostrara o resultado da coverção

elif opcao == 2: # se escolher opção 2
    horas = float(input("Digite o número de horas: ")) # variavel "horas" vai pedir as horas 
    
    total_segundos = int(horas * 3600) #variavel total_segundos vai ser igual a divisão de horas por 3600

    h = total_segundos // 3600 # "h" vai ser igual total_segundos dividido por inteiro po 3600
    resto = total_segundos % 3600 # resto vai retornar o que sobrar de h 
    m = resto // 60 # m vai ser igual a resto dividido por inteiro por 60
    s = resto % 60 # s vai ser igual o resto que vai retornar da divisão inteira

    print(h,"hora(s)", m,"minuto(s)",s,"sugundo(s)" ) # vai mostrar a converção das horas

else:
    print("Opção inválida!") # se não escolher nenhuma das opções vai dar invalida

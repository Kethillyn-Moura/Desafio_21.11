# Desafio 1:

mes = (input("Qual o número do mês? "))
atividade = {
    "1": {"January"},
    "2": {"February"},
    "3": {"March"},
    "4": {"April"},
    "5": {"May"},
    "6": {"June"},
    "7": {"July"},
    "8": {"August"},
    "9": {"September"},
    "10": {"October"},
    "11": {"November"},
    "12": {"December"},
}

print(atividade[mes])

#Desafio 2:

texto = len(input("Insira o texto aqui: "))

if (texto <= 280):
    print("Isso é um Tweet")

if (texto > 280):
    print("Esse texto é maior do que o esperado")

#Desafio 3:

idade = int(input("Qual é a sua idade? "))

if (idade >= 16) and (idade <= 69):
    kg = int(input('Quantos quilos você pesa? '))
    if (kg > 50):
        sono = int(input("Quantas horas de descanso você teve na noite passada? "))
        if (sono > 6):
            print('Você está liberado para realizar doação de sangue')
        else:
            print('Você não descansou o suficiente para realizar a doação de sangue')
    else:
        print('Você está abaixo do peso mínimo para realizar a doação de sangue')
else:
    print('Você não tem a idade necessária para doar sangue.')


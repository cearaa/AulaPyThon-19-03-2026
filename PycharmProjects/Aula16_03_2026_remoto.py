#Exercício 9 - Algoritimo de Distribuição

#Entrada de Dados
#totalDeRegistros = int(input("Digíte a quantidade total de registros: "))
#quantidade_servidores = int(input("Digite a quantidade de servidores dísponiveis: "))

#Processamento de Dados
#registros_por_servidor = totalDeRegistros / quantidade_servidores

#print("Cada servidor deverá processar", registros_por_servidor, "registros")

#a=4
#b=5
#print(a==b)

#Calculadora de Notas da Escola
#nota=float(input("Digite a sua nota: "))
#if nota >= 7:
#   print("Aprovado")
#elif nota < 5:
#    print("Reprovado")
#else:
#    print("Recuperação!")

#quantidade_de_erros=int(input("Quantos erros existem?" ))
#if quantidade_de_erros==0:
#    print("Sistema estável")
#elif quantidade_de_erros<=5:
#    print("Ajustes necessários")
#else:
#    print("Sistemas crítico")

#Exercício 3 - Resposta de uma APi

tempo_de_resposta_de_uma_api = int(input("Qual o tempo de resposta da sua APi? "))
if tempo_de_resposta_de_uma_api <=100:
    print("Excelente!!")
elif tempo_de_resposta_de_uma_api <=300:
    print("Aceítavel!!")
elif tempo_de_resposta_de_uma_api <=800:
    print("Lento.")
else:
    print("Crítico")
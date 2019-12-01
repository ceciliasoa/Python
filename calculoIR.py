from time import sleep

def contribuicaoPrevidencia(salario):
    contribuicao = 0
    
    if salario <= 1174.86:
        contribuicao = salario*0.08
    elif 1174.87 <= salario <= 1958.10:
        contribuicao = salario*0.09
    elif 1958.11 <= salario <= 3916.20:
        contribuicao = salario*0.11
    elif salario >= 3916.21:
        contribuicao = 430.78
    
    return contribuicao

def impostoDeRenda(salario, contribuicao):
    ir = 0
    baseDeCalculo = salario - contribuicao

    if baseDeCalculo <= 1637.11:
        return "Isento"
    elif 1637.12 <= baseDeCalculo <= 2453.50:
        ir = (baseDeCalculo*0.075)-122.78
    elif 2453.51 <= baseDeCalculo <= 3271.38:
        ir = (baseDeCalculo*0.15)-306.80
    elif 3271.39 <= baseDeCalculo <= 4087.65:
        ir = (baseDeCalculo*0.225)-552.15
    elif baseDeCalculo >= 4087.66:
        ir = (baseDeCalculo*0.275)-756.53
    
    return 'R${:.2f}'.format(ir)


print(60*"=")
print("Simulador INSS e Imposto de renda".center(60))       
print(60*"=")

while True:
    salario = float(input("Informe o salário bruto do trabalhador (0 para sair): "))
    if salario == 0:
        print("Encerrando...")
        sleep(1)
        print(60*"=")
        break
    elif salario < 0:
        print("\nValor invalido!\n")
        continue

    contribuicao = contribuicaoPrevidencia(salario)

    print("\nINSS: R$%.2f"%contribuicao)
    print("Imposto de renda: {}\n".format(impostoDeRenda(salario,contribuicao)))
    print(60*"=")




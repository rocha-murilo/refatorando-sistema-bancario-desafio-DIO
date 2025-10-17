# 1-) Criar funções para as operações existentes: sacar depositar e visualizar extrato.  

# Passagem de argumentos obrigatório:

# Saque: Argumentos apenas por nome (keyword only). 
# Seguestão de argumentos: "saldo", "valor", "extrato", "limite", "numero_saques", "limite_saques". 
# Sugestão de retorno: "saldo" e "extrato".

# Depósito: Argumentos por posição (position only).
# Sugestão de argumentos: saldo, valor, extrato. 
# Sugestão de retorno: saldo e extrato

# Extrato: Argumentos por posição e nome (positional only e keyword only). 
# Argumentos posicionais: saldo, argumentos nomeados: extrato.

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
    
def sacar(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return saldo, extrato

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato = sacar(
            saldo=saldo,
            valor=valor,
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
            extrato=extrato
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato="extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
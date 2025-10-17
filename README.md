# 🏦 Sistema Bancário em Python

Projeto desenvolvido como parte dos desafios da **Digital Innovation One (DIO)**.  
O objetivo foi criar um sistema bancário simples em **Python**, aplicando **funções, argumentos posicionais e nomeados, retorno múltiplo** e boas práticas de código limpo.

---

## 💡 Objetivo do Projeto

Simular operações bancárias básicas, permitindo que o usuário:
- 💰 Faça **depósitos**  
- 💸 Realize **saques** com limite diário  
- 📜 Visualize o **extrato** de movimentações  

Tudo isso utilizando uma estrutura de código **modularizada** e **de fácil manutenção**.

---

## 🧠 Conceitos Aplicados

- Funções e modularização do código  
- Argumentos **posicionais** (`/`) e **nomeados** (`*`)  
- Retorno múltiplo de valores  
- Estrutura de controle e validação de entradas  
- Boas práticas de organização e clareza no código  

---

## 🧩 Estrutura das Funções

| Função | Tipo de Argumento | Descrição |
|--------|--------------------|------------|
| `depositar(saldo, valor, extrato)` | Posicional | Realiza o depósito e atualiza o saldo e o extrato |
| `sacar(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato)` | Nomeado (keyword only) | Controla os saques e valida limite e saldo |
| `exibir_extrato(saldo, /, *, extrato)` | Posicional e Nomeado | Exibe as movimentações e o saldo atual |

---

## ⚙️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git

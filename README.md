# 💰 Projeto Banco DIO - Sistema Bancário em Python

Este projeto é uma simulação de um **sistema bancário** desenvolvido como parte do desafio da [Digital Innovation One (DIO)](https://web.dio.me/). O código foi escrito em Python puro e executado via terminal, com o objetivo de praticar conceitos de programação como funções, estruturas de repetição, condicionais, manipulação de listas e dicionários.

## 🚀 Funcionalidades

O sistema oferece as seguintes operações:

- **[1] Depositar**: Permite realizar depósitos na conta.
- **[2] Sacar**: Realiza saques respeitando limites diários.
- **[3] Extrato**: Exibe todas as movimentações e o saldo atual.
- **[4] Nova Conta**: Cria uma nova conta para um usuário existente.
- **[5] Listar Contas**: Lista todas as contas criadas com seus respectivos titulares.
- **[6] Novo Usuário**: Cadastra um novo usuário com CPF, nome, data de nascimento e endereço.
- **[7] Sair**: Finaliza a aplicação.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- Bibliotecas padrão: `datetime`, `textwrap`

## 📂 Estrutura de Dados

- **Usuário**:
  ```python
  {
      'cpf': '12345678900',
      'nome': 'Nome do Usuário',
      'data_nascimento': 'dd-mm-aaaa',
      'endereco': 'Rua, Nº - Bairro - Cidade/UF'
  }

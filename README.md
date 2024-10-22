# Sistema de Gerenciamento de Estoque

Este é um sistema de gerenciamento de estoque desenvolvido para uma empresa de comércio eletrônico em rápido crescimento. O sistema tem como objetivo otimizar o gerenciamento de produtos, rastrear a localização dos itens, e gerar relatórios sobre o estado do estoque.

## Funcionalidades

- **Cadastro de Produtos**: Permite o cadastro de novos produtos com informações detalhadas, incluindo nome, categoria, quantidade em estoque, preço e localização no depósito.
- **Atualização de Estoque**: Atualiza a quantidade de produtos em estoque conforme novas entradas ou vendas.
- **Rastreamento de Localização**: Rastreia a localização dos produtos dentro dos depósitos para facilitar a logística interna.
- **Relatórios**: Gera relatórios sobre o estado do estoque, destacando produtos com estoque baixo, excesso de produtos, e movimentações de itens.
- **Movimentação de Estoque**: Registra a entrada e saída de produtos, mantendo o estoque sempre atualizado.

## Estrutura do Projeto

O projeto está dividido em arquivos separados para melhor organização e modularização do código:

- **produto.py**: Contém a classe `Produto`, que define a estrutura dos produtos.
- **movimentacao.py**: Define a classe `Movimentacao` e as operações de movimentação de produtos.
- **estoque.py**: Contém funções para cadastro, consulta, e movimentação de produtos.
- **relatorio.py**: Funções para gerar relatórios sobre o estado do estoque.
- **main.py**: Arquivo principal que executa o menu interativo para interagir com o sistema.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/gianvictorvieira/ProjetoFacul

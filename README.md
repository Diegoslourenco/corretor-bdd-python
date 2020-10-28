# Corretor de Banco de Dados Corrompido em Python

Programa para recuperação de um banco de dados corrompido em JSON:

- Lê o arquivo;
- Corrige caracteres errados, trocando 'æ', '¢', 'ø' e 'ß' por 'a', 'c', 'o' e 'b', respectivamente;
- Caso a categoria quantidade esteja faltando, insere 'quantidade' com valor 0;
- Exporta a versão corrijida para um arquivo JSON;
- Imprime lista dos produtos e valor total em estoque por produto.

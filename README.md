# PDV com Descontos

## O que o código faz

Este programa simula um PDV (ponto de venda) simples em Python. O cliente informa a sua idade e, em seguida, registra quantas compras quiser. Ao encerrar, o programa aplica as regras de desconto a cada compra (20% para clientes com 65 anos ou mais e 10% extra para valores acima de R$ 100) e exibe um resumo do dia com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final.

## Como o código faz

1. Pede a **idade** do cliente e, se for negativa, avisa e pede novamente.
2. Mostra um menu com duas opções: `1` para fazer uma compra e `0` para encerrar. Qualquer outra entrada gera um aviso e a opção é pedida de novo.
3. Na opção `1`, lê o **valor da compra** (número decimal) e guarda o valor original na lista `compras` com `.append()`. O menu volta a aparecer até o usuário digitar `0`.
4. Ao encerrar, calcula o **total bruto** somando os valores originais.
5. Para cada compra, aplica as regras de desconto:
   - **Regra 1 (idade):** se a idade for maior ou igual a 65, aplica 20% de desconto.
   - **Regra 2 (valor):** se o valor **já com o desconto de idade** for maior que R$ 100, aplica mais 10% sobre esse valor. Para clientes com menos de 65 anos, o teste é feito sobre o valor original.
6. Guarda o valor final de cada compra na lista `valores_com_desconto` e soma tudo para obter o **total final**.
7. Calcula o total de descontos em reais (total bruto menos total final) e a quantidade de descontos aplicados.
8. Exibe o **resumo do dia** com idade do cliente, quantidade de compras, total bruto, descontos concedidos (quantidade e valor em R$) e total final.

## Como rodar

O projeto usa um ambiente virtual chamado `.venv`. Ative-o antes de executar o programa.

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando):**

```cmd
.venv\Scripts\activate.bat
```

**Linux ou macOS:**

```bash
source .venv/bin/activate
```

Com o ambiente ativado (o nome `(.venv)` aparece no início da linha do terminal), execute:

```bash
python pdv.py
```

Para sair do ambiente virtual quando terminar:

```bash
deactivate
```
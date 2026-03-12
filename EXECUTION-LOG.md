# Log de Execucoes - Historico de Regressoes

---

## Execucao 003 - v2.15.0

| Campo | Valor |
|---|---|
| Data | 10/03/2026 |
| Versao | v2.15.0 |
| Motivo | Deploy com nova feature: parcelamento no checkout |
| Executado por | Lucas Montenegro |
| Duracao | 2h30 |
| Resultado | FAIL - 1 bug encontrado |

| Modulo | Total | PASS | FAIL |
|---|---|---|---|
| Autenticacao | 6 | 6 | 0 |
| Cadastro | 5 | 5 | 0 |
| Catalogo | 6 | 6 | 0 |
| Carrinho | 6 | 6 | 0 |
| Checkout/Pagamento | 7 | 6 | 1 |
| Conta do Usuario | 5 | 5 | 0 |
| Total | 35 | 34 | 1 |

Bug encontrado: BUG-312 - Valor parcelado exibe centavos incorretos no resumo do pedido

---

## Execucao 002 - v2.14.0

| Campo | Valor |
|---|---|
| Data | 03/03/2026 |
| Versao | v2.14.0 |
| Motivo | Deploy com correcao do BUG-217 (cupom de desconto) |
| Executado por | Lucas Montenegro |
| Duracao | 2h15 |
| Resultado | PASS - Nenhum bug encontrado |

| Modulo | Total | PASS | FAIL |
|---|---|---|---|
| Autenticacao | 6 | 6 | 0 |
| Cadastro | 5 | 5 | 0 |
| Catalogo | 6 | 6 | 0 |
| Carrinho | 6 | 6 | 0 |
| Checkout/Pagamento | 7 | 7 | 0 |
| Conta do Usuario | 5 | 5 | 0 |
| Total | 35 | 35 | 0 |

---

## Execucao 001 - v2.13.0

| Campo | Valor |
|---|---|
| Data | 20/02/2026 |
| Versao | v2.13.0 |
| Motivo | Primeira execucao da suite - baseline |
| Executado por | Lucas Montenegro |
| Duracao | 3h |
| Resultado | PASS - Suite baseline aprovada |
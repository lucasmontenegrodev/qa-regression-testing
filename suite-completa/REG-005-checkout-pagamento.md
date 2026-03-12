# REG-005 - Regressao: Checkout e Pagamento

| Campo | Valor |
|---|---|
| ID | REG-005 |
| Modulo | Checkout e Pagamento |
| Prioridade | Alta |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | FAIL (6/7 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Fluxo completo de checkout | Pedido criado, e-mail enviado | PASS |
| 2 | Pagamento com cartao valido (sandbox) | Aprovado, tela de confirmacao | PASS |
| 3 | Pagamento com cartao expirado | Mensagem "Cartao expirado" | PASS |
| 4 | Pagamento com CVV invalido | Mensagem "CVV invalido" | PASS |
| 5 | Checkout sem endereco | Validacao nos campos obrigatorios | PASS |
| 6 | Cancelar e voltar ao carrinho | Carrinho preservado com itens | PASS |
| 7 | Parcelamento 3x - valor por parcela | 3x de R$ 60,00 exibido corretamente | FAIL |

---

## Bug Encontrado

BUG-312 - Valor da parcela exibe centavos incorretos

| Campo | Valor |
|---|---|
| Severidade | Media |
| Resultado Esperado | 3x de R$ 60,00 |
| Resultado Obtido | 3x de R$ 59,99 (erro de arredondamento) |
| Hipotese | Divisao de float sem arredondamento no front-end |

---

## Observacoes v2.15.0

Bug encontrado na nova feature de parcelamento, nao em funcionalidade anterior. Demais fluxos de pagamento estaveis.
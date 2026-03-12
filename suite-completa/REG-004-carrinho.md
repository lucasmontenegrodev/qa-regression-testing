# REG-004 - Regressao: Carrinho

| Campo | Valor |
|---|---|
| ID | REG-004 |
| Modulo | Carrinho de Compras |
| Prioridade | Alta |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | PASS (6/6) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Adicionar produto | Badge atualizado, produto listado | PASS |
| 2 | Remover produto | Produto removido, total atualizado | PASS |
| 3 | Alterar quantidade | Quantidade e total atualizados | PASS |
| 4 | Multiplos produtos | Todos listados, total correto | PASS |
| 5 | Cupom de desconto valido | Desconto aplicado e total atualizado | PASS |
| 6 | Carrinho persiste apos relogar | Produto ainda presente apos relogar | PASS |

---

## Observacoes v2.15.0

BUG-217 corrigido na v2.14.0 permanece corrigido. Regressao do carrinho aprovada.
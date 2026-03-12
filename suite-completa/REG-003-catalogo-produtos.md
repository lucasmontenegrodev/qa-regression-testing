# REG-003 - Regressao: Catalogo de Produtos

| Campo | Valor |
|---|---|
| ID | REG-003 |
| Modulo | Catalogo de Produtos |
| Prioridade | Media |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | PASS (6/6) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Listagem de produtos | Produtos com imagem, nome e preco | PASS |
| 2 | Filtro por categoria | Apenas produtos da categoria selecionada | PASS |
| 3 | Ordenacao por menor preco | Produtos reordenados corretamente | PASS |
| 4 | Ordenacao por maior avaliacao | Produtos reordenados corretamente | PASS |
| 5 | Busca por nome | Produtos correspondentes ao termo | PASS |
| 6 | Pagina de detalhes do produto | Imagens, descricao, preco e botao visiveis | PASS |

---

## Observacoes v2.15.0

Catalogo sem regressoes. Filtros e ordenacoes funcionando normalmente.
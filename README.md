# QA Regression Testing - Suite Completa

Suite de testes de regressao documentada para garantir que novas atualizacoes nao quebrem funcionalidades ja aprovadas. Executada a cada deploy no ambiente de Staging.

---

## O que e Regressao?

Teste de regressao e a re-execucao de testes ja aprovados apos uma mudanca no sistema (nova feature, correcao de bug, refatoracao).

Quando executar: a cada PR aprovado, antes de todo deploy, apos correcao de bug critico.

---

## Estrutura do Repositorio

```
qa-regression-testing/
├── README.md
├── EXECUTION-LOG.md
├── suite-completa/
│   ├── REG-001-autenticacao.md
│   ├── REG-002-cadastro.md
│   ├── REG-003-catalogo-produtos.md
│   ├── REG-004-carrinho.md
│   ├── REG-005-checkout-pagamento.md
│   └── REG-006-conta-usuario.md
└── evidencias/
    └── README.md
```

---

## Suite de Regressao - Indice

| ID | Modulo | Casos | Ultima Execucao | Status |
|---|---|---|---|---|
| [REG-001](./suite-completa/REG-001-autenticacao.md) | Autenticacao | 6 | 10/03/2026 | PASS |
| [REG-002](./suite-completa/REG-002-cadastro.md) | Cadastro | 5 | 10/03/2026 | PASS |
| [REG-003](./suite-completa/REG-003-catalogo-produtos.md) | Catalogo de Produtos | 6 | 10/03/2026 | PASS |
| [REG-004](./suite-completa/REG-004-carrinho.md) | Carrinho | 6 | 10/03/2026 | PASS |
| [REG-005](./suite-completa/REG-005-checkout-pagamento.md) | Checkout e Pagamento | 7 | 10/03/2026 | FAIL |
| [REG-006](./suite-completa/REG-006-conta-usuario.md) | Conta do Usuario | 5 | 10/03/2026 | PASS |

---

## Resultado da Ultima Execucao

| Data | Versao | Total | PASS | FAIL | Aprovacao |
|---|---|---|---|---|---|
| 10/03/2026 | v2.15.0 | 35 | 34 | 1 | 97% |

---

## Criterio de Entrada e Saida

Entrada:
- Novo deploy no ambiente de Staging
- Apos correcao de bug critico
- Antes de toda release para Producao

Saida:
- 100% dos casos de alta prioridade com PASS
- Nenhum bug critico em aberto
- Evidencias coletadas e salvas

---

## Ferramentas

| Ferramenta | Uso |
|---|---|
| Jira | Controle de execucao e abertura de bugs |
| Chrome DevTools | Coleta de evidencias e logs |
| Postman | Validacao de APIs durante a regressao |
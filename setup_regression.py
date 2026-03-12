import os

README = """# QA Regression Testing - Suite Completa

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
"""

EXECUTION_LOG = """# Log de Execucoes - Historico de Regressoes

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
"""

REG001 = """# REG-001 - Regressao: Autenticacao

| Campo | Valor |
|---|---|
| ID | REG-001 |
| Modulo | Autenticacao |
| Prioridade | Alta |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | PASS (6/6) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Login com credenciais validas | Redireciona para home logada | PASS |
| 2 | Login com senha incorreta | Mensagem "E-mail ou senha incorretos" | PASS |
| 3 | Login com e-mail nao cadastrado | Mensagem "E-mail ou senha incorretos" | PASS |
| 4 | Login com campos vazios | Validacao nos campos obrigatorios | PASS |
| 5 | Logout | Sessao encerrada, redireciona para login | PASS |
| 6 | Sessao expirada | Redireciona para login com mensagem | PASS |

---

## Observacoes v2.15.0

Nenhuma regressao identificada. Fluxo de login e logout estaveis apos o deploy.
"""

REG002 = """# REG-002 - Regressao: Cadastro

| Campo | Valor |
|---|---|
| ID | REG-002 |
| Modulo | Cadastro de Usuario |
| Prioridade | Alta |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | PASS (5/5) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Cadastro com dados validos | Conta criada, e-mail de confirmacao enviado | PASS |
| 2 | Cadastro com e-mail ja existente | Mensagem "E-mail ja cadastrado" | PASS |
| 3 | Cadastro com senhas diferentes | Mensagem "As senhas nao coincidem" | PASS |
| 4 | Cadastro com senha fraca | Mensagem de requisito minimo de senha | PASS |
| 5 | Campos obrigatorios vazios | Validacao em todos os campos | PASS |

---

## Observacoes v2.15.0

Modulo de cadastro sem regressoes. Validacoes funcionando corretamente.
"""

REG003 = """# REG-003 - Regressao: Catalogo de Produtos

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
"""

REG004 = """# REG-004 - Regressao: Carrinho

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
"""

REG005 = """# REG-005 - Regressao: Checkout e Pagamento

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
"""

REG006 = """# REG-006 - Regressao: Conta do Usuario

| Campo | Valor |
|---|---|
| ID | REG-006 |
| Modulo | Conta do Usuario |
| Prioridade | Media |
| Ultima execucao | 10/03/2026 - v2.15.0 |
| Status | PASS (5/5) |

---

## Casos de Teste

| # | Cenario | Resultado Esperado | Status |
|---|---|---|---|
| 1 | Editar dados pessoais | Dados atualizados e salvos | PASS |
| 2 | Alterar senha | Senha atualizada, sessao mantida | PASS |
| 3 | Historico de pedidos | Lista com status e valores | PASS |
| 4 | Lista de desejos | Produtos salvos exibidos | PASS |
| 5 | Excluir conta | Conta excluida, sessao encerrada | PASS |

---

## Observacoes v2.15.0

Modulo de conta sem regressoes. Todas as funcionalidades estaveis.
"""

EVIDENCIAS = """# Evidencias de Regressao

Organizado por versao e modulo.

Estrutura:
```
evidencias/
├── v2.15.0/
│   ├── REG-001-autenticacao/
│   ├── REG-002-cadastro/
│   ├── REG-003-catalogo/
│   ├── REG-004-carrinho/
│   ├── REG-005-checkout/
│   └── REG-006-conta/
├── v2.14.0/
└── v2.13.0/
```

Boas praticas: uma pasta por versao, uma pasta por modulo, screenshot + log de rede para bugs.
"""

arquivos = {
    "README.md":                                        README,
    "EXECUTION-LOG.md":                                 EXECUTION_LOG,
    "suite-completa/REG-001-autenticacao.md":           REG001,
    "suite-completa/REG-002-cadastro.md":               REG002,
    "suite-completa/REG-003-catalogo-produtos.md":      REG003,
    "suite-completa/REG-004-carrinho.md":               REG004,
    "suite-completa/REG-005-checkout-pagamento.md":     REG005,
    "suite-completa/REG-006-conta-usuario.md":          REG006,
    "evidencias/README.md":                             EVIDENCIAS,
}

print("Criando repositorio qa-regression-testing...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print("\nPronto. 9 arquivos criados.")
print("\nProximos passos:")
print("  1. Crie o repositorio 'qa-regression-testing' no GitHub")
print("  2. git clone https://github.com/lucasmontenegrodev/qa-regression-testing.git")
print("  3. cd qa-regression-testing")
print("  4. Coloque este script aqui e rode: python setup_regression.py")
print("  5. git add .")
print('  6. git commit -m "feat: suite completa de testes de regressao"')
print("  7. git push origin main --force")

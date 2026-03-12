# REG-001 - Regressao: Autenticacao

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
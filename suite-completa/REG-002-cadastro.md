# REG-002 - Regressao: Cadastro

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
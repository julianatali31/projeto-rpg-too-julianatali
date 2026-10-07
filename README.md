# ⚔️ RPG – Missões com Herança, Encapsulamento e Enum

Trabalho avaliativo de **Tecnologia de Orientação a Objetos (TOO) – 2026/1**.
O projeto evolui a classe `Missao` do RPG feito em aula: atributos protegidos, status controlado por `Enum` e três tipos de missão que pagam XP ao herói.

## 📁 Estrutura

```
TOO_2026_1_Trabalho_JuliaNatali/TOO_2026_1_Julia_Natali/
├── main.py                      # demonstração
└── model/
    ├── enums.py                 # ClasseHeroi, TipoInimigo, StatusMissao
    ├── personagem.py            # (já pronto) XP e nível
    ├── heroi.py / inimigo.py
    ├── missao.py                # classe mãe
    ├── missao_caca.py           # MissaoCaca
    ├── missao_coleta.py         # MissaoColeta
    └── missao_exploracao.py     # MissaoExploracao
```

## ✅ O que foi implementado

| Parte | Descrição |
|---|---|
| 1 – Encapsulamento | Todos os atributos de `Missao` são privados, com `@property`. Só o `status` tem setter, pois é o único que muda durante o jogo (justificado no comentário da classe). |
| 2 – Enum | `StatusMissao` (PENDENTE → EM_ANDAMENTO → CONCLUIDA). O setter bloqueia pular etapa ou retroceder (`ValueError`) e rejeita valores que não sejam do enum (`TypeError`). |
| 3 – Subclasses | Cada tipo tem um atributo privado próprio e sobrescreve `calcular_recompensa()` com `super()` + bônus. |
| 4 – XP ao herói | `concluir_missao(heroi)` muda o status para CONCLUIDA **antes** de pagar a recompensa via `ganhar_experiencia()`. |
| 5 – Demonstração | `main.py` percorre a lista de missões, sobe o herói de nível e trata erros com `try/except`. |

### 🎯 Tipos de missão

| Missão | Atributo próprio | Bônus |
|---|---|---|
| `MissaoCaca` | `quantidade_inimigos` | +10 XP por inimigo |
| `MissaoColeta` | `quantidade_itens` | +5 XP por item |
| `MissaoExploracao` | `areas_exploradas` | +20 XP por área |

Exemplo: caça com recompensa base 100 e 5 inimigos → **150** XP quando concluída e **0** enquanto pendente ou em andamento.

## ▶️ Como executar

```bash
cd TOO_2026_1_Trabalho_JuliaNatali/TOO_2026_1_Julia_Natali
python main.py
```

## 🧪 Resultado da execução

```text
 Recompensa de cada missão
missão [MissaoCaca]: Caça aos Orcs | status: Pendente -> recompensa: 0
missão [MissaoColeta]: Ervas Raras | status: Pendente -> recompensa: 0
missão [MissaoExploracao]: Ruínas Antigas | status: Pendente -> recompensa: 0

 Ciclo completo até subir de nível

Dados do Heroi:

Nome: Aragorn
Vida: 100
Ataque: 15
Defesa: 8
Nível: 1
XP: 0
Tipo: Guerreiro

A missão Caça aos Orcs começou! O objetivo é derrotar os orcs da floresta.
Aragorn subiu para o nível 2!
missão [MissaoCaca]: Caça aos Orcs | status: Concluída -> recompensa paga: 150
A missão Ervas Raras começou! O objetivo é coletar ervas medicinais.
missão [MissaoColeta]: Ervas Raras | status: Concluída -> recompensa paga: 90
A missão Ruínas Antigas começou! O objetivo é explorar as ruínas ao norte.
Aragorn subiu para o nível 3!
missão [MissaoExploracao]: Ruínas Antigas | status: Concluída -> recompensa paga: 140

Dados do Heroi:

Nome: Aragorn
Vida: 120
Ataque: 19
Defesa: 10
Nível: 3
XP: 80
Tipo: Guerreiro

Erros de propósito
Erro: Transição inválida: Concluída -> Pendente
Erro: Transição inválida: Pendente -> Concluída
Erro: O status precisa ser um StatusMissao
```

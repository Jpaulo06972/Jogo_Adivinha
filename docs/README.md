# 📌 AdivinhaNumérico – Jogo de Adivinhação de 4 Dígitos

## 📝 Descrição
Projeto acadêmico desenvolvido para a disciplina de Lógica de Programação, onde o jogador deve adivinhar um número secreto de 4 dígitos com:

- 10 tentativas para acertar
- Dicas progressivas a partir da 5ª tentativa
- Validação de entradas
- Sistema de reinício automático

## ⚙️ Funcionalidades
### ✔ Sistema de Jogabilidade
- Geração aleatória do número (1000-9999)
- Controle de tentativas restantes
- Dicas posicionais (dígitos corretos revelados)

### ✔ Mecânicas de Dicas
- A partir da 5ª tentativa:
  - Mostra dígitos corretos na posição certa
  - Marca incorretos com `_`
  - Exemplo: `4 _ 9 _`

### ✔ Validações
- Bloqueio de números fora do intervalo
- Prevenção de inputs inválidos
- Confirmação para reiniciar o jogo

## 🛠️ Tecnologias Utilizadas
| Área           | Tecnologias |
|----------------|------------|
| **Linguagem**  | Python 3   |
| **Bibliotecas**| `random`, `os` |
| **Plataforma** | Terminal (CLI) |

## 📦 Estrutura do Código
📂 adivinhacao/
├── src/
│   └── adivinhacao.py (código principal)
├── docs/
│   └── README.md
└── LICENSE

## 🎮 Menu do Jogo

    => Bem Vindo ao Jogo do Adivinha !|! <=

    Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999]
    a partir da 5a. tentativa o jogo irá te ajudar, dando dicas 

    Digite sua tentativa de código: [input]

## 📌 Regras do Jogo
    - Números entre 1000-9999 apenas

    - 10 tentativas totais

    - Dicas ativadas após 5 tentativas

    - Vitória ao acertar todos dígitos na posição correta

## 📌 Melhorias Futuras
- Sistema de pontuação

- Dificuldades progressivas

- Ranking de jogadores

- Interface gráfica (Tkinter/PyGame)

## 📄 Licença
        GNU General Public License v3.0.

## ✉️ Contato
    [João Paulo Ferreira] - [jpauloferreira2006@gmail.com]
    https://www.linkedin.com/in/jo%C3%A3o-paulo-ferreira-6a1ab8328/
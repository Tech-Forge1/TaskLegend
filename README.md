# TaskAdventure
TaskLegend is a task manager (for human tasks) that includes gamification features, such as its own in-app currency, mini-games, and more.

# Project Members

- **Vitor Berniz Lopes** ( https://github.com/Vibelon ) — Project management and interface design 
- **Renato Lois M. Silva** ( https://github.com/RLois4 ) — Frontend-backend communication using Flask  
- **Wagner Luiz** ( https://github.com/Wagner0070 ) — Frontend  
- Omar Augusto Rodrigues ( https://github.com/omariscode/omariscode ) — Login System
- Nícolas "N_loco" ( https://github.com/n-loco ) — MineGames

# Notes

All names listed above were included with the explicit permission of each individual. For this reason, some entries only display the GitHub profile without the name, as those individuals did not consent to having their names disclosed.

# Gerenciador de Tarefas Inteligente com Gamificação

# Visão Geral

O projeto é um gerenciador de tarefas inteligente baseado em inteligência artificial (IA) que combina ferramentas de produtividade com elementos de gamificação para tornar o gerenciamento de tarefas mais envolvente e eficiente.

## Funcionalidades Principais

### 1. **Chatbot Assistente:**

- O sistema inclui um chatbot para auxiliar os usuários na criação, organização e acompanhamento de tarefas.
- O chatbot utiliza IA para entender comandos e oferecer sugestões personalizadas.

### 2. **Recomendação de Prioridade:**

- Uma IA especializada avalia as tarefas criadas e atribui uma prioridade de 0 a 10 com base em diversos fatores, como:
  - Prazo de conclusão.
  - Importância relativa.
  - Impacto no progresso do usuário.

### 3. **Gamificação e Minijogos:**

- A cada tarefa concluída, o usuário ganha moedas virtuais.
- Essas moedas podem ser usadas para desbloquear acesso a uma seção especial com múltiplos minijogos.

### 4. **Recompensas Personalizáveis:**

- O usuário pode definir a quantidade de moedas recebidas ao criar uma tarefa, respeitando limites estabelecidos.
- Limites ajustáveis com base no nível do usuário para evitar abusos (como definir recompensas exorbitantes).

### 5. **Progressão e Níveis:**

- Concluir tarefas aumenta o nível do usuário.
- Cada nível alcançado desbloqueia melhorias, como:
  - Aumento no limite de moedas atribuídas por tarefa.
  - Novas funcionalidades ou acessos exclusivos.

### 6. **Decaimento de Recompensas:**

- A recompensa de uma tarefa é dividida pelo número de segundos estimados para concluí-la.
- A cada segundo que passa, a recompensa diminui progressivamente até chegar a 0.
- Se a tarefa não for concluída dentro do prazo, começam a ser descontadas moedas do saldo do usuário como penalidade, incentivando a conclusão rápida.


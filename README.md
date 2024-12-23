# TaskAdventure
TaskLegend is a task manager (for human tasks) that includes gamification features, such as its own in-app currency, mini-games, and more.

# Project Members

- **Vitor Berniz Lopes** ( https://github.com/Vibelon ) — Project management and interface design
- **Renato Lois M. Silva** ( https://github.com/RLois4 ) — Frontend-backend communication using Flask
- **Wagner Luiz** ( https://github.com/Wagner0070 ) — Frontend
- **Omar Augusto Rodrigues** ( https://github.com/omariscode/omariscode ) — Login System
- **Nícolas "N_loco"** ( https://github.com/n-loco ) — MineGames

# Notes

All names listed above were included with the explicit permission of each individual. For this reason, some entries only display the GitHub profile without the name, as those individuals did not consent to having their names disclosed.

# Intelligent Task Manager with Gamification

### Overview

The project is an intelligent task manager based on artificial intelligence (AI) that combines productivity tools with gamification elements to make task management more engaging and efficient.

## Main Features

### 1. **Assistant Chatbot:**

- The system includes a chatbot to assist users in creating, organizing, and tracking tasks, as well as serving as a knowledge source, etc.

### 2. **Priority Recommendation:**

- A specialized AI evaluates the created tasks and assigns a priority from 0 to 10 based on various factors such as:
  - Completion deadline.
  - Relative importance.

### 3. **Gamification and Mini-Games:**

- Each completed task rewards the user with virtual coins.
- These coins can be used to unlock access to a special section with multiple mini-games.

### 4. **Customizable Rewards:**

- The user can set the amount of coins received when creating a task, within established limits.
- Adjustable limits based on the user's level to avoid abuse (such as setting exorbitant rewards).

### 5. **Progression and Levels:**

- Completing tasks increases the user's level.
- Each level reached unlocks improvements, such as:
  - Increased coin limit per task.
  - Access to different themes on the website (such as the cloud theme).

### 6. **Reward Decay:**

- The reward for a task is divided by the number of seconds to complete it.
- For each passing second, the reward decreases progressively until it reaches 0.
- If the task is not completed within the deadline, coins are deducted from the user's balance as a penalty, encouraging fast completion.

### 7. **User Ranking:**

- The system includes a global ranking that displays users with the most accumulated coins and highest levels.
- The ranking is updated daily, with the possibility to view positions of friends or a specific group of users.
- **Ranking Criteria:**
  - Accumulated coins.
  - Reached level.
  - Tasks completed on time.
  - Performance in mini-games.

- Users with the best positions in the ranking can receive additional rewards, such as extra coins, new exclusive mini-games, or special features.
- The ranking serves as an extra motivation for users, encouraging healthy competition and progress within the system.

### 8. **Group Challenges:**

- The system allows creating group challenges, where a set of users can collaborate to complete tasks together.
- Group results also contribute to the ranking competition, with additional points given to the group with the best performance.
- **Benefits of Group Challenges:**
  - Group rewards distributed among participants.
  - Increased coins for the winning group.
  - Specific ranking for groups, in addition to the individual ranking.

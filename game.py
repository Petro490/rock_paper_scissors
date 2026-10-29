import random

# --- ДОБАВЛЕННЫЙ КЛАСС ---
class ScoreBoard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def update(self, winner):
        """Обновление счета в зависимости от результата раунда."""
        if winner == "You win!":
            self.player_score += 1
        elif winner == "Computer wins!":
            self.computer_score += 1

    def display(self):
        """Вывод текущего счета на экран."""
        print(f"Score: Player {self.player_score} - Computer {self.computer_score}")

    def save_to_file(self, filename="scores.txt"):
        """Сохранение итогового результата в текстовый файл."""
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Final Result\nPlayer: {self.player_score}\nComputer: {self.computer_score}")
            print(f"Results successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")
# -------------------------

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower().strip()
        if user_input == 'q':
            return 'quit'
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid input! Please enter 'rock', 'paper', 'scissors' or 'q' to quit.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if rules[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    # Инициализируем объект счета
    scoreboard = ScoreBoard() 
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            # Сохраняем счет перед выходом
            scoreboard.save_to_file() 
            print("Thanks for playing! Goodbye.")
            break
            
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        
        # Обновляем и выводим счет
        scoreboard.update(result)
        scoreboard.display()
        
        print("-" * 30)

if __name__ == "__main__":
    main()

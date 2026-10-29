import random

def get_computer_choice():
    """Случайный выбор компьютера."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Получение и проверка ввода пользователя."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower().strip()
        
        if user_input == 'q':
            return 'quit'
        
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        
        print("Invalid input! Please enter 'rock', 'paper', 'scissors' or 'q' to quit.")

def determine_winner(user_choice, computer_choice):
    """Определение победителя раунда."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Словарь правил: ключ побеждает значение
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if rules[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
            
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        print("-" * 30)

if __name__ == "__main__":
    main()

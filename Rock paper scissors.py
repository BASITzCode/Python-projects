import random
def game():
    user = input("Enter your choice (rock, paper or scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!") 
    ask=input(" Enter yes to play  or no to exit...")
    if ask.lower() == "yes":
        game()
    else:
        print("Thanks for playing!")
game()
    
    
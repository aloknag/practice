#
# rock, paper, scissors implementation
#
import random

user_input_history = {'rock': 0, 'paper': 0, 'scissors': 0}
choices = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
number_of_games = 0
win_record = {'computer': 0, 'user': 0, 'tie': 0}


def make_guess():
    # get sorted key,value from user_input_history
    sorted_list = sorted(user_input_history.items(), key=lambda t: t[1], reverse=True)
    if sorted_list[0][1] != sorted_list[1][1]:
        # first element and second element are used equally.
        our_guess = choices[sorted_list[0][0]]
    else:
        # first and second choice is equal No real candidate for choice.
        our_guess = random.choice(choices.keys())
    return our_guess


def play_game():
    user_choice = raw_input("Enter your choice: 'rock, paper, scissors or 'q' to quit: ").lower()
    if user_choice == 'q':
        print "Thanks for playing the game"
        print "Total games played: %d" % number_of_games
        print "Wins:"
        for k, v in win_record.items():
            print "\t %s: %d" % (k,v)
        print "Your pattern of choices:"
        for k, v in user_input_history.items():
            print "\t %s: %d" % (k,v)
        exit()
    else:
        user_input_history[user_choice] += 1
        computer_choice = make_guess()
        if user_choice == 'rock':
            if computer_choice == 'scissors':
                print 'User Wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['user'] += 1
            elif computer_choice == 'paper':
                print 'Computer wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['computer'] += 1
        if user_choice == 'scissors':
            if computer_choice == 'paper':
                print 'User Wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['user'] += 1
            elif computer_choice == 'rock':
                print 'Computer Wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['computer'] += 1
        if user_choice == 'paper':
            if computer_choice == 'rock':
                print 'User Wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['user'] += 1
            elif computer_choice == 'scissors':
                print 'Computer wins: Your choice: %s, Computer Choice: %s' % (user_choice, computer_choice)
                win_record['computer'] += 1
        if user_choice == computer_choice:
            print "It's a tie: Your choice: %s, Computer Choice: %s" % (user_choice, computer_choice)
            win_record['tie'] += 1

if __name__ == '__main__':
    while True:
        play_game()
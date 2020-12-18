#Explaining the rules

import secrets
choices = {'r':'ROCK','p':'PAPER','s':'SCISSOR'}
comp_win = 0
user_win = 0
draw = 0

what_to_fetch = input('---WELCOME TO ROCK PAPER SCISSOR GAME---\n\nPRESS I TO BRING INSTRUCTIONS OR PRESS P TO PLAY ')
#Showing the user what Computer chose and printing the winner along with
#increasing the winning count
while True:    
    #TO DO or user_ip in 'iI':
    if what_to_fetch in 'iI':
        print('\n\nBELOW ARE THE INSTRUCTIONS FOR PLAYING\n\n')
        print('Select your input by pressing the first word: \n')
        print('*R for Rock','*P for Paper','*S for Scissor', sep='   ')
        print('WIN -> 1 pt.    LOSE -> -1 pt.    DRAW -> 0pt.\n','GOOD LUCK!')
        what_to_fetch = 'x'
    else:
        pass
    
    #Computer randomly choosing the input
    comp_ip = secrets.choice('rps')
    
    #TO DO Press I for Instructions\n
    user_ip = input('Enter R for Rock, P for Paper, S for Scissor: \nPress E to End the game. ')
    user_ip = user_ip.lower()
    #Check user input valid or not
    while True:
        if user_ip not in 'rpsei' :
            print('INVALID INPUT!')
            user_ip = input('\nEnter R for Rock, P for Paper, S for Scissor: \nPress E to End the game. ')
        elif user_ip == 'e':
            break
        else:
            break
    print('\n\n')

#User wants to play (not wants to end)
    if user_ip != 'e':
        
        if user_ip == 'r' and comp_ip == 'p':
            print('YOU CHOSE ROCK\n')
            print('COMPUTER PLAYED PAPER')
            print('COMPUTER WINS!')
            comp_win += 1
            continue

        elif user_ip == 'r' and comp_ip == 's':
            print('YOU CHOSE ROCK\n')
            print('COMPUTER PLAYED SCISSOR')
            print('YOU WIN!')
            user_win += 1
            continue

        elif user_ip == 'p' and comp_ip == 'r':
            print('YOU CHOSE PAPER\n')
            print('COMPUTER PLAYED ROCK')
            print('YOU WIN!')
            user_win += 1
            continue

        elif user_ip == 'p' and comp_ip == 's':
            print('YOU CHOSE PAPER\n')
            print('COMPUTER PLAYED SCISSOR')
            print('COMPUTER WINS!')
            comp_win += 1
            continue

        elif user_ip == 's' and comp_ip == 'r':
            print('YOU CHOSE SCISSOR\n')
            print('COMPUTER PLAYED ROCK')
            print('COMPUTER WINS!')
            comp_win += 1
            continue

        elif user_ip == 's' and comp_ip == 'p':
            print('YOU CHOSE SCISSOR\n')
            print('COMPUTER PLAYED PAPER')
            print('YOU WIN!')
            user_win += 1
            continue
        
        elif user_ip == 'i':
            print('\n\nBELOW ARE THE INSTRUCTIONS FOR PLAYING\n\n')
            print('Select your input by pressing the first word: \n')
            print('*R for Rock','*P for Paper','*S for Scissor', sep='   ')
            print('WIN -> 1 pt.    LOSE -> -1 pt.    DRAW -> 0pt.\n','GOOD LUCK!')
            continue
            

        else:
            print(f'You CHOSE {choices[user_ip]}')
            print(f'COMPUTER ALSO CHOSE {choices[user_ip]}')
            print('DRAW!')
            print('NO POINTS AWARDED')
            draw += 1
            continue

#If user wants to end the game    
    else:
        break

#If YES, then simply print scorecard and show who won overall 
#out of how many matches
print('---END OF THE GAME---\n\n')
print('---SCORECARD IS AS FOLLOWS: \n')
print(f'OUT OF {user_win+comp_win+draw} round(s),')
print(f'Computer won {comp_win} round(s).')
print(f'You have won {user_win} round(s).')

if user_win > comp_win:
    print("\n\nCONGRATULATIONS!   YOU'VE WON THE GAME!")
elif user_win < comp_win:
    print('\n\nCOMPUTER HAS WON THE GAME. BETTER LUCK NEXT TIME!')
elif user_win+comp_win+draw == 0:
    print('\n\nNo games were played. See you soon!')
else:
    print('DRAW!')
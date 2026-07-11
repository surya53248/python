import random
game=['rock','paper','scissors']
my_points=0
computer_points=0
while True:
    computer_choice=random.choice(game)
    my_choice=input('enter--rock,paper,scissors or quit: ').lower()
    if my_choice=='quit':
        break
    print('')
    print('--> '+'you picked '+my_choice)
    print('--> '+'computer picked '+computer_choice)
    print('')
    if my_choice==computer_choice:
        print("it's a draw"+ " , "+ "computer picked "+my_choice)
    if my_choice=='rock'and computer_choice=='paper':
        print('you lose!')
        computer_points=computer_points+1
    if my_choice=='rock'and computer_choice=='scissors':
        print('you win!')
        my_points=my_points+1
    if my_choice=='paper'and computer_choice=='rock':
        print('you win!')
        my_points=my_points+1
    if my_choice=='paper'and computer_choice=='scissors':
        print('you lose!')
        computer_points=computer_points+1
    if my_choice=='scissors'and computer_choice=='rock':
        print('you lose!')
        computer_points=computer_points+1
    if my_choice=='scissors'and computer_choice=='paper':
        print('you win!')
        my_points=my_points+1
    print("me"+' --> '+str(my_points) +" , "+"computer "+"--> "+str(computer_points))
import random
choices_list = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
computer = random.choice(choices_list)
player_win = 0
computer_win = 0
while player_win < 2 and computer_win < 2:
    ind = int(input('choose one num(0-石头|1-剪刀|2-布): '))
    player = choices_list[ind]

    print('outcome you:%s vs computer: %s' % (player, computer))
    if player == computer:
        print('Tie')
    elif [player, computer] in win_list:
        print('you win')
        player_win += 1
    else:
        print('you lose')
        computer_win += 1
else:
        print('result  you:%s vs computer: %s' % (player_win, computer_win 
              

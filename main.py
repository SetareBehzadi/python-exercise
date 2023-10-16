import random

from config import GAME_CHOICES, RULES, scoreboard

from datetime import datetime, timedelta

from decorators import log_time


def get_user_choice():
    user_input = input('please enter your choice (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print("please choice again!")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)


def find_winner(user,system):
    """
    :param user:
    :param system:
    :return:
    """
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]

def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
    else:
        scoreboard['system'] += 1
    print("#" * 20)
    print("#", f"user : {scoreboard['user']}", "#")
    print("#", f"system : {scoreboard['system']}", "#")


def play_one_hand():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        if winner == user_choice:
            result['user'] += 1
            msg = 'You win'
        elif winner == system_choice:
            result['system'] += 1
            msg = 'You lose'
        else:
            msg = 'Draw'
        print(f"user: {user_choice}\t system: {system_choice}\t result: {msg}")
    update_scoreboard(result)
    play_again = input("Do you want play again? (y/n)")
    if play_again == "y":
        play_one_hand()


@log_time
def play():
    play_one_hand()


if __name__ == '__main__':
    play()


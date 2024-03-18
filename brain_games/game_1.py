#!/usr/bin/env python3
from brain_games.scripts.brain_games import hello_user
import random
import prompt


def game_1():
    sum_answer = 0
    name = hello_user()
    print('Answer "yes" if the number is even, otherwise answer \"no\".')
    while sum_answer != 3:
        question_1 = random.randint(1, 100)
        print(f'Question: {question_1}')
        answer_1 = prompt.string('Your answer: ')

        if question_1 % 2 == 0 and answer_1.strip() == 'yes':
            print('Correct!')
            sum_answer += 1
            continue
        elif question_1 % 2 != 0 and answer_1.strip() == 'no':
            print('Correct!')
            sum_answer += 1
            continue
        elif question_1 % 2 == 0:
            print(f"""\'{answer_1}\' is wrong answer ;(. Correct answer was 'yes'.
Let\'s try again, {name}!""")
            break
        else:
            print(f"""\'{answer_1}\' is wrong answer ;(. Correct answer was 'no'.
Let\'s try again, {name}!""")
            break
    else:
        print(f'Congratulations, {name}!')

#!/usr/bin/env python3
from brain_games.cli import welcome_user


def hello_user():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    return name


def main():
    hello_user()


if __name__ == '__main__':
    main()

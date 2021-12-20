#! /usr/bin/env python3
import prompt

def main():
    print("Welcome to the Brain Games!")
    welcome_user()

def welcome_user():    
    name = prompt.string(prompt="May I have your name? ", empty=False)
    print(f"Hello, {name}!")

if __name__ == '__main__':
    main()
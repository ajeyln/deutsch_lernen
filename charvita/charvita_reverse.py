# This file helps German learners to memorize the vocabulary
# Program flashes a word and user must "memorize" the right response
# Program name is inspired by Samskruta word "Charvita Charvana"
# kind of Rote learning
# developed by vazudew

# -*- coding: iso-8859-1 -*-
import codecs

import time
import sys
import os
import random

encoding_type='utf-8'
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def get_loaded_data(file_path):
    with open(file_path, 'r', encoding=encoding_type) as fileHandle:  
        data = fileHandle.readlines() 
    return {
                item.split()[0] : ' '.join(item.split()[1:]) or "No response given" for item in data
            }

def charvita(wordsDictionary):
    count = 0
    while True:
        print("Learn German Vocabulary !")
        print(f"======Memorized word count is {count}===")
        print("****TYPE Q to quit !*****")
        question, answer= random.choice(list(wordsDictionary.items()))
        print(f'WORD :{answer }\n', end='')
        signal = input("type Y to display the answer : ")

        if signal.lower() == 'y':
            print(f'\r ANSWER: {question} \n', end='', flush=True)
            count +=1
            weiter= input("type Y to continue ")
            if weiter.lower() != 'y':
                print(" End of Game ! Have a good day!")
                print("Today you have solved {} words".format(count))
                break
        else:
            print(" End of Game ! Have a good day!")
            print("Today you have solved {} words".format(count))
            break
        clear_screen()

if __name__ == '__main__':

    if (len(sys.argv) <2):
        print("File path is not given and hence exit")
        exit()
    
    file_path = sys.argv[1] # file path

    if not os.path.exists(file_path):
        print("file does not exist!") 
        exit()

    dictionary = get_loaded_data(file_path)
    charvita(dictionary)

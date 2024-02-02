# This script is part of the Customer Satisfaction Survey.
# Holds the following functions:
# (1) to slow down the words appearing in the console
# (2) to provide a banner
# (3) to validate user input
from colorama import Fore
import sys
import time
import surveyinfo


def slowDown(*inputtxt: str, timedel=float, colour=False):
    """
    to slow down the words appearing on the screen
    to print the questions in purple
    :param inputtxt:
    :param timedel:
    :return:
    """
    for txt in inputtxt:
        if colour:
            print(f'{Fore.MAGENTA}')
        for character in txt:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(timedel)
        print(f'{Fore.LIGHTWHITE_EX}')


def niceOutput(width: int, *inputtxt: str):
    """
    formats text
    :param my_txt:
    :param my_width:
    :return:
    """
    my_line = '-'
    print(f'{Fore.BLUE} + {my_line.center(width,"-" )} +')
    for txt in inputtxt:
        print(f'{Fore.GREEN} {txt.center(width)}')
    print(f'{Fore.BLUE} + {my_line.center(width,"-" )} + {Fore.LIGHTWHITE_EX}')


def responseCheck(input_str: str):
    """
    check is the string is empty or if it contains numbers
    calls itself again if the user input is incorrect
    :param input_str:
    :return:
    """
    if len(input_str) == 0:
        print(surveyinfo.validationtext2)
        answer1 = input(surveyinfo.validationtext1)
        return responseCheck(answer1)
    elif input_str.isdigit():
        if int(input_str) > 0 and int(input_str) < 7:
            return input_str
        else:
            print(surveyinfo.validationtext3)
            answer1 = input(surveyinfo.validationtext1)
            return responseCheck(answer1)
    else:
        print(surveyinfo.validationtext3)
        answer1 = input(surveyinfo.validationtext1)
        return responseCheck(answer1)

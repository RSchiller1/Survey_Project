# This script part of the Customer Satisfaction Survey.
# Holds the following functions:
# (1) checks if the results file already exists
# (2) creates results file if not existing
# (3) imports results file if exists
import random
import os.path
import ast


def checkFile():
    """
    to check if the results file already exists
    :return:True or False
    """
    path = './Results.txt'
    check_file = os.path.isfile(path)
    return check_file


def createInitialresults(questions_list, results_dict):
    """
    to randomly create the results for the previous 6 people who answered the survey
    :return: results_dict
    """
    counter = 0
    for all in questions_list:
        for question in all:
            counter += 1
            random_nums = random.sample(range(1, 7), 6)
            results_dict.update({counter: random_nums})
    return results_dict


def importResults(questions_list, results_dict):
    """
    checks if the results file exists, otherwise it is created with random data
    :return:
    """
    if checkFile():
        #print(f'Results file has been found and will be imported')
        with open('Results.txt', 'r') as existing_results:
            data = existing_results.read()
        results_dict = ast.literal_eval(data)
        return results_dict
    else:
        #print(f'Results file cannot be found and will be created')
        return createInitialresults(questions_list, results_dict)
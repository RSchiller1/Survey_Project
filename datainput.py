# This script is part of the Customer Satisfaction Survey.
# Holds the following functions:
# (1) imports json file
# (2) splits json file
import json


def importData():
    """
    imports the json file containing the questions and the valid options for answers
    :return: questions_data
    """
    with open("questions.json") as questions_file:
        questions_data = json.load(questions_file)
        return questions_data


def splitoptionsData(questions_data: dict):
    """
    splits up the original json file to obtain a list with the answer options
    :param questions_data:
    :return: options_list
    """
    options_list = questions_data.get('options')
    return options_list


def splitquestionssData(questions_data: dict):
    """
    splits up the original json file to obtain a list with the questions
    :param questions_data:
    :return: questions_list
    """
    questions_list = questions_data.get('questions')
    return questions_list


def optionsOutput(options_list: list):
    """
    concatenates the answers options into a string
    :param options_list:
    :return: options_sentence
    """
    for index in range(len(options_list)):
        if index == 0:
            options_sentence = options_list[index]['Option']
        else:
            options_sentence = options_sentence + ';  ' + options_list[index]['Option']
    return options_sentence


def headingsOutput(questions_list: list):
    """
    creates a list for the graph headings
    :param questions_list:
    :return: question_headers
    """
    question_headers = []
    for index in range(len(questions_list)):
        header = questions_list[index]['Question'].partition('-')[0]
        question_headers.append(header)
    return question_headers
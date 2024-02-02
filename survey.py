# This script is part of the Customer Satisfaction Survey.
# Holds the following functions:
# (1) ask the questions for the survey
# (2) prints summary of the participants choices
import manageconsole
import surveyinfo
new_results = []


def askQuestions(questions_list: list, options_sentence: str):
    """
    loops through the survey questions and adds the results to a new list
    :param questions_list:
    :param options_sentence:
    :return: new_results
    """
    for index in range(len(questions_list)):
        manageconsole.slowDown(questions_list[index]['Question'], timedel=0.1, colour=True)
        print()
        manageconsole.slowDown(options_sentence,  timedel=0.05)
        print()
        answer1 = input(surveyinfo.validationtext1)
        valid_answer = manageconsole.responseCheck(answer1)
        new_results.append(valid_answer)
    return new_results


def printSummary(question_headers: list, new_results: list):
    """
    prints summary of the participants choices
    :param question_headers:
    :param new_results:
    :return:
    """
    summary_list = list(zip(question_headers, new_results))
    print(surveyinfo.ansfeedback1)
    print(*summary_list, sep='\n')

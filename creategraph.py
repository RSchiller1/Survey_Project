# This script is part of the Customer Satisfaction Survey.
# This package:
# (1) calculates the average for each question on the survey
# (2) sets up the bar chart
# (3) creates the graph

from matplotlib import pyplot as plt
import surveyinfo


def createAverage(results_dict: dict):
    """
    create the average score for a question
    then uses the round method to obtain a num to 2 dec places
    updates average_list and question_names
    :return: average_results
    """
    length = list(map(len, results_dict.values()))
    average_results = [round((sum(values) / length[0]),2) for key, values in results_dict.items()]
    #print(average_results)
    return average_results


def plotGraph( x_values: list, y_values: list):
    """
    to show the average score obtained for each question
    :param x_values: the questions
    :param y_values: the averages
    :return:
    """
    plt.rcParams["figure.figsize"] = [12.00, 6.50]
    plt.rcParams["figure.autolayout"] = True
    plt.get_current_fig_manager().set_window_title(surveyinfo.graphwindow)
    plt.bar(x_values, y_values)
    plt.xlabel(surveyinfo.graphxlabel)
    plt.ylabel(surveyinfo.graphylabel)
    plt.title(surveyinfo.graphtitle)
    plt.show()


def createGraph(question_headers: list, results_dict: dict):
    """
    calls the above 2 functions to find the average and polt the graph
    :param question_headers:
    :param results_dict:
    :return:
    """
    average_results = createAverage(results_dict)
    plotGraph(question_headers, average_results)


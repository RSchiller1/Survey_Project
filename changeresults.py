# This script part of the Customer Satisfaction Survey.
# This package:
# (1) adds the customers answers to the results file
# (2) export the end results back to the pc


def addResult(add_list: list, results_dict: dict):
    """
    add the answers to the questions from the current input to the existing survey results
    change type to int so that average results can be calculated
    :param add_list:
    :param results_dict:
    :return: results_dict
    """
    counter = 0
    for key in results_dict:
        results_dict[key].append(int(add_list[counter]))
        counter += 1
    return results_dict


def exportResults(imported_info: dict):
    """
    exports the results file back to the pc
    :param imported_info:
    :return:
    """
    with open('Results.txt', 'w') as data:
        data.write(str(imported_info))


# This is the main script for the Customer Satisfaction Survey.
# Handle with tlc (tender love & care!)

import createresults
import changeresults
import creategraph
import datainput
import survey
import surveyinfo
import manageconsole
import time

#set up required objects
results_dict = {}

#import questions and options and manipulate them into the required formats
questions_data = datainput.importData()
options_list = datainput.splitoptionsData(questions_data)
questions_list = datainput.splitquestionssData(questions_data)
question_headers = datainput.headingsOutput(questions_list)

#create string sentence for outputting options onto console
options_sentence = datainput.optionsOutput(options_list)

#import existing survey results or create results file
imported_results = createresults.importResults(questions_list, results_dict)

#provide participant with instructions
manageconsole.niceOutput(80,surveyinfo.intro1, surveyinfo.intro2, surveyinfo.intro3, surveyinfo.intro4, surveyinfo.intro5)
time.sleep(10)

#implement survey and provide summary
manageconsole.slowDown(surveyinfo.intro6, timedel=0.1)
new_results = survey.askQuestions(questions_list, options_sentence)
survey.printSummary(question_headers, new_results)

#create new results from user input and export these results
updated_results = changeresults.addResult(new_results, imported_results)
changeresults.exportResults(updated_results)

#thank the user for participation and display results
manageconsole.niceOutput(120,surveyinfo.end1, surveyinfo.end2, surveyinfo.end3, surveyinfo.end4)
creategraph.createGraph(question_headers, updated_results)
















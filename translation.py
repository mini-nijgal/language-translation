import json
from language import language
import pandas as pd

#-----------------lang_dict-------------
masterData = pd.read_csv("./input/MergedList.csv")
with open('./input/en_US.json') as f:
    englishLabels = json.load(f)

#------------------Filter---------------------
masterData = masterData[masterData['English (ENG)'].isin(englishLabels.keys())]

#-----------------lang_dict-------------
with open('./input/languages.json') as f:
    languages = json.load(f)
#---------------------------------------

for lang in languages:
    print("-----------------Copy started for - <" + lang["name"] + ">--------------------------")
    outputFileName = './output/' + lang["filename"] + '.json'
    dictionary = masterData.set_index('English (ENG)')[lang["name"]].to_dict()
    with open(outputFileName, "w") as outfile: 
        json.dump(dictionary , outfile)
    print("-----------------Copy completed for - <" + lang["name"] + ">--------------------------")

#--------------Not tranlated labels---
for translatedLabel in masterData['English (ENG)']:
    englishLabels.pop(translatedLabel)

#
with open("./pending/LabelsNotTranslated.json", "w") as outfile: 
    json.dump(englishLabels , outfile)
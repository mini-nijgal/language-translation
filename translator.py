import json
from google_trans_new import google_translator  
import pathlib
from language import language

#------------------------

class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
#------------------------

#-----------------lang_dict-------------
with open('./input/languages.json') as f:
    languages = json.load(f)
#---------------------------------------

#---------input labels in english-------
with open('./pending/LabelsNotTranslated.json') as f:
    data = json.load(f)
#--------------------------------------


outputDict = my_dictionary();
translator = google_translator() 

for lang in languages:
    print("-----------------Translation started for - <" + lang["name"] + ">--------------------------")
    for  value in data:
        res = translator.translate(data.get(value), lang_tgt=lang["languageCode"])
        outputDict.add(value,res)
        
    print("-----------------Translation completed for - <" + lang["name"] + ">--------------------------")
	
    outputFileName = './pending/TranslatedUsingGoogleTranslator/' + lang["filename"] + '.json'

    with open(outputFileName, "w") as outfile: 
        json.dump(outputDict , outfile)
        
    outputDict.clear()
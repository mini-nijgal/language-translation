import os

cmd1 = "translation.py"
os.system(cmd1)

print("################ Translation unproccessed labels  ###################")

cmd2 = "translator.py"
os.system(cmd2)

cmd3 = "cls" # replace it with "clear" in mac
os.system(cmd3)

print("################ All Done - refer output folder ###################")
print(" ***** you can find unproccessed labels in pending/LabelsNotTranslated.json ******")
print(" ***** Contact Godson for label translations ******")
print("---------------------------------------------------------------------")
print(" !! All unproccessed files are translated using google translator !! ")
print(" !! you can find those files under pending/TranslatedUsingGoogleTranslator folder!! ")
print(" !! use it only for development phase !! ")
print("---------------------------------------------------------------------")

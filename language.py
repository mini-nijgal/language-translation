class language:
    def __init__(self, name, languageCode,filename):
        self.name = name
        self.languageCode = languageCode
        self.filename = filename

    def print_language(self):
        return "{" + "'name':'" + self.name + '\'' + ", 'languageCode':'" + self.languageCode + '\'' +", 'filename':'" + self.filename + '\'' +'},'

    
import os,sys, json
import jinja2
# from jinja2 import Template

books = ["ഉല്പത്തി", "പുറപ്പാട്", "ലേവ്യപുസ്തകം", "സംഖ്യാപുസ്തകം", "ആവർത്തനം", "യോശുവ", "ന്യായാധിപന്മാർ",
"രൂത്ത്", "1 ശമൂവേൽ", "2 ശമൂവേൽ", "1 രാജാക്കന്മാർ", "2 രാജാക്കന്മാർ", "1 ദിനവൃത്താന്തം",
"2 ദിനവൃത്താന്തം", "എസ്രാ", "നെഹെമ്യാവു", "എസ്ഥേർ", "ഇയ്യോബ്", "സങ്കീർത്തനങ്ങൾ",
"സദൃശ്യവാക്യങ്ങൾ", "സഭാപ്രസംഗി", "ഉത്തമഗീതം", "യെശയ്യാ", "യിരമ്യാവു", "വിലാപങ്ങൾ",
"യെഹേസ്കേൽ", "ദാനീയേൽ", "ഹോശേയ", "യോവേൽ", "ആമോസ്", "ഓബദ്യാവു", "യോനാ",
"മീഖാ", "നഹൂം", "ഹബക്കൂക്ക്", "സെഫന്യാവു", "ഹഗ്ഗായി", "സെഖര്യാവു", "മലാഖി", "മത്തായി",
"മർക്കൊസ്", "ലൂക്കോസ്", "യോഹന്നാൻ", "പ്രവൃത്തികൾ", "റോമർ", "1 കൊരിന്ത്യർ", "2 കൊരിന്ത്യർ",
"ഗലാത്യർ", "എഫെസ്യർ", "ഫിലിപ്പിയർ", "കൊലൊസ്സ്യർ", "1 തെസ്സലൊനീക്യർ", "2 തെസ്സലൊനീക്യർ",
"1 തിമൊഥെയൊസ്", "2 തിമൊഥെയൊസ്", "തീത്തൊസ്", "ഫിലേമോൻ", "എബ്രായർ", "യാക്കോബ്",
"1 പത്രൊസ്", "2 പത്രൊസ്", "1 യോഹന്നാൻ", "2 യോഹന്നാൻ", "3 യോഹന്നാൻ","യൂദാ", "വെളിപ്പാട്"]

class GenerateHtml:
    def __init__(self):
        with open("bible.json", "r") as fp:
            self.data = json.load(fp)

        for i in range(len(self.data['Book'])):
            for j in range(len(self.data['Book'][i]['Chapter'])):
                self.create_html_file(i+1,j+1)
                
        # self.create_html_file(1,1)

    def load_template(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        return templateEnv.get_template('index.html')

    def create_html_file(self,book,chapter):
        # create a chapter eg: 1/1.html
        verses = self.data['Book'][book-1]['Chapter'][chapter-1]['Verse']
        template = self.load_template()

        filedata = template.render(
            books = books, # malayalam book name list
            chapters = range(1, len(verses)+1),
            activebook = book, # book number
            chapter = chapter,
            verses = verses
        )
        html_dir = os.path.join('site',str(book))
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)

        fname = '{0}/{1}.html'.format(html_dir,chapter)
        if os.path.isfile(fname):
            print('Chapter already exist')
        else:
            print('Book: {0}, Chapter: {1}'.format(book,chapter))
            fp = open(fname, 'w')
            fp.write(filedata)
            # create index.html file
            if book==1 and chapter==1:
                fp = open('site/index.html','w')
                fp.write(filedata)

if __name__=='__main__':
    c=GenerateHtml()
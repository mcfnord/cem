import sys
from HTMLParser import HTMLParser

gfImporting = False
gstrClassname = None

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global gfImporting
        global gstrClassname
        if tag == 'div': # is apparently lower-ized caseically speaking
            for attr in attrs:
                if attr[0] == 'id':
                    if attr[1] == gstrClassname: # name that class
                        gfImporting = True

    def handle_endtag(self, tag):
        global gfImporting
        if tag == 'div': ## Div fails. case sensitive html!
            gfImporting = False

    def handle_data(self, data):
        global gfImporting
        if gfImporting==True:
            mainoutfile.write(data) # show contents when we're importing

fname = sys.argv[1]                # arg1 is source pathspec
fname = fname.replace("ref/", "")  # remove /ref source prefix, if found
fname = fname.replace(".md", "")   # remove .md suffix, so I can add S1, S2 to core fname before .md
mainoutfile = open("tmp/" + fname + ".md", "w")
slide = 1

parser = MyHTMLParser()
for line in sys.stdin:
    if line.lower().startswith('# see '):
        slide = slide + 1
        mainoutfile.write('**[' + line[2:].strip() + '](' + fname + 'S' + str(slide) + '.html)**\r\n<br><br>\r\n')
        mainoutfile.close()
        mainoutfile = open("tmp/" + fname + "S" + str(slide) + ".md", "w")
        line = '# ' + line[6:]

    if line.lower().startswith('insert:'):
        params = line[len('insert:'):].split()
        filename ='src/' +  params[0]
        gstrClassname = params[1]
        f =  open(filename, "r")
	parser.feed(f.read())
        parser.close()
    else:
        mainoutfile.write(line),

mainoutfile.close()

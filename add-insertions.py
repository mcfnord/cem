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
            print (data) # show contents when we're importing

parser = MyHTMLParser()
for line in sys.stdin:
    if line.lower().startswith('insert:'):
        params = line[len('insert:'):].split()
        filename ='src/' +  params[0]
        gstrClassname = params[1]
        f =  open(filename, "r")
	parser.feed(f.read())
    else:
        print line,
#    parser.feed(line)
# parser.feed('foo bar bat <diV class="foo"> foopants </DIV> <div class="bar"> no dont show me</div>')


import sys
import os.path
import time
from HTMLParser import HTMLParser

gfImporting = False
gstrDivFName = None
gstrDivId = None
gInsertSought = False

def S3BinaryHostReplace( str ):
    str = str.replace("(img/", "(http://b00p.s3-us-west-2.amazonaws.com/img/")
    str = str.replace("(doc/", "(http://b00p.s3-us-west-2.amazonaws.com/doc/")
    return str ;

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global gfImporting
        global gstrDivId
        if tag == 'div': # is apparently lower-ized caseically speaking
            for attr in attrs:
                if attr[0] == 'id':
                    if attr[1] == gstrDivId: # name that div
                        gfImporting = True
                        print("found: " + gstrDivId)

    def handle_endtag(self, tag):
        global gfImporting
        global gInsertSought
        if tag == 'div': ## Div fails. case sensitive html!
            gfImporting = False
            gInsertSought = False
#            print("div closed for " + gstrDivId)

    def handle_data(self, data):
        global gfImporting
        if gfImporting==True:
            mainoutfile.write(S3BinaryHostReplace(data)) # show contents when we're importing
            print("imported some stuff")

fname = sys.argv[1]                # arg1 is source pathspec
fname = fname.replace("ref/", "")  # remove /ref source prefix, if found
print("for source file: " + fname)
fname = fname.replace(".md", "")   # remove .md suffix, so I can add S1, S2 to core fname before .md
mainoutfile = open("tmp/" + fname + ".md", "w")
slide = 1

parser = MyHTMLParser()
for line in sys.stdin:
    # if we want a slice, start with # see, and get a hyperlink of See Foobat, and new file desty Foobat
    if line.lower().startswith('# see '):
        slide = slide + 1
        mainoutfile.write('**[' + line[5:].strip() + '](' + fname + 'S' + str(slide) + '.html)**  \r\n\r\n')
        mainoutfile.close()
        mainoutfile = open("tmp/" + fname + "S" + str(slide) + ".md", "w")
        line = '<title>' + line[6:] + '</title>\r\n# ' + line[6:]
# The top title is # See Foobat minus the # See portion

    if line.lower().startswith('insert:'):
        gInsertSought = True
        print("an insert is sought")
        params = line[len('insert:'):].split()
#        filename ='src/' +  params[0]
        gstrDivFName = params[0]
        gstrDivId = params[1]                   # set this global
        insertfilename = 'src/' + params[0]
        if False == os.path.isfile(insertfilename):
            insertfilename = 'src/ref/' + params[0] # sometimes i forget to prepend the ref/
            print("want: " + insertfilename)
        if False == os.path.isfile(insertfilename):
            insertfilename = 'src/ref/_' + params[0] #refs have the underscore but i can omit it (should be sure there's no same name in root!)
        if False == os.path.isfile(insertfilename):
            print("insert: source file not found, so ctrl-c and fix: " + params[0])
            time.sleep(99999)
            sys.exit() # won't stop this but worthy effort
        print("found it, opening..." + insertfilename)
        f =  open(insertfilename, "r")
	parser.feed(f.read())
        parser.close()
    else:
        mainoutfile.write(S3BinaryHostReplace(line)),

if True == gInsertSought:
    print("insert id not found, so ctrl-c and fix. fname:" + gstrDivFName + ", with div id: " + gstrDivId)
    time.sleep(99999)

mainoutfile.close()

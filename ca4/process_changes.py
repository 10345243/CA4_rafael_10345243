import csv
# open the file - and read all of the lines.
###### ATENTION PYTHON IS READING A .TXT file ##########
changes_file = 'changes_python.txt'

data = [line.strip() for line in open(changes_file, 'r')]

sep = 72*'-'

# i will not use all those enities, but i will keep if i wanna change my search in the fucture

class Commit:
    'class for commits'
   
    def __init__(self, nlines = None, revision = None, author = None, time = None, day = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.day = day
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.nlines = nlines
    def get_commit_comment(self): # I want extrat day of week, date and time, author, and number lines of each commit
        return self.day + "." + self.date + " " +  self.time  + "." + self.author + "." +  self.nlines 
        
        # + ';'.join(self.changes)+ str(self.revision-1) + "  .  " + str(self.revision) + "  .  " \
               
            
         

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # getting only parts of commit i want.
        current_commit = Commit()
        details = data[index + 1].split('|')
        #current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip().split(' ')[0]
        current_commit.time = details[2].strip().split(' ') [1]
        current_commit.day = details[2].strip().split(' ')[3][1:4]
        current_commit.nlines = details[3].strip().split(' ')[0] #number of lines
        #current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        #current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        #current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break



commits.reverse()


#exporting my filtered data for another CSV file.



listaParaGerarCsv = [] #CSV list 
for index, commit in enumerate(commits):
    listaInterna = []
    listaInterna.append(commit.get_commit_comment())
    listaParaGerarCsv.append(listaInterna)

with open("arquivoOutput.csv", 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([])
    for linha in listaParaGerarCsv:
        spamwriter.writerow(linha)   
        
print "done"
print "arquivoOutput.csv was criated in your diretory"
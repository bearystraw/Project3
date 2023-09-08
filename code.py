with open('http_access_log') as f:
    [print(line) for line in f.readlines()]


theFile = open('http_access_log','r')
FILE = theFile.readlines()
theFile.close()
printList = []
for line in FILE:
    if ('TestName' in line) or ('Totals' in line):
         printList.append(line)

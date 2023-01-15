tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David',],
            ['dogs', 'cats', 'moose', 'goose',]]

def printtable(tabledata):
    colWidths = [0] * len(tableData)
    c=len(colWidths)
    max=0

    for i in range (len(tabledata)):
        for j in  range(len(tableData[0])):
            a=len(tableData[i][j])
            if a>max:
                max=a
        colWidths[i]=max
        max=0
    

    for i in range (len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]),end=" ")
        print()

printtable(tableData)
            




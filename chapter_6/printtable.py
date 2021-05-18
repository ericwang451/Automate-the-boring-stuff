def printTable(list):
    if len(list) == 0:
        print("Empty Table") 
    else:
        for innerList in list:
            print(' '.join(innerList).ljust(10))

def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)


main()
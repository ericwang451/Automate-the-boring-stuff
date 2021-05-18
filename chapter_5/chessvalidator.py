def isValidChessBoard(chessDict):
    for k,v in chessDict.items():
        if (isValidString(v) != True) or (isValidSquare(k) != True):
            return False
    return True
    
def isValidString(string):
    if (string[0] != "w") and (string[0] != "b"):
        return False
    else:
        pieces = ['king','queen', 'bishop', 'pawn', 'rook', 'knight']
        checkPieces = string[1:(len(string))]
        if (checkPieces in pieces):
            return True
        else: 
            return False

def isValidSquare(string):
    if (len(string) != 2):
        return False
    else:
        validLetters = ['a','b','c','d','e','f','g','h']

        if (int(string[0]) < 1 or int(string[0]) > 8):
            return False
        elif (string[1] not in validLetters):
            return False
        else: 
            return True

def main():
    sampleDict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    if (isValidChessBoard(sampleDict)):
        print("True")
    else:
        print("False")

main()
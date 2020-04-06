from generateTable import table

with open("files/textSample.txt", encoding="utf-8") as inputFile:
    with open("files/encrypted.txt", "w") as outputFile:
        while True:
            c = inputFile.read(1)
            if not c:
                break
            outputFile.write(str(table[c]) + " ")

file_is_open= False

try:
    csvFile= open('people.csv')
    print (csvFile.name)
    # print(csvFile.wookens())
except FileNotFoundError:
    print("The file doesn't exist")
except Exception as e:
    print(e)
else:
    file_is_open=True
    print("\nmehmehmeeeh\n")
    for one_line in csvFile:
        print(one_line)
    csvFile.close()
finally:
    if file_is_open:
        csvFile.close()
        file_is_open= False
        print(file_is_open)
        # file_is_open
    print("Tangazo kwa wote")
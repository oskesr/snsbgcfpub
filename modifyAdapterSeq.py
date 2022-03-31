# importing csv module
import csv

# csv file name, are currently hardcoded

filenameBam = "/Users/omkulkarni/Documents/snsb/AB1/RADseq_adapter_06_2021_bam.csv"
filenameKpl = "/Users/omkulkarni/Documents/snsb/AB1/RADseq_adapter_06_2021_kpl.csv"

# initializing the titles and rows list
fields = []
rows = []
rowsOdd = []
rowsEven = []

# reading csv file
with open(filenameBam, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

rowsOdd = rows[1::2]  # Elements from list1 starting from 1 iterating by 2
rowsEven = rows[::2]  # Elements from list1 starting from 0 iterating by 2

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
with open("topEnzBam.fasta", "w") as file1:
    # print('\nFirst 3 top enzymes are:\n')
    for row in rowsEven:
        # print('>' + row[0])
        # print(row[3])
        # Writing data to a file
        file1.write('>' + row[0] + '\n')
        file1.write(row[3] + '\n')
    # parsing each column of a row
    # for col in row:
    #     print("%10s" % col, end=" "),
    # print('\n')

with open("botEnzBam.fasta", "w") as file2:
    # print('\nFirst 3 bottom enzymes are:\n')
    for row in rowsOdd:
        # print('>' + row[0])
        # print(row[3])

        # Writing data to a file
        file2.write('>' + row[0] + '\n')
        file2.write(row[3] + '\n')

    # parsing each column of a row
    # for col in row:
    #     #print("%10s" % col, end=" "),
    #     print(col),
    # print('\n')

# Reading from file
with open("topEnzBam.fasta", "r+") as file1:
    # Reading form a file
    print('\ncontents of ' + file1.name)
    # print(file1.read())

with open("botEnzBam.fasta", "r+") as file1:
    # Reading form a file
    print('\ncontents of ' + file2.name)
    # print(file1.read())

# initializing the titles and rows list
fields = []
rows = []
rowsOdd = []
rowsEven = []

# reading csv file
with open(filenameKpl, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

rowsOdd = rows[1::2]  # Elements from list1 starting from 1 iterating by 2
rowsEven = rows[::2]  # Elements from list1 starting from 0 iterating by 2

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
with open("topEnzKpl.fasta", "w") as file1:
    # print('\nFirst 3 top enzymes are:\n')
    for row in rowsEven:
        # print('>' + row[0])
        # print(row[3])
        # Writing data to a file
        file1.write('>' + row[0] + '\n')
        file1.write(row[3] + '\n')
    # parsing each column of a row
    # for col in row:
    #     print("%10s" % col, end=" "),
    # print('\n')

with open("botEnzKpl.fasta", "w") as file2:
    # print('\nFirst 3 bottom enzymes are:\n')
    for row in rowsOdd:
        # print('>' + row[0])
        # print(row[3])

        # Writing data to a file
        file2.write('>' + row[0] + '\n')
        file2.write(row[3] + '\n')

    # parsing each column of a row
    # for col in row:
    #     #print("%10s" % col, end=" "),
    #     print(col),
    # print('\n')

# Reading from file
with open("topEnzKpl.fasta", "r+") as file1:
    # Reading form a file
    print('\ncontents of ' + file1.name)
    print(file1.read())

with open("botEnzKpl.fasta", "r+") as file1:
    # Reading form a file
    print('\ncontents of ' + file2.name)
    print(file1.read())

print('done with both enzymes')


# Python code to reverse a string
# using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "Geeksfor.geeks"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

filenamesFasta = ['botEnzBam.fasta', 'botEnzKpl.fasta', 'topEnzBam.fasta', 'topEnzKpl.fasta']


# print(filenamesFasta[0].split('.')[0])

def createReverseFasta(filename):
    rows = []
    rowsOdd = []
    rowsEven = []
    with open(filename, "r+") as file1:
        # Reading form a file
        print('\nProcessing ' + file1.name)
        lines = file1.readlines()
        with open(filename.split('.')[0] + 'Reverse.fasta', "w") as fileNew:
            count = 0
            # Strips the newline character
            for line in lines:
                count += 1
                print("Line{}: {}".format(count, line.strip()))
                if (count % 2) == 0:
                    print("Even")
                    fileNew.write(reverse(line.strip()) + '\n')
                else:
                    print("Odd")
                    fileNew.write(line.strip() + '_rev\n')
        # with open(filename.split('.')[0] + 'Reverse.fasta', "w") as fileNew:
        #     for  in rowsEven:
        #         # print('>' + row[0])
        #         # print(row[3])
        #         # Writing data to a file
        #         fileNew.write('>' + row[0] + '\n')
        #         fileNew.write(row[3] + '\n')
        # #print('Procesing ', filename.split('.')[0])
        #print(file1.read())

list(map(createReverseFasta, filenamesFasta))

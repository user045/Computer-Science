import urllib.request as web

url = "https://www.fda.gov/media/191968/download?attachment"

webpage = web.urlopen(url)

# Files have different modes: n
# 'r' - read only (the file has to exist for this to work)
# 'w' - write (if file doesn't exist, it will be created; if it does exist 
# new data will be appended to the end of the file)

# fd = open("recall_data.xml", 'w') Open a file for writing

# fd.close() #YoU have to close a file to make sure everything in the buffer got saved

# print(webpage.readline().decode('utf-8))

# for _ in range(20):     # we don't need the counter so we ignore
#    print(webpage.readline().decode('utf-8'))

line = ""

while line[:14] != "<RECALLS_DATA":
    pass

product_num = 1

line = webpage.readline().decode('utf-8')

while line[:14] != "</recallsdata>": # While there are recalls to process
    print(product_num)

    while line[:10] != "<recalls>":
        print(line.rstrip())
        line = webpage.readline().decode('utf-8')
    print(line.rstrip())

    product_num += 1

    line = webpage.readline().decode('utf-8')

webpage.close()

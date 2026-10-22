import os.path
import re
import urllib

import webquery

url = "https://www.fda.gov/media/191968/download?attachment"

if (not os.path.isfile("recall_data.xml")):  # Check if the file exists
    webpage = webquery.urlopen(url)  # Open the webpage
    xml_data = webpage.read() # It will read this as a byte string

    fd = open("recall_data.xml", 'wb') # Open a file for writing in binary mode
    fd.write(xml_data) # Write the byte string to the file
    fd.close() # Close the file to make sure everything in the buffer got saved

xml_file = open("recall_data.xml", 'r') # Open the file for reading

line = ""

while(line != "<recallsdata>")
    line = xml_file.readline().strip()

productNum = 1

while(line  != "<recallsdata>"): #
    print(f"Product {productNum}"", end=": \n")

while(line  != "<recallsdata>"):
    line = xml_file.readline().strip()

    matches = re.search(r'<(\w+)>(.*?)</\1>', line)

    if(matches != None and matches.group(1) in ["Brand, "Company", "Date"]):
        print(f"\t ")

    productNum += 1

    line = xml_file.readline().strip()
    print(line)

xml_file.close()

# Exercise for you
# Change this program to save the processed data to an output file

# called recalls.txt instead of printing it out to the console
# out = open("recalls.txt, "w")
# out.write(line)

'''
while(line  != "<recallsdata>"):
    print(f"Product {productNum}"", end=": \n")

while(line  != "<recallsdata>"):
    line = xml_file.readline().strip()

    matches = re.search(r'<(\w+)>(.*?)</\1>', line)

    if(matches != None and matches.group(1) in ["Brand, "Company", "Date"]):
        print(f"\t ")

    productNum += 1

    line = xml_file.readline().strip()
    out = open("recalls.txt", "w")
    out.write(out)
'''


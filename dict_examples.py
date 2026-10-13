# Dictionaries
'''
Dictionaries are implemented as hash maps or hash tables with hash functions.
A dictionary is a pairing between teh set of keys and the set values. Every entry in the dictionary
is a key : value pair.

Immutable and Mutable data. Mutable data can be changed and ofetn is in memory. 
Example of a mutable data structure is a list.
Immutable data structures cannot be changed.
Example of an immutable data structure is a string.

The keys in a dictionary need to be an immutable type.
This is so that the hash function obtains the same value every time the key is looked up.

The values can be mutable or immutable.

Adding and retrieving things out of a dictionary can be done quickly.
This is what makes them a well-used data structure.
'''

# Empty dictionary
my_dict = {}

phone_list = {"Caroline" : "555-3691", "Mori" : "4444-2211", "Koeki": "0555-5834"}

print(phone_list)
print(phone_list.keys()) # The method to get the dictionary keys is keys()
print(phone_list.values()) # The method to get the dictionary values is values()

# Lookup the value for a particular key phone_list[key]
print(phone_list["Mori"])

# Add to a dictionary
phone_list["Saanvi"] = "222-3145"
print(phone_list)

# Change a value in a dictionary
phone_list["Koeki"]="555-1133"
print(phone_list)


# Frequency counts
new_phrase = "the quick brown fox jumped over the quick brown dog who jumped over the brown log"
word_count = {}
words = new_phrase.split()

def freq_count(phrase):
    word_count = {}
    words = phrase.split()

    for word in words:
        if word in word_count:      # Is word already a key in word_count?
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(freq_count(new_phrase))

# Write a function

def classList(students, year):
    '''
    Purpose: To take a dictionary students with student : grad year pairs and produce a list with students who graduated in the parameter year. 

    Parameters:
        students = a dictionary with names as keys and class years as values; dict
        year - the year that students are graduating

    Return Value: List of students who are graduating in year; list

    student_List = {"Caroline": 2027, "Xavier": 2030, "Melissa": 2029, "Kathy": 2027}
    
            classList(studentList, 2030)
                ["Xavier"]
            classList(student_List, 2027)
                ["Caroline", "Kathy"]
            classList(student_List, 2029)
                ["Melissa"]
    '''
    student_List = {"Caroline": 2027, "Xavier": 2030, "Melissa": 2029, "Kathy": 2027}
    names = []

    for name in student_List:
        if student_List[name] == year:
            names.append(name)
    return names

print(classList(student_List, 2022))

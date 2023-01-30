"""
Modify this docstring.

"""

tupleA = (12, 22, 32, 42, 52)
tupleB = (43, 53, 63, 73, 83)
tupleCat = tupleA + tupleB
tupleAThrice = tupleA * 3
print(f"{tupleA = }")
print(f"{tupleB = }")
print(f"{tupleCat = }")
print(f"{tupleAThrice = }")
tupleD = (13, 22, 34)
hasOne = 1 in tupleD  
hasFour = 4 in tupleD  
my_tuple = (13, 22, 36)
first = my_tuple[0]
second = my_tuple[1]
third = my_tuple[2]
last = my_tuple[-1]

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(14, 5)
print(f"Quotient: {q}, Remainder: {r}")


setA = {13, 23, 33, 43, 53}
setB = {43, 53, 63, 73, 83}

setC = setA | setB

setD = setA & setB

setE = setA - setB

listWords = ["arms", "Legs", "arms", "Back", "chest", "shoulders"]
setWords = set(listWords)
listWordsNoDuplicates = list(setWords)
listWordsNoDuplicates = [setWords]  

Ashbeforelifitng_dict = {"name": "Ashlee", "age": 24, "weight_kg": 150}
Ashafterlifting_dict = {"name": "Ashlee", "age": 26, "weight_kg": 165}
print(f'Ashlee before lifting data:', Ashbeforelifitng_dict)
print(f'Ashlee After lifting data:', Ashafterlifting_dict)

assessment_dict = {"low": 0, "medium": 1, "high": 2}

data_dict = {
    "name": ["Andy", "Rafael", "Amela", "Tiff"],
    "age": [24, 33, 28, 43],
    "Weight": [167, 235, 354, 154],
}

print(f'data from gym members:', data_dict)


with open("text_names_in.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

print(word_counts_dict)


word_counts_dict = {word: word_list.count(word) for word in word_list}


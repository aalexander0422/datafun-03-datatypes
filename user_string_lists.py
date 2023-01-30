"""
Modify this docstring.

"""

# imports first
import random
# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":
List_Arms = ["curls", "flys", "raises"]
list_legs = ["squats", "deadlift", "lunges"]
list_back = ["pullups", "rows", "latextensions"]
list_cardio = ["biking", "running", "swimming"]
list_abs = ["crunches", "situps", "twists"]
print(f'Here are the list of workouts \n', list_abs, list_legs, list_back, list_cardio, List_Arms)
for List_Arms, list_legs in zip(List_Arms, list_legs):
    print(f'Arms ={List_Arms}: Legs={list_legs}')
for list_back, list_cardio in zip(list_back, list_cardio):
    print(f'back ={list_back}: Cardio={list_cardio}')
exercise_count = len(list_abs)
print(f'exercise count per muscle:', exercise_count)

sentence = (
    f"Your exercises for the day will be {random.choice(List_Arms)} {random.choice(list_legs)} "
    f"{random.choice(list_back)} {random.choice(list_cardio)}."
)
print(sentence)

with open("text_hamlet.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  
    unique_words = set(list_words)  

word_ct = len(list_words)
print(word_ct)
unique_word_ct = len(unique_words)
print(unique_word_ct)


#1. People and Facts (Dictionary)

# people = {
#     "Muskan": {"age": 20, "city": "Indore"},
#     "Ravi": {"age": 22, "city": "Bhopal"},
#     "Anjali": {"age": 19, "city": "Ujjain"}
# }
# for name, info in people.items():
#     print(f"{name} is {info['age']} years old and lives in {info['city']}.")




# 2. Find the Runner-Up Score (List)

# scores = [90, 85, 95, 100, 100, 70, 85]
# unique_scores = list(set(scores))  # Remove duplicates
# unique_scores.sort()
# if len(unique_scores) >= 2:
#     print("Runner-Up Score is:", unique_scores[-2])
# else:
#     print("Not enough unique scores to find a runner-up.")




# 3. Find the Percentage (Dict + List)
# students = {
#     "Muskan": [90, 85, 80],
#     "Ravi": [75, 70, 78],
#     "Anjali": [88, 90, 84]
# }
# search_name = input("Enter student name to find percentage: ")

# if search_name in students:
#     marks = students[search_name]
#     avg = sum(marks) / len(marks)
#     print(f"{search_name}'s average percentage is: {avg:.2f}%")
# else:
#     print("Student not found in record.")



# 4. Find the Name (String)
# sentence = "Hello, my name is Muskan and I love Python programming."
# search_word = input("Enter a name or word to search in the sentence: ")

# if search_word in sentence:
#     print(f"Yes, '{search_word}' is found in the sentence.")
# else:
#     print(f"No, '{search_word}' is not found in the sentence.")



#Step 1: Create a sample file with text
with open("secret_file.txt", "w") as file:
    file.write("Welcome to the mini project.\n")
    file.write("This file contains a lot of words.\n")
    file.write("Somewhere inside is a SECRET.\n")
    file.write("Can you find the SECRET word?\n")

#Step 2: Read the file and search for the word "SECRET"
secret_found = False

with open("secret_file.txt", "r") as file:
    print("Reading file...\n")
    for line_number, line in enumerate(file, start=1):
        if "SECRET" in line:
            print(f"secret found in line {line_number}: {line.strip()}")
            secret_found = True
            break

if not secret_found:
    print("secret not found in the file.")

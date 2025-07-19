import sys

# Check if proper arguments are given
if len(sys.argv) != 3:
    print("Usage: python happiness_project.py <Your_Name> <Your_Mood>")
    sys.exit(1)

# Read arguments
name = sys.argv[1]
mood = sys.argv[2].lower()

# Simple response based on mood
print(f"\nHello, {name}!")

if mood == "happy":
    print("It's great to know you're feeling happy! Keep smiling!")
elif mood == "sad":
    print(" Don't worry, {name}. Better days are coming!")
elif mood == "angry":
    print("Take a deep breath, {name}. Relax and stay calm.")
elif mood == "excited":
    print("🎉 Wow, that's awesome! Enjoy your excitement, {name}!")
else:
    print(f"Thanks for sharing your mood: {mood}. Have a great day, {name}!")


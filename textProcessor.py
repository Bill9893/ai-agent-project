text = input("Enter your text:")
print("choose action: 1. Count Words 2. Uppercase 3. Reverse Text")
action = input()
if action == "Count Words":
   print(len(text.split()))
elif action == "Uppercase":
   print(text.upper())
elif action == "Reverse Text":
   print(text[::-1])
else:   print("Invalid action")
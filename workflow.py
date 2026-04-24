from fake_llm import fake_llm

user_input = input("Enter your task: ")

response = fake_llm(user_input)

print("Response:", response)
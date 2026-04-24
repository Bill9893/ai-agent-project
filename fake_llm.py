def fake_llm(prompt):
    if "summarize" in prompt.lower():
        return "This is a short summary."
    elif "plan" in prompt.lower():
        return "Step 1 → Step 2 → Step 3"
    else:
        return "I don't understand the task"
# commands.py

def cmd_exit():
    print("Exiting chat. Goodbye!")
    return 'break'

def cmd_clear(messagesSent):
    messagesSent = []
    print("Chat history cleared.")

def cmd_models(indexed_models, models, selectedModel):
    for line in indexed_models:
        print(line)
    try:
        selected_index = int(input("Select a model by entering its index (e.g., 0 for the first model):"))
        if 0 <= selected_index < len(models.data):
            selectedModel[0] = models.data[selected_index].id
            print(f"You selected: {selectedModel[0]}")
            print("You are now chatting with", selectedModel[0], "!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def cmd_help():
    print("Available commands:")
    print("!exit - Exit the chat")
    print("!clear - Clear the chat history")
    print("!models - Show available models")
    print("!help - Show this help message")

def get_commands():
    return {
        "!exit": cmd_exit,
        "!clear": cmd_clear,
        "!models": cmd_models,
        "!help": cmd_help
    }

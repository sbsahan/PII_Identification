# commands.py
import style_utils as su
def cmd_exit():
    print(su.dim("Exiting chat. Goodbye!"))
    return 'break'

def cmd_clear(messagesSent):
    messagesSent = []
    print(su.dim("Chat history cleared."))

def cmd_models(model_ids, selectedModel, messagesSent=None):
    # Sort the model_ids alphabetically
    sorted_models = sorted(model_ids, key=lambda x: x.lower())
    for i, model_id in enumerate(sorted_models):
        print(f"[{su.cyan(str(i))}] {su.dim(model_id)}")
    try:
        selected_index = int(input(su.yellow("Select a model by entering its index (e.g., 0 for the first model):")))
        if 0 <= selected_index < len(sorted_models):
            selectedModel[0] = sorted_models[selected_index]
            print(su.dim("Model changed to:"), 
                  su.cyan(selectedModel[0]))
            print(su.dim("Now you are chatting with"), 
                  su.cyan(selectedModel[0]), 
                  su.dim("!"))
            # Clear chat history if messagesSent is provided
            if messagesSent is not None:
                messagesSent.clear()
                print(su.dim("Chat history cleared due to model change."))
        else:
            print(su.dim("Invalid index."))
    except ValueError:
        print(su.dim("Please enter a valid number."))
    

def cmd_help():
    print(su.dim("Available commands:\n"),
          su.cyan("!exit"), 
          su.dim("- Exit the chat\n"),
          su.cyan("!clear"),
          su.dim("- Clear the chat history\n"),
          su.cyan("!models"),
          su.dim("- Show available models\n"),
          su.cyan("!help"),
          su.dim("- Show this help message")
    )

def get_commands():
    return {
        "!exit": cmd_exit,
        "!clear": cmd_clear,
        "!models": cmd_models,
        "!help": cmd_help
    }

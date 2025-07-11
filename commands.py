# commands.py
import utils
def cmd_exit():
    utils.outputText.exiting()
    return 'break'

def cmd_clear(messagesSent):
    utils.outputText.chatHistoryCleared()
    messagesSent = []

def cmd_models(model_ids, selectedModel, messagesSent=None):
    # Sort the model_ids alphabetically
    sorted_models = sorted(model_ids, key=lambda x: x.lower())
    for i, model_id in enumerate(sorted_models):
        print(f"[{utils.cyan(str(i))}] {utils.dim(model_id)}")
    try:
        selected_index = int(input(utils.outputText.modelSelection() + " "))
        if 0 <= selected_index < len(sorted_models):
            selectedModel[0] = sorted_models[selected_index]
            utils.outputText.modelChanged(selectedModel[0])
            # Clear chat history if messagesSent is provided
            if messagesSent is not None:
                utils.outputText.modelClear()
                messagesSent = []
        else:
            print(utils.dim("Invalid index."))
    except ValueError:
        print(utils.dim("Please enter a valid number."))
    

def cmd_help():
    utils.outputText.helpCommand()

def get_commands():
    return {
        "!exit": cmd_exit,
        "!clear": cmd_clear,
        "!models": cmd_models,
        "!help": cmd_help
    }

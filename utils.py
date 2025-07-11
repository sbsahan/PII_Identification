# style_py

from colorama import Fore, Style, init

init(autoreset=True)

def dim(text):
    return Style.DIM + str(text) + Style.RESET_ALL

def bright(text):
    return Style.BRIGHT + str(text) + Style.RESET_ALL

def yellow(text):
    return Fore.YELLOW + str(text) + Style.RESET_ALL

def green(text):
    return Fore.GREEN + str(text) + Style.RESET_ALL

def cyan(text):
    return Fore.CYAN + str(text) + Style.RESET_ALL

def red(text):
    return Fore.RED + str(text) + Style.RESET_ALL

def magenta(text):
    return Fore.MAGENTA + str(text) + Style.RESET_ALL

def user_label():
    return green("user:")

def assistant_label():
    return cyan("assistant:")

class outputText:
    def chattingWith(model):
        print(dim("You are now chatting with"), 
        cyan(model), 
        dim("!"))

    def messageAnonymized(text):
        print(dim("PII identified, your message has been anonymized to:"), 
              yellow(text)
        )
        print(dim("Wrongly identified PII? Type"), 
              green('\"y\"'), 
              dim("to send the original message,"), 
              magenta('\"n\"'), 
              dim("to send the anonymized message or"), 
              red('\"c\"'), 
              dim("to cancel sending the message.")
        )

    def exiting():
        print(dim("Exiting chat. Goodbye!"))

    def chatHistoryCleared():
        print(dim("Chat history cleared."))

    def unknownCommand():
        print(dim("Unknown command. Type"), 
              cyan("!help"), 
              dim("for a list of commands.")
        )
    
    def messageCancelled():
        print(dim("Message sending cancelled."))
    
    def invalidInput():
        print(dim("Invalid input. Type"), 
              green('\"y\"'), 
              dim("to send the original message,"), 
              magenta('\"n\"'), 
              dim("to send the anonymized message or"), 
              red('\"c\"'), 
              dim("to cancel sending the message.")
        )
    
    def modelSelection():
        return yellow("Select a model by entering its index (e.g., 0 for the first model):")
    
    def modelChanged(model):
        print(dim("Model changed to:"), 
              cyan(model))
        print(dim("Now you are chatting with"), 
              cyan(model), 
              dim("!"))
    
    def modelClear():
        print(dim("Chat history cleared due to model change."))

    def helpCommand():
        print(dim("Available commands:\n"),
              cyan("!exit"), 
              dim("- Exit the chat\n"),
              cyan("!clear"),
              dim("- Clear the chat history\n"),
              cyan("!models"),
              dim("- Show available models\n"),
              cyan("!help"),
              dim("- Show this help message")
        )
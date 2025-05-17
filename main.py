
from textblob import TextBlob
from colorama import init, Fore, Style
print(f"{Fore.CYAN}🎉 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")
print("Type a sentence and ill analyze its sentiment!")
print(f"Commands: {Fore.RED} 'reset'{Style.RESET_ALL}, {Fore.RED} 'history'{Style.RESET_ALL}, {Fore.RED}'exit'{Style.RESET_ALL}.\n")

name=input("Please enter your name: ").strip()
if not name:
    name="Mystery Agent"
print(f"\nHello, Agent {Fore.GREEN}{name}{Style.RESET_ALL}! lets begin.")
history=[]
while True:
    user_input=input(f"{Fore.YELLOW}>>{Style.RESET_ALL}").strip()
    if user_input.lower()=="exit":
        print(f"{Fore.MAGENTA} 🚶‍♂️ Exiting Sentiment Spy. Farwell, Agent {name}! 🏁")
        break
    elif user_input.lower() == "history":
        if not history:
            print(f"{Fore.RED}📜 No conversation history found")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:")
            for idx, (text, polarity, sentiment_type) in enumerate(history, 1):
                color = Fore.GREEN if sentiment_type == "Positive" else Fore.RED if sentiment_type == "Negative" else Fore.YELLOW
                print(f"{idx}. {color}{text} (Polarity: {polarity:.2f}, {sentiment_type})")
    else:
        polarity = TextBlob(user_input).sentiment.polarity
        if polarity > 0.25:
            sentiment_type, color, emoji = "Positive", Fore.GREEN, "😊"
        elif polarity < -0.25:
            sentiment_type, color, emoji = "Negative", Fore.RED, "😢"
        else:
            sentiment_type, color, emoji = "Neutral", Fore.YELLOW, "😐"
        result = f"{emoji} {color}{sentiment_type} sentiment detected! (Polarity: {polarity:.2f})"
        print(result)
        history.append((user_input, polarity, sentiment_type))
        

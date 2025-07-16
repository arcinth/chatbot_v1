from engine.chat_engine import *
import pyfiglet


ASCII_art_1 = pyfiglet.figlet_format("Welcome to Chatbot_v1")
print(ASCII_art_1)

print("CHAT BOT STARTED!")
print("# to end chat type exit")
while True:
    get=input("you:")
    if get.lower()=="exit" or get.lower()=="bye":
        print("Chatbot: Goodbye!")
        break
    result=get_chat(get)
    print(f"chatbot:{result}")



    
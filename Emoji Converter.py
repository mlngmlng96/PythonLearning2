"""new= message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "🥲"
}
updated_message = ""
for word in new:
    for emoji in emojis:
        if word == emoji:
            word = emojis[emoji]
    updated_message += word + " "
print(updated_message)"""

"Solution and make them into subflows"
def emoji_converter(message):
    new= message.split(' ')
    #this is a dictionary
    emojis = {
     ":)": "😊",
     ":(": "🥲"
    }
    updated_message = ""
    for word in new:
        x = emojis.get(word,word)
        updated_message += x + " "
    return updated_message

message = input(">")
updated_message = emoji_converter(message)
print(updated_message)
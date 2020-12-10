def chats(comm: str, comms: list, sub: object) -> list:
    chatT = sub.get_public_chat_threads().title
    chatI = sub.get_public_chat_threads().chatId
    return chatT, chatI

def public_chats(chatT):
    s = ""
    c = 0
    for x in chatT:
        s += "[{}]{}\n".format(c, x)
        c += 1
    return s


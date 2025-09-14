import lab_chat

#part_1
def get_username():
    username = input("Enter your username: ").strip()
    return username.upper()

def get_group():
    group = input("Enter your group name: ").strip()
    return group.upper()

def get_message():
    message = input("Enter your message: ").strip()
    return message

#part_3

def initialize_chat():
    user = get_username()
    group = get_group()

    node = lab_chat.get_peer_node(user)
    lab_chat.join_group(node, group)

    print(f"{user} joined group: {group}")
    channel = lab_chat.get_channel(node, group)
    return channel


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")
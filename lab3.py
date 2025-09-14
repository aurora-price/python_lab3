#part_1
def get_username():
    username = input("Enter your username: ").strip()
    return username.upper()
user=get_username()
print(f"Welcome {user}!")

def get_group():
    group = input("Enter your group name: ").strip()
    return group.upper()
group=get_group()
print(f"Welcome to {group}!")

def get_message():
    message = input("Enter your message: ").strip()
    return message.upper()
message=get_message()
print(f"{message}!")

#part_3
import lab_chat

def initialize_chat():
    user = get_username()
    group = get_group()

    node = lab_chat.get_peer_node(user)
    node.join(group)

    print(f"{user} joined group: {group}")
    return node, group


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
        channel.send("$$STOP".encode('utf_8'))
        print("Finished!")
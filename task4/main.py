def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

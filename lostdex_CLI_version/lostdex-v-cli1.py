import textwrap
from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y %H:%M")

lost_list = []
found_list = []
home = {'lost': lost_list, 'found': found_list}

#style
def b(text):
    """Wraps text in ANSI codes to make it bold in the terminal."""
    BOLD_START = '\033[1m'
    BOLD_END = '\033[0m'
    return f"{BOLD_START}{text}{BOLD_END}"

class Post:
    def __init__(self, type, item_name, description, location, time, contact, post_time):
        self.type = type
        self.item_name = item_name
        self.description = description
        self.location = location
        self.post_time = post_time 
        self.time = time
        self.contact = contact 
    def __repr__(self):
        return (f"{b(self.item_name)} \n{self.description} \nItem location  {self.location}\n Time {self.time}\n Your contact details {self.contact}\n Posted time: {self.post_time}")

def view_home():
    selection = ["lost list", "found list", "all"]
    print(f"Which list do you want to view?")
    for option in selection:
        print(f"- {option}")
    select_input = input("Enter the list name: ").strip().lower()

    if select_input == "lost list":
        print(b("Lost Items:"))
        if lost_list:
            for post in lost_list:
                print(post)
        else:
            print("No lost items found.")
    elif select_input == "found list":
        print(b("Found Items:"))
        if found_list:
            for post in found_list:
                print(post)
        else:
            print("No found items posted.")
    elif select_input == "all":
        print(b("All Posts:"))
        any_posted = False
        if lost_list:
            print(b("Lost Items:"))
            for post in lost_list:
                print(post)
            any_posted = True
        if found_list:
            print(b("Found Items:"))
            for post in found_list:
                print(post)
            any_posted = True
        if not any_posted:
            print("No items posted yet.")
    else:
        print("Invalid selection. Try 'lost list', 'found list', or 'all'.")
        
def publish():
    item_type = input("Is this item lost or found? ").strip().lower()
    item_name = input("Enter item name: ")
    user_description = input("Enter description: ")
    description = textwrap.fill(user_description, width=80)
    location = input("Enter location: ")
    time = input("Enter an estimated time(dd-mm-yyyy, time include am or pm): ")
    contact = input("Enter your contact details: ")
    post_time = formatted_time
    new_post = Post(item_type, item_name, description, location,time, contact, post_time)
    if item_type == "found":
        found_list.append(new_post)
        print("your list has been posted successfully. Select view list to view")
    elif item_type == "lost":
        lost_list.append(new_post)
        print("your list has been posted successfully. Select view list from home menus to view")

choice = ["view list", "post item", "exit"]

def main():
    running = True
    while running:
        print(f"{b('Welcome to Lostdex')}")
        print("To interact with the options just type the option name")
        for option in choice:
            print(f"- {option}")
        promt1 = input("Please select an option: ").strip().lower()
        if promt1 == choice[0]:               
            view_home()
        elif promt1 == choice[1]:             
            publish()
        elif promt1 == choice[2]:            
            print("Exiting Lostdex. Goodbye!")
            running = False                   
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
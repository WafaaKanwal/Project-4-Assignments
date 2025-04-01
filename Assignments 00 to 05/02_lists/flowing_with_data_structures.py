# Message Copying Program
# This program prompts the user to enter a message and then adds three copies of the message to a list.

def add_three_copies(my_list, data):
    for _ in range(3):  # 3 copies add karega
        my_list.append(data)

def main():
    message = input("Enter a message to copy: ")  # User input 
    my_list = []  # Empty list
    print("List before:", my_list)  # empty list print 
    
    add_three_copies(my_list, message)  # Function calling
    
    print("List after:", my_list)  # Modified list print 

if __name__ == "__main__":
    main()

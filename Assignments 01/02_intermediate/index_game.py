# Problem #2: Index Game

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element modified successfully"
    return "Index out of range"

def slice_list(lst, start, end):
    return lst[start:end]

def main():
    my_list = [10, 20, 30, 40, 50]
    
    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            index = int(input("Enter index: "))
            print("Element at index", index, ":", access_element(my_list, index))
        elif choice == "2":
            index = int(input("Enter index: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

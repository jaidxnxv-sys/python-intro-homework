numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# functions
def find_min(lst):
    if not lst:
        return None
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def find_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def search(numbers, target):
    try:
        for i in range(len(numbers)):
            if numbers[i] == target:
                return i
        return -1
    except ValueError:
        print("Please enter a valid integer.")
        return -1

# User input/ display
def display_menu():
    print("\n==== Number Cruncher ====")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search Number")
    print("4. Sort List")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    print("Sorted List:", numbers)
# Choice function
def main():
    while True:
        choice = display_menu()
        # 1 min
        if choice == "1":
            option = find_min(numbers)
            print(f"The minimum number is: {option}")
        # 2 max
        elif choice == "2":
            option = find_max(numbers)
            print(f"The maximum number is: {option}")
        # 3 search lin
        elif choice == "3":
            target = int(input("Enter a number to search: "))
            option = search(numbers, target)
            if option != -1:
                print(f"Number found at index: {option}")
            else:
                print("Number not found in the list.")
        # 4 bubble sort
        elif choice == "4":
            bubble_sort(numbers)
        # 5 exit
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
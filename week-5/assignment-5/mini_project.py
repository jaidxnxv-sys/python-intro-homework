numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


while True:
    print("\n=== Number Cruncher ===")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    # minimum
    if choice == "1":
        smallest = numbers[0]

        for num in numbers:
            if num < smallest:
                smallest = num
        print("minimum:", smallest)

    # maximum
    elif choice == "2":
        largest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num
        print("maximum:", largest)

    # search
   
    elif choice == "3":
        search_num = int(input("Search Number: "))
        found = False

        for i in range(len(numbers)):
            if numbers[i] == search_num:
                found = True
                print(f"{search_num} found at index {i}")
                break

        if not found:
            print(f"{search_num} not found in the list")

    # bubble sort
    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print("Sorted List:", numbers)

    # quit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 5.")




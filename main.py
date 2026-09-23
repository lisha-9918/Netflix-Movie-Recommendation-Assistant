def main():
    # 1. START PROGRAM
    
    # 2. Print banner
    print("=" * 45)
    print("   Netflix Movie Recommendation Assistant   ")
    print("=" * 45)

    # 3. DISPLAY MAIN MENU
    print("\nMAIN MENU")
    print("1. Home")
    print("2. Films")
    print("3. My List")
    print("4. Exit")

    # 4. PROMPT INPUT: Store choice in userChoice
    user_choice = input("\nEnter your choice (1-4): ").strip()

    # 5. EVALUATE INPUT
    if user_choice == '1':
        # IF userChoice == 1 (Home)
        print("\n--- Trending Now ---")
        print("Title: Chu Yu | 99% Match | Top 10 in TV Shows Today")

    elif user_choice == '2':
        # IF userChoice == 2 (Films)
        print("\n--- Films Menu ---")
        print("1. By Genre")
        print("2. By Year")
        
        films_choice = input("\nEnter your choice (1-2): ").strip()

        if films_choice == '1':
            # IF filmsChoice == 1 (Genre)
            print("\n--- Genre Menu ---")
            print("1. Action")
            print("2. Comedy")
            print("3. Thriller")
            print("4. Horro")
            print("5. Romance")
        elif films_choice == '2':
            print("\nFiltering by year...")
        else:
            print("\nInvalid selection in Films menu.")

    elif user_choice == '3':
        # IF userChoice == 3 (My List)
        print("\n--- My List ---")
        print("Your saved movies/shows will appear here.")

    elif user_choice == '4':
        # IF userChoice == 4 (Exit)
        print("\nExiting program. Thank you!")

    else:
        print("\nInvalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
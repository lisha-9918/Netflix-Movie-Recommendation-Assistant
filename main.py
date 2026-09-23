def main():
    # 1. START PROGRAM
    
    # Data structure to hold movies by genre
    movies_by_genre = {
        '1': ("Action", ["Extraction", "Red Notice", "The Gray Man", "John Wick"]),
        '2': ("Comedy", ["Glass Onion", "Murder Mystery", "Red Notice", "The Hangover"]),
        '3': ("Thriller", ["Bird Box", "The Platform", "Leave the World Behind", "Gone Girl"]),
        '4': ("Horror", ["A Classic Horror Story", "The Conjuring", "Polong", "Veronica"]),
        '5': ("Romance", ["To All the Boys I've Loved Before", "The Kissing Booth", "Set It Up", "Plastic Beauty"])
    }
    
    # Store user's saved titles
    my_list = []

    # 2. Print banner once at start
    print("=" * 45)
    print("   Netflix Movie Recommendation Assistant   ")
    print("=" * 45)

    # Use a loop so the menu keeps showing until the user exits
    while True:
        # 3. DISPLAY MAIN MENU
        print("\n" + "="*30)
        print("MAIN MENU")
        print("1. Home")
        print("2. Films")
        print("3. My List")
        print("4. Exit")

        # 4. PROMPT INPUT: Store choice in user_choice
        user_choice = input("\nEnter your choice (1-4): ").strip()

        # 5. EVALUATE INPUT
        if user_choice == '1':
            # IF userChoice == 1 (Home)
            print("\n--- Trending Now ---")
            print("1. Stranger Things Tales From 85 | New On Netflix")
            print("2. POLONG | Top 10 on Netflix | New On Netflix")
            print("3. Plastic Beauty | Top 10 On Netflix | New On Netflix")

        elif user_choice == '2':
            # IF userChoice == 2 (Films)
            print("\n--- Films Menu ---")
            print("1. By Genre")
            
            films_choice = input("\nEnter your choice (1): ").strip()

            if films_choice == '1':
                # IF filmsChoice == 1 (Genre)
                print("\n--- Genre Menu ---")
                print("1. Action")
                print("2. Comedy")
                print("3. Thriller")
                print("4. Horror")
                print("5. Romance")
                
                genre_choice = input("\nSelect a genre (1-5): ").strip()
                
                if genre_choice in movies_by_genre:
                    genre_name, movies = movies_by_genre[genre_choice]
                    print(f"\n--- {genre_name} Movies ---")
                    for idx, movie in enumerate(movies, start=1):
                        print(f"{idx}. {movie}")
                    
                    # Option to add to My List
                    add_choice = input("\nDo you want to add a movie to My List? (Enter number or 'N' to skip): ").strip()
                    if add_choice.isdigit():
                        idx = int(add_choice) - 1
                        if 0 <= idx < len(movies):
                            selected_movie = movies[idx]
                            if selected_movie not in my_list:
                                my_list.append(selected_movie)
                                print(f"\n✓ '{selected_movie}' added to My List!")
                            else:
                                print(f"\n! '{selected_movie}' is already in My List.")
                        else:
                            print("\nInvalid movie selection.")
                else:
                    print("\nInvalid genre selection.")
                
            else:
                print("\nInvalid selection in Films menu.")

        elif user_choice == '3':
            # IF userChoice == 3 (My List)
            print("\n--- My List ---")
            if not my_list:
                print("Your list is currently empty. Browse genres to add titles!")
            else:
                print("Saved Movies/Shows:")
                for idx, movie in enumerate(my_list, start=1):
                    print(f"{idx}. {movie}")

        elif user_choice == '4':
            # IF userChoice == 4 (Exit)
            print("\nExiting program. Thank you!")
            break  # Stops the loop and exits

        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
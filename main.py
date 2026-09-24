import json
import os

# File used to persist "My List" between runs
MY_LIST_FILE = "my_list.json"


def load_my_list():
    # Load the saved My List from disk. 
    # Returns an empty list if no file exists or if the file is corrupted/unreadable.
    if os.path.exists(MY_LIST_FILE):
        try:
            with open(MY_LIST_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            print("! Could not read saved My List file. Starting with an empty list.")
    return []


def save_my_list(my_list):
    # Save the current My List to disk.
    try:
        with open(MY_LIST_FILE, "w", encoding="utf-8") as f:
            json.dump(my_list, f, indent=2)
    except OSError:
        print("! Could not save My List to disk.")


def ask_go_back_to_main_menu():
    # Ask the user if they want to return to the main menu.
    # Returns True if yes, False if no (in which case the program will exit).
    while True:
        choice = input("\nGo back to Main Menu? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")


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

    # Store user's saved titles (loaded from previous runs, if any)
    my_list = load_my_list()

    # 2. Print banner once at start
    print("=" * 45)
    print(" 🍿 Netflix Movie Recommendation Assistant 🎦  ")
    print("=" * 45)

    # Use a loop so the menu keeps showing until the user exits
    while True:
        # 3. DISPLAY MAIN MENU
        print("\n" + "="*30)
        print("MAIN MENU")
        print("1. Home 🏠")
        print("2. Films 🎬")
        print("3. My List ❤️")
        print("4. Exit ➜]")

        # 4. PROMPT INPUT: Store choice in user_choice
        user_choice = input("\nEnter your choice (1-4): ").strip()

        # 5. EVALUATE INPUT
        if user_choice == '1':
            # IF userChoice == 1 (Home)
            print("\n--- Trending Now 🔥---")
            print("1. Stranger Things Tales From 85 |                   | New On Netflix")
            print("2. POLONG                        | Top 10 on Netflix | New On Netflix")
            print("3. Plastic Beauty                | Top 10 On Netflix | New On Netflix")

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == '2':
            # IF userChoice == 2 (Films)
            print("\n--- Films Menu 🎬---")
            print("1. By Genre")

            films_choice = input("\nEnter your choice (1): ").strip()

            if films_choice == '1':
                # IF filmsChoice == 1 (Genre)
                print("\n--- Genre Menu ---")
                print("1. Action 🕹️")
                print("2. Comedy 😂")
                print("3. Thriller 🔥")
                print("4. Horror 👻")
                print("5. Romance 💕")

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
                                save_my_list(my_list)
                                print(f"\n✓ '{selected_movie}' added to My List!")
                            else:
                                print(f"\n! '{selected_movie}' is already in My List.")
                        else:
                            print("\nInvalid movie selection.")
                else:
                    print("\nInvalid genre selection.")

            else:
                print("\nInvalid selection in Films menu.")

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == '3':
            # IF userChoice == 3 (My List)
            print("\n--- My List ❤️  ---")
            if not my_list:
                print("Your list is currently empty. Browse genres to add titles!")
            else:
                print("Saved Movies/Shows:")
                for idx, movie in enumerate(my_list, start=1):
                    print(f"{idx}. {movie}")

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == '4':
            # IF userChoice == 4 (Exit)
            print("\nExiting program. Thank you!")
            break  # Stops the loop and exits

        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()
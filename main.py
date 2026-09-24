import json
import os

# File used to persist "My List" between runs
MY_LIST_FILE = "my_list.json"

# text formatting for Film Titles and Synopses
BOLD = "\033[1m"
RESET = "\033[0m"

def clean_saved_entry(entry):
    # Repair an old/corrupted My List entry saved by a previous buggy version of this script
    # Returns a plain title string.
    if isinstance(entry, (list, tuple)) and len(entry) > 0:
        entry = entry[0]
    if isinstance(entry, str):
        entry = entry.strip("{}").strip()
    return entry

def load_my_list():
    # Load the saved My List from disk.
    # Returns an empty list if no file exists or if the file is corrupted/unreadable.
    if os.path.exists(MY_LIST_FILE):
        try:
            with open(MY_LIST_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    cleaned = [clean_saved_entry(item) for item in data]
                    # Remove duplicates that may appear after cleaning, while keeping order
                    seen = set()
                    deduped = []
                    for item in cleaned:
                        if item not in seen:
                            seen.add(item)
                            deduped.append(item)
                    return deduped
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

def ask_go_back(target_name):
    # Ask the user if they want to return to a given menu 
    # Returns True if yes, False if no.
    while True:
        choice = input(f"\nGo back to {target_name}? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def ask_go_back_to_main_menu():
    # Kept as a thin wrapper so existing calls still work.
    return ask_go_back("Main Menu")

def get_int_choice(prompt, valid_range):
    # Prompt for an integer choice. Catches ValueError if the user types a non-numeric value, and checks the number falls within valid_range.
    # Returns the valid integer, or None if the user's input was invalid (caller decides whether to loop again).
    raw = input(prompt).strip()
    try:
        user_choice = int(raw)
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return None

    if user_choice not in valid_range:
        print(f"\nInvalid choice. Please select a number from {min(valid_range)} to {max(valid_range)}.")
        return None

    return user_choice

def get_int_choice_retry(prompt, valid_range):
    # Like get_int_choice, but keeps re-prompting with the same message
    # until the user enters a valid number, instead of giving up after one try.
    while True:
        choice = get_int_choice(prompt, valid_range)
        if choice is not None:
            return choice

def offer_add_to_my_list(movies, my_list):
    # Shared logic: ask the user if they want to add a movie from the given
    # list to My List, and save it if so.
    add_choice = input("\nDo you want to add a movie to My List? (Enter number or 'N' to skip): ").strip()
    if add_choice.isdigit():
        idx = int(add_choice) - 1
        if 0 <= idx < len(movies):
            selected_movie = movies[idx][0]
            if selected_movie not in my_list:
                my_list.append(selected_movie)
                save_my_list(my_list)
                print(f"\n✓ '{BOLD}{selected_movie}{RESET}' added to My List!")
            else:
                print(f"\n! '{BOLD}{selected_movie}{RESET}' is already in My List.")
        else:
            print("\nInvalid movie selection.")

def main():
    # 1. START PROGRAM

    # Data structure to hold movies by genre
    movies_by_genre = {
        1: ("Action 🕹️", [
            ("Extraction", "A black-ops mercenary is hired to rescue a drug lord's kidnapped son."),
            ("Red Notice", "An FBI profiler teams up with a con artist to catch the world's most wanted art thief."),
            ("The Gray Man", "A CIA operative uncovers agency secrets and becomes the target of a sadistic ex-colleague."),
            ("John Wick", "A retired hitman comes out of retirement to track down the gangsters who took everything from him."),
        ]),
        2: ("Comedy 😂", [
            ("Glass Onion", "Detective Benoit Blanc investigates a murder among a group of friends at a billionaire's private island."),
            ("Murder Mystery", "A New York cop and his wife become suspects when a billionaire is murdered on a yacht."),
            ("Red Notice", "An FBI profiler teams up with a con artist to catch the world's most wanted art thief."),
            ("The Hangover", "Three friends wake up from a wild bachelor party with no memory of the night and a missing groom."),
        ]),
        3: ("Thriller 🔥", [
            ("Bird Box", "A woman and two children make a harrowing journey blindfolded to escape an unseen entity."),
            ("The Platform", "Trapped in a vertical prison, inmates fight for food that only reaches the top few levels."),
            ("Leave the World Behind", "A family's getaway is upended by strangers and a series of ominous events."),
            ("Gone Girl", "A man becomes the prime suspect when his wife mysteriously disappears on their anniversary."),
        ]),
        4: ("Horror 👻", [
            ("A Classic Horror Story", "A group of strangers on a road trip find themselves trapped in a nightmare in the woods."),
            ("The Conjuring", "Paranormal investigators help a family terrorized by a dark presence in their farmhouse."),
            ("Polong", "A woman turns to a supernatural spirit for revenge, with deadly consequences."),
            ("Veronica", "A teenage girl accidentally opens a door to the supernatural during a séance."),
        ]),
        5: ("Romance 💕", [
            ("To All the Boys I've Loved Before", "A teen's secret love letters are accidentally sent to all her past crushes."),
            ("The Kissing Booth", "A high schooler's first kiss with her longtime crush turns her world upside down."),
            ("Set It Up", "Two overworked assistants scheme to set up their demanding bosses so they can catch a break."),
            ("Plastic Beauty", "A woman's pursuit of perfection leads her down a dangerous and transformative path."),
        ]),
    }

    # Data structure to hold movies by release-year range: each movie is (title, synopsis)
    movies_by_year = {
        1: ("New Releases (2024-2026)", [
            ("The Gray Man", "A CIA operative uncovers agency secrets and becomes the target of a sadistic ex-colleague."),
            ("Leave the World Behind", "A family's getaway is upended by strangers and a series of ominous events."),
            ("Plastic Beauty", "A woman's pursuit of perfection leads her down a dangerous and transformative path."),
        ]),
        2: ("The 2010s", [
            ("John Wick", "A retired hitman comes out of retirement to track down the gangsters who took everything from him."),
            ("The Hangover", "Three friends wake up from a wild bachelor party with no memory of the night and a missing groom."),
            ("The Kissing Booth", "A high schooler's first kiss with her longtime crush turns her world upside down."),
        ]),
        3: ("Classics (Pre-2010)", [
            ("Gone Girl", "A man becomes the prime suspect when his wife mysteriously disappears on their anniversary."),
            ("The Conjuring", "Paranormal investigators help a family terrorized by a dark presence in their farmhouse."),
        ]),
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
        user_choice = get_int_choice_retry("\nEnter your choice (1-4): ", range(1, 5))

        # 5. EVALUATE INPUT
        if user_choice == 1:
            # IF userChoice == 1 (Home)
            print("\n--- Trending Now 🔥 ---")
            print(f"1. {BOLD}Stranger Things Tales From 85{RESET} |                   | New On Netflix")
            print(f"2. {BOLD}POLONG{RESET}                        | Top 10 on Netflix | New On Netflix")
            print(f"3. {BOLD}Plastic Beauty{RESET}                | Top 10 On Netflix | New On Netflix")

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == 2:
            # IF userChoice == 2 (Films)
            print("\n--- Films Menu 🎬 ---")
            print("1. By Genre")
            print("2. By Year")

            films_choice = get_int_choice_retry("\nEnter your choice (1-2): ", range(1, 3))

            if films_choice == 1:
                # IF filmsChoice == 1 (Genre)
                # Loop so the user can browse multiple genres before leaving this section
                while True:
                    print("\n--- Genre Menu ---")
                    print("1. Action 🕹️")
                    print("2. Comedy 😂")
                    print("3. Thriller 🔥")
                    print("4. Horror 👻")
                    print("5. Romance 💕")

                    genre_choice = get_int_choice_retry("\nSelect a genre (1-5): ", range(1, 6))

                    genre_name, movies = movies_by_genre[genre_choice]
                    print(f"\n--- {genre_name} Movies ---")
                    for idx, (title, synopsis) in enumerate(movies, start=1):
                        print(f"{idx}. {BOLD}{title}{RESET}")
                        print(f"   {synopsis}")

                    offer_add_to_my_list(movies, my_list)

                    if not ask_go_back("Genre menu"):
                        break

            elif films_choice == 2:
                # IF filmsChoice == 2 (Year)
                # Loop so the user can browse multiple time periods before leaving this section
                while True:
                    print("\n--- Year Menu ---")
                    print("1. New Releases (2024-2026)")
                    print("2. The 2010s")
                    print("3. Classics (Pre-2010)")

                    year_choice = get_int_choice_retry("\nSelect a time period (1-3): ", range(1, 4))

                    year_name, movies = movies_by_year[year_choice]
                    print(f"\n--- {year_name} Movies ---")
                    for idx, (title, synopsis) in enumerate(movies, start=1):
                        print(f"{idx}. {BOLD}{title}{RESET}")
                        print(f"   {synopsis}")

                    offer_add_to_my_list(movies, my_list)

                    if not ask_go_back("Year menu"):
                        break

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == 3:
            # IF userChoice == 3 (My List)
            print("\n--- My List ❤️  ---")
            if not my_list:
                print("Your list is currently empty. Browse genres to add titles!")
            else:
                print("Saved Movies/Shows:")
                for idx, movie in enumerate(my_list, start=1):
                    print(f"{idx}. {BOLD}{movie}{RESET}")

            if not ask_go_back_to_main_menu():
                print("\nExiting program. Thank you!")
                break

        elif user_choice == 4:
            # IF userChoice == 4 (Exit)
            print("\nExiting program. Thank you!")
            break  # Stops the loop and exits

if __name__ == "__main__":
    main()
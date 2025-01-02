import sys
from pathlib import Path
from colorama import init, Fore, Style

def display_directory_structure(directory_path: Path, prefix: str = ""):
    try:
        if not directory_path.exists():
            print(f"Path '{directory_path}' does not exist")
            return
        if not directory_path.is_dir():
            print(f"'{directory_path}' is not a directory")
            return

        for item in sorted(directory_path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                display_directory_structure(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"Permission denied to access '{directory_path}'")
    except Exception as e:
        print(f"Error: {e}")

def main():
    init()
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    
    print(f"{Fore.YELLOW}{directory_path}{Style.RESET_ALL}")
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
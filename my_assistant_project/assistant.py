import webbrowser
import datetime
import pyttsx3




NOTES_FILE = "notes.txt"

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    print(f"Търся: {query}")
    webbrowser.open(url)

def search_youtube(query2):
    url2 = f"https://www.youtube.com/search?q={query2}"
    print(f"Търся: {query2}")
    webbrowser.open(url2)

def add_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"[{timestamp}] {note}\n")
    print("✅ Бележката е записана.")

def list_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()
            if not notes:
                print("📭 Няма записани бележки.")
            else:
                print("🗒️ Бележки:")
                for note in notes:
                    print(note.strip())
    except FileNotFoundError:
        print("⚠️ Все още няма файл с бележки.")

def main():
    print("🤖 Личен асистент – въведи команда (help за помощ):")
    while True:
        command = input("> ").strip().lower()

        if command.startswith("google "):
            query = command[7:]
            search_google(query)

        elif command.startswith("youtube "):
            query2 = command[7:]
            search_youtube(query2)

        elif command.startswith("note add "):
            note = command[9:]
            add_note(note)

        elif command == "note list":
            list_notes()

        elif command == "help":
            print("""
Команди:
  google [търсене]      – търси в Google
  youtube [търсене]     - търси в YouTube
  note add [текст]      – добавя бележка
  note list             – показва бележките
  exit                  – изход от програмата
            """)

        elif command == "exit":
            print("👋 Довиждане!")
            break

        else:
            print("❓ Непозната команда. Въведи 'help' за списък.")

if __name__ == "__main__":
    main()

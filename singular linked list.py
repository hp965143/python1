class Song:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return "PLAYLIST IS EMPTY"
        else:
            return "PLAYLIST HAS SONGS"

    def append(self, data):
        new_song = Song(data)
        if self.head is None:
            self.head = new_song
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_song

    def prepend(self, data):
        new_song = Song(data)
        new_song.next = self.head
        self.head = new_song

    def delete(self, data):
        if self.head is None:
            print("PLAYLIST IS EMPTY, NOTHING TO DELETE")
            return
        if self.head.data == data:
            self.head = self.head.next
            print(data, "DELETED SUCCESSFULLY")
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print(data, "DELETED SUCCESSFULLY")
                return
            current = current.next
        print(data, "NOT FOUND IN PLAYLIST")

    def insert(self, data, prev):
        current = self.head
        while current:
            if current.data == prev:
                song = Song(data)
                song.next = current.next
                current.next = song
                print(data, "INSERTED AFTER", prev)
                return
            current = current.next
        print(prev, "NOT FOUND, INSERT FAILED")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(data, "IS AVAILABLE IN THE PLAYLIST")
                return
            current = current.next
        print(data, "IS NOT AVAILABLE IN THE PLAYLIST")

    def display(self):
        if self.head is None:
            print("PLAYLIST IS EMPTY")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("--END OF PLAYLIST--\n")


def menu():
    print("""
1. Append song
2. Prepend song
3. Delete song
4. Insert song after another
5. Search song
6. Display playlist
7. Check if playlist is empty
8. Exit
""")


def main():
    song_playlist = Playlist()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            data = input("Enter song name to append: ")
            song_playlist.append(data)

        elif choice == "2":
            data = input("Enter song name to prepend: ")
            song_playlist.prepend(data)

        elif choice == "3":
            data = input("Enter song name to delete: ")
            song_playlist.delete(data)

        elif choice == "4":
            data = input("Enter new song name: ")
            prev = input("Enter the song after which to insert: ")
            song_playlist.insert(data, prev)

        elif choice == "5":
            data = input("Enter song name to search: ")
            song_playlist.search(data)

        elif choice == "6":
            print("\n--CURRENT PLAYLIST--")
            song_playlist.display()

        elif choice == "7":
            print(song_playlist.is_empty())

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

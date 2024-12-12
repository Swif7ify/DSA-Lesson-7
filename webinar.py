class BSTNode:
    def __init__(self, name: str, webinar_id: str):
        self.name = name
        self.webinar_id = webinar_id
        self.left = None
        self.right = None


class WebinarRegistration:
    def __init__(self):
        self.webinars = {
            "1": {"name": "Python Programming", "root": None},
            "2": {"name": "Web Development", "root": None},
            "3": {"name": "Data Science", "root": None}
        }

    def _insert_participant(self, root, name, webinar_id):
        if not root:
            return BSTNode(name, webinar_id)

        if name < root.name:
            root.left = self._insert_participant(root.left, name, webinar_id)
        else:
            root.right = self._insert_participant(root.right, name, webinar_id)
        return root

    def register_participant(self, webinar_id: str, name: str):
        if webinar_id not in self.webinars:
            print("Invalid webinar selection")
            return

        self.webinars[webinar_id]["root"] = self._insert_participant(
            self.webinars[webinar_id]["root"],
            name,
            webinar_id
        )

        filename = f"webinar_{webinar_id}_participants.txt"
        with open(filename, "a") as f:
            f.write(name + "\n")
        print(f"Successfully registered {name} for {self.webinars[webinar_id]['name']}")

    def show_webinars(self):
        print("\nAvailable Webinars:")
        for id, info in self.webinars.items():
            print(f"{id}. {info['name']}")


def webinar_menu():
    registration = WebinarRegistration()
    while True:
        print("\n=== WEBINAR REGISTRATION MENU ===")
        print("1. Register for webinar")
        print("2. View webinars")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            registration.show_webinars()
            webinar_id = input("Enter webinar number (1-3): ")
            if webinar_id in registration.webinars:
                name = input("Enter participant name: ")
                registration.register_participant(webinar_id, name)
        elif choice == "2":
            registration.show_webinars()
        elif choice == "3":
            break

webinar_menu()
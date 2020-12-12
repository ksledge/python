class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

kelvin = User('kelvin', 'sledge', 'ksledge', 'ksledge@gmail.com', 'Flossmoor')
kelvin.describe_user()
kelvin.greet_user()

deja = User('Deja', 'Washington', 'dwashington', 'dwashington@outlook.com', 'Tuscaloosa')
deja.describe_user()
deja.greet_user()


    

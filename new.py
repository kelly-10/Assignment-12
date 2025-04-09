# Superhero class with encapsulation and methods
class Superhero:
    def __init__(self, real_name, superhero_name, power):
        self.__real_name = real_name  # Private attribute
        self.superhero_name = superhero_name
        self.power = power
    
    # Method to reveal the superhero's identity
    def reveal_identity(self):
        print(f"Secret identity: {self.__real_name}")
    
    # Method to perform an action
    def fight_crime(self):
        print(f"{self.superhero_name} is fighting crime using {self.power}!")

    # Getter method to access the real name (Encapsulation)
    def get_real_name(self):
        return self.__real_name

# Hero class inheriting from Superhero to show polymorphism
class Hero(Superhero):
    def __init__(self, real_name, superhero_name, power, sidekick):
        # Call to the parent constructor
        super().__init__(real_name, superhero_name, power)
        self.sidekick = sidekick

    # Overriding the method to include sidekick's name
    def fight_crime(self):
        print(f"{self.superhero_name} and {self.sidekick} are fighting crime together using {self.power}!")

# Create instances
superhero1 = Superhero("Bruce Wayne", "Batman", "Martial Arts & Gadgets")
hero1 = Hero("Peter Parker", "Spider-Man", "Superhuman Strength & Web-slinging", "Miles Morales")

# Show the functionality
superhero1.fight_crime()  # Batman fighting crime
hero1.fight_crime()  # Spider-Man and Miles fighting crime together

# Reveal identities
superhero1.reveal_identity()  # Bruce Wayne
print(f"Hero real name: {hero1.get_real_name()}")  # Peter Parker

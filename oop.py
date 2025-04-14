class CelestialBeing:
    """Represents a being from another planet with unique abilities."""

    def __init__(self, name, planet, power_source):
        """Initializes a CelestialBeing object."""
        self.name = name
        self.planet = planet
        self.power_source = power_source
        self._energy_level = 100  # Encapsulated attribute

    def describe(self):
        """Provides a basic description of the celestial being."""
        return f"{self.name} hails from the planet {self.planet} and draws power from {self.power_source}."

    def display_energy(self):
        """Displays the current energy level."""
        return f"{self.name}'s current energy level: {self._energy_level}%"

    def _drain_energy(self, amount):
        """Internal method to decrease energy level (encapsulation)."""
        if self._energy_level >= amount:
            self._energy_level -= amount
            return True
        else:
            print(f"{self.name} doesn't have enough energy for that!")
            return False

    def recharge(self, amount):
        """Increases the energy level."""
        self._energy_level += amount
        print(f"{self.name}'s energy level increased to {self._energy_level}%.")

class Superhero(CelestialBeing):
    """Represents a superhero with specific abilities derived from a CelestialBeing."""

    def __init__(self, name, planet, power_source, alias, special_ability):
        """Initializes a Superhero object, inheriting from CelestialBeing."""
        super().__init__(name, planet, power_source)
        self.alias = alias
        self.special_ability = special_ability
        self.battles_won = 0

    def describe(self):
        """Overrides the describe method to include superhero details."""
        return f"{self.alias}, secretly known as {self.name} from {self.planet}. Their power source is {self.power_source} and their special ability is {self.special_ability}."

    def use_ability(self):
        """Demonstrates the superhero using their special ability."""
        if self._drain_energy(20):
            return f"{self.alias} uses their {self.special_ability}!"
        return ""

    def fight(self, villain):
        """Engages in a fight with a villain."""
        if self.use_ability():
            self.battles_won += 1
            return f"{self.alias} fought {villain} and emerged victorious! Battles won: {self.battles_won}"
        else:
            return f"{self.alias} doesn't have enough energy to fight {villain}!"

class Kryptonian(Superhero):
    """Represents a superhero specifically from the planet Krypton."""

    def __init__(self, name, alias, special_ability):
        """Initializes a Kryptonian object."""
        super().__init__(name, "Krypton", "Solar Radiation", alias, special_ability)
        self.weakness = "Kryptonite"

    def describe(self):
        """Overrides the describe method to include Kryptonian weakness."""
        return f"{self.alias}, the Kryptonian hero known as {self.name}. Powered by solar radiation, their special ability is {self.special_ability}. Their weakness is {self.weakness}."

    def encounter_weakness(self):
        """Simulates encountering their weakness."""
        self._energy_level = max(0, self._energy_level - 50)
        return f"{self.alias} is exposed to {self.weakness}! Energy level reduced."

# Creating instances
alien_being = CelestialBeing("Zylar", "Xylos", "Cosmic Rays")
super_guy = Superhero("Jax", "Terra Nova", "Quantum Field", "Nova Force", "Energy Blasts")
super_kryptonian = Kryptonian("Kal-El", "Superman", "Flight and Super Strength")

# Interacting with the objects
print(alien_being.describe())
print(alien_being.display_energy())
alien_being.recharge(30)
print(alien_being.display_energy())

print("\n" + super_guy.describe())
print(super_guy.display_energy())
print(super_guy.use_ability())
print(super_guy.display_energy())
print(super_guy.fight("Dr. Doom"))
print(super_guy.fight("Lex Luthor"))

print("\n" + super_kryptonian.describe())
print(super_kryptonian.display_energy())
print(super_kryptonian.use_ability())
print(super_kryptonian.encounter_weakness())
print(super_kryptonian.display_energy())
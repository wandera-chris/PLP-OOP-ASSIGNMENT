# PLP-OOP-ASSIGNMENT
#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

Explanation:

CelestialBeing Class:

Attributes:
name: The name of the celestial being.
planet: Their home planet.
power_source: The source of their power.
_energy_level: An encapsulated attribute (indicated by the single underscore) representing their current energy. We intend for this to be accessed and modified through the class's methods, demonstrating a form of encapsulation.
Constructor (__init__): Initializes the name, planet, and power_source attributes when a CelestialBeing object is created. It also sets a default _energy_level.
Methods:
describe(): Returns a basic description of the being.
display_energy(): Shows the current _energy_level.
_drain_energy(): An internal method to decrease the _energy_level. The underscore suggests it's intended for internal use within the class and its subclasses.
recharge(): Increases the _energy_level.
Superhero Class:

Inheritance: Inherits from the CelestialBeing class using class Superhero(CelestialBeing):. This means Superhero objects automatically have the attributes and methods of CelestialBeing.
Additional Attributes:
alias: The superhero's code name.
special_ability: Their unique superpower.
battles_won: A counter for the number of battles won.
Constructor (__init__): Calls the __init__ of the parent class (CelestialBeing) using super().__init__(name, planet, power_source) to initialize the inherited attributes. It then initializes the alias, special_ability, and battles_won specific to superheroes.
Overridden Method (describe): Provides a more detailed description specific to a superhero, including their alias.
New Methods:
use_ability(): Simulates using their special ability, which drains energy using the inherited _drain_energy() method.
fight(): Simulates a fight, using the use_ability() and updating the battles_won count. This demonstrates polymorphism through method calls on potentially different Superhero subclasses.
Kryptonian Class:

Inheritance: Inherits from the Superhero class.
Additional Attribute:
weakness: A specific weakness of Kryptonians.
Constructor (__init__): Calls the __init__ of the parent class (Superhero), providing specific values for planet and power_source that are characteristic of Kryptonians. It also initializes the weakness.
Overridden Method (describe): Further overrides the describe method to include the Kryptonian's weakness.
New Method (encounter_weakness): Simulates encountering their weakness, which reduces their energy level, further demonstrating the specialized behavior of this subclass.
Key Concepts Demonstrated:

Class Definition: Creating blueprints for objects.
Attributes: Data associated with an object.
Methods: Functions that an object can perform.
Constructor (__init__): Initializing object attributes with unique values when an object is created.
Inheritance: The Superhero and Kryptonian classes inherit attributes and methods from the CelestialBeing and Superhero classes, respectively, promoting code reuse and establishing an "is-a" relationship.
Polymorphism: The describe() method is overridden in the subclasses (Superhero and Kryptonian) to provide behavior specific to those types, even though you might call the describe() method on different types of CelestialBeing (or its descendants) through a common interface. The fight() method in Superhero could potentially interact with different types of villains in a polymorphic way (though not explicitly shown with a Villain class here).
Encapsulation: The _energy_level attribute in CelestialBeing is intended to be accessed and modified through the class's methods (_drain_energy() and recharge()), hiding the internal implementation details and controlling how the energy level is changed. The single underscore is a convention in Python indicating a "protected" member, suggesting it shouldn't be directly accessed from outside the class.

# Define a Car class
class Car:
    def __init__(self, make, model, year, color, mileage):
        """
        Initialize a Car object with attributes:
        - make (str)
        - model (str)
        - year (int)
        - color (str)
        - mileage (int)
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.score = 0  # initialize score to 0

    def drive(self, miles):
        """
        Simulate driving the car for a certain number of miles
        and update the mileage attribute
        """
        self.mileage += miles
        print(f"You drove {miles} miles. Current mileage: {self.mileage}")

    def get_score(self):
        """
        Calculate a score based on the car's attributes
        - newer cars (higher year) score higher
        - cars with lower mileage score higher
        - cars with certain colors (e.g. red, black) score higher
        """
        score = self.year * 10  # newer cars score higher
        score -= self.mileage / 100  # lower mileage scores higher
        if self.color in ["red", "black"]:
            score += 50  # certain colors score higher
        self.score = score
        return score

    def __str__(self):
        """
        Return a string representation of the Car object
        """
        return f"{self.make} {self.model} ({self.year}) - {self.color} - {self.mileage} miles"

# Create some Car objects
car1 = Car("Toyota", "Corolla", 2020, "silver", 30000)
car2 = Car("Ford", "Mustang", 2018, "red", 50000)
car3 = Car("Honda", "Civic", 2022, "black", 10000)

# Drive some cars and calculate scores
car1.drive(100)
car2.drive(50)
car3.drive(200)

print("Car scores:")
print(car1.get_score())
print(car2.get_score())
print(car3.get_score())

# Print the Car objects
print("\nCars:")
print(car1)
print(car2)
print(car3)
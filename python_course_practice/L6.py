#Part One

# 1. Define the class "Stadium"
class Stadium:
    # 2. The docstring for the "Stadium" class
    """The summary docstring for the stadium class. This class represents a Stadium."""

    def __init__(self, name, city_state, capacity):
        self.name = name    
        self.city_state = city_state    
        self.capacity = capacity    
   
    
    def describe_stadium(self):
        """Describes the stadium."""
        print("The " + self.name + " is located in " + self.city_state + " and holds " + self.capacity + " fans.")


# Create instance 
stadium1 = Stadium("Mercedes Benz Arena", "Atlanta, GA", "70,000" )

# Call the function

stadium1.describe_stadium()

#Part two

class Stadium:
    # 2. The docstring for the "Stadium" class
    """The summary docstring for the stadium class. This class represents a Stadium."""

    def __init__(self, name, city_state, capacity, sports_played, seats_available):
        self.name = name    
        self.city_state = city_state    
        self.capacity = capacity   
        self.sports_played = sports_played
        self.seats_available = seats_available

    def describe_stadium(self):
        """Describes the stadium."""
        print("The " + self.name + " is located in " + self.city_state + " and holds " + self.capacity + " fans.")
        print("The following sport is mainly played in this stadium: " + self.sports_played)
        print("There are still " + self.seats_available + " for tonight's game.");


# Create instance 
stadium1 = Stadium("Dodd Stadium", "Norwich, CT", "30,000", "Baseball", "5000")

# Call the function

stadium1.describe_stadium()
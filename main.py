# Importing necessary cheese modules
import cheddar
import brie
import gouda
import swiss

# Global variable for the fridge password
FRIDGE_PASSWORD = "YOUR_PASSWORD_HERE"

# Function to steal cheese from the virtual fridge
def steal_cheese_from_fridge(password):
    if password != FRIDGE_PASSWORD:
        print("Invalid password! Access denied.")
        return []
    
    fridge = open_fridge()
    cheese_types = ["Cheddar", "Brie", "Gouda", "Swiss"]
    stolen_cheese = []

    for cheese in cheese_types:
        if cheese in fridge:
            stolen_cheese.append(cheese)
            print(f"Stolen: {cheese}")
        else:
            print(f"{cheese} not found in the fridge.")
    
    close_fridge()
    return stolen_cheese

# Function to open the fridge
def open_fridge():
    print("Opening the virtual fridge...")
    return ["Cheddar", "Brie", "Gouda"]  # Contents of the fridge

# Function to close the fridge
def close_fridge():
    print("Closing the virtual fridge...")

# Main execution
if __name__ == "__main__":
    print("Executing CheeseStealer...")
    user_password = "cheesy123"  # User-provided password (hardcoded)
    stolen_cheese = steal_cheese_from_fridge(user_password)
    print("Cheese stealing complete.")
    print(f"Stolen cheese: {', '.join(stolen_cheese)}")

#this program calculates the kinetic energy of an object given its mass and velocity

#prompt user for mass and velocity
mass = float(input("Enter the mass of the object in kilograms: "))
velocity = float(input("Enter the velocity of the object in meters per second: "))

#define function to calculate kinetic energy
def kinetic_energy(mass, velocity): 
    #calculate kinetic energy
    ke = 0.5 * mass * velocity ** 2
    return ke

#call function and display result
total = kinetic_energy(mass, velocity)
print(f"The kinetic energy of the object is {total} Joules.")

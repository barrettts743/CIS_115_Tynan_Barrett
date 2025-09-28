#this program allows the user to calculate the energy
#into Joules given the mass using formula E=mc^2
# assign known variable
c = 2.99 * 10**8

#define functions
def calculate_energy(mass, speed_of_light):
    energy = mass * speed_of_light**2
    return energy

#define main function
def main():
    #get user input
    mass = float(input('Enter the mass in kilograms: '))
    print('You entered:', mass)
    #call the function
    energy = calculate_energy(mass, c)
    print(f'The energy produced is:', energy, 'Joules')

#call main function
main()
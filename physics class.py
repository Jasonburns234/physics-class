# Simple physics program

# Define variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Define function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

# Test the f_to_c function
print(f_to_c(32))

# Convert 100 degrees Fahrenheit to Celsius
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Define function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

# Test the c_to_f function
print(c_to_f(0))

# Define function to calculate force
def get_force(mass, acceleration):
  return mass * acceleration

# Calculate the force of the train
train_force = get_force(train_mass, train_acceleration)

# Print the calculated force
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Define function to calculate energy
def get_energy(mass, c=3*10**8):
  return mass * c**2

# Calculate the energy of the bomb
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Define function to calculate work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# Calculate the work done by the train
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

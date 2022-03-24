# https://www.codecademy.com/courses/learn-python-3/projects/physics-class
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
# Q1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Q2
f100_in_celsius = f_to_c(100)
# print(f100_in_celsius)

#  Q3
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

# Q4
c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)

# Q5 Reached the Use The Force part uncommented 1st lines of code 2 - 5
def get_force(mass, acceleration):
  return mass * acceleration

# Q6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Q7
print("The GE train supplies "+str(train_force)+" Newtons of force.")

# Q8
def get_energy(mass, c = 3*10**8):
  return mass * c**2

# Q9
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# Q10
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Q11
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# Q12
train_work = get_work(train_mass, train_acceleration, train_distance)

# Q13
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
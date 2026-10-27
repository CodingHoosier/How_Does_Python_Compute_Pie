# https://www.youtube.com/watch?v=huUDnh6pZjI
# How Does Python Compute Pie ?
# First, define some delicious 
#  types of Pie
# We use the list data structure
#  to store the flavors of Pie.
flavors = ["Apple", 
           "Peach", 
           "Lemon", 
           "Cherry"]
# Next, we need sizes
sizes = ["Baby", 
         "Small", 
         "Medium", 
         "Large",
         "Party"]
# And we need crust types
crusts = ["flaky", 
          "Shortcrust", 
          "Graham", 
          "Crumb"]
# Now we can compute Pie by combining the attributes.
my_pie = f"{sizes[2]} {flavors[0]} Pie with a {crusts[0]} crust"
print(f"My Pie is {my_pie}")
# How about a random Pie?
# Are you in the mood
#  for a random Pie?
# Let's compute one.
# We use the random module
#  to select a 
#  flavor, size, and crust.
import random
my_pie = f"{random.choice(sizes)} {random.choice(flavors)} Pie with a {random.choice(crusts)} crust"
print(f"My random Pie is {my_pie}")
# How about 10 random Pies?
my_pies = []
for i in range(10):
    my_pies.append(f"{random.choice(sizes)} {random.choice(flavors)} Pie with a {random.choice(crusts)} crust")
print(f"My random Pies are {my_pies}")
# Now we want a specific pie...
#  It's a baby size apple pie
#  with a flaky crust.
# We know the index of 
#  each attribute, 
#  so we can use that 
#  to compute the pie.
my_pie = f"{sizes[0]} {flavors[0]} Pie with a {crusts[0]} crust"
print(f"My specific Pie is {my_pie}")

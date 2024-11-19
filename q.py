# write a function rolls() that takes no arguments and simulate a sequence of rolls of a pair dice.The simulation should continue rolling the pair of dice and stop only when a rolled pair matches the pair on the original roll. when comparing rolls, the pair of numbers should be the same regardless of order. E.g.g the pair (2,4) matches both the pair (2,4) and the pair (4,2). The function then returns the total number of rolls made. 

# >>> rolls()  # Suppose rolls were : (2,4) (3,5) (4,2)
# 3 

# >>> rolls()  # (5,1) (2,4) (3,3) (4,5) (4,2) (5,1)
# 6




# Implement a class StopLight that represents a traffic signal, which during each cycle goes from green, to yellow, to red. Each StopLight will have 4 numeric attributes: 1)-3) are the duration (in seconds) of the green, yellow, and red signals and 4) is the current time in the cycle. 

# __init__  constructor - accepts four optional arguments. Each of these is stored as an attribute , no validation required. The arguments are: 1. duration of green ( defaults to 30.0), 2. duration of yellow (defaults to 10.0), 3. duration of red  (defaults to 40.0), 4. current time in the cycle (defaults to 0.0).

# __repr__ - see sample below

# >> light1 = StopLight(20.0, 15.0, 30.0, 12.0) # green, yellow, red, time
# >> light1
# StopLight(20.0, 15.0, 30.0, 12.0)
# >> light2 = StopLight() # use defaults
# light2
# StopLight(30.0, 10.0, 40.0, 0.0)


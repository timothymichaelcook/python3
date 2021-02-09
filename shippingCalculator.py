#IMPORT MODULES
#DECLARE INITIAL VARIABLES
#CONDITIONAL STATEMENTS
#OUTPUTS

#IMPORT MODULES

#DECLARE INITIAL VARIABLES
weight = 41.5

#CONDITIONAL EXPRESSIONS 

#GROUND SHIPPING COST
if weight <= 2:
  cost_to_ship_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_to_ship_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_to_ship_ground = weight * 4.00 + 20
elif weight > 10:
  cost_to_ship_ground = weight * 4.75 + 20

#PREMIUM SHIPPING COST
cost_to_ship_premium = 125.00

#DRONE SHIPPING COST
if weight <= 2:
  cost_to_ship_drone = weight * 4.50 + 0
elif weight > 2 and weight <= 6:
  cost_to_ship_drone = weight * 9.00 + 0
elif weight > 6 and weight <= 10:
  cost_to_ship_drone = weight * 12.00 + 0
elif weight > 10:
  cost_to_ship_drone = weight * 14.25 + 0

#OUTPUT COSTS OF ALL SHIPPING METHODS
print("Your current package weight is: " + str(weight) + "lbs.")
print("The cost to ship via ground would be $" + str(cost_to_ship_ground) + ".")
print("The cost to ship via premium would be $" + str(cost_to_ship_premium) + ".")
print("The cost to ship via drone would be $" + str(cost_to_ship_drone) + ".")

#OUTPUT RECOMMENDATION
if cost_to_ship_ground < cost_to_ship_premium and cost_to_ship_ground < cost_to_ship_drone:
  print("Ground shipping is the best value.")
elif cost_to_ship_premium < cost_to_ship_ground and cost_to_ship_premium < cost_to_ship_drone:
  print ("Premium shipping is the best value.")
else:
  print("Drone shipping is the best value.")


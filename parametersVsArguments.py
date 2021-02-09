#NO PARAMETER OR ARGUMENT

def mult_two_add_three():
    number = 5
    print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three()

#FUNCTION WITH PARAMETER AND ARGUMENT
#
#NUMBER IS THE FUNCTION'S PARAMETER
#
#6 IS THE FUNCTION'S ARGUMENT
#
def mult_two_add_three(number):
      print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(6)

#FUNCTION WITH MULTIPLE PARAMETERS AND ARGUMENTS
def mult_x_add_y(number, x, y):
    print(number*x + y)

mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)

#ANOTHER FUNCTION
# Define create_spreadsheet():
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications", row_count = 10)

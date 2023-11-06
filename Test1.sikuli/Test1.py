# SikuliX script for testing the Windows Calculator
# This script assumes that the Windows Calculator is open and visible.

# Import the required SikuliX functions
from sikuli import *

# Define the calculator symbols and their coordinates
click ("1699256005822.png")
wait ("1699256038282.png")
type ('calc' + Key.ENTER)

wait ("1699256093445.png")

# Click on the "1" button
click ("1699255777843.png")

# Click on the "+" button
click( "1699255800584.png") 

# Click on the "2" button
click( "1699255809297.png")
# Click on the "=" button
click( "1699255816961.png")

#verify result
exists ("1699256322162.png")    
 
# Close the calculator (optional)
# You may need to adjust this part based on your operating system
# For Windows, Alt+F4 is commonly used to close the calculator.
type(Key.F4, Key.ALT)
# %%
input_number = input("Specify a number: ")
input_base = input("What is the base of the number? ")
output_base = int(input("What base to convert to? "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Initialize alphabet string for handling base-10 -> base-10+n conversions

# %%

separatedNumber = input_number.split('.') # Split number into int and float (if inputted number is float which is not supported)

result_int = [] # Initialize result list for storing converted ints

temp1 = int(separatedNumber[0], int(input_base)) # Temporarily convert number to base-10 for conversion into base-n

while True:
    if(temp1 // output_base == temp1): # Break out of while loop if function has divided input number to lowest possible floor
        break
    else:
        result_int.append(temp1 % output_base) # The result of temp1 % output_base is equivalent to the digits of the output number in base-n, hence we append the result to our result_int list.
        temp1 = temp1 // output_base           # Floor temp1 by output_base, then repeat loop until break condition is achieved.

result_int.reverse() # result_int list is inputted in reverse order, hence we apply the reverse() method to compensate.

# %%
 
output = ""

for item in result_int:
    if (item > 9):  # If the value of a digit in the resulting int list is over 9, then represent the digit with it's base-10+n equivalent
        output += alphabet[item - 10]
    else:        
        output += str(item)

print("Base-%d -> Base-%d:" % (int(input_base), output_base))
print(output)
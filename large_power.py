def large_power(base, exponent):
  result = base ** exponent
  if result > 5000:
    return "True"
  else:
    return "False"
print(f"large_power(2, 13) = {large_power(2, 13)}")


# divisible by 10
def divisiblle_by_ten(num):
  if num % 10 == 0:
    return "True"
  else:
    return "False"



# week 3 assignment  

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price 
  else:
    return price
 
# prompt user for original price and discount percentage

original_price = float(input("Enter the original price of the item "))
discount_percent = float(input("Enter the discount percentage "))


# the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# if discount was applied print the appropriate message
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
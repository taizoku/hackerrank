def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input()) / 100
    # tax percentage
    tax_percent = int(input()) / 100

    # Write your calculation code here
    tip = meal_cost * tip_percent  # calculate tip
    tax = meal_cost * tax_percent  # calculate tax

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = int(round(meal_cost + tip + tax))

    return str(total_cost)


# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
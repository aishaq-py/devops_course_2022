def _input(message, input_type=int):
    while True:
      try:
        return input_type (input(message))
      except:
        pass

total_cost = _input("Cost of dream home?\n")
annual_salary = _input("What is your annual salary?\n")
portion_saved = input("What portion of your salary is saved? (0.00 to 1.00)\n")
current_savings = _input("Current savings?\n")
semi_annual_raise = input("Semi-annual raise factor (0.00 - 1.00):\n")

portion_down_payment = 0.25
r = 0.04

def time_to_purchase(total_cost,annual_salary,portion_saved,current_savings,portion_down_payment,r):
  savings_return = current_savings*r/12
  deposit_target = portion_down_payment*int(total_cost)
  deficit = deposit_target-float(portion_saved)
  monthly_salary_saved = int(annual_salary)*float(portion_saved)/12
  monthly_total_saved = monthly_salary_saved + savings_return
  time_to_purchase = int(deficit)/int(monthly_total_saved)
  if time_to_purchase >= 6.0:
    saved_list = []
    saved_list.append(monthly_salary_saved*6)
    number_of_raises = int(time_to_purchase/6)
    i = 1
    while i <= number_of_raises:
      annual_salary = annual_salary + int(annual_salary)*float(semi_annual_raise)
      #print(annual_salary)
      monthly_salary_saved = int(annual_salary)*float(portion_saved)/12
      #print(monthly_salary_saved)
      saved_list.append(monthly_salary_saved*6)
      i += 1
    actual_monthly_saved = sum(saved_list)/float(time_to_purchase) + float(savings_return)
    time_to_purchase = float(deficit)/float(actual_monthly_saved)
  else:
    pass
  if time_to_purchase > 0:
    return time_to_purchase
  else:
    pass
  
x = time_to_purchase(total_cost,annual_salary,portion_saved,current_savings,portion_down_payment,r)
print(x)

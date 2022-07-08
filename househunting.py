# House Hunting Part B


# =============================================================================
# def monthly_saving(current_savings,monthly_salary,portion_saved):
#     annual_roi = 0.04
#     monthly_roi = annual_roi/12
#     
#     current_savings *= (1+monthly_roi)
#     current_savings += monthly_salary*portion_saved
#     return current_savings
# 
# def raised_monthly_salary(monthly_salary,semi_annual_raise,):
#     new_monthly_salary = monthly_salary*(1+semi_annual_raise)
#     return new_monthly_salary
#     
# 
# 
# annual_salary = float(input("Your annual salary: "))
# monthly_salary = annual_salary/12
# portion_saved = float(input("Percent of your salary to save: "))
# 
# 
# total_cost = float(input("The cost of your dream home: "))
# portion_down_payment = 0.25
# down_payment = total_cost*portion_down_payment
# 
# semi_annual_raise = float(input("Semi-annual raise: "))
# 
# current_savings = 0.0
# month_passed = 0
# 
# while current_savings < down_payment:
#     if month_passed % 6 == 0 and month_passed != 0:
#         monthly_salary = raised_monthly_salary(monthly_salary, semi_annual_raise)
#     current_savings = monthly_saving(current_savings, monthly_salary,portion_saved)
#     month_passed += 1
#     
# print("Number of months:", month_passed)
# =============================================================================




# =============================================================================
# #House Hunting Part C
# 
# 
# def monthly_saving(current_savings,monthly_salary,portion_saved):
#     annual_roi = 0.04
#     monthly_roi = annual_roi/12
#     
#     current_savings *= (1+monthly_roi)
#     current_savings += monthly_salary*portion_saved
#     return current_savings
# 
# def raised_monthly_salary(monthly_salary,semi_annual_raise,):
#     new_monthly_salary = monthly_salary*(1+semi_annual_raise)
#     return new_monthly_salary
#     
# 
# def targeted_month_saving(target,monthly_salary,portion_saved,semi_annual_raise):
#     
#     current_savings = 0.0
#     month_passed = 0
#     
#     while month_passed < target:
#         if month_passed % 6 == 0 and month_passed != 0:
#             monthly_salary = raised_monthly_salary(monthly_salary, semi_annual_raise)
#         current_savings = monthly_saving(current_savings, monthly_salary,portion_saved)
#         month_passed += 1
#     return current_savings     
# 
# def middle(low_boundary,high_boundary):
#     return (low_boundary+high_boundary)/2
#        
#        
# annual_salary = float(input("Your annual salary: "))
# monthly_salary = annual_salary/12
# 
# total_cost = float(input("The cost of your dream home: "))
# portion_down_payment = 0.25
# down_payment = total_cost*portion_down_payment
# 
# semi_annual_raise = float(input("Semi-annual raise: "))
# 
# epsilon = 10.0
# target = 24
# 
# low_boundary = 0.00
# high_boundary = 1.00
# portion_saved = middle(low_boundary, high_boundary)
# 
# number_of_tries = 1 
# 
# while abs(targeted_month_saving(target, monthly_salary, portion_saved, semi_annual_raise)-down_payment) > epsilon:
#     if targeted_month_saving(target, monthly_salary, portion_saved, semi_annual_raise) > down_payment:
#         high_boundary = (low_boundary+high_boundary)/2
#         portion_saved = middle(low_boundary, high_boundary)
#     else:
#         low_boundary = (low_boundary+high_boundary)/2
#         portion_saved = middle(low_boundary, high_boundary)
#     number_of_tries += 1
#     
# print(portion_saved)
# print(number_of_tries)      
# =============================================================================
       
       
       
       
       
       
       
       
       
       
       
       
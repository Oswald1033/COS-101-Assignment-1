
print("Mr yusuf And Sons")
print("Enter the repaired information to calculate simple and compound intrest respectively")
initial_principal = float(input("Enter your initial principal:  "))
interest_rate = float(input("Enter your initial rate:  "))
number_of_times_interest_per_time_period = float(input("Enter number times ineterst per time period:  "))
number_of_times_period_elapsed = float(input("Enter your number of times period elapsed:  "))
simple_interest = initial_principal * (1 + interest_rate * number_of_times_interest_per_time_period )
compound_interest = (initial_principal * (1 + (interest_rate/number_of_times_period_elapsed))
                     ** number_of_times_period_elapsed*number_of_times_interest_per_time_period)

print("YUSUF AND SONS COMPANY")
print(f'simple intrest : {simple_interest}')
print(f'compound intrest:{simple_interest}')








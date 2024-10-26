print("Calculating age for 90 years")
age = int(input("What is your age?: "))

remaining_age_in_years = 90 - age
remaining_age_in_months = remaining_age_in_years * 12
remaining_age_in_weeks = remaining_age_in_years * 54
remaining_age_in_days = remaining_age_in_years * 365

print(f"Your remaining life span is {remaining_age_in_years} years or {remaining_age_in_months} months or "
      f"{remaining_age_in_weeks} weeks or {remaining_age_in_days} in days.")


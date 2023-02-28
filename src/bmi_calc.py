height = input("What is your height?  [m]: ")
weight = input("What is your weight? [kg]: ")

bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)

print ("\nBMI is equal to:", bmi_as_int)
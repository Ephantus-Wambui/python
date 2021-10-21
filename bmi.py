height = float(input('What is your height in meters? '))
weight = float(input('What is your weight in kilograms? '))

bmi_calc = weight/(height**2)

if (bmi_calc < 18.5):
    print('Under weight')
    print(f'Your bmi is {bmi_calc}')

elif (bmi_calc >= 18.5 or bmi_calc < 25):
    print('Your bmi is normal')
    print(f'Your bmi is {bmi_calc}')

elif (bmi_calc >= 25 or bmi_calc < 30):
    print('Overweight')
    print(f'Your bmi is {bmi_calc}')

elif (bmi_calc > 30):
    print("Obesity")
    print(f'Your bmi is {bmi_calc}')

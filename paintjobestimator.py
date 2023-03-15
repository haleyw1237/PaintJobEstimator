print("Welcome to Paint Estimator")


#function 
def calculate(area, price_of_paint):
    #gallon
    print('The number of gallons of paint required is', format(area / 350,'.2f'))
    #labor
    print('The ho urs of labor required is', format(area / 350 * 8, '.2f'))
     #cost
    print('The cost of the paint is $', format(area / 350 * price_of_paint,'.2f'), sep='')
    #labor charge
    print('The labor charges is $', format(area / 350 * 8 * 62.35, '.2f'), sep='')
    #total
    print('The total cost of the paint job is $',format(area / 350 * price_of_paint + area / 350 * 8 * 62.35, '.2f'),sep='')

do_calculation = True
while(do_calculation):
    area = float(input('Enter the square feet of wall space to be painted: '))
    price_of_paint = float(input('Enter the price of the paint per gallon: $'))
    calculate(area, price_of_paint)
    continue_ = input("Do you want to perform another calculation? (y/n): ")
    if (continue_ != "y"):
        do_calculation = False

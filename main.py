#made by Laurin Seeholzer

x_values = [1,2,3]      #given x values
y_values = [2,4,6]      #given y values
x_given = 200           #given x value to predict the y value for
y_prediction = 0

#calculate the averages of given y and given x values
x_average = (sum(x_values))/(len(x_values))
x_average = (sum(y_values))/(len(y_values))

#calculate b1
b1_counter = 0
z = 0
for i in x_values:
    x = x_values[z]
    y = y_values[z]

    valule1 = (x - x_average)
    valule2 = (y - x_average)
    result = (valule1 * valule2)

    b1_counter = b1_counter + result
    z = z+1

#calculate b2
b2_counter = 0
z = 0
for i in x_values:
    x = x_values[z]

    valule1 = (x - x_average)
    result = (valule1 * valule1)

    b2_counter = b2_counter + result
    z = z+1

#calculate b
b = b1_counter / b2_counter

#calculate a
a = x_average - (b * x_average)


#maincalculation
y_prediction = a + (b * x_given)

#output
z = 0
for i in x_values:
    x = x_values[z]
    y = y_values[z]
    z = z+1
    print(x,y)

print("")
print("prediction:")
print(x_given, y_prediction)
print("")

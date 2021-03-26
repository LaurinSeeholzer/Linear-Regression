# Linear-Regression

This is a project to understand and programatically implement linear regression and the mathematics behind it.

## The mathematics behind linear regression

If you visualize the given x and y values, you will see a more or less precise straight line that depends on the accuracy of the given x and y values. This straight line or the slope of this straight line and thus the dependency of the x and y values is approximated with the linear regression. This straight line allows you to assign unknown y-values to an x-value.
When calculating the straight line, two parameters (a, b) are used, which can be calculated from the existing x and y values.

![image](https://user-images.githubusercontent.com/76901165/112689908-30749380-8e7b-11eb-8545-c51c6aae1c1f.png)

A straight line is generally defined as follows by two parameters (a, b), where y is the y-value to be calculated, which corresponds to x, the already specified x-value.

![image](https://user-images.githubusercontent.com/76901165/112690603-5b131c00-8e7c-11eb-92ea-31d0d6420b09.png)

The parameter b can be calculated as follows from the available x and y values, where the numerator of the fraction of the sum of x minus the x average multiplied by y minus the y average, for each x and y Value. 

![image](https://user-images.githubusercontent.com/76901165/112690567-4a62a600-8e7c-11eb-9e2a-5c286601976c.png)

The calculation of parameter a is much easier than the calculation of parameter ö. B, but the calculation of; àParameter a, parameter b required. Parameter a is defined by the y-average minus parameter B multiplied by the x-average.

![image](https://user-images.githubusercontent.com/76901165/112690673-767e2700-8e7c-11eb-816c-5592ed559676.png)

## Programatical implementation

```python

x_values = [1,2,3]
y_values = [2,4,6]
x_given = 200
y_prediction = 0

x_average = (sum(x_values))/(len(x_values))
x_average = (sum(y_values))/(len(y_values))

#Zähler von b bestimmen
b_counter = 0
z = 0
for i in x_values:
    x = x_values[z]
    y = y_values[z]

    valule1 = (x - x_average)
    valule2 = (y - x_average)
    result = (valule1 * valule2)

    b_counter = b_counter + result
    z = z+1

#Nenner von b bestimmen
b2_counter = 0
z = 0
for i in x_values:
    x = x_values[z]

    valule1 = (x - x_average)
    result = (valule1 * valule1)

    b2_counter = b2_counter + result
    z = z+1


b = b_counter / b2_counter
#a berechnen
a = x_average - (b * x_average)

#Endberechnung
y_prediction = a + (b * x_given)

#Ausgaben
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

```

 


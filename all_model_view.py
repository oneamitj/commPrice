#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange, date2num, MONTHLY, DAILY, SU, WeekdayLocator, num2date
import datetime
from dataset import *
from numpy import *
from numpy.linalg import *


def linear_regression(x, y):
	length = len(x)
	sum_x = sum(x)
	sum_y = sum(y)

	sum_x_squared = sum(map(lambda a: a * a, x)) # to compute Σx^2
	covariance = sum([x[i] * y[i] for i in range(length)]) # to compute Σxy

	a = (covariance - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
	b = (sum_y - a * sum_x) / length

	return a, b


def higher_regression(x, y, order):
	# Form of non-linear (higher order) regression y = a + bx + cx**2
	# Normal equation X'XB = X'y
	# X = [1 x x**2] X' = transpose(X) B(required soln) = [[a], [b], [c]] 

	X = []

	if order == 2:
		for i in x:
		 	X.append([1, i, i*i])
	elif order == 3:
		for i in x:
		 	X.append([1, i, i*i, i*i*i])
	else:
		return "Invalid order (valids 1 or 2)"

	XT = transpose(X)

	A = dot(XT, X)
	Y = dot(XT, y)

	B = solve(A,Y)

	return B



def main(data):
	x = data.dates
	y = data.price

	X, Y = linear_regression(x, y)# for linear regression uncomment this line
	p, q, r = higher_regression(x, y, 2)# for quadratic regression uncomment this line
	a, b, c, d = higher_regression(x, y, 3)# for cubic regression uncomment this line


	print '\nRegression Model for price prediction of %s' % (str(data).replace("dataset.",''))
	print '\nRegression Model::\n\t a = %f\tb = %f' % (X, Y)
	print 'Regression Equation::\n\t predicted price = %f * date + (%f)' % (X, Y)
	print

	loc = WeekdayLocator(byweekday = SU, interval=1)
	formatter = DateFormatter('%y-%m-%d')

	date1 = datetime.date( 2013, 4, 1 )
	date2 = datetime.date( 2015, 3, 1 )
	delta = datetime.timedelta(days=7)
	dates = drange(date1, date2, delta)

	price1 = []
	price2 = []
	price3 = []
	for date in dates:
		price_calc1 = X*date + Y	# for linear regression uncomment this line
		price_calc2 = p + q*date + r*date*date	# for quadratic regression uncomment this line
		price_calc3 = a + b*date + c*date*date + d*date*date*date # for cubic regression uncomment this line
		price1.append(price_calc1)
		price2.append(price_calc2)
		price3.append(price_calc3)


	Title = "Graph plot of %s\nIndex\n<original data black> <linear green>\n<quadratic blue> <cubic red>" % (str(data).replace("dataset.",''))

	fig, ax = plt.subplots()
	ax.set_title(Title)
	plt.plot_date(dates, price1, '-', color='green', label='Linear Regression Fit Line', markersize=10)
	plt.plot_date(dates, price2, '-', color='blue', label='Quardatic Regression Fit Line', markersize=10)
	plt.plot_date(dates, price3, '-', color='red', label='Cubic Regression Fit Line', markersize=10)
	plt.plot_date(x, y, '.', color='black', markersize=10)
	ax.xaxis.set_major_locator(loc)
	ax.xaxis.set_major_formatter(formatter)
	ax.xaxis.set_label("Date")
	ax.yaxis.set_label("Price")
	labels = ax.get_xticklabels()

	plt.setp(labels, rotation=45, fontsize=12)

	qstn = raw_input("Enter date? (y/n):: ")
	if qstn == 'y':
		yr = int(raw_input("Enter Date (YYYY):: "))
		mnt = int(raw_input("Enter Date (MM):: "))
		day = int(raw_input("Enter Date (DD):: "))

		date_x = date2num(datetime.date(yr, mnt, day))

		price_x1 = X*date_x + Y 	# for linear regression uncomment this line
		price_x2 = p + q*date_x + r*date_x*date_x	# for quadratic regression uncomment this line
		price_x3 = a + b*date_x + c*date_x*date_x + d*date_x*date_x*date_x # for cubic regression uncomment this line

		avg_price = (price_x1 + price_x2 + price_x3) / 3

		print "\nLinear Regression predicted price of %s on %s is %f.\n" % (str(data).replace("dataset.",''), str(num2date(date_x))[:10], price_x1)
		print "\nQuardatic Regression predicted price of %s on %s is %f.\n" % (str(data).replace("dataset.",''), str(num2date(date_x))[:10], price_x2)
		print "\nCubic Regression predicted price of %s on %s is %f.\n" % (str(data).replace("dataset.",''), str(num2date(date_x))[:10], price_x3)
		print "\nAverage predicted price of %s on %s is %f.\n" % (str(data).replace("dataset.",''), str(num2date(date_x))[:10], avg_price)

		plt.plot_date(date_x, price_x1, 'o', color='green', markersize=10)
		plt.plot_date(date_x, price_x2, 'o', color='blue', markersize=10)
		plt.plot_date(date_x, price_x3, 'o', color='red', markersize=10)
		plt.plot_date(date_x, avg_price, '*', color='violet', markersize=10)

		plt.show()
	else:
		plt.show()

def options():
	choice = int(raw_input("\nView regression model of \n1. Cress_Leaf\t\t 2. Tofu\t\t 3. Papaya\t\t \n4. Clive_Green\t\t 5. Pumpkin\t\t 6. Pineapple\t\t \n7. Fish_Fresh\t\t 8. Potato_Red\t\t 9. Chilli_Dry\t\t \n10. Snake_Gourd\t\t 11. Cabbage\t\t 12. Orange\t\t \n13. Green_Peas\t\t 14. Asparagus\t\t 15. Spinach_Leaf\t\t \n16. Banana\t\t 17. Smooth_Gourd\t\t 18. Arum\t\t \n19. Tomato_Small\t\t 20. Sweet_Orange\t\t 21. Onion_Dry\t\t \n22. Jack_Fruit\t\t 23. Sword_Bean\t\t 24. Parseley\t\t \n25. Okara\t\t 26. Carrot\t\t 27. French_Bean\t\t \n28. Potato_White\t\t 29. Sponge_Gourd\t\t 30. Soyabean_Green\t\t \n31. Brocauli\t\t 32. Garlic_Dry_Chinese\t\t 33. Bauhania_flower\t\t \n34. Drumstick\t\t 35. Sugarcane\t\t 36. Pointed_Gourd\t\t \n37. Brinjal_Round\t\t 38. Raddish_Red\t\t 39. Coriander_Green\t\t \n40. Tomato_Big\t\t 41. Bakula\t\t 42. Mango\t\t \n43. Squash\t\t 44. Apple\t\t 45. Mushroom\t\t \n46. Capsicum\t\t 47. Christophine\t\t 48. Sweet_Potato\t\t \n49. Mint\t\t 50. Fennel_Leaf\t\t 51. Barela\t\t \n52. Raddish_White\t\t 53. Sweet_Lime\t\t 54. Guava\t\t \n55. Cauli_Terai\t\t 56. Pear\t\t 57. Bamboo_Shoot\t\t \n58. Lettuce\t\t 59. Ginger\t\t 60. Cow_pea\t\t \n61. Grapes\t\t 62. Kinnow\t\t 63. Lemon\t\t \n64. Turnip_A\t\t 65. Knolkhol\t\t 66. Maize\t\t \n67. Cucumber\t\t 68. Celery\t\t 69. Yam\t\t \n70. Strawberry\t\t 71. Mombin\t\t 72. Turnip\t\t \n73. Tamarind\t\t 74. Onion_Green\t\t 75. Cauli_Local\t\t \n76. Garlic_Dry_Nepali\t\t 77. Litchi\t\t 78. Chilli_Green\t\t \n79. Mustard_Leaf\t\t 80. Mandarin\t\t 81. Lime\t\t \n82. Pomegranate\t\t 83. Gundruk\t\t 84. Red_Cabbbage\t\t \n85. Clive_Dry\t\t 86. Fenugreek_Leaf\t\t 87. Brinjal_Long\t\t \n88. Bottle_Gourd\t\t 89. Sugarbeet\t\t 90. Garlic_Green\t\t \n91. Neuro\t\t 92. Bitter_Gourd\t\t 93. Water_Melon\t\t \n94. Brd_Leaf_Mustard\n\nEnter your choice:: "))

	if choice == 1: main(Cress_Leaf)

	elif choice == 2: main(Tofu)

	elif choice == 3: main(Papaya)

	elif choice == 4: main(Clive_Green)

	elif choice == 5: main(Pumpkin)

	elif choice == 6: main(Pineapple)

	elif choice == 7: main(Fish_Fresh)

	elif choice == 8: main(Potato_Red)

	elif choice == 9: main(Chilli_Dry)

	elif choice == 10: main(Snake_Gourd)

	elif choice == 11: main(Cabbage)

	elif choice == 12: main(Orange)

	elif choice == 13: main(Green_Peas)

	elif choice == 14: main(Asparagus)

	elif choice == 15: main(Spinach_Leaf)

	elif choice == 16: main(Banana)

	elif choice == 17: main(Smooth_Gourd)

	elif choice == 18: main(Arum)

	elif choice == 19: main(Tomato_Small)

	elif choice == 20: main(Sweet_Orange)

	elif choice == 21: main(Onion_Dry)

	elif choice == 22: main(Jack_Fruit)

	elif choice == 23: main(Sword_Bean)

	elif choice == 24: main(Parseley)

	elif choice == 25: main(Okara)

	elif choice == 26: main(Carrot)

	elif choice == 27: main(French_Bean)

	elif choice == 28: main(Potato_White)

	elif choice == 29: main(Sponge_Gourd)

	elif choice == 30: main(Soyabean_Green)

	elif choice == 31: main(Brocauli)

	elif choice == 32: main(Garlic_Dry_Chinese)

	elif choice == 33: main(Bauhania_flower)

	elif choice == 34: main(Drumstick)

	elif choice == 35: main(Sugarcane)

	elif choice == 36: main(Pointed_Gourd)

	elif choice == 37: main(Brinjal_Round)

	elif choice == 38: main(Raddish_Red)

	elif choice == 39: main(Coriander_Green)

	elif choice == 40: main(Tomato_Big)

	elif choice == 41: main(Bakula)

	elif choice == 42: main(Mango)

	elif choice == 43: main(Squash)

	elif choice == 44: main(Apple)

	elif choice == 45: main(Mushroom)

	elif choice == 46: main(Capsicum)

	elif choice == 47: main(Christophine)

	elif choice == 48: main(Sweet_Potato)

	elif choice == 49: main(Mint)

	elif choice == 50: main(Fennel_Leaf)

	elif choice == 51: main(Barela)

	elif choice == 52: main(Raddish_White)

	elif choice == 53: main(Sweet_Lime)

	elif choice == 54: main(Guava)

	elif choice == 55: main(Cauli_Terai)

	elif choice == 56: main(Pear)

	elif choice == 57: main(Bamboo_Shoot)

	elif choice == 58: main(Lettuce)

	elif choice == 59: main(Ginger)

	elif choice == 60: main(Cow_pea)

	elif choice == 61: main(Grapes)

	elif choice == 62: main(Kinnow)

	elif choice == 63: main(Lemon)

	elif choice == 64: main(Turnip_A)

	elif choice == 65: main(Knolkhol)

	elif choice == 66: main(Maize)

	elif choice == 67: main(Cucumber)

	elif choice == 68: main(Celery)

	elif choice == 69: main(Yam)

	elif choice == 70: main(Strawberry)

	elif choice == 71: main(Mombin)

	elif choice == 72: main(Turnip)

	elif choice == 73: main(Tamarind)

	elif choice == 74: main(Onion_Green)

	elif choice == 75: main(Cauli_Local)

	elif choice == 76: main(Garlic_Dry_Nepali)

	elif choice == 77: main(Litchi)

	elif choice == 78: main(Chilli_Green)

	elif choice == 79: main(Mustard_Leaf)

	elif choice == 80: main(Mandarin)

	elif choice == 81: main(Lime)

	elif choice == 82: main(Pomegranate)

	elif choice == 83: main(Gundruk)

	elif choice == 84: main(Red_Cabbbage)

	elif choice == 85: main(Clive_Dry)

	elif choice == 86: main(Fenugreek_Leaf)

	elif choice == 87: main(Brinjal_Long)

	elif choice == 88: main(Bottle_Gourd)

	elif choice == 89: main(Sugarbeet)

	elif choice == 90: main(Garlic_Green)

	elif choice == 91: main(Neuro)

	elif choice == 92: main(Bitter_Gourd)

	elif choice == 93: main(Water_Melon)

	elif choice == 94: main(Brd_Leaf_Mustard)



if __name__ == '__main__':
	options()
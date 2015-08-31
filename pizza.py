#pizza.py

#This program will compute the cost per squae inch of a pizza.

import math

def main():
  print("This program will calculate the cost per square inch of a pizza.")

  d = input ("Enter the diameter of the pizza: ")
  price = input ("Enter the price of a the pizza: ")

  area = math.pi * (d/2)**2

  price_per_area = price / area

  print("The price of the pizza per square inch is $" + str("%.2f" % price_per_area))

main()

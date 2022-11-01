#Authors: Peter Nguyen
#Assignment: Lab #8
#Completed (or last revision): 10/28/2022
from statistics import *

#put first variable into one list and the other into another and then zip them
userInput = input("Please enter the file you would like to open: ")
#task 1
try:
     #task 2
     city_name = []
     rain_fall_data_in_cm = []
     tuple = ()
     k = 0
     file = open(userInput, 'r')
     for line in file:
          oneLine = line.split()
          city_name.append(oneLine[0])
          rain_fall_data_in_cm.append(oneLine[1])
     file.close()
     rain_fall_data_in_inches = [float(i) for i in rain_fall_data_in_cm]
     entries = len(rain_fall_data_in_inches)
     
     
     #finding which city is the biggest using variables that can help find to locate
     smallestCM = min(rain_fall_data_in_cm)
     rain_fall_data_in_cmLENGTH = len(rain_fall_data_in_cm)
     for i in range(rain_fall_data_in_cmLENGTH):
          if smallestCM == rain_fall_data_in_cm[i]:
               smallestNumber = i   
     biggestCM = max(rain_fall_data_in_cm)
     for i in range(rain_fall_data_in_cmLENGTH):
          if biggestCM == rain_fall_data_in_cm[i]:
               biggestNumber = i
     

     
     
     
     
     #calculations for task 3
     for i in range(entries):
          rain_fall_data_in_inches[i] = rain_fall_data_in_inches[i] / 2.53
     tupleList = list(zip(city_name, rain_fall_data_in_inches))
     average = str(mean(rain_fall_data_in_inches))
     maximum = str(max(tupleList))
     minimum = str(min(tupleList))
     tupleList = list(zip(city_name, rain_fall_data_in_inches))
     rain_fall_data_in_inches = [str(i) for i in rain_fall_data_in_inches]
     str(average)
     str(maximum)
     str(minimum)
     
     
     

     #outputting for task 4
     outputFile = open('data.txt', 'w')
     for j in range(entries):
          outputFile.write(city_name[j])
          outputFile.write(', ')
          outputFile.write(rain_fall_data_in_inches[j])
          outputFile.write(" inches of rainfall.\n")
     outputFile.write("The average amount of rainfall is ")
     outputFile.write(average)
     outputFile.write(" inches.\n")
     outputFile.write("The maximum amount of rainfall is ")
     outputFile.write(rain_fall_data_in_inches[biggestNumber])
     outputFile.write(" inches in the city of ")
     outputFile.write(city_name[biggestNumber])
     outputFile.write("\n")
     outputFile.write("The minimum amount of rainfall is ")
     outputFile.write(rain_fall_data_in_inches[smallestNumber])
     outputFile.write(" inches in the city of ")
     outputFile.write(city_name[smallestNumber])
     print("Process Completed! Please see the new file!")
except FileNotFoundError:
     print("The file does not exist.")
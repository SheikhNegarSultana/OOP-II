a = int(input('Check The Number : ')) 

if (a%400 == 0) or (a%100 != 0 and a%4 == 0):   
    print("Leap Year! :) ")   
     
else:   
 print("Not A Leap Year! :( ")  
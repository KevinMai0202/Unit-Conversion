# Unit-Conversion
Unit Conversion
[Unit Conversion.pdf](https://github.com/KevinMai0202/Unit-Conversion/files/15355272/Unit.Conversion.pdf)


Communication Contract

UML diagram
![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/8a35c89a-1ce8-454f-8903-51b486de8639)
![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/d6674a6a-e89c-45b4-b2c7-af991a50b62e)

The program is communicated through text file Json, similar to the first assignment of microservices warm up. 
After running all the microservice programs and main program.
The main program will display a list menu of what program can convert. The user interface allows a user to input their value in the command line.  

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/b7a21ac3-e6e3-4211-a15d-dbdfdf64b4ba)

Other microservice programs are constantly reading in the background, waiting for value entered in the input txt file. 
First, the main program prompts the user to select the type of unit conversion.
Invalid selection will alert user invalid input and back to menu to prompt user to re-enter again.

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/19a26162-fcf7-4308-a5e6-525799f9a343)

After accepting the unit conversion, then prompt user to enter the numeric value they want to convert.

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/06a79c3a-0d71-4c5b-905c-22f96a2f2f16)

Invalid input will alert the user, return to menu, and prompt user to restart the process.

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/ddd507f8-e0ed-4208-a44c-fce3c1431885)

After accepting the value, it will write the value in the input txt file, other programs will be constantly reading, after reading the input txt file, it will call the microservice program to do the calculation and conversion, write the calculation result on the output txt file. Then the main program opens and reads the output txt file, and finally the main program will display the result. And the process repeats. 

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/7c367901-e4b7-41c6-b350-cdb984883bb1)

For example, after the user enters a valid input, it will write the value in the input txt file (height_input.txt), in this example is 100.

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/735e382f-bf81-4798-b3fb-db2445732ff4)

Making the request to convert the value 100. The height program that is constantly listening in the background, receives and reads the data from height_input.txt, then it calls height function to convert cm to inches. It will calculate 100 * 0.393701 = 39.37. After conversion, it will write the result (39.27) in output txt file (height_output.txt).

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/839a875e-b8b2-4c3c-a096-bff9eebdc9ee)

The main program reads the output txt file (height_output.txt), grabs the result and displays it. 

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/b8db56f0-297d-4f1f-9956-c0a70b24b65f)


![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/57b6b82b-83dd-49ed-91c1-b4ed099afcae)

Another example for weight conversion, after the user enters valid input, it will write the value in the input txt file (weight_input.txt), in this example is 1000. 

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/627ed01a-3451-4393-a28d-e2f6e00d0366)

Making the request to convert the value 1000. The weight program that is constantly listening in the background, receives and reads the data from weight_input.txt, then it calls the weight function to convert grams to pounds and ounces. It will calculate 1000 * 0.00220462 = 2.20 for pounds; then it calculates 1000 * 0.035274 = 35.27 for ounces. After conversion, it will write both results (2.20462 pounds and 35.277 ounces) in output txt file (weight_output.txt file).

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/a215d3b6-e950-4cd2-8d03-d61886b6b124)

The main program reads the output txt file (weight_output.txt), grabs the result and displays it.

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/db3186c5-e3ad-4959-8cc9-5350dade8aa7)

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/8cd22a88-6005-49e7-b302-6932e7ba0b28)

For example, after the user enters valid input, it will write the value in the input txt file (temperature_input.txt), in this example is 18 Celsius degrees. 

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/0ceaa261-02cc-4391-819d-c5f4905a151f)

Making the request to convert the value 18. The temperature program that is constantly listening in the background, receives and reads the data from temperature_input.txt, then it calls temperature function to convert Celsius to Fahrenheit. It will calculate 18 * 9 / 5 + 32 = 64.40. After conversion, it will write the result (64.40) in output txt file (temperature_output.txt).

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/fb5b3c03-54e9-47c1-91f6-18808bf25367)

The main program reads the output txt file (temperature_output.txt), grabs the result and displays it. 

![image](https://github.com/KevinMai0202/Unit-Conversion/assets/129697366/0b0d2176-a6e7-4d72-bb69-76d56a19fd3e)














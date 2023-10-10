# CS104
# Anthony Mendes
# conditions.py

valid_input = False

while not valid_input:
    temp = input("Please enter the current temperature: ")

    if temp.isdigit():  # Check if the input is a positive integer
        temp = int(temp)

        if temp > 90:
            print("Wear Shorts")
        elif temp > 70:
            print("Short sleeves are fine")
        elif temp > 50:
            print("Wear a jacket")
        elif temp > 32:
            print("Wear a heavy coat")
        else:
            print("Stay Inside")

        valid_input = True
    else:
        print("Invalid input. Please enter a valid temperature as an integer.")


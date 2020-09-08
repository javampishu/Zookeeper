# Save the input in this variable
ticket = int(input())
digit1 = ticket // 100000
ticket = ticket % 100000
digit2 = ticket // 10000
ticket = ticket % 10000
digit3 = ticket // 1000
ticket = ticket % 1000
digit4 = ticket // 100
ticket = ticket % 100
digit5 = ticket // 10
ticket = ticket % 10
digit6 = ticket
# Add up the digits for each half
half1 = digit1 + digit2 + digit3
half2 = digit4 + digit5 + digit6

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")

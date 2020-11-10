while True:
    try:
        num = int(input("Enter month number : "))
        break
    except:
        print("Invalid input")

if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("Month is March")
elif num == 4:
    print("Month is April")
elif num == 5:
    print("Month is May")
elif num == 6:
    print("Month is June")
elif num == 7:
    print("Month is July")
elif num == 8:
    print("Month is August")
elif num == 9:
    print("Month is September")
elif num == 10:
    print("Month is October")
elif num == 11:
    print("Month is November")
elif num == 12:
    print("Month is December")
else:
    print('Invalid number')

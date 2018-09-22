weeklyhours = int(input("How many hours do you work a week? > "))
pay = int(input("What is you hourly rate of pay?(£) > "))
weeklyrate = weeklyhours*pay
daylyrate = weeklyrate/5
daylyhours = weeklyhours/5
yearlyrate= weeklyrate*56
monthlyhours = weeklyhours*4
if weeklyhours > 40 and monthlyhours < 60:
    newmonth = monthlyhours - 40
    fourtyhours = 40*pay
    newpay = pay*1.5
    bonus = newmonth*newpay
    total1 = fourtyhours+bonus
    print("You earn £", daylyrate, "a day")
    print("You earn £", yearlyrate, "a year")
    print("you work ", daylyhours, " hours a day")
    print("You worked", monthlyhours, " hours this month")
    print("You were payed", total1, "this month")
elif weeklyhours < 40:
    total2 = monthlyhours*pay
    print("You earn £", daylyrate, "a day")
    print("You earn £", yearlyrate, "a year")
    print("you work ", daylyhours, " hours a day")
    print("You worked", monthlyhours, " hours this month")
    print("You were payed £", total2, "this month")
elif weeklyhours > 60:
    print("ERROR\nPossible reasons:\nData entered incorrectly\nYou work too much!")

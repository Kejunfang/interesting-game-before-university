import calendar

def display_calendar(year,month):
    cal= calendar.month(year,month)
    print("Calendar")
    print(cal)

def main():
    print("welcome to use simple calendar!")
    year=int(input("Please input a year:"))
    month=int(input("Please input a month:"))
    print(display_calendar(year,month))

if __name__ == "__main__":
    print(main())
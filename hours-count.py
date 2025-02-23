from datetime import datetime, timedelta


# polskie dni wolne od pracy 2025
polish_holidays = [
    "01.01.2025",  # nowy rok
    "06.01.2025",  # trzech kroli
    "20.04.2025",  # wielkanoc
    "21.04.2025",  # wielkanoc 2 
    "01.05.2025",  # swieto pracy
    "03.05.2025",  # 3 maja
    "19.06.2025",  # boze cialo
    "15.08.2025",  # wniebowziecie nmp
    "01.11.2025",  # wszystkich swietych 
    "11.11.2025",  # swieto niepodleglosci
    "25.12.2025",  # boze narodzenie 1 dzien
    "26.12.2025"  # boze narodzenie 2 dzien
]


holidays = [datetime.strptime(date, "%d.%m.%Y") for date in polish_holidays]


start_date_str = input("Enter start date (dd.mm.yyyy): ")
end_date_str = input("Enter end date (dd.mm.yyyy): ")

start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
end_date = datetime.strptime(end_date_str, "%d.%m.%Y")

missed_days = 0
current_date = start_date

while current_date <= end_date:
    
    if current_date.weekday() in (5, 6) or current_date in holidays:
        missed_days += 1
        print(f"{current_date.strftime('%d.%m.%Y')} dzien wolny")
    current_date += timedelta(days=1)


extra_missed_days = int(input("Enter out of office days: "))
missed_days += extra_missed_days  
rate = float(input("Enter rate: "))
daily_pay = rate * 8  


total_days = (end_date - start_date).days + 1  
work_days = total_days - missed_days  
total_hours = work_days * 8
total_pay = total_hours * rate


print("\n--- podsumowanie miesiaca ---")
print("dni:", total_days)
print("dni wolne (weekendy + swieta):", missed_days)
print("przepracowane dni:", work_days)
print("przepracowane godziny:", total_hours)
print("wyplata:", total_pay)

##TODO editing pdf file with output data
##TODO send email with output data?!?!

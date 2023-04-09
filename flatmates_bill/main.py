from flat import Bill, Flatmate
from report import PdfReport

# Input names
first_flatmate = input('Name of the first flatmate: ')
second_flatmate = input('Name of the second flatmate: ')

# Input amounts of days
first_flatmate_days = int(input('Days of the first flatmate: '))
second_flatmate_days = int(input('Days of the second flatmate: '))

# Input price and period
price = float(input('Total of the bill for the month: '))
period = input('Month: ')

bill = Bill(amount=price, period=f'{period}')
first_flatmate_obj = Flatmate(name=f'{first_flatmate}', days_in_house=first_flatmate_days)
second_flatmate_obj = Flatmate(name=f'{second_flatmate}', days_in_house=second_flatmate_days)

pdf_report = PdfReport(filename=f'{bill.period}.pdf')
pdf_report.generate(flatmate1=first_flatmate_obj, flatmate2=second_flatmate_obj, flatmates_bill=bill)

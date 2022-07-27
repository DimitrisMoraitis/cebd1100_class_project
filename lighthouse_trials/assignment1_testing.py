from decimal import Decimal
import csv
import datetime                         # to produce date on report
this_file = '50000_Sales_Records.csv'   # enter csv path here in quotations

# verifying file is error free
with open(this_file) as file_object:
    report = file_object.readable()
    if report:
        print("\n*** Your File has no errors ***\n")
    else:
        print("\n*** Your File has errors and cannot open ***\n")

# setting up to read csv file, remove header and give today's date
    next(file_object)
    report = csv.reader(file_object)
    day = datetime.date.today()

# Identifying regions analyzed
    regions = set()
    for row in report:
        region = row[0]
        regions.add(region)

# Getting grand totals
with open(this_file) as file_object:
    report = csv.DictReader(file_object)

    total_units = 0
    total_revenues = 0
    for txt in report:
        if txt['Units Sold'] != "":
            total_units += int(txt['Units Sold'])

        if txt['Total Revenue'] != "":
            total_revenues += Decimal(txt['Total Revenue'])

    average_revenue = Decimal(total_revenues / total_units)

# Final sales data report
print("\tSales report\t\n\t------------\t")
print(f"\t{day}\t\n")
print(f"Regions Analyzed: {regions}\nTotal regions: {len(regions)}")
print(f"\nTotal units sold: {total_units}")
print(f"Average revenue per unit: ${average_revenue:.2f}")
print(f"Total revenue of sales: ${total_revenues:.2f}")

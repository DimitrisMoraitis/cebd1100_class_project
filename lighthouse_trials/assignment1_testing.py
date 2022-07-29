from decimal import Decimal
import csv
import datetime                         # to produce date on report
this_file = '100_sales_recs.csv'   # enter csv path here in quotations

# Identifying regions analyzed
with open(this_file) as file_object:
    next(file_object)
    report = csv.reader(file_object)

    regions = set()
    for row in report:
        region = row[0]
        regions.add(region)

regions = list(regions)
regions.sort()

with open(this_file) as file_object:
    next(file_object)
    report = csv.reader(file_object)

    i = 0
    name_units = 0
    name_revenue = 0
    name_average = 0

    for i in range(len(regions)):
        for row in report:
            if row[0] == regions[i]:
                name_units += Decimal(row[8])
                name_revenue += Decimal(row[11])
                name_average = Decimal(name_revenue / name_units)

        print(regions[i])
        print(name_units)
        print(name_revenue)
        print(name_average)

# Getting grand totals
# with open(this_file) as file_object:
#     report = csv.DictReader(file_object)
#
#     total_units = 0
#     total_revenues = 0
#     for txt in report:
#         if txt['Units Sold'] != "":
#             total_units += int(txt['Units Sold'])
#
#         if txt['Total Revenue'] != "":
#             total_revenues += Decimal(txt['Total Revenue'])
#
#     average_revenue = Decimal(total_revenues / total_units)
#
# # Final sales data report
# print("\tSales report\t\n\t------------\t")
# print(f"\t{day}\t\n")
# print(f"Regions Analyzed: {regions}\nTotal regions: {len(regions)}")
# print(f"\nTotal units sold: {total_units}")
# print(f"Average revenue per unit: ${average_revenue:.2f}")
# print(f"Total revenue of sales: ${total_revenues:.2f}")

from decimal import Decimal
FEDERAL_TAX = Decimal("0.06")
QC_TAX = Decimal('0.13')

meal_price = Decimal('44.50')
meal_price2 = Decimal('100.95')

total_price = (meal_price * FEDERAL_TAX) + (meal_price * QC_TAX) + meal_price
total_price2 = (meal_price2 * FEDERAL_TAX) + (meal_price2 * QC_TAX) + meal_price2

print(total_price)
print(total_price2)

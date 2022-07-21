# senior_count = 0
# junior_count = 0
#
# with open('employees.txt') as file_object:
# #     contents = file_object.read()
# #     print(contents)
#
#     for ln in file_object:
#         # print(ln.strip())
#         # print(ln[49:54])
#
#         if ln[50:54] == "TRUE":
#             senior_count += 1
#         if ln[49:54] == "FALSE":
#             junior_count += 1
# print(f"Senior employees: {senior_count}")
# print(f"Junior employees: {junior_count}")

# double_digit = 0
# single_digit = 0
#
# with open('employees.txt') as file_object:
#     for ln in file_object:
#
#         if float(ln[42:48]) >= 9.999:
#             double_digit += 1
#
#         if float(ln[42:48]) < 9.999:
#             single_digit += 1
#
# print(f" Double digit bonuses given to {double_digit} employees")
# print(f" Single digit bonuses given to {single_digit} employees")

# with open('employees.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

with open('employees.txt') as file_object:
    contents = file_object.readable()
    if contents:
        print("Your File is readable")
    else:
        print("Your File is not readable")

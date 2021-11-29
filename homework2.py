def bank(a, years, percents= 10):
    for year in range(years):
        a = a*(percents/100)+a 
    return "%.2f" % a
a = int(input("Enter sum of vklad: "))
years = int(input("Enter years: "))
print(bank(a, years))
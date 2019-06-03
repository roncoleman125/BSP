AVG_LIFETIME_SALARY = 151204.0
EXPENSE = 552000.0
EXPECTED_YEARS_WORKING = 40.0

MARGINAL_TAX_RATES = [0.20, 0.15, 0.10 ]

print("Grads", end=' ')
for tax_rate in MARGINAL_TAX_RATES:
    print("%4.2f " % tax_rate, end=" ")

print("")

for num in range(31,0,-1):
    print("%d" % num, end=" ")
    for tax_rate in MARGINAL_TAX_RATES:
        income = AVG_LIFETIME_SALARY * tax_rate * EXPECTED_YEARS_WORKING * num

        cagr = (income / EXPENSE) ** (1 / 46.) - 1

        print('%f ' % (cagr), end=' ')

    print(" ")
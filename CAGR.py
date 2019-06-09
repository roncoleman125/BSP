# This program computes a table of CAGR for Marist College first S-STEM award.
# See the unpublished paper, Coleman, R., et al, "Outcomes and Lessons from S-STEM Program", unpublished, 5 Sep 2014
STARTING_SALARY = 70000.

WORKING_YEARS = 40.0

SALARY_CAGR = 0.03

NSF_GRANT = 552000.0

NSF_OVERHEAD = 0.058

TERMINAL_SALARY = STARTING_SALARY * (1.0 + SALARY_CAGR ) ** WORKING_YEARS

AVG_LIFETIME_SALARY = (STARTING_SALARY + TERMINAL_SALARY) / 2

BEGINNING_VALUE = NSF_GRANT * (1 + NSF_OVERHEAD)

DELAY = 1 + 4 + 2  # 1st year plus six years to graduate

EFFECTIVE_TAX_RATES = [0.20, 0.15, 0.10]

print("Grads", end=' ')
for tax_rate in EFFECTIVE_TAX_RATES:
    print("%4.2f " % tax_rate, end=" ")

print("")

for num in range(31,0,-1):
    print("%d" % num, end=" ")
    for tax_rate in EFFECTIVE_TAX_RATES:
        ending_value = AVG_LIFETIME_SALARY * tax_rate * WORKING_YEARS * num

        cagr = (ending_value / BEGINNING_VALUE) ** (1 / (WORKING_YEARS + DELAY)) - 1

        print('%f ' % (cagr), end=' ')

    print(" ")
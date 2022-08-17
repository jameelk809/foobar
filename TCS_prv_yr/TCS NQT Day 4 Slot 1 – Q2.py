"""Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the increase in the
concentration of PMs include vehicle emission by applying Odd Even concept for all types of vehicles. The vehicles
with the odd last digit in the registration number will be allowed on roads on odd dates and those with even last
digit will on even dates. Given an integer array a[], contains the last digit of the registration number of N
vehicles traveling on date D(a positive integer). The task is to calculate the total fine collected by the traffic
police department from the vehicles violating the rules. """

veh = [2, 5, 1, 6, 8]
D = 3
fine = 200
odd = 0
even = 0
total = 0

for v in veh:
    if v % 2 != 0:
        odd += 1
    else:
        even += 1
if D % 2 == 0:
    total = fine * odd
else:
    total = fine * even
print(total)

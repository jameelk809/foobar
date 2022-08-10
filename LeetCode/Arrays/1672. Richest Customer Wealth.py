def maximumWealth(accounts):
    s = -1
    for cust in accounts:
        s_money = sum(cust)
        if s_money > s:
            s = s_money
    return s


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
print(maximumWealth(accounts))

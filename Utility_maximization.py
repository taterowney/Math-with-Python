from sympy import *


def maximize_utility(commodity_vars, U, prices, budget):
    eq_system = []
    for i in range(len(commodity_vars)-1):
        eq_system.append(Eq(diff(U, commodity_vars[i])/prices[i], diff(U, commodity_vars[i+1])/prices[i+1]))
    budget_line = 0
    for i in range(len(prices)):
        budget_line+=commodity_vars[i]*prices[i]
    eq_system.append(Eq(budget_line, budget))
    return solve(eq_system, commodity_vars)

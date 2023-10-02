import random

def gamblers_ruin(p, initial_stake=5):
    """
    Simulates the gambler's ruin problem for a given probability p.

    Returns:
    - T: Total number of bets until the gambler is ruined.
    - M: Maximal amount of money the gambler has until he is ruined.
    """
    current_stake = initial_stake
    T = 0
    M = initial_stake

    while current_stake > 0:
        if random.random() < p:
            current_stake += 1
        else:
            current_stake -= 1
        
        M = max(M, current_stake)
        T += 1

    return T, M

def monte_carlo_estimates(p, num_trials=10**5):
    total_T = 0
    total_M = 0
    count_M_geq_10 = 0

    T_values = []
    M_values = []

    for _ in range(num_trials):
        T, M = gamblers_ruin(p)
        total_T += T
        total_M += M
        T_values.append(T)
        M_values.append(M)
        
        if M >= 10:
            count_M_geq_10 += 1

    mu1 = total_T / num_trials
    mu2 = total_M / num_trials
    mu3 = count_M_geq_10 / num_trials

    # Calculate standard deviations
    std_dev_T = (sum([(t - mu1)**2 for t in T_values]) / num_trials) ** 0.5
    std_dev_M = (sum([(m - mu2)**2 for m in M_values]) / num_trials) ** 0.5

    return mu1, mu2, mu3, std_dev_T, std_dev_M

p_values = [0.4, 0.45, 0.48]
for p in p_values:
    mu1, mu2, mu3, std_dev_T, std_dev_M = monte_carlo_estimates(p)
    print(f"For p = {p}:")
    print(f"μ1(p) = {mu1:.2f}, Standard Deviation = {std_dev_T:.2f}")
    print(f"μ2(p) = {mu2:.2f}, Standard Deviation = {std_dev_M:.2f}")
    print(f"μ3(p) = {mu3:.4f}")
    print("---------")

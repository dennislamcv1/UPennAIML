import math

# Given values
p_hat = 0.12
n = 100
Z = 1.96

# Standard error
SE = math.sqrt(p_hat * (1 - p_hat) / n)

# Margin of error
ME = Z * SE

# Confidence interval
lower_bound = p_hat - ME
upper_bound = p_hat + ME

print(lower_bound, upper_bound)

# Given values
p_hat_2 = 0.18
n_2 = 200

# Standard error
SE_2 = math.sqrt(p_hat_2 * (1 - p_hat_2) / n_2)

print(SE_2)

# Given values
p_hat_1 = 0.12
p_hat_2 = 0.18
n_1 = 100
n_2 = 200

# Variance
variance_d = (p_hat_1 * (1 - p_hat_1) / n_1) + (p_hat_2 * (1 - p_hat_2) / n_2)

# Standard error
SE_d = math.sqrt(variance_d)

print(variance_d, SE_d)


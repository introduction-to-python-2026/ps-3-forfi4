def approximate_pi(n_terms):
    if n_terms <= 0:
        return 0.0

    total_sum = 0.0
    
    for n in range(n_terms):
        numerator = (-1)**n
        
        denominator = 2 * n + 1
        total_sum += numerator / denominator

    return 4 * total_sum
print(f"approximate_pi(10):   {approximate_pi(10)}")
print(f"approximate_pi(100):  {approximate_pi(100)}")
print(f"approximate_pi(1000): {approximate_pi(1000)}")
print(f"approximate_pi(1):    {approximate_pi(1)}") # Should be 4 * (1/1) = 4.0
print(f"approximate_pi(2):    {approximate_pi(2)}") # Should be 4 * (1/1 - 1/3) = ~2.667

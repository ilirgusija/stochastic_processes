import numpy as np

def find_invariant_distribution(P):
    # Adjust the matrix to solve (P^T - I)pi = 0
    A = np.transpose(P) - np.eye(len(P))
    
    # Replace the last row with the condition sum(pi) = 1
    A[-1, :] = 1
    
    # Create a target vector with 0s and a 1 at the end
    b = np.zeros(len(P))
    b[-1] = 1
    
    # Solve the linear system
    pi = np.linalg.solve(A, b)
    return pi

# Example usage
P = np.array([
    [11.0/20.0, 9.0/40.0,   9.0/40.0,   0.0,        0.0,        0.0],
    [11.0/20.0, 9.0/40.0,   0.0,        0.0,        9.0/40.0,   0.0],
    [11.0/20.0, 0.0,        9.0/40.0,   9.0/40.0,   0.0,        0.0],
    [1.0/10.0,  0.0,        9.0/40.0,   9.0/40.0,   0.0,        9.0/20.0],
    [1.0/10.0,  9.0/40.0,   0.0,        0.0,        9.0/40.0,   9.0/20.0],
    [1.0/10.0,  0.0,        0.0,        9.0/40.0,   9.0/40.0,   9.0/20.0],
])
# P = np.array([
#     [0.5, 0.25, 0.25],
#     [0.33333333, 0.33333333, 0.33333333],
#     [0.25, 0.25, 0.5]
# ])
invariant_distribution = find_invariant_distribution(P)
print("Invariant Distribution:", invariant_distribution)

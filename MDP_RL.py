import numpy as np

# Define the state and action spaces
states = [1, 2, 3]
actions = [1, 2]

# Define the policy mu
mu = {1: 1, 2: 2, 3: 1}

# Define the transition matrices for the actions (to be filled in with your values)
P = {
    1: np.array([[0.5, 0.25, 0.25],   # Transition matrix when action 1 is taken
                 [0.25, 0.5, 0.25],
                 [0.25, 0.25, 0.5]]),
    2: np.array([[1.0/3.0, 1.0/3.0, 1.0/3.0],   # Transition matrix when action 2 is taken
                 [1.0/3.0, 1.0/3.0, 1.0/3.0],
                 [1.0/3.0, 1.0/3.0, 1.0/3.0]])
}

# Define the cost function c(s, u)
def cost(s, u):
    return s * u

# Define gamma
gamma = 0.8

# Initialize the matrix P^mu and vector C
P_mu = np.zeros((len(states), len(states)))
P_mu = np.array([P[mu[s]][s - 1] for s in states])
C = np.zeros(len(states))

# Fill in the entries of P^mu and C based on the policy
for i in states:
    C[i - 1] = cost(i, mu[i])
    P_mu[i - 1] = P[mu[i]][i - 1]

# Now we solve for J^mu using linear algebra
# J^mu = C + gamma * P^mu * J^mu
# (I - gamma * P^mu) * J^mu = C
# J^mu = inv(I - gamma * P^mu) * C
I = np.eye(len(states)) # Identity matrix
J_mu = np.linalg.inv(I - gamma * P_mu).dot(C)

print("C:", C)
print("P^mu:", P_mu)
print("J^mu:", J_mu)

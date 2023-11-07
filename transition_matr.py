import numpy as np

# Define the transition matrix P
P = np.array([
    [1/4,  0,   1/4,  0,   0,   0  ],
    [0,   1/2,  0,   1/4,  0,   0  ],
    [1/4,  0,   1/2,  0,   1/4,  0  ],
    [0,   1/4,  0,   1/2,  0,   1/4],
    [0,    0,   1/4,  0,   1/2,  0  ],
    [0,    0,    0,   1/4, 0,   1/4]
])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(P)

# The eigenpairs
eigenpairs = [(eigenvalues[i], eigenvectors[:, i]) for i in range(len(eigenvalues))]

eigenpairs

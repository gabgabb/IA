import numpy as np
x = np.random.rand(500) * 5
print(f'first few values {x[:5]}')
print(f'minimum hours studied {x.min()}, maximum hours studied {x.max()}')
print(f'mean hours studied {x.mean()}')
print(f'standard deviation of hours studied {x.std()}')

y= ((3 * x + 3) + np.random.randn(len(x)) * 2.5).clip(0, 20)
print(f'minimum grade {y.min()}')
print(f'maximum grade {y.max()}')
print(f'mean grade {y.mean()}')
print(f'standard deviation of the grades {y.std()}')

import matplotlib.pyplot as plt
plt.figure(figsize = (8, 8))
plt.xlabel('Number of hours studied')
plt.ylabel('Exam grade')
plt.scatter(x, y)


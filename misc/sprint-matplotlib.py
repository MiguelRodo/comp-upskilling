import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.scatter([1, 2, 3], [4, 7, 5])
plt.show()

ages = np.array([35, 42, 29, 51])
responses = np.array([0.82, 0.65, np.nan, 0.91])


# part a
plt.figure()
plt.scatter(
  ages,
  responses
)
plt.xlabel("Age")
plt.ylabel("Response")
plt.title("Response by Age")
plt.show()

# part b
plt.figure()
bool_mask = ~np.isnan(ages) & ~np.isnan(responses)
plt.scatter(
  ages[bool_mask],
  responses[bool_mask]
)
plt.xlabel("Age")
plt.ylabel("Response")
plt.title("Response by Age")
path_fig = Path("response_by_age.png")
plt.savefig(path_fig)
plt.show()
path_fig.exists()
path_fig.resolve()

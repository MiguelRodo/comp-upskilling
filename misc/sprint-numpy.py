import numpy as np

x = np.array([1, 2, 3])
print(x * 2)

# part a

ages = np.array([35, 42, 29, 51])
responses = np.array([0.82, 0.65, np.nan, 0.91])

ages.dtype
responses.dtype
ages.shape
responses.shape
ages.mean()
responses.mean()

responses.mean(where=~np.isnan(responses))

responses.mean(where=~np.isnan(responses))

# part b

ages[ages >= 40]
responses_ge40  = responses[ages >= 40]
responses_ge40.mean(where=~np.isnan(responses_ge40))

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression

ages = np.array([35, 42, 29, 51])
responses = np.array([0.82, 0.65, np.nan, 0.91])

bool_mask = ~np.isnan(ages) & ~np.isnan(responses)
ages_tidy = ages[bool_mask]
responses_tidy = responses[bool_mask]

y = responses_tidy
X = ages_tidy.reshape(-1, 1)

# part b
model = LinearRegression()
model.fit(X, y)
model.coef_
model.intercept_
model.predict(X)

# predictions and plotting
ages_arr_pred = np.array([30, 40]).reshape(2, 1)
pred_arr = model.predict(ages_arr_pred)
resid_arr = y - model.predict(X)

plt.figure()
plt.scatter(ages_tidy, responses_tidy)
plt.xlabel("Age")
plt.ylabel("Response")
plt.title("Response by age")

fit_arr_x = np.array([ages_tidy.min(), ages_tidy.max()])
fit_arr_y = model.predict(fit_arr_x.reshape(-1, 1))
plt.plot(fit_arr_x, fit_arr_y)

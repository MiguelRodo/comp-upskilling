import torch

torch.manual_seed(42)

z_true = torch.randn(100, 2)

W = torch.randn(2, 6)

X = z_true @ W + 0.05 * torch.randn(100, 6)

X[0]
X.shape
z_true.shape
W.shape

# A: valid because Z # cols and W # rows same, and E has same dim as # rows Z and # cols W
# B: Okaay, it's data type (I suppose I don't excatly kjnow what this is because we skipped the dataclass package exercise) is torch.float32, whereas for numpy I think it's just "base" dtype flaot64? Not sure if torch's dtype inherits from the corresponding base dtype (obviously not for differing # of bits and object types, but you get the point)
# C: X[0] I think is the first row of X, so I think that's a 1x6. Also drop a dimension, I see
# X[:, 0], is that the first column? I think that's 100x1. Okay, I see it's just 100, no other dimension, so we actually drop a dimension then
# X[0:1, :] # first two rows and all columns, so 2x6. Okay, I see it's something else

# construct the model componets
encoder = torch.nn.Sequential(
  torch.nn.Linear(6, 3),
  torch.nn.ReLU(),
  torch.nn.Linear(3, 2)
)
decoder = torch.nn.Sequential(
  torch.nn.Linear(2, 3),
  torch.nn.ReLU(),
  torch.nn.Linear(3, 6)
)

# there was no output,
# so perhaps weights were randomised?
latent = encoder(X) # 100 x 2
# so, it can take another nnet as input,
# and not simply the *x2 matrix (tensor)?
reconstructed = decoder(latent) # 100 * 6

# ah, okay, so the above is a "run"

# okay, so we're now saying that
# okay, we're taking in two stes of layers
autoencoder = torch.nn.Sequential(encoder, decoder)

loss_fn = torch.nn.MSELoss()
# so, before is Xhat (autoencoder output),
# and afterwards is what we're trying to reconstruct,
# and item is the item
loss_before = loss_fn(autoencoder(X), X).item()

# okay, so now, we're telling it we want to 
# optimise these parameters,
# but we haven't actually given it the loss function,
# what we're optimising for or what the inputs are.
# right. 
optimizer = torch.optim.Adam(
  autoencoder.parameters(),
  lr=0.01
)

for i in range(500):
  # okay, so, setting gradients to zero
  optimizer.zero_grad()

  # okay, so, we're now getting the predictions (which
  # initially are bad)
  X_hat = autoencoder(X)

  # getting the loss
  loss = loss_fn(X_hat, X)

  # okay, so, this must have the weights and the neural
  # net structure, otherwise it couldn't get the gradients
  loss.backward()

  # okay, and now adam is going to somehow know 
  # that it's supposed to take that autoencoder (which
  # it does via autoencoder.parameters(), even
  # though that only looks like it's passing part of the autoencoder),
  # and then it's going to update those parameters,
  # somehow knowing what the loss is

  optimizer.step()


optimizer.zero_grad()

# okay, so, we're now getting the predictions (which
# initially are bad)
X_hat = autoencoder(X)

# getting the loss
loss = loss_fn(X_hat, X)

# okay, so, this must have the weights and the neural
# net structure, otherwise it couldn't get the gradients
loss.backward()

loss.item()

with torch.no_grad():
  X_hat = autoencoder(X)

print(X[0])
print(X_hat[0])

X - X_hat[0]
row_mse = ((X - X_hat)**2).mean(dim = 1)
overall_mse = row_mse.mean()

# c: didn't train for long enough, also just stat error, we've got only so many parameters and 600 observations
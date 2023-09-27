# %%
import numpy as np

# %%
def gini(x):

    # Mean absolute difference
# %%
 # Mean absolute difference
x = np.array([1,1,2,2.1])
# all numbers have to positive?
mad = np.abs(np.subtract.outer(x, x)).mean()
rmad = mad/np.mean(x)
print(rmad/2)
# %%
np.subtract.outer(x, x)
# %%
np.abs(np.subtract.outer(x, x))
# %%
np.abs(np.subtract.outer(x, x)).mean()
# %%
np.mean([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
# %%
u = np.mean(x)
# %%
np.abs(x-u)
# %%
np.mean(np.abs(x-u))
# %%
# same response
mad * .5
# %%

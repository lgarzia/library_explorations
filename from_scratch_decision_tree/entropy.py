# %%
from math import log2

p = .1 # 0.5 --> 1 bit
h = -log2(p)
print('p(x)=%.3f, information: %.3f bits' % (p, h))
# %%
# calculate the entropy for a dice roll
from math import log2

n = 6
p = 1.0 /n
entropy = -sum([p * log2(p) for _ in range(n)])
print('entropy: %.3f bits' % entropy)
# %%

import numpy as np
import pysal

c = np.array([['b','a','c'],['c','c','a'],['c','b','c'],['a','a','b'],['a','b','c']])
print(c)

m = pysal.Markov(c)
print(m.classes)

print(m.transitions)
#################################################################Classic Markov
f = pysal.open(r'C:\Anaconda\Lib\site-packages\pysal\examples\us_income\usjoin.csv')
pci = np.array([f.by_col[str(y)] for y in range(1929,2010)])
print(pci.shape)
print(pci)

q5 = np.array([pysal.Quantiles(y).yb for y in pci]).transpose()
print(q5.shape)
print(q5[:,0])
print(q5[4,:])

m5 = pysal.Markov(q5)
print(m5.transitions)

print(m5.p)

print(m5.steady_state)

print(pysal.ergodic.fmpt(m5.p))
################################################################# Spatial Markov
fpci = pci.transpose()/(pci.transpose().mean(axis=0))
print(fpci)

w = pysal.open(r'C:\Anaconda\Lib\site-packages\pysal\examples\us_income\states48.gal').read()
w.transform = 'r'
sm = pysal.Spatial_Markov(fpci, w, fixed=True, k=5)
for p in sm.p:
    print(p)

for f in sm.F:
    print(f)
################################################################# LISA Markov
lm = pysal.LISA_Markov(pci.transpose(),w)
print(lm.classes)

# the estimated transition probability matrix
print(lm.transitions)
print(lm.p)
print(lm.steady_state)
print(pysal.ergodic.fmpt(lm.p))

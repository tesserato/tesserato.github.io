import keras as K
import numpy as np
from Hlib import save_wav, create_signal

def scaled_tanh(x):
  return K.activations.tanh(6 * x - 3) / 2 + 1 / 2



key = 1
partials = 100
n = 44100
fps = 44100

f0 = np.power(2, (key - 49) / 12) * 440
P = np.arange(1, partials + 1, 1)
key = (key - 1) / 87
ipt = np.array([[key, p] for p in np.linspace(0, 1, partials)])

[ma, Ma] = np.genfromtxt('02_predictions/piano/amplitudes/m_M.csv', delimiter=',')
[md, Md] = np.genfromtxt('02_predictions/piano/decays/m_M.csv', delimiter=',')
[mf, Mf] = np.genfromtxt('02_predictions/piano/frequencies/m_M.csv', delimiter=',')

a_net = K.models.load_model('02_predictions/piano/amplitudes/#model.H5', {'scaled_tanh': scaled_tanh})
d_net = K.models.load_model('02_predictions/piano/decays/#model.H5', {'scaled_tanh': scaled_tanh})
f_net = K.models.load_model('02_predictions/piano/frequencies/#model.H5', {'scaled_tanh': scaled_tanh})

A = np.ndarray.flatten(a_net.predict(ipt)) * ((Ma - ma) + ma) * 5000
D = np.ndarray.flatten(d_net.predict(ipt)) * ((Md - md) + md) * 0.000113026536390889 #average decay
F = (np.ndarray.flatten(f_net.predict(ipt)) * (Mf - mf) + mf) * P * f0

print(A.shape,D.shape,F.shape, P.shape)
w = np.zeros(n)
for i in range(partials):
  print('partial:', i)
  ph = np.random.uniform(0, 2 * np.pi)
  w += create_signal(n, fps, F[i], ph, A[i], D[i])

save_wav(w)
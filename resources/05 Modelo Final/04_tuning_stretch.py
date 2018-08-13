from numpy.fft import rfft, irfft
import numpy as np
import matplotlib.pyplot as plt
from Hlib import read_wav, save_wav, create_signal
from scipy.signal import argrelmax
from scipy.optimize import curve_fit
import os

def pad(X, n, value = 0):
  l = X.shape[0]
  if l >= n:
    padded = X[0:n]
  else:
    zeros = np.zeros(n - l) #.fill(np.nan)
    padded = np.hstack([X, zeros])
  # print('p:', padded.shape[0])
  return padded
##########################################
##########################################
################ Settings ################
piece_name = 'piano'
partials = 100
##########################################
##########################################
##########################################

filenames = os.listdir('00_samples/' + piece_name + '/')
names = []
for filename in filenames:
  names.append(filename.replace('.wav', ''))
names = np.sort(np.array(names, dtype=np.int)).astype(np.str)

save_path = '01_Info/' + piece_name + '/'
os.makedirs(save_path, exist_ok=True)
os.makedirs(save_path + 'graphs/', exist_ok=True)

# extract frequencies, amplitudes and decays per partials
max_amps = []
max_decays = []
fractions_of_max_amps = []
fractions_of_max_decays = []
Mfreqs_over_Tfreqs = []
phases = []

stretch = []
for name in names:
  print('\nsample:', name)
  s, fps = read_wav('00_samples/' + piece_name + '/' + name + '.wav')
  n = s.shape[0]
  F = rfft(s) * 2 / n
  P = np.abs(F)
  max_amp = np.max(P)                                              #<| <| <| <| <|
  f0 = np.power(2, (int(name) - 49) / 12) * 440
  local_f0 = int(round(f0 / fps * n))
  idxs = argrelmax(P, order=local_f0 // 2)[0] #Local Frequencies
  idx0 = idxs[np.argmin(np.abs(idxs - local_f0))]
  
  f0_measured = idx0 * fps / n                                   #<| <| <| <| <|
  stretch.append(f0_measured / f0)


np.savetxt(save_path + 'tuning_stretch.csv', np.array(stretch), delimiter=',')

# fig = plt.figure()
# fig.set_size_inches(2000 / fig.dpi, 400 / fig.dpi)
# plt.xticks(np.arange(1, 88+1))
# plt.plot(stretch, 'k.')
# plt.show()
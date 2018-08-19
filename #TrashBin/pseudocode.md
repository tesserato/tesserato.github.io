
amplitude <- 0.005                 # metros
L <- 0.6                           # metros
pluck_position <- .5               # fração do comprimento L
pickup_position <- .5              # fração do comprimento L
fps <- 44100                       # amostras / segundo
frequency <- 440                   # Hz
duration <- 1                      # segundos
sustain <- .9998
N <- duration * fps                # número de pontos do grid temporal
dt <- 1 / fps                      # espaço entre pontos sucessivos no grid temporal
M <- fps / (2 * frequency)         # número de pontos do grid espacial
dx <- L / M                        # espaço entre pontos sucessivos no grid espacial
c <- frequency * 2 * L             # metros / segundo
C <- c * dt / dx                   # número de Courant
x <- [0, dx, 2 dx,..., M dx]
t <- [0, dt, 2 dt,..., N dt]
pickup <- M * pickup_position
y_0 <- vetor com "M" zeros
y_1 <- vetor representando o formato inicial do deslocamento vertical
y_2 <- vetor com "M" zeros
ctr <-0
W <- []
FOR i IN [1, 2,..., M]:
  y_0[i] <- y_1[i] + 0.5 * C^2 *(y_1[i+1] - 2 * y_1[i] + y_1[i-1])
y[0] <- 0
y[M] <- 0
APPEND y_0[pickup] TO W
y_2 <- y_1
y_1 <- y_0
ctr <- ctr + 1
FOR j IN [1, 2,..., N]:
  FOR i IN [1, 2,..., M]:
    y_0[i] <- 2 * y_1[i] - y_2[i] + C^2 * (y_1[i+1] - 2 * y_1[i] + y_1[i-1])
  y_0[0] <- y[0] * 0.5
  y_0[M] <- y[M] * 0.5
  y_0 <- y_0 * sustain
  APPEND y_0[pickup] TO W
  y_2 <- y_1 
  y_1 <- y_0
  ctr <- ctr + 1
*OUTPUT* W







N <- 44100                         # número final de amostras geradas
fps <- 44100                       # amostras / segundo
frequency <- 440                   # Hz
L <- fps / (2 * frequency)
pluck_position <- .5               # fração do comprimento L
pickup_position <- .5              # fração do comprimento L
sustain <- .99
smoothing <- 3
pickup <- L * pickup_position
delay_r <- vetor representando o formato inicial do deslocamento vertical
delay_l <- vetor com "L" zeros
W <- vetor com "N" zeros
FOR i IN [1, 2,..., N]:
  W[i] <- delay_r[pickup] + delay_l[pickup]
  to_l <- -1 * AVERAGE(delay_r[delay_r.LENGTH - smoothing : delay_r.LENGTH]) * sustain
  FOR i IN [delay_r.LENGTH - 2, delay_r.LENGTH - 3,...,0]:
    delay_r[i+1] <- delay_r[i]
  delay_r[0] <- -1 * delay_l[0]
  FOR i IN [0,1,...,delay_l.LENGTH - 2]:
    delay_l[i] <- delay_l[i+1]
  delay_l[L-1] <- to_l  
OUTPUT W


~~~~py
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
# Discrete Fourier Transform | Transformada Discreta de Fourier
def DFT(x):
  N = x.shape[0]
  # cria um vetor de N entradas complexas, preenchido com zeros
  X = np.zeros(N, dtype='complex64')
  n = np.array([p for p in range(N)]) # n = {0,1,2,...,N-1}
  # Versão de "alta resolução" de n, usada para o gráfico apenas
  Hn = np.linspace(0, N-1, 100*N) # Hn ={0,...,1,...,2,...,N-1}
  for m in range(N): # m E {0,1,2,...,N-1}
    C_Si = np.exp(-2 * np.pi * m * n / N * 1j) # C(m) - S(m) i
    # Versão de "alta resolução" de C_Si, usada para o gráfico apenas
    HC_Si = np.exp(-2 * np.pi * m * Hn / N * 1j)
    X[m] = sum(np.multiply(x, C_Si)) # multiplicação termo a termo
    # plotando:
    plt.figure(1)
    plt.suptitle('M =' + str(m), fontsize=16)
    plt.subplot(211)
    plt.plot(n,x[n].real, 'k:.', label='x[n]')
    plt.plot(n,C_Si.real, 'k--o', label='C[n]')
    plt.plot(Hn,HC_Si.real, 'k-',label='C[n] ideal')
    plt.ylabel('Real', fontsize=14, color='k')    
    plt.subplot(212)
    plt.plot(n,x[n].imag, 'k:.', label='x[n]')
    plt.plot(n,C_Si.imag, 'k--o', label='C[n]')
    plt.plot(Hn,HC_Si.imag, 'k-',label='C[n] ideal')
    plt.ylabel('Imaginário', fontsize=14, color='k')
    plt.legend()
    plt.savefig('0' + str(m) + '.png', dpi=150)
    plt.close('all')
  #calcula o erro em relação ao algoritmo da biblioteca Scipy
  error = sum((X-fft(x))**2)
  print(round(error,5))
  # retorna a parte não redundante da transformada
  return X[0 : int(N/2+1)] if (N % 2 == 0) else X[0 : int((N+1)/2)]

def s(t):
  return np.cos(2 * np.pi * t)

t = np.linspace(0, 1, 8) # 8 pontos entre 0 e 1
x = s(t) # aplica a função ponto a ponto
X = DFT(x)
# plotando:
plt.figure(1)
plt.subplot(211)
plt.ylabel('Real', fontsize=14, color='k')
plt.stem(X.real,linefmt='k--',markerfmt='ko', basefmt='k--')
plt.subplot(212)
plt.stem(X.imag,linefmt='k--',markerfmt='ks', basefmt='k--')
plt.ylabel('Imaginário', fontsize=14, color='k')
plt.savefig('transform.png', dpi=150)
plt.close('all')
~~~~
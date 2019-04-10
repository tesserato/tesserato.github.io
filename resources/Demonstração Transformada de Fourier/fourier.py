import numpy as np
import matplotlib.pyplot as plt
# from scipy.fftpack import fft

# Discrete Fourier Transform | Transformada Discreta de Fourier
def DFT(x, plot = False):
  n = x.shape[0]  
  FT = np.zeros(n, dtype='complex64') # cria um vetor de N entradas complexas, preenchido com zeros
  N = np.array([p for p in range(n)]) # n = {0,1,2,...,N-1}
  
  if plot:# Versão de "alta resolução" de N, usada para o gráfico apenas
    HN = np.linspace(0, n-1, 100*n) # Hn ={0,...,1,...,2,...,N-1}
  for f in range(n): # m E {0,1,2,...,N-1}

    C_Si = np.exp(-2 * np.pi * f * N / n * 1j) # Cos(f) - Sin(f) i
    FT[f] = sum(np.multiply(x, C_Si)) # multiplicação termo a termo
    
    if plot: # plotando:
      HC_Si = np.exp(-2 * np.pi * f * HN / n * 1j) # Versão de "alta resolução" de C_Si, usada para o gráfico apenas
      plt.figure(1)
      plt.suptitle(f'f={f}', fontsize=16)

      plt.subplot(211)
      # plt.plot(n,x[n].real, 'k:.', label='x[n]')
      plt.plot(HN,HC_Si.real, 'r-',label=f'$\cos (2 \pi t {f} / {n})$ ideal')
      plt.plot(N,C_Si.real, 'k--o', label=f'$\cos (2 \pi t {f} / {n})$ amostrado')
      plt.xlabel('$t$', fontsize=14, color='k')
      cur_axes = plt.gca()
      cur_axes.axes.get_xaxis().set_ticklabels([])
      cur_axes.axes.get_yaxis().set_ticklabels([])
      plt.legend()

      plt.subplot(212)
      # plt.plot(n,x[n].imag, 'k:.', label='x[n]')
      plt.plot(HN,HC_Si.imag, 'r-',label=f'$\sin (2 \pi t {f} / {n})$ ideal')
      plt.plot(N,C_Si.imag, 'k--o', label=f'$\sin (2 \pi t {f} / {n})$ amostrado')
      # plt.ylabel('Imaginário', fontsize=14, color='k')
      # plt.axis('off')
      cur_axes = plt.gca()
      cur_axes.axes.get_xaxis().set_ticklabels([])
      cur_axes.axes.get_yaxis().set_ticklabels([])
      plt.legend()

      plt.savefig('0' + str(f) + '.png', dpi=150, transparent="True", pad_inches=0)
      plt.close('all')

  FT = FT[0 : int(n/2+1)] if (n % 2 == 0) else FT[0 : int((n+1)/2)] # retorna a parte não redundante da transformada
  error = np.sum(np.abs(FT - np.fft.rfft(x))) #calcula o erro em relação ao algoritmo da biblioteca numpy
  print(round(error,5))

  if plot:
    plt.figure(1)
    plt.subplot(211)
    plt.ylabel('Real', fontsize=14, color='k')
    plt.stem(FT.real,linefmt='k--',markerfmt='ko', basefmt='k--')
    plt.subplot(212)
    plt.stem(FT.imag,linefmt='k--',markerfmt='ks', basefmt='k--')
    plt.ylabel('Imaginário', fontsize=14, color='k')
    plt.savefig('transform.png', dpi=150)
    plt.close('all')

  return FT

##########

t = np.linspace(0, 1, 8) # 8 pontos entre 0 e 1
x = np.cos(2 * np.pi * t) # aplica a função ponto a ponto
X = DFT(x, True)

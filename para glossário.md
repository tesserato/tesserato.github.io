framerate
FPS
GANs
MIDI
pooling
MNIST
LSTM
Digital Waveguides
Courant
delay lines
circular buffer
samples
backward pass
backpropagation
Fast Fourier Transform
Forward Pass
learning rate taxa de aprendizado
DFT
Creative Commons Attribution 4.0 International
DMI
round-robins
batches
grid search
épocas
descida em gradiente (standard gradient descent - sgd FIXME:)
Tensorboard
lms
neurons
steps
biases
_sampling rate_
_smoothstep_
transiente
efeito *machine-gun*
_overfitting_
pizzicato

$\mathcal{F}$


------------------
{.python .numberLines}

[]{custom-style="quadro"}

[Fonte: Elaboração própria]{custom-style="fonte"}

{#fig:id}
+@fig:id

$$ y = mx + b $$ {#eq:id}
+@eq:id

{#tbl:id}
+@tbl:id


::: {custom-style="Fonte"}
Fonte: Elaboração própria
:::


------------------

<div>
<audio controls preload> 
    <source src="resources\Demo Digital Waveguide\DW_440_Pluck_0-1_Pick_0-5.wav"></source>
</audio>
</div>

O objetivo geral deste trabalho é desenvolver um modelo de simulação em tempo real de instrumentos acústicos que tire proveito do estado da arte relacionado à redes neurais artificias para exibir maior eficiência, quando comparado aos algoritmos tradicionais, dando origem a simulações mais realistas, principalmente do ponto de vista da percepção humana, e menos intensivas computacionalmente.
A lista abaixo enumera os objetivos específicos necessários à essa finalidade:

- Identificar formas compactas de representação das ondas sonoras mais adequadas à predição/generalização via redes neurais;

- Identificar arquiteturas neurais que possam ser utilizadas na modelagem acústica;

- Identificar na literatura sobre modelos acústicos de instrumentos musicais ferramentas que possam ser utilizadas para simplificação e aumento de eficiência, tanto do modelo quanto das representações.

- Tendo em vista o foco na síntese em tempo real, identificar as arquiteturas e hiperparametros neurais e técnicas em geral mais eficientes,

- Delinear a capacidade de generalização do modelo criado.


<!-- O estado da arte da síntese sonora ainda não foi estabelecido por abordagens totalmente baseadas em redes neurais, embora pesquisas nesse sentido sejam abundantes, e estejam rapidamente aproximando-se da qualidade necessária para a implementação em produtos finais. O trabalho de [@zen2015unidirectional] aborda a tarefa a partir de uma rede recorrente com camadas FIXME:LSTM (long short-term memory), enquanto [@wu2016investigating] investiga a influência de aspectos específicos dessa topologia em sua eficiência na tarefa de síntese da voz falada. -->

<!-- Além disso, alguns dos algoritmos e técnicas convencionais, ainda que de forma muitas vezes ineficiente, prestam-se de maneira razoável à simulação *off-line* de instrumentos acústicos, razão pela qual o foco deste trabalho é a síntese em tempo real.  -->



<!-- É interessante investigar, diante disso, algumas aplicações na área de computer vision: aplicações relacionadas à compressão de imagens nos oferecem insights sobre o potencial de geração de representações simplificadas, e são de especial interesse. 

Apesar da importancia do tema[@rehman2014image], sobretudo frente ao crescente fluxo de imagens na internet, a última revisão bibliográfica sobre a aplicação de redes neurais à compressão de imagens pode ser vista em [@jiang1999image] e já data de quase duas décadas.

A despeito disso, alguns trabalhos vem sendo desenvolvidos, como é o caso de [@balle2016end], que propõe um arquitetura alternando filtros convolucionais com ativações não lineares, que alcança, para todos os bitrates, uma melhora na métrica MS-SSIM (Multiscale Structural Similarity for Image Quality Assessment).

Usando uma rede neural fuzzy, [@wang2015image] alcança melhorias na velocidade, robustez e qualidade na tarefa de compressão de imagem com perdas.
[@toderici2015variable] desenvolve um método progressivo, com foco na redução de tráfego em dispositivos móveis, que permite qualidade arbitrária dependendo da quantidade de bits transferidos
[@toderici2016full] alcança resultados superiores a codecs, utilizando diferentes arquiteturas baseadas em redes recorrentes, um binarizador e uma rede neural para codificar a entropia dos dados.

Mais recentemente, utilizando a métrica SSIM como a própria função de perda de uma arquitetura baseada em redes recorrentes e um algoritimo de alocação adaptativa de bits,[@johnston2017improved] supera métodos *industry standard*, como JPEG e WebP. Similarmente, com uma função de perda modificada, [@theis2017lossy] demonstra que arquiteturas baseadas em autoencoders alcançam resultados comparáveis ao formato JPEG 2000.

O trabalho de [@santurkar2017generative] investiga a resiliência da compressão baseada em redes neurais, através de um modelo generativo capaz de oferecer *graceful degradation* às imagens comprimidas.
[@gregor2016towards] investiga o conceito de compressão conceitual, uma técnica que permite que imagens sejam recuperadas de símbolos. -->



<!-- No domínio do tempo, a onda é representada por N números inteiros, cada qual conservadoramente entre +/- 100000. Tomando como referência a linguagem C, na qual a maioria dos motores são implementados, cada um deles ocuparia o espaço de um long integer, ou seja, 4 bytes, para um total de 4 * N bytes por sample. No domínio da frequência, teríamos cada uma das N/2 frequências representadas por dois números reais (floats, em C), que ocupam, cada um, o mesmo espaço de 4 bytes, para um total de 8 * N/2 bytes por sample: o mesmo espaço, portanto. -->


<!-- Face a essas limitações, tanto de qualidade quanto de eficiência, formulou-se uma abordagem analítica, tomando como base a teoria relacionada à transformada de Fourier e seu teorema da convolução.

Como posto anteriormente, outras formulações existem visando a extração de envelopes, notadamente no campo de processamento de sinais. A metodologia proposta, contudo, é mais apropriada ao trabalho em tela, já que reflete diretamente a amplitude da frequência específica do sinal no domínio do tempo, além de prestar-se à implementações eficientes, duas das quais serão exemplificadas.

Considerando que $s(t)$ é o sinal a ser analisado, no domínio da frequência, e e^{-2 \pi t f / n i} o kernel da transformada de Fourier em função unicamente do tempo $t$, com $f$ fixo na frequência local para a qual deseja-se o envelope temos, para o caso discreto, que a integral de menos a mais infinito, no tempo, da multiplicação desses dois termos nos fornece a amplitude (média, com a normalização adequada) da frequência $f$ na onda $s$. De fato, reparando que o que temos é um dos termos da transformada de Fourier para uma frequência específica, e relembrando a forma geométrica do kernel, as informações que temos no sentido da fração correspondente a uma seno puro e a um cosseno puro (representados pelo número complexo $z$) nos permite reconstruir a amplitude e a fase da frequência $f$ no sinal. Assim $z(f,t) = s(t) ~ e^{\frac{-2 \pi t f} {n} i } $

Para investigar essas informações em partes específicas do sinal, podemos "mascarar" a integral acima, multiplicando a por uma função janela que assume o valor 1 em uma parte do intervalo de duração do sinal ($t \in [0,n)$) e o valor 0 no resto. Sem perda de generalidade, podemos supor que essa função $w(t)$ assume o valor 1 no intervalo entre $t=0$ e $t=l$, e é nula para o restante dos valores de $t$. Fazendo-a função também de l, temos:

$$z(f,t) =  s(t) ~ e^{\frac{-2 \pi t f} {n} i } $$


$$z(f) = \int_{-\infty}^{\infty} s(\tau) ~ e^{\frac{-2 \pi \tau f} {n} i } ~ w(t - \tau) ~ d\tau$$

$$z(f) = \int_{t-l}^{t} s(\tau) ~ e^{\frac{-2 \pi \tau f} {n} i }  ~ d\tau$$ -->

<!-- A representação no domínio da frequência é pouco conveniente para ser utilizada no treinamento de redes neurais, por três razões principais:
trata-se de uma representação indireta, pouco intuitiva.
Além disso, pequenos erros propagam-se por toda a onda
Não há informação parcial do decay, que é reproduzido pela interferência destrutiva de todas as ondas.
A informação sobre a amplitude sofre de problema análogo.




#### Senoides Principais
Redução de Dimensionalidade dos Dados
Podemos sanar o problema da falta de informação parcial sobre decay e amplitude ajustando as principais ondas obtidas pela transformada de Fourier.

4 * senoides < N -->
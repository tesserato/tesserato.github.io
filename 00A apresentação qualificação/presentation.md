<!-- ---
author: Carlos Tarjano 
title: Redes Neurais Aplicadas à Modelagem de Instrumentos Acústicos para Síntese Sonora em Tempo Real
date: Niterói, 31 / 07 / 2018
--- -->

::: slide
# UNIVERSIDADE FEDERAL FLUMINENSE

ESCOLA DE ENGENHARIA

PROGRAMA DE PÓS-GRADUAÇÃO EM ENGENHARIA DE PRODUÇÃO

**Redes Neurais Aplicadas à Modelagem de Instrumentos Acústicos para Síntese Sonora em Tempo Real**

por Carlos Tarjano 

Prof. Dr. Valdecy Pereira (Orientador)

Niterói, 31 / 07 / 2018

:::


::: slide
# Introdução

## Motivação:

ANNs aplicadas com sucesso em várias áreas

Estado da arte em áreas afins

Poucos trabalhos relacionados a síntese sonora (nenhum em tempo real)

Indústria de DMI “estagnada”

## Objetivo: Elaborar um modelo baseado em ANNs para emulação de instrumentos em tempo real

Mapear o estado da arte em áreas (direta ou indiretamente) correlatas

Mapear o estado da arte da modelagem acústica “tradicional”

Potencial de inclusão de teoria acústica na eficiência
:::

::: slide
# Teste Imagem

## Motivação:

ANNs aplicadas com sucesso em várias áreas

Estado da arte em áreas afins

![teste](media/35.png)

## Objetivo: Elaborar um modelo baseado em ANNs para emulação de instrumentos em tempo real

Mapear o estado da arte em áreas (direta ou indiretamente) correlatas

Mapear o estado da arte da modelagem acústica “tradicional”

Potencial de inclusão de teoria acústica na eficiência
:::


::: slide
# Teste video

## Motivação:

ANNs aplicadas com sucesso em várias áreas

Estado da arte em áreas afins

<div>
  <video controls>
    <source src="media/DigitalWaveguide.webm" type="video/webm">
  </video>
</div>

## Objetivo: Elaborar um modelo baseado em ANNs para emulação de instrumentos em tempo real

Mapear o estado da arte em áreas (direta ou indiretamente) correlatas

Mapear o estado da arte da modelagem acústica “tradicional”

Potencial de inclusão de teoria acústica na eficiência
:::


<script>
var FontMultiplier = 0.0;
var FontSteps = 0.1
var CurrentSlide = 0;
var slides = document.getElementsByClassName("slide");
var n = slides.length;

function draw(){
  slides[CurrentSlide].style.opacity = 0;
  FontMultiplier = 0.0;
  document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);
  while (slides[CurrentSlide].clientHeight < document.body.clientHeight){
    FontMultiplier += FontSteps
    document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);
  }
  FontMultiplier -= FontSteps
  document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);

  slides[CurrentSlide].style.opacity = 1;
}

function PassSlide(inc){
  slides[CurrentSlide].style.display = "none";
  CurrentSlide += inc;
  if (CurrentSlide > n - 1) {CurrentSlide = 0};
  if (CurrentSlide < 0) {CurrentSlide = n - 1};
  slides[CurrentSlide].style.display = "block";
}

for (i = 0; i < n; i++) {
  slides[i].style.display = "none";
}
slides[CurrentSlide].style.display = "block";
draw()

window.onresize = function(){
  draw()
};

document.onkeydown = function(e){
  if (e.key=='ArrowRight'|| e.key=='Enter'|| e.key==' ') {
    PassSlide(1)
    draw()
  }
  if (e.key=='ArrowLeft') {
    PassSlide(-1)
    draw()
  }

};

var l_div = document.createElement("div");
l_div.style.zIndex = 2;
l_div.className = 'btn';
l_div.style.position = "fixed";
l_div.style.background = "black";
l_div.style.opacity = "0.0";
l_div.style.top = '0px';
l_div.style.left = '0px';
l_div.style.width = "3%";
l_div.style.height = "100%";
l_div.onmouseenter = function(e){
  l_div.style.opacity = "0.5";
  l_div.style.width = "10%";
}
l_div.onmouseleave = function(e){
  l_div.style.opacity = "0.0";
  l_div.style.width = "3%";
}
l_div.onmousedown = function(e){
  PassSlide(-1);
  draw();
}
document.body.appendChild(l_div);


var r_div = document.createElement("div");
r_div.style.zIndex = 2;
r_div.className = 'btn';
r_div.style.position = "fixed";
r_div.style.background = "black";
r_div.style.opacity = "0.0";
r_div.style.top = '0px';
r_div.style.left = '97%';
r_div.style.width = "3%";
r_div.style.height = "100%";
r_div.onmouseenter = function(e){
  r_div.style.opacity = "0.5";
  r_div.style.left = '90%';
  r_div.style.width = "10%";
}
r_div.onmouseleave = function(e){
  r_div.style.opacity = "0.0";
  r_div.style.left = '97%';
  r_div.style.width = "3%";
}
r_div.onmousedown = function(e){
  PassSlide(+1);
  draw();
}
document.body.appendChild(r_div);
</script>


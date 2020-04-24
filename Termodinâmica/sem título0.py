# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:11:21 2020

@author: Celso Henrique
"""

import numpy as np
from vpython import *
import matplotlib.pyplot as plt

##################Palco######################################################
cena = canvas(
                title=' Fluidos: Viscosidade ', # Criar o palco onde ocorrerá o movimento
               # width=800, height=400,
                userzoom = False,                         # O usuário não pode aproximar ou afastar a câmera
                userspin = False,                         # O usuário pode girar a câmera.
                ambient  = color.gray(.3),               # Cor da iluminação dos objetos
                  center = vector(0,2.5,0),              # Posição central do código
              background = vec(.6,.9,.6)                   # Cor do background
         )       

####################Objetos##################################################
 
tubo = cylinder(pos=vector(0,60,0), 
                axis=vector(0,0,0), 
                radius=.5,
                opacity=.3,
                color = color.blue)
xfera =  sphere(pos=tubo.pos, 
                radius=.3,
                vel=vec(0,0,0),
                color = color.black)
#dot = dot(pos=vec(0,0,0))

##################Forças####################################################
m=10
g=10
t=0
dt=.01
vol = 4/3*np.pi*xfera.radius**3
dens = .8
visc = .3


axisp = vec(0,-1,0)
def peso(m):
    return m*g

def empuxo(vol,dens,g):
    return - vol*dens*g

def atrito():
    F = -6* np.pi * visc * xfera.radius * mag(xfera.vel)
    C = ((9*xfera.radius)/(4*tubo.radius))**2 + ((9*xfera.radius)/(4*tubo.radius))
    return (1 + C) * F
    
posicao=[]
tempo=[]

while (xfera.pos.y > 0 ):
    
    rate(1000)
    acc = (peso(m)+empuxo(vol,dens,g)+atrito())/m
    
    xfera.vel = xfera.vel + acc*dt*axisp
    xfera.pos = xfera.pos + xfera.vel*dt + acc/2*axisp*dt**2
    t=t+dt

    
    
    if  xfera.pos.y > 0:
       posicao.append(round(xfera.pos.y,2))
       tempo.append(round(t,3))
    
    
plt.plot(tempo,posicao)
    
# -*- coding: utf-8 -*-
# Launcher to the tri-dimensionnal game of life.
from gol import *
import gol
print("Welcome to Valentin PEARCE's Game·Of·Life·3D")
print("Conway's Game Of Life is a mathematic cell life simulation.")
print("It models the evolution of single cell generations in a table.")
print("My idea was to transpose this problem in a three dimension matrix")
print("=================================================================")
print("Here is a small demonstration of the evolution of the following matrix :")
gol.createTab(3)

gol.live(0,0,0)
gol.live(1,0,0)
gol.live(0,1,0)
gol.live(0,0,1)
gol.live(1,1,1)
print tab
gol.generation(3)
print gol.tab

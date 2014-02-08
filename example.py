# -*- coding: utf-8 -*-
# Launcher to the tri-dimensionnal game of life.
from gol import *
import gol
print("Welcome to Valentin PEARCE's Game·Of·Life·3D")
print("Conway's Game Of Life is a mathematic cell life simulation.")
print("It models the evolution of single cell generations in a table.")
print("My idea was to transpose this problem in a three dimension matrix")
print("=================================================================")	
gol.createTab(10)
print tab
# "arrowhead" at one corner of the cube
gol.live(0,0,0)
gol.live(1,0,0)
gol.live(0,1,0)
gol.live(0,0,1)

# Cube at the opposite corner of the cube
gol.live(9,9,9)
gol.live(8,9,9)
gol.live(9,8,9)
gol.live(9,9,8)
gol.live(8,8,9)
gol.live(8,9,8)
gol.live(9,8,8)
gol.live(8,8,8)
print tab

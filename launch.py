# -*- coding: utf-8 -*-
# Launcher to the tri-dimensionnal game of life.
from gol import *
import gol
print("Welcome to Valentin PEARCE's Game·Of·Life·3D")
print("Conway's Game Of Life is a mathematic cell life simulation.")
print("It models the evolution of single cell generations in a table.")
print("My idea was to transpose this problem in a three dimension matrix")
print("=================================================================")
i = 0
j = 0
k = 0
size = input("Please input the size of one side of the grid : ")	
gol.createTab(size)
print tab
gol.generation(size)
print tab

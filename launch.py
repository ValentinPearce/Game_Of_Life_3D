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
cells = 0
countdown = 0
size = input("Please input the size of one side of the grid : ")	
gol.createTab(size)
print("Here is your blank grid")
gol.display()
print("How many live cells do you want ? ")
cells = input()
for a in range (cells) :
    coord = input("Please enter the coordinates of the cell like so i,j,k")
    gol.live(coord)
print("Here is your grid with living cells")
gol.display()
for time in range(1000000000):
    countdown = countdown + 1
gen=input("Which generation do you want to observe? (At this time you have defined generation nº0)")
for generate in range (gen):
    gol.generation(size)
gol.display()

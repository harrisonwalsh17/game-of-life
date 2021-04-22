# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 01:24:33 2021

@author: harri
"""

import pygame
import numpy as np
pygame.init()


block_size = 20
x_blocks = 20
y_blocks = 20
#width and height in units * block_size
width = x_blocks * block_size
height = y_blocks * block_size

OCHRE = (203, 163, 40)
PURPLE = (90, 11, 77)
GREY = (76, 85, 93)
WHITE = (255,255,255)

WINDOW = pygame.display.set_mode((width,height))
pygame.display.set_caption('Gridlocked')
grid_thickness = 1
x_block_start = 0
y_block_start = 0

grid_map = np.zeros((y_blocks, x_blocks), dtype = int)

glider = np.array([[0,0,1],[1,0,1],[0,1,1]], dtype = int)
glider_dimensions = np.shape(glider)


glider_start = (4,4)

for row in range(0, glider_dimensions[0]):
    for column in range (0,glider_dimensions[1]):
        grid_map[row + glider_start[0]][column + glider_start[1]] = glider[row][column]

#print(grid_map)



         

def drawGrid():

    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pygame.Rect(x,y, block_size, block_size)
            pygame.draw.rect(WINDOW, WHITE, rect, grid_thickness)
            
    

run = True

while run:
    CLOCK = pygame.time.Clock()
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            run = False
        
    WINDOW.fill(GREY)    
    drawGrid()
    for row in range(0, y_blocks):
        for column in range(0,x_blocks):
            if grid_map[row][column] != 0: 
                rect_glider = pygame.Rect(column * block_size + grid_thickness, row * block_size + grid_thickness, block_size - 2 * grid_thickness, block_size - 2 * grid_thickness)
                pygame.draw.rect(WINDOW, OCHRE, rect_glider, 0)
    rect_color = pygame.Rect(x_block_start + grid_thickness, y_block_start + grid_thickness, block_size-2*grid_thickness, block_size-2*grid_thickness)
    """
    pygame.draw.rect(WINDOW, OCHRE, rect_color, 0)
    if x_block_start + grid_thickness + block_size < width:
        x_block_start += block_size
    elif y_block_start + grid_thickness + block_size < height:
        y_block_start += block_size
        
    """
 
    grid_map_next = np.zeros((y_blocks, x_blocks), dtype = int)
    for row in range(0, y_blocks):
        for column in range(0, x_blocks):
            if row > 0 and column > 0 and row < y_blocks - 1 and column < x_blocks - 1:
                alive_neighbors = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i !=0 or j !=0:
                            alive_neighbors += grid_map[row + i][column + j]
                                   
                if grid_map[row][column] == 1:
                    if alive_neighbors < 2:
                        grid_map_next[row][column] = 0
                    elif alive_neighbors < 4:
                        grid_map_next[row][column] = 1
                    else:
                        grid_map_next[row][column] = 0
                else:
                    if alive_neighbors == 3:
                        grid_map_next[row][column] = 1
                #print(alive_neighbors)
    
    grid_map = grid_map_next


    pygame.display.update()
    CLOCK.tick(3)


pygame.quit()  


            
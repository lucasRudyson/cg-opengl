import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_io(position_x=0, position_z=0):
    """IO do Dota 2 - versão SIMPLES e LIMPA"""

    glPushMatrix()
    glTranslatef(position_x, 2, position_z)

    time = pygame.time.get_ticks() / 1000.0
    pulse = 1 + 0.3 * math.sin(time * 3)  # Pulsação

    quadric = gluNewQuadric()

    # ============================================
    # ESFERA PRINCIPAL DO IO (azul brilhante)
    # ============================================
    glDisable(GL_LIGHTING)
    glColor3f(0.3, 0.7, 1.0)  # Azul
    gluSphere(quadric, 0.8 * pulse, 30, 30)

    # Núcleo interno mais brilhante
    glColor3f(0.7, 0.9, 1.0)  # Azul claro
    gluSphere(quadric, 0.5 * pulse, 20, 20)

    # ============================================
    # 6 ESFERAS ORBITANDO
    # ============================================
    for i in range(6):  # Apenas 6 partículas
        angle = (i * 60) + (time * 50)  # Espaçadas em 60 graus
        radius = 1.2

        x = radius * math.cos(math.radians(angle))
        z = radius * math.sin(math.radians(angle))
        y = 0.3 * math.sin(time * 2 + i)  # Movimento vertical

        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3f(0.5, 0.8, 1.0)  # Azul médio
        gluSphere(quadric, 0.15, 12, 12)  # Partícula pequena
        glPopMatrix()

    glEnable(GL_LIGHTING)
    glPopMatrix()

from OpenGL.GL import *
from OpenGL.GLU import *
from bloco import draw_block
def draw_steve(arm_angle=0):
    # Cores aproximadas do Steve
    skin_color = (0.8, 0.6, 0.5)  # Pele
    shirt_color = (0.3, 0.7, 0.8)  # Camisa azul
    pants_color = (0.2, 0.2, 0.5)  # Calça azul escura

    # CABEÇA
    glPushMatrix()
    glTranslatef(0, 3.5, 0)  # Posicionar no topo
    draw_block(1, 1, 1, skin_color)
    glPopMatrix()

    # CORPO
    glPushMatrix()
    glTranslatef(0, 2.25, 0)
    draw_block(1, 1.5, 0.5, shirt_color)
    glPopMatrix()

    # BRAÇO ESQUERDO (estático)
    glPushMatrix()
    glTranslatef(-0.75, 2.25, 0)
    draw_block(0.5, 1.5, 0.5, skin_color)
    glPopMatrix()


    # BRAÇO DIREITO (animado - levanta com J)
    glPushMatrix()
    glTranslatef(0.75, 3, 0)  # Pivot no ombro (mais alto)
    glRotatef(-arm_angle, 1, 0, 0)  # Rotacionar em torno do eixo X
    glTranslatef(0, -0.75, 0)  # Deslocar para posição correta
    draw_block(0.5, 1.5, 0.5, skin_color)
    glPopMatrix()

    # PERNA ESQUERDA
    glPushMatrix()
    glTranslatef(-0.25, 0.75, 0)
    draw_block(0.5, 1.5, 0.5, pants_color)
    glPopMatrix()

    # PERNA DIREITA
    glPushMatrix()
    glTranslatef(0.25, 0.75, 0)
    draw_block(0.5, 1.5, 0.5, pants_color)
    glPopMatrix()


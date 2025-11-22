from OpenGL.GL import *
from OpenGL.GLU import *

def draw_block(width, height, depth, color):
    """Desenha um bloco retangular com dimensões personalizadas"""
    w, h, d = width/2, height/2, depth/2
    r, g, b = color

    glBegin(GL_QUADS)

    # Face FRONTAL
    glColor3f(r, g, b)
    glNormal3f(0, 0, 1)
    glVertex3f(-w, -h, d)
    glVertex3f(w, -h, d)
    glVertex3f(w, h, d)
    glVertex3f(-w, h, d)

    # Face TRASEIRA
    glColor3f(r*0.8, g*0.8, b*0.8)  # Um pouco mais escuro
    glNormal3f(0, 0, -1)
    glVertex3f(-w, -h, -d)
    glVertex3f(-w, h, -d)
    glVertex3f(w, h, -d)
    glVertex3f(w, -h, -d)

    # Face SUPERIOR
    glColor3f(r*0.9, g*0.9, b*0.9)
    glNormal3f(0, 1, 0)
    glVertex3f(-w, h, -d)
    glVertex3f(-w, h, d)
    glVertex3f(w, h, d)
    glVertex3f(w, h, -d)

    # Face INFERIOR
    glColor3f(r*0.7, g*0.7, b*0.7)
    glNormal3f(0, -1, 0)
    glVertex3f(-w, -h, -d)
    glVertex3f(w, -h, -d)
    glVertex3f(w, -h, d)
    glVertex3f(-w, -h, d)

    # Face DIREITA
    glColor3f(r*0.85, g*0.85, b*0.85)
    glNormal3f(1, 0, 0)
    glVertex3f(w, -h, -d)
    glVertex3f(w, h, -d)
    glVertex3f(w, h, d)
    glVertex3f(w, -h, d)

    # Face ESQUERDA
    glColor3f(r*0.85, g*0.85, b*0.85)
    glNormal3f(-1, 0, 0)
    glVertex3f(-w, -h, -d)
    glVertex3f(-w, -h, d)
    glVertex3f(-w, h, d)
    glVertex3f(-w, h, -d)

    glEnd()

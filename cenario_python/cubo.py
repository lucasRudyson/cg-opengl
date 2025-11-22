
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cubo():
    glBegin(GL_QUADS)

    # Face FRONTAL (Z positivo)
    glColor3f(1, 0, 0)
    glNormal3f(0, 0, 1)  # Normal apontando para frente
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Face TRASEIRA (Z negativo)
    glColor3f(0, 1, 0)
    glNormal3f(0, 0, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    # Face SUPERIOR (Y positivo)
    glColor3f(0, 0, 1)
    glNormal3f(0, 1, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Face INFERIOR (Y negativo)
    glColor3f(1, 1, 0)
    glNormal3f(0, -1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # Face DIREITA (X positivo)
    glColor3f(1, 0, 1)
    glNormal3f(1, 0, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    # Face ESQUERDA (X negativo)
    glColor3f(0, 1, 1)
    glNormal3f(-1, 0, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    glEnd()

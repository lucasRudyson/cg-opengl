from OpenGL.GL import *

def draw_plataforma():
    """Desenha uma plataforma/chão para o cenário"""
    glPushMatrix()
    glTranslatef(0, 0, 0)  # Abaixo dos personagens

    # Plataforma principal
    glColor3f(0.3, 0.5, 0.3)  # Verde grama
    glNormal3f(0, 1, 0)  # Normal apontando para cima

    glBegin(GL_QUADS)
    size = 10  # Tamanho da plataforma
    glVertex3f(-size, 0, -size)
    glVertex3f(size, 0, -size)
    glVertex3f(size, 0, size)
    glVertex3f(-size, 0, size)
    glEnd()

    glPopMatrix()
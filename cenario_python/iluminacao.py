from OpenGL.GL import *
from OpenGL.GLU import *
def iluminacoes():
    glEnable(GL_LIGHTING)  # Ativar sistema de iluminação
    glEnable(GL_LIGHT0)    # Ativar a luz 0 (OpenGL tem várias luzes)
    glEnable(GL_COLOR_MATERIAL)  # Permitir que as cores dos objetos sejam afetadas pela luz
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Posição da luz (x, y, z, w) - w=1 significa luz posicional
    light_position = [10, 10, 10, 1]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Cor da luz ambiente (luz geral fraca)
    ambient_light = [0.2, 0.2, 0.2, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)

    # Cor da luz difusa (luz principal)
    diffuse_light = [1.0, 1.0, 1.0, 1.0]  # Luz branca
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)

    # Cor da luz especular (brilho)
    specular_light = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)

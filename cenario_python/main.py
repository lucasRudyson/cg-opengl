import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubo import draw_cubo
from iluminacao import iluminacoes
from bloco import draw_block
from steve import draw_steve
from io_dota import draw_io
from plataforma import draw_plataforma

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Meu Cenário 3D")

    init_opengl()

    clock = pygame.time.Clock()
    running = True
    mao_angulo = 0

    # CÂMERA DE FRENTE:
    camera_x, camera_y, camera_z = 1.5, 1, -10
    camera_yaw = -180  
    camera_pitch = 0 

    while running:
        # CONTROLE COM TECLADO:
        keys = pygame.key.get_pressed()
        move_speed = 0.1

        # Calcular direção da câmera
        yaw_rad = math.radians(camera_yaw)

        # LUZ FIXA (não se move)
        glLightfv(GL_LIGHT0, GL_POSITION, [5, 5, 5, 1])

        # W/S - Frente/Trás
        if keys[K_w]:
            camera_x += move_speed * math.sin(yaw_rad)
            camera_z -= move_speed * math.cos(yaw_rad)
        if keys[K_s]:
            camera_x -= move_speed * math.sin(yaw_rad)
            camera_z += move_speed * math.cos(yaw_rad)

        # A/D - Esquerda/Direita
        if keys[K_a]:
            camera_x -= move_speed * math.cos(yaw_rad)
            camera_z -= move_speed * math.sin(yaw_rad)
        if keys[K_d]:
            camera_x += move_speed * math.cos(yaw_rad)
            camera_z += move_speed * math.sin(yaw_rad)

        # ESPAÇO/SHIFT - Cima/Baixo
        if keys[K_SPACE]:
            camera_y += move_speed
        if keys[K_LSHIFT]:
            camera_y -= move_speed

        # SETAS - Rotacionar câmera
        rotation_speed = 2
        if keys[K_LEFT]:
            camera_yaw -= rotation_speed
        if keys[K_RIGHT]:
            camera_yaw += rotation_speed
        if keys[K_UP]:
            camera_pitch -= rotation_speed
            camera_pitch = min(89, camera_pitch)
        if keys[K_DOWN]:
            camera_pitch += rotation_speed
            camera_pitch = max(-89, camera_pitch)

        # J - Levantar braço
        if keys[K_j]:
            mao_angulo = min(180, mao_angulo + 3)
        else:
            mao_angulo = max(0, mao_angulo - 3)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # RENDERIZAÇÃO
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ATUALIZAR CÂMERA:
        glLoadIdentity()
        glRotatef(camera_pitch, 1, 0, 0)
        glRotatef(camera_yaw, 0, 1, 0)
        glTranslatef(-camera_x, -camera_y, -camera_z)

        # DESENHAR OBJETOS
        glPushMatrix()
        draw_plataforma()
        glPopMatrix()

        glPushMatrix()
        draw_steve(mao_angulo) 
        glPopMatrix()

        glPushMatrix()
        draw_io(position_x=4, position_z=0)
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.7, 1.0, 1.0)

    iluminacoes()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


if __name__ == "__main__":
    main()

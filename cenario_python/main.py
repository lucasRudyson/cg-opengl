import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubo import draw_cubo
from iluminacao import iluminacoes
from bloco import draw_block
from stive import draw_steve
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Meu Cenário 3D")

    init_opengl()

    clock = pygame.time.Clock()
    running = True
    rotacao_angulo = 0

    mao_angulo = 0

    # CÂMERA DE FRENTE:
    camera_x, camera_y, camera_z = 0, 0, -8
    camera_yaw = 180  # Olhando para o cubo
    camera_pitch = 0  # Sem inclinação

    while running:
        # CONTROLE COM TECLADO:
        keys = pygame.key.get_pressed()
        move_speed = 0.1

        # Calcular direção da câmera
        import math
        yaw_rad = math.radians(camera_yaw)
        light_x = 5 * math.sin(rotacao_angulo * 0.05)
        light_z = 5 * math.cos(rotacao_angulo * 0.05)
        glLightfv(GL_LIGHT0, GL_POSITION, [light_x, 5, light_z, 1])

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
            camera_pitch = min(89, camera_pitch)  # Limitar
        if keys[K_DOWN]:
            camera_pitch += rotation_speed
            camera_pitch = max(-89, camera_pitch)  # Limitar

        if keys[K_j]:
            mao_angulo = min(180, mao_angulo + 3)  # Levantar até 180°
        else:
            mao_angulo = max(0, mao_angulo - 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ATUALIZAR CÂMERA:
        glLoadIdentity()
        glRotatef(camera_pitch, 1, 0, 0)
        glRotatef(camera_yaw, 0, 1, 0)
        glTranslatef(-camera_x, -camera_y, -camera_z)

        glPushMatrix()
        (rotacao_angulo, 0, 1, 0)  
        draw_steve(mao_angulo) 
     
        glPopMatrix()
    



        rotacao_angulo += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.7, 1.0, 1.0)

    # iluminacoes()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,
                   800/600,
                   0.1,
                   50.0)
    glMatrixMode(GL_MODELVIEW)



def setup_camera():
    glLoadIdentity()
    gluLookAt(0,0,8,
              0,0,0,
              0,1,0)




if __name__ == "__main__":
    main()

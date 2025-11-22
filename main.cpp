#include <GL/glut.h>

void init() {
    glEnable(GL_DEPTH_TEST); // Habilita o buffer de profundidade (3D)
    glClearColor(0.1, 0.1, 0.1, 1.0); // Cor de fundo
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // Limpa a tela e profundidade

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    // Câmera (posição, alvo, eixo "up")
    gluLookAt(0.0, 2.0, 5.0,  // posição da câmera
              0.0, 0.0, 0.0,  // ponto que ela olha
              0.0, 1.0, 0.0); // eixo vertical

    // 🔸 Iluminação
    GLfloat light_position[] = { 1.0, 2.0, 1.0, 1.0 };
    GLfloat light_color[] = { 1.0, 1.0, 1.0, 1.0 };
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color);

    // 🔸 Objeto — cubo
    glColor3f(0.5, 0.5, 1.0);
    glutSolidCube(1.5);

    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)w/h, 1.0, 100.0); // 🔸 Projeção
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Cenario 3D com Iluminacao");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);

    glutMainLoop();
    return 0;
}

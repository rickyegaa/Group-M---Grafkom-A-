from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inisialisasi Variabel
window = 0
width, height = 500, 500
field_width, field_height = 50, 50

snake = [(40, 40),(39, 40),(38, 40)]
snake_dir =(1, 0)
interval = 300
food = [(25,25)]
state='right'
score = 0
collision = False
r,g,b = 1,1,1

# Fungsi Untuk Mengatur Tampilan 2D Pada Jendela Permainan
def custom_2D_gameWindow(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, internal_width, 0, internal_height)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# Fungsi Membuat Map/Arena Batas Bidang Permainan
def board():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(2,2)
    glVertex2f(3,2)
    glVertex2f(3,45)
    glVertex2f(2,45)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(2,46)
    glVertex2f(2,45)
    glVertex2f(48,45)
    glVertex2f(48,46)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(47,45)
    glVertex2f(48,45)
    glVertex2f(48,2)
    glVertex2f(47,2)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(2,2)
    glVertex2f(2,3)
    glVertex2f(48,3)
    glVertex2f(48,2)
    glEnd()

# Fungsi Untuk Menampilkan Skor Pada Jendela Permainan
def score_display():
    glColor3f(0,1,0)
    glRasterPos2f(1, 47)
    score_str = "Score : {}".format(score)
    for char in score_str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

# Fungsi Untuk Menggambar Persegi Panjang Dengan Sudut Kiri Atas di (x, y), lebar Width, dan Tinggi Height.
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Fungsi Untuk Menggambar Seluruh Tubuh Ular
def draw_snake():
    glColor3f(r,g,b)
    for x, y in snake:
        draw_rect(x, y, 1, 1)

# Fungsi untuk Menggambar Makanan Ular
def draw_food():
    glColor3f(0, 1, 0)
    draw_rect(food[0][0], food[0][1], 1, 1)

# Fungsi Untuk Menggambar Semua Elemen Tampilan Permainan Seperti Makanan, Ular, Skor, dan Batasan Bidang.
def draw_display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    custom_2D_gameWindow(width, height, field_width, field_height)
    draw_food()
    draw_snake()
    board()
    score_display()
    glutSwapBuffers()

# Inisialisasi GLUT
if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Snake Slither (Group M : Grafika Komputer A)")
    glutDisplayFunc(draw_display)
    glutIdleFunc(draw_display)
    glutMainLoop()

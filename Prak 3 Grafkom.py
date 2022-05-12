#Nama         : Nurma Sari Laras Aji
#NIM          : 20051397062
#Prodi/Kelas  : D4 Manajemen Informatika/2020B

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MenggambarGarisMenggunakanBresenham(x1,y1,x2,y2,):
    #menghitung dx dan dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    #menghitung parameter 
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
        
   #menentukan titik awal dan akhir
    if (abs(x1) > abs(x2)):
        x = x2
        y = y2
        xend = abs(x1)
    else:
        x = x1
        y = y1
        xend = abs(x2)
        
    #memulai menggambar Bresenham
    #membersihkan window 
    glClear(GL_COLOR_BUFFER_BIT)
    #menentukan warna 
    glColor3f(1.0,0.0,0.0)
    #spesifikasikan diameter dari pixel yang akan digambar
    glPointSize(10.0)
    #memilih mode point
    glBegin(GL_POINTS)
    
    #looping untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2f(x, y)

    glEnd()
    glFlush()


def main():
    x1 = int(60)
    y1 = int(40)
    x2 = int(50)
    y2 = int(70)
    
    #inisialisasi glut
    glutInit(sys.argv)
    #inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_RGB)
    #inisialisasi ukuran layar glut
    glutInitWindowSize(500,500)
    #inisialisasi posisi layar glut
    glutInitWindowPosition(0,0)
    #inisialisasi pembuatan window
    glutCreateWindow("Menggambar Garis Bresenham")
    glutDisplayFunc(lambda: MenggambarGarisMenggunakanBresenham(x1,y1,x2,y2))
    glutIdleFunc(lambda: MenggambarGarisMenggunakanBresenham(x1,y1,x2,y2))

    #membersihkan layar dan memberikan warna
    glClearColor(0.0,0.0,0.0,0.1)
    #set origin dari grid dan ukurannya 100x100
    gluOrtho2D(0,100,0,100)
    glutMainLoop()

main()  
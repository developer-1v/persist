'''
TODO:
    - Ensure that at least while i'm testing, that we .gitignore by default
    all build/dist folders... So make this an optional arg, that for
    me is set to true but for production is set to false. 
    
    

DIFFICULT libraries to get to compile: 
- My goal is to have these libraries as tests, to try to get my apps to compile with them.

When compiling Python applications into an executable (exe) using tools like PyInstaller, cx_Freeze, or Py2exe, certain libraries can pose challenges due to their complexity, dependencies, or the way they interact with the system. Here are some libraries that are notoriously difficult to handle:
1. pygame: Pygame can be tricky because it relies heavily on SDL libraries and often requires additional configuration to ensure all multimedia resources are included in the executable.
2. tkinter: While generally well-supported, tkinter can sometimes cause issues, especially with locating and embedding the necessary Tcl/Tk libraries.
3. matplotlib: This library can be problematic due to its numerous backend dependencies and the need to include additional data files and DLLs.
4. numpy and scipy: These libraries are complex due to their C extensions and dependencies on other libraries like BLAS and LAPACK. Ensuring all binary dependencies are correctly packaged is crucial.
5. pandas: Similar to numpy and scipy, pandas can be difficult because it depends on several other libraries and sometimes requires specific versions of these libraries.
6. tensorflow or pytorch: These machine learning libraries are large and have numerous dependencies, making them challenging to package into a single executable.
7. kivy: Kivy applications can be difficult to compile into an exe because of their graphical and event-driven nature, requiring specific OpenGL and other graphical backend dependencies.
sqlalchemy: While not as complex as graphical libraries, sqlalchemy can still pose challenges due to its dynamic and flexible nature, especially when dealing with different database backends.

'''





import math, sys, os 








''' TEST '''





''' TEST '''
from print_tricks import pt
from icecream import ic

var = math.pi
pt(var)
ic(var)
# while True: 
#     ...

''' TEST '''
from ursina import *

# app = Ursina(development_mode=False)
# ee = Entity(model='cube', color=color.rgba(1, 0, 0, 1), rotation=(44, 44, 44))
# EditorCamera()
# pt(application.development_mode)
# pt(ee)
# app.run()


''' TEST '''
# import pygame
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((400, 300))

#     rect_surface = pygame.Surface((100,50))
#     rect_surface.fill((255, 255, 255))  # Fill the rectangle surface with white color

#     size = 0
#     while True:
#         screen.fill((0, 0, 0))
#         size += .1  
#         new_rect = pygame.transform.rotate(rect_surface, size)
#         screen.blit(new_rect, (0,0))
#         pygame.display.flip()

# main()


''' TEST '''
import pygame
def main():
    pygame.init()
    size = width, height = 640, 480
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    # Load an image, which must be in the same directory as the script
    ball = pygame.image.load(f"{os.path.join(os.getcwd(), 'test_source_dir', 'ball.png')}")
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        pygame.time.delay(10)

main()

''' TEST '''
# import tkinter
# pt(tkinter.TclVersion)
# from tkinter import messagebox

# def on_button_click():
#     messagebox.showinfo("Information", "Hello, Tkinter!")

# app = tkinter.Tk()
# app.title("Tkinter Example App")
# button = tkinter.Button(app, text="Click Me", command=on_button_click)
# button.pack(pady=20)

# app.mainloop()

''' TEST '''
# import matplotlib
# matplotlib.use('TkAgg')  # Set the backend to TkAgg
# import matplotlib.pyplot as plt
# import numpy as np
# import sys

# def plot_data():
#     # Generate some data
#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)

#     # Create a plot
#     plt.figure()
#     plt.plot(x, y, label='sin(x)')
#     plt.title('Sine Wave')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.legend()
#     plt.show()

# plot_data()



''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''

''' TEST '''


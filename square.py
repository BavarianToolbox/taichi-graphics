import taichi as ti

ti.init(arch = ti.cpu)

n = 200
pixels = ti.field(dtype = float, shape = (n, n))

@ti.func
def square():


    return ...

@ti.kernel
def paint(t: int):
    for i, j in pixels:
        pixels[i,j]

gui = ti.GUI("Growing Square", res = (n, n))

i = 0
while gui.running:
    paint(i)
    gui.set_image(pixels)
    gui.show()
    i += 1
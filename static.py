import taichi as ti

ti.init(arch=ti.cpu)

n = 320
pixels = ti.field(dtype = float, shape = (n, n))

@ti.kernel
def paint():
    for i, j in pixels:
        pixels[i, j] = ti.random()

gui = ti.GUI("Static", res = (n, n))

while gui.running:
    paint()
    gui.set_image(pixels)
    gui.show()
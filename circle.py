import taichi as ti

ti.init(arch=ti.cpu)

n = 320
pixels = ti.field(dtype = float, shape = (n, n), offset = (-160, -160))

@ti.func
def circle(r, i, j):
    ret = 0.1
    if i**2 + j**2 == r**2:
        ret = 1
    # else:
    #     ret = 0
    return ret

@ti.kernel
def paint(t: int):
    for i, j in pixels:
        pixels[i, j] = circle(t, i, j)

gui = ti.GUI("Growing Circle", res = (n, n))

i = 0
while gui.running:
    # for i in range (1000000):
    paint(i % 160)
    gui.set_image(pixels)
    gui.show()
    i += 1
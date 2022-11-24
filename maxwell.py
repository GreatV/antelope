# Baumgarte, Thomas & Shapiro, Stuart. (2021). Numerical Relativity: Starting from Scratch. 10.1017/9781108933445.

import taichi as ti

arch = ti.vulkan if ti._lib.core.with_vulkan() else ti.cuda
ti.init(arch=arch)


@ti.data_oriented
class Maxwell:
    def __init__(self, n_grid, x_out, n_vars):
        self.n_grid = n_grid
        self.n_vars = n_vars
        self.delta = x_out / (n_grid - 2.0)

        self.x = ti.field(ti.f64, shape=n_grid)
        self.y = ti.field(ti.f64, shape=n_grid)
        self.z = ti.field(ti.f64, shape=n_grid)
        self.r = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))

        self.E_x = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))
        self.E_y = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))
        self.E_z = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))

        self.A_x = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))
        self.A_y = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))
        self.A_z = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))

        self.phi = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))
        self.constraint = ti.field(ti.f64, shape=(n_grid, n_grid, n_grid))

        # keep track of time
        self.t = 0.0
    
    def initialize(self):
        pass


        


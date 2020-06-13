'''
Agosh Saini - as7saini@uwaterloo.ca
2D Diffusion Function using fick's law

Resources used:
    http://math.tifrbng.res.in/~praveen/notes/cm2013/heat_2d.pdf
    https://en.wikipedia.org/wiki/Finite_volume_method_for_two_dimensional_diffusion_problem#cite_note-3
    http://opencourses.emu.edu.tr/course/view.php?id=27&lang=en
'''
# =========================================
''' Importing Modules '''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ==========================================
''' Global Variables '''
bd_condition_x, bd_condition_y = 100, 100

t_rng, x_rng, y_rng = np.array([0,1]), np.array([0,1]), np.array([0,1]) 

nt, nx, ny = 9606, 50, 50

coeff = 1

dt, dx, dy = (t_rng[1]-t_rng[0])/(nt-1), (x_rng[1]-x_rng[0])/(nx-1), (y_rng[1]-y_rng[0])/(ny-1)
# =======================================
''' Functions '''

def check_stability(dx, dy, dt, t_rng, coeff):
    # ==== Step 1: Stability Check ====== #
    max_dt = (1 / (2*coeff)) * (dx*dy)**2 / (dx**2 + dy**2)
    
    # returns a stable nt
    if dt > max_dt: 
        nt_stable = (t_rng[1]-t_rng[0]) / max_dt + 1
        raise Exception('time step too large, system unstable. use nt of ' + str(nt_stable))


def grid_formation (nt, nx, ny):
    # === Step 2: Grid Formation ====== #
    
    grid = np.zeros([nt, nx, ny])
    
    return grid

def boundary_cond(grid, bd_condition_x, bd_condition_y, nx, ny):
    # ==== Step 3: Boundary Condition ===== #
    grid[0, :, 0] = bd_condition_x * np.ones(nx)
    grid[0, 0, :] = bd_condition_y * np.ones(ny)
    
    return grid

def diffusion_interation(u, dt, dx, dy, nt, coeff):
    # ======= Step 4: Interating over time ======= #
    
    # aplha and beta are all the constants used in the scheme
    alpha, beta = coeff**2*dt/dx**2, coeff**2*dt/dy**2
    
    # this is an FTCS scheme
    for i in range(nt - 1):
        u_x = alpha*(u[i, 2:, 1:-1] - 2*u[i, 1:-1, 1:-1] + u[i, :-2, 1:-1])
        
        u_y = beta*(u[i, 1:-1, 2:] - 2*u[i, 1:-1, 1:-1] + u[i, 1:-1, :-2])
        
        u[i+1, 1:-1, 1:-1] = u[i, 1:-1, 1:-1] + u_x + u_y 
        
    return u

def images(grid, nt):
    # ======== Step 5: Creating images ======= #    
    for i in range(nt):
        t_step_grid = grid[i,:,:]
        plt.imshow(t_step_grid, cmap=cm.get_cmap('hot'))
        plt.savefig("data/"+str(i))

# ========================================================
''' Running All Functions '''        

# stability check
check_stability(dx, dy, dt, t_rng, coeff)

# Running the difusion 
grid = grid_formation(nt, nx, ny)
grid = boundary_cond(grid, bd_condition_x, bd_condition_y, nx, ny)
grid = diffusion_interation(grid, dt,dx, dy,nt, coeff)


# Generating Images 
images(grid, nt)


    





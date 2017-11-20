
# coding: utf-8

# Tools to study different variations of the the somma cube
# ----------------------------------
# ---------------------------------

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Rotation, shifting and transposition of 2D--shapes
# ----------------------------------------------------------------

# In[2]:


def shift_fX(x):
    shift_order_fX = [8, 0, 1, 2, 3, 4, 5, 6, 7]
    return [x[i] for i in  shift_order_fX] 

def shift_bX(x):
    shift_order_bX = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return [x[i] for i in  shift_order_bX] 

def shift_fY(x):
    shift_order_fY = [6, 7, 8, 0, 1, 2, 3, 4, 5]
    return [x[i] for i in  shift_order_fY] 

def shift_bY(x):
    shift_order_bY = [3, 4, 5, 6, 7, 8, 0, 1, 2]
    return [x[i] for i in  shift_order_bY]

def transposition(x):
    transpose_order = [0,3,6,1,4,7,2,5,8] 
    return  [x[i] for i in transpose_order]


# In[3]:


def turn(x):
    turn_order =   [6,3,0,7,4,1,8,5,2] 
    return  [x[i] for i in turn_order]


# Graphical representation of 2D shapes
# ------------------------------------------------

# In[4]:


def build_shape(x):
    dx = 1/3
    pos_2d ={
         0:(0,0), 
         1:(dx,0),
         2:(2*dx,0),
         3:(0,dx), 
         4:(dx,dx),
         5:(2*dx,dx), 
         6:(0,2*dx), 
         7:(dx,2*dx),
         8:(2*dx,2*dx)}
    pieces = []
    frame = patches.Rectangle(
        (0.0, 0.0),1, 1, fill=False, edgecolor="red",linewidth=2) 
    pieces.append(frame)
    for i in range(9):
        if x[i]==1:
            p = patches.Rectangle(pos_2d[i], dx,dx, fill=True)
            pieces.append(p)
    return pieces


# In[5]:


def show_shape(x):
    ax1=plt.subplot(111,aspect='equal')
    shape = build_shape(x)
    for p in shape: ax1.add_patch(p)
    plt.axis('off')
    plt.show() 


# Spatial rotation and shifting of 3D--shapes
# ----------------------------------------------------

# In[6]:


def shift3D_fX(x):
    return  shift_fX(x[0:9]) + shift_fX(x[9:18])+ shift_fX(x[18:27])

def shift3D_bX(x):
    return  shift_bX(x[0:9]) + shift_bX(x[9:18])+ shift_bX(x[18:27])

def shift3D_fY(x):
    return  shift_fY(x[0:9]) + shift_fY(x[9:18])+ shift_fY(x[18:27])

def shift3D_bY(x):
    return  shift_bY(x[0:9]) + shift_bY(x[9:18])+ shift_bY(x[18:27])

def shift3D_fZ(x):
    return x[18:27] + x[0:9] + x[9:18]

def shift3D_bZ(x):
    return x[9:18] + x[18:27] + x[0:9]


# In[7]:


def turn3D_Z(x):
    return  turn(x[0:9])+ turn(x[9:18])+ turn(x[18:27])

def turn3D_Y(x):
    turn_order_Y = [18,  9,  0, 21, 12,  3, 24, 15,  6, 19, 10,  1, 22, 13,  4, 25, 16,
                   7, 20, 11,  2, 23, 14,  5, 26, 17,  8]
    return  [x[i] for i in turn_order_Y]

def turn3D_X(x):
    turn_order_X = [18, 19, 20,  9, 10, 11,  0,  1,  2, 21, 22, 23, 12, 13, 14,  3,  4,
        5, 24, 25, 26, 15, 16, 17,  6,  7,  8]
    return  [x[i] for i in turn_order_X]


# Graphical representation of the horizontal sections of the cube
# ---------------------------------------------------------------

# In[8]:


def show3D_shape(x):
    ax1 = plt.subplot(131,aspect='equal')
    shape = build_shape(x[:9])
    for p in shape: ax1.add_patch(p)
    plt.axis('off')
    ####################
    ax2=plt.subplot(132,aspect='equal')
    shape = build_shape(x[9:18])
    for p in shape: ax2.add_patch(p)
    plt.axis('off')
    ##########################
    ax3=plt.subplot(133,aspect='equal')
    shape = build_shape(x[18:])
    for p in shape: ax3.add_patch(p)
    plt.axis('off')
    ###################
    plt.show() 


# Some shapes mading up the Soma cube and several of its variations: black devil and red devil
# ------------------------------------------------------------------

# Soma
# -----

# In[9]:


AA = [1,0,0,1,0,0,0,0,0,
      0,0,0,1,1,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomA = (1,1,1)

BB = [0,0,0,1,1,0,0,0,0,
      1,0,0,1,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomB = (1,1,1)
LL = [1,1,0,1,0,0,1,0,0,
      0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomL = (1,2,0)
PP = [1,0,0,0,0,0,0,0,0,
      1,1,0,1,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomP = (1,1,1)
TT = [1,1,1,0,1,0,0,0,0,
      0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0]
#freedomT = (0,1,2)
VV = [1,1,0,1,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomV = (1,1,2)
ZZ = [1,1,0,0,1,1,0,0,0,
      0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0] 
#freedomZ = (0,1,2)


# Black devil
# -------------

# The black devil is made up of six polycubes: AA, BB, LL, TTB, GAB, ZZB, three of which are share with the Soma cube. Therefore it suffies to describe GAB, TTB and ZZB only.

# In[10]:


GAB = [1,0,0,1,0,0,1,1,0,
       0,0,0,0,0,0,0,1,0,
       0,0,0,0,0,0,0,0,0]
#freedomGAB = (1,0,1)
TTB = [1,0,0,1,1,0,1,0,0,
       1,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0]
#freedomTTB = (1,0,1)
ZZB = [0,0,0,1,0,0,0,0,0,
       1,1,0,1,0,0,0,0,0,
       0,1,0,0,0,0,0,0,0]
#freedomZZB = (1,1,0)


# Red devil
# -----------

# The Red devil cube is made up of six polycubes: AA, BB, LL, GAR, TTI, ZZR

# In[11]:


GAR = [1,1,1,0,0,0,0,0,0,
       1,0,0,1,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0] 

TTR =  [1,1,1,0,0,1,0,0,0,
        0,1,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0] 

ZZR =  [0,1,1,0,1,0,0,0,0,
        0,0,0,1,1,0,0,0,0,
        0,0,0,0,0,0,0,0,0] 


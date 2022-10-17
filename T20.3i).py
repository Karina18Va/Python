import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def fun(x,f):

    try:
        y = f(x)
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.zeros(n)
        for i in range(n):
            y[i] = f(x[i])
    return y

def func(x,k):
    s=np.ones(x.size)
    for n in range(1,k):
        t = ((-1)**n)*n*(x**(n-1))
        s += t
    return s

fig=plt.figure()
ax=plt.axes(xlim=(-2,2),ylim=(0,2))
line,=ax.plot([],[],lw=1)

def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(n):
    x=np.linspace(-2,1,100)
    y =func(x,n)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=500, blit=True)


xx=np.linspace(-2,1,100)
s=fun(xx,np.exp)
plt.plot(xx,s,'r')

plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
##x(s)=a sin(ps),y(s)=b sin(qs+t)

##0<=s<=2pi,t∈[0,π/2]
#X=np.arange(-2*np.pi,2 * np.pi,0.001)
#length = len(X)

#a = eval(input("Please input 'a' in   a * cos(p*theta) "))
#b = eval(input("Please input 'b' in   b * cos(q*theta + t) "))
#p = eval(input("Please input 'p' in   a * cos(p*theta) "))
#q = eval(input("Please input 'q' in   b * cos(q*theta + t) "))
#t = np.pi/4

#Ysin=a * np.cos(p * X)

#Ysin1=b * np.cos(q*X + t)
##plt.plot(X,Ysin,"b-",label='Ysin',linewidth=2.0)
##plt.plot(X,Ysin*2,color="red",linestyle="--",linewidth=2.0,label="Ysin *2")
##plt.plot(X,Ysin1,"c-.",linewidth=2.0,label="Ysin1")
##plt.plot(Ysin,,color="black",linestyle=":",linewidth=2.0,label="Ysin1*2")
#flag = 10

#plt.plot(Ysin[:],Ysin1[:],color="black",linestyle=":",linewidth=2.0,label="Ysin1*2")


#plt.legend()
#plt.grid(True)
#plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], color = "black", linestyle= ":",  animated=False)

a = eval(input("Please input 'a' in   a * cos(p*theta) "))
b = eval(input("Please input 'b' in   b * cos(q*theta + t) "))
p = eval(input("Please input 'p' in   a * cos(p*theta) "))
q = eval(input("Please input 'q' in   b * cos(q*theta + t) "))
print("If you wanna input π, just use pi first and arithmetic after it")
t = eval("np." + input("Please input 't' in   b * cos(q*theta + t) "))





def init():
    global a, b
    ax.set_xlim(-b-1, b+1)
    ax.set_ylim(-a-1.1,a + 1)
    return ln,

def update(frame):
    global ln
    global xdata
    global ydata
    global a,b,p,q,t
    Ysin=a *  np.cos(p * frame + t)
    Ysin1=b * np.cos(q * frame)
    xdata.append(Ysin)
    ydata.append(Ysin1)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 50),
                    init_func=init, blit=True)
plt.show()


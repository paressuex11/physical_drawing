import numpy as np
import matplotlib.pyplot as plt

X=np.arange(-np.pi,np.pi,0.1)

Ysin=np.sin(X)

Ycos=np.cos(X)
plt.plot(X,Ysin,"b-",label='Ysin',linewidth=2.0)
plt.plot(X,Ysin*2,color="red",linestyle="--",linewidth=2.0,label="Ysin *2")
plt.plot(X,Ycos,"c-.",linewidth=2.0,label="Ycos")
plt.plot(X,Ycos*2,color="black",linestyle=":",linewidth=2.0,label="Ycos*2")

plt.legend()
plt.grid(True)
plt.show()
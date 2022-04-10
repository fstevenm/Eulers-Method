""" Euler's Method """

import numpy as np
import matplotlib.pyplot as plt

# differential equations
def f(x,y):
    return (x-y)/2

# exact solution
def exact():
    global t1,y1,y_exact
    t1 = np.arange(0,3,0.01)
    y_exact = lambda t: t - 2 + (3/(np.e**(0.5*t)))
    y1 = y_exact(t1)


def euler(f,a,b,h,y_init,color):
    n = int( (b-a)/h + 1 )
    print("Number of intervals =",n,"with h =",h)
    
    xs = a + np.arange(n)*h
    ys = np.zeros(n)
    y = y_init
    
    print("-----------------------------------------------------------------------")
    print("| iteration\t |    x\t   |     y\t\t   |   y exact\t  | absolute relative error |")
    print("-----------------------------------------------------------------------")
    
    for j,x in enumerate(xs):
#        y = float('%.5f'%(y))
        ys[j] = y
        
#        error_relatif = abs((float('%.5f'%(ys[j])) - float('%.5f'%(y_exact(x))))/float('%.5f'%(y_exact(x))) )
        error_relatif = abs((ys[j]-y_exact(x))/y_exact(x))
        
        """print the results"""
        print("|    %.0f\t    |"%(j)," %.4f\t|"%(xs[j]),
              "  %.5f\t\t|"%(ys[j]),"  %.5f\t  |"%(y_exact(x)),
              "      %.5f\t\t     |"%(error_relatif))
        
        y += h*f(x,y)

    print("-----------------------------------------------------------------------")
    
    plt.plot(xs,ys, color, label = 'Eulers method h={}'.format(h))
    
    return xs[-1],ys[-1]


exact()
euler(f,0,3,0.25,1,'bo--')

plt.plot(t1,y1,'r',label = 'Exact Solutions')
plt.title('Comparison between Eulers Method\nand its exact solutions')
plt.xlabel('t')
plt.ylabel('Value of y')
plt.axis([0,3,0,2])
plt.legend(loc = 'best')
plt.grid()
plt.show()



""" You can also use this syntax (code program) below """

#def euler(y_0,a,b,h):
#    M = int((b-a)/h)
#    t = a
#    y = y_0
#    t_e = np.array([t])
#    y_e = np.array([y])
#    while t < b:
#        y += h*f(t,y)
#        t += h
#        t_e = np.append(t_e,t)
#        y_e = np.append(y_e,y)
#        
#    print('\n----------SOLUTION----------')
#    print('-------Eulers method---------')    
#    print('k\tt_k\ty_k')
#    print('----------------------------')
#    for i in range(M+1):
#        print('%.f\t%.1f\t%.7f'% (i,t_e[i],y_e[i]))
#    
#    plt.plot(t_e,y_e,'--o',label='Eulers method h={}'.format(h))
#
#euler(1,0,3,0.5)

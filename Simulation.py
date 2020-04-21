
import matplotlib
matplotlib.use('Tkagg')
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
global t ,x ,y , z,h2
t=0
def update_line(hl,h2, new_data,de=False):
	xdata, ydata, zdata = hl._verts3d
	if de == False :

		hl.set_xdata(list(np.append(xdata, new_data[0])))
		hl.set_ydata(list(np.append(ydata, new_data[1])))
		hl.set_3d_properties(list(np.append(zdata, new_data[2])))
        #  	xdata1, ydata1, zdata1 = h2._verts3d
		h2.set_xdata(list([0, new_data[0]]))
		h2.set_ydata(list([0,new_data[1]]))
		h2.set_3d_properties(list([0, new_data[2]]))
		plt.draw()


def excitation(W,T1,T2,flip_angle):
    no_of_p = 3
    x = [0]*no_of_p 
    y = [0]*no_of_p 
    z = [1]*no_of_p 
    t = 0
    color = [['b','r'] , ['g','y'] , ['c' ,'m'] ]
    h1=[0]*3
    h2=[0]*3
    for i in range(no_of_p):
        h1[i], = map_ax.plot3D([x[i]], [y[i]], [z[i]],color[i][0])
        h2[i], = map_ax.plot3D([0], [0], [0],color[i][1]) 
 
    
    excitation_period  = ( (np.cos((flip_angle/180)*3.1415))**2  + 0.019)
    end_excitation = excitation_period

    while (min(z) > end_excitation ):
        for i in range(len(W)):
            #MX
            x[i] = 1*(1 -np.exp(-1*(t/T2))) *np.sin(W[i]*t)
            
            #My
            y[i] = 1*(1- np.exp(-1*(t/T2)))*np.cos(W[i]*t)
            
            #Mz 
            z[i]= 1*( np.exp(-1*(t/T1))) 
            
            update_line(h1[i],h2[i], (x[i],y[i], z[i]))
            t= t + 0.001
            plt.show(block=False)
            plt.pause(0.00000001)
        
    return  z , y ,x,h2

def relaxation(W,T1,T2,flip_angle,z,y,x,h2):
    t=[0]*3
    h3=[0]*3
    for i in range(3):
        t[i] = -1*np.log(1 -(z[i]))*T1
        #Mx
        x[i] = 1*(np.exp(-1*(t[i]/T2))) *np.sin(W[i]*t[i])    
        #My 
        y[i] = 1*(np.exp(-1*(t[i]/T2)))*np.cos(W[i]*t[i])    
        #Mz 
        z[i]= 1*(1- np.exp(-1*(t[i]/T1))) 
        h3[i], = map_ax.plot3D([x[i]], [y[i]], [z[i]],color[i][0])
    #h2, = map_ax.plot3D([0], [0], [0],color= 'r') 
    while (max(z)< 0.98): 
        for i in range(3):
            #Mx = 2*np.exp(t/T2) np.sin(W*t)
            x[i] = 1*(np.exp(-1*(t[i]/T2))) *np.sin(W[i]*t[i])
            
            #My = 2*np.exp(t/T2) np.cos(W*t)
            y[i] =1*(np.exp(-1*(t[i]/T2)))*np.cos(W[i]*t[i])
            
            #Mz = 10*(1 -np.exp(t/T1))
            z[i]= 1*(1- np.exp(-1*(t[i]/T1))) 
            
            #ax.plot([0,1],[0,1] ,[0,1], zdir='z')
            update_line(h3[i],h2[i], (x[i],y[i], z[i]))
            t[i]= t[i] + 0.001
            plt.show(block=False)
            plt.pause(0.00000001)
 
def get_parameters():
    W = []
    for i in range(3):
        b= float(input(f"Enter B no {i+1} in Micro: "  )) 
        w = 42.6 * b 
        dw = w* 3.5*10**(-6)
        w = w-dw
        W.append(w)
    T1 = float(input("Enter T1 in sec: "))
    T2 = float(input("Enter T2 sec: "))
    flip_angle = float(input("Float angle Degree:  "))
    return W ,T1,T2,flip_angle
 
map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)
 
# # # Setting the axes properties
map_ax.set_xlim3d([-1.0, 1.5])
map_ax.set_ylim3d([-1.0, 1.5])
map_ax.set_zlim3d([-1.0, 1.0])

color = [['b','r'] , ['g','y'] , ['c' ,'m'] ]
patch =[]
for i in range(3):
    patch.append(mpatches.Patch(color=color[i][0], label=f'Trajectory_{i+1}'))
    patch.append(mpatches.Patch(color=color[i][1], label=f'BulkVector_{i+1}'))

plt.legend(handles=patch)

#plt.show()
#get parameters by console
W , T1 ,T2  , flip_angle =get_parameters()
#Excitation
z , y ,x , h2 =excitation(W , T1 ,T2  , flip_angle)
# Relaxiation
relaxation(W , T1 ,T2  , flip_angle,z , y ,x , h2)
 
plt.show(block=True)





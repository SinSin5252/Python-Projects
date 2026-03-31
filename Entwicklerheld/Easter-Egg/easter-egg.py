import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure()

degree_list = list(range(1,360))
egg_list = [np.array([0, 160])]
mx, my = 0, 0 #Ortspunkt
r = 160 #Eigrenze
circle = 160 #minimale grenze zum Ortspunkt
eps = circle * math.sin(math.radians(1))
pointx, pointy = 0 , 0


def place_egg_on_equation():
    return 


#die liste mit den Winkel abarbeiten und für jedes Grad in der liste schauen ob die Entfernung zu allen anderen Eiern passt
#Neue Überlegung: Den ersten Kreis anlegen und den nächsten am ersten angrenzen und zum Ortspunkt am ersten Eigrenze wandern lassen


for element in degree_list[:]:
    
    radiant = math.radians(element)
    pointx = mx + circle * math.cos(radiant)
    pointy = my + circle * math.sin(radiant)
    #degree_eq_y = math.tan(radiant) * degree_eq_x


    #für jeden ei wir die distanz ausgerechnet



    d = math.sqrt((pointx - egg_list[-1][0])**2 + (pointy - egg_list[-1][1])**2)


    if d == r or r + eps >= d > r : 
        egg_list.append(np.array([pointx, pointy]))
        

        if element in degree_list:
            degree_list.remove(element)



print(len(egg_list))



#Notiz: logik wo gegen ende erstes ei vom orbit und letztes ei mit dem nächsten ei verglichen wird. eine schnittgerade könnte als hilfe dienen 
#

for egg in egg_list:

    plt.scatter(egg[0], egg[1])
    winkel = np.linspace(0, 2*np.pi, 360)
    x_circle = egg[0] + r * np.cos(winkel)
    y_circle = egg[1] + r * np.sin(winkel)
    plt.plot(x_circle, y_circle)


plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlim(-2500, 2500)
plt.ylim(-2500, 2500)

plt.grid(True)
plt.gca().set_aspect("equal", adjustable="box")

plt.show()
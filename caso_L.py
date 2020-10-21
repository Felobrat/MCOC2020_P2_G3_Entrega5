from reticulado import Reticulado
from barra import Barra

def caso_L(R=12/100,t = 6/1000):
    # Unidades base
    m = 1.
    kg = 1.
    s = 1.
    g = 9.81 *m/s**2

    #Unidades derivadas
    N = kg*m/s**2
    cm = m/100
    mm = m/1000
    KN = 1000 *N

    Pa = N / m**2
    KPa = 1000 *Pa
    MPa = 1000 *KPa
    GPa = 1000 *MPa

    #Parametros
    P0 = 5*m
    H0 = 100*m
    L = 5.75 *m
    H = 5*m
    B = 2.0 *m
    nodes = 41
    ql = ((400*kg)/(m**2))
    F = (ql*L*B*g)/4.



    #Inicializar modelo
    ret = Reticulado()
    [R,R1,R2,R3,R4]= [R,R,R,R,R]        #linea de soporte
    [t,t1,t2,t3,t4]= [t,t,t,t,t]         #linea de soporte
    R= 11.5/100        #linea de soporte
    t = 5/1000         #linea de soporte
    R1= 9.5/100         #Pasarela
    t1 = 3/1000         #Pasarela
    R2= 8/100         #soporte Pasarela
    t2 = 3/1000         #soporte Pasarela
    R3= 11/100         #columnas
    t3 = 5.5/1000         #columnas
    R4= 6/100         #diagonales
    t4 = 2/1000         #diagonales
    R5= 4/100         #soporte columnas
    t5 = 2/1000         #soporte columnas
    #Inicializar modelo
    ret = Reticulado()
    
    props = [R, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    props1 = [R1, t1, 200*GPa, 7600*kg/m**3, 420*MPa]
    props2 = [R2, t2, 200*GPa, 7600*kg/m**3, 420*MPa]
    props3 = [R3, t3, 200*GPa, 7600*kg/m**3, 420*MPa]
    props4 = [R4, t4, 200*GPa, 7600*kg/m**3, 420*MPa]
    props5 = [R5, t5, 200*GPa, 7600*kg/m**3, 420*MPa]
#Tableros
#Nodos

    for i in range(nodes):
        ret.agregar_nodo(P0+i*L     , 0   , H0         )
        ret.agregar_nodo(P0+i*L     , B   , H0         )
    for i in range(nodes-1):
        ret.agregar_nodo(P0+L/2+i*L     , B/2   , H0+H         )
#Barras (1) pasarela
    for i in range(2*nodes-1):
        ret.agregar_barra(Barra(i, i+1, *props1))
    
    for i in range(nodes-1):
        ret.agregar_barra(Barra(2*i, 2*i+3, *props1))
        ret.agregar_barra(Barra(2*i, 2*i+2, *props1))
        ret.agregar_barra(Barra(2*i+1, 2*i+3, *props1))

#Barras (2) soporte
    for i in range(nodes-2):
        ret.agregar_barra(Barra(2*nodes+i, 2*nodes+i+1, *props))
    
    for i in range(nodes-1):
        ret.agregar_barra(Barra(2*nodes+i, 2*i, *props2))
        ret.agregar_barra(Barra(2*nodes+i, 2*i+1, *props2))
        ret.agregar_barra(Barra(2*nodes+i, 2*i+2, *props2))
        ret.agregar_barra(Barra(2*nodes+i, 2*i+3, *props2))
        

    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
#------------------------------------
    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)
#------------------------------------
    ret.agregar_restriccion(80, 0, 0)
    ret.agregar_restriccion(80, 1, 0)
    ret.agregar_restriccion(80, 2, 0)
#------------------------------------
    ret.agregar_restriccion(81, 0, 0)
    ret.agregar_restriccion(81, 1, 0)
    ret.agregar_restriccion(81, 2, 0)

#Torre
    #Base
    ret.agregar_nodo(115*m     , -2*m   , H0-30*m         )
    ret.agregar_nodo(115*m     , 4*m   , H0-30*m         )
    ret.agregar_nodo(125*m     , -2*m   , H0-30*m         )
    ret.agregar_nodo(125*m     , 4*m   , H0-30*m         )
    
    ret.agregar_restriccion(122, 0, 0)
    ret.agregar_restriccion(122, 1, 0)
    ret.agregar_restriccion(122, 2, 0)
#------------------------------------
    ret.agregar_restriccion(123, 0, 0)
    ret.agregar_restriccion(123, 1, 0)
    ret.agregar_restriccion(123, 2, 0)
#------------------------------------
    ret.agregar_restriccion(124, 0, 0)
    ret.agregar_restriccion(124, 1, 0)
    ret.agregar_restriccion(124, 2, 0)
#------------------------------------
    ret.agregar_restriccion(125, 0, 0)
    ret.agregar_restriccion(125, 1, 0)
    ret.agregar_restriccion(125, 2, 0)
    
    #ESTRUCTURA
    ret.agregar_nodo((115-6.5/3)*m     , (-1)*m   , H0-20*m         )
    ret.agregar_nodo((115-6.5/3)*m     , (3)*m   , H0-20*m         )
    ret.agregar_nodo((125+6.5/3)*m     , -1*m   , H0-20*m         )
    ret.agregar_nodo((125+6.5/3)*m     , 3*m   , H0-20*m         )
    
    ret.agregar_nodo((115-2*6.5/3)*m     , (0)*m   , H0-10*m         )
    ret.agregar_nodo((115-2*6.5/3)*m     , (2)*m   , H0-10*m         )
    ret.agregar_nodo((125+2*6.5/3)*m     , 0*m   , H0-10*m         )
    ret.agregar_nodo((125+2*6.5/3)*m     , 2*m   , H0-10*m         )
    
    
    ret.agregar_nodo((115+5/3)*m     , (-1)*m   , H0-20*m         )
    ret.agregar_nodo((115+5/3)*m     , (3)*m   , H0-20*m         )
    ret.agregar_nodo((125-5/3)*m     , -1*m   , H0-20*m         )
    ret.agregar_nodo((125-5/3)*m     , 3*m   , H0-20*m         )
    
    ret.agregar_nodo((115+2*5/3)*m     , (0)*m   , H0-10*m         )
    ret.agregar_nodo((115+2*5/3)*m     , (2)*m   , H0-10*m         )
    ret.agregar_nodo((125-2*5/3)*m     , 0*m   , H0-10*m         )
    ret.agregar_nodo((125-2*5/3)*m     , 2*m   , H0-10*m         )
    
    ##Columnas (3)
    ret.agregar_barra(Barra(122,126 , *props3))
    ret.agregar_barra(Barra(126,130 , *props3))
    ret.agregar_barra(Barra(130,36 , *props3))
    
    ret.agregar_barra(Barra(123,127 , *props3))
    ret.agregar_barra(Barra(127,131 , *props3))
    ret.agregar_barra(Barra(131,37 , *props3))
    
    ret.agregar_barra(Barra(124,128 , *props3))
    ret.agregar_barra(Barra(128,132 , *props3))
    ret.agregar_barra(Barra(132,44 , *props3))
    
    ret.agregar_barra(Barra(125,129 , *props3))
    ret.agregar_barra(Barra(129,133 , *props3))
    ret.agregar_barra(Barra(133,45 , *props3))
    
    ret.agregar_barra(Barra(122,134 , *props3))
    ret.agregar_barra(Barra(134,138 , *props3))
    ret.agregar_barra(Barra(138,40 , *props3))
    
    ret.agregar_barra(Barra(123,135 , *props3))
    ret.agregar_barra(Barra(135,139 , *props3))
    ret.agregar_barra(Barra(139,41 , *props3))

    ret.agregar_barra(Barra(124,136 , *props3))
    ret.agregar_barra(Barra(136,140 , *props3))
    ret.agregar_barra(Barra(140,40 , *props3))
    
    ret.agregar_barra(Barra(125,137 , *props3))
    ret.agregar_barra(Barra(137,141 , *props3))
    ret.agregar_barra(Barra(141,41 , *props3))
    
    ##diagonales ((4))
    ret.agregar_barra(Barra(130,38 , *props4))
    ret.agregar_barra(Barra(38,138 , *props4))
    ret.agregar_barra(Barra(131,39 , *props4))
    ret.agregar_barra(Barra(39,139 , *props4))
    
    ret.agregar_barra(Barra(130,134 , *props4))
    ret.agregar_barra(Barra(126,138 , *props4))
    ret.agregar_barra(Barra(131,135 , *props4))
    ret.agregar_barra(Barra(127,139 , *props4))
    
    
    ret.agregar_barra(Barra(140,42 , *props4))
    ret.agregar_barra(Barra(42,132 , *props4))
    ret.agregar_barra(Barra(141,43 , *props4))
    ret.agregar_barra(Barra(43,133 , *props4))
    
    ret.agregar_barra(Barra(140,128 , *props4))
    ret.agregar_barra(Barra(136,133 , *props4))
    ret.agregar_barra(Barra(129,141 , *props4))
    ret.agregar_barra(Barra(137,133 , *props4))
    
    ret.agregar_barra(Barra(130,131 , *props5))
    ret.agregar_barra(Barra(131,139 , *props5))
    ret.agregar_barra(Barra(139,138 , *props5))
    ret.agregar_barra(Barra(138,130 , *props5))
    ret.agregar_barra(Barra(131,138 , *props4))
    ret.agregar_barra(Barra(130,139 , *props4))
    
    ret.agregar_barra(Barra(126,127 , *props5))
    ret.agregar_barra(Barra(127,135 , *props5))
    ret.agregar_barra(Barra(135,134 , *props5))
    ret.agregar_barra(Barra(134,126 , *props5))
    ret.agregar_barra(Barra(134,127 , *props4))
    ret.agregar_barra(Barra(126,135 , *props4))
    
    ret.agregar_barra(Barra(140,141 , *props5))
    ret.agregar_barra(Barra(141,133 , *props5))
    ret.agregar_barra(Barra(133,132 , *props5))
    ret.agregar_barra(Barra(132,140 , *props5))
    ret.agregar_barra(Barra(140,133 , *props4))
    ret.agregar_barra(Barra(141,132 , *props4))
    
    ret.agregar_barra(Barra(136,137 , *props5))
    ret.agregar_barra(Barra(137,129 , *props5))
    ret.agregar_barra(Barra(129,128 , *props5))
    ret.agregar_barra(Barra(128,136 , *props5))
    ret.agregar_barra(Barra(136,129 , *props4))
    ret.agregar_barra(Barra(128,137 , *props4))
    
    for i in range(2*nodes-1):
        ret.agregar_fuerza(i, 2, -F)
    return ret
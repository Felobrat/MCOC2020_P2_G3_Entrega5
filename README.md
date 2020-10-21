# MCOC2020_P2_G3_Entrega5 - Concurso: ¡Diseñe su puente!

# Diseño 0:

Se diseño primero la pasarela donde se observó una gran deformacion en el centro de la pasarela, tal como se muestra en la primera imagen.

![image](https://user-images.githubusercontent.com/69157203/96669275-49f53a80-1333-11eb-86de-0bb6248d56b6.png)

Se decidio diseñar una torre en las posiciones 115 [m] y 125 [m] del acantilado, dado que coincidian con los puntos medios del puente. se decidio un diseño simple, pero resistente tal como lo muetsra la imagen.

![image](https://user-images.githubusercontent.com/69157203/96669442-9fc9e280-1333-11eb-8115-0ca88799f22a.png)

de esa manera, se calcula la deformada comparandola con la anterior, sin torre:

![image](https://user-images.githubusercontent.com/69157203/96669505-bcfeb100-1333-11eb-8528-5749d5154abb.png)

Propiedades de diseño iniciales:

```
R = 12/100       #linea de soporte
t = 6/1000       #linea de soporte
R1 = 12/100      #Pasarela
t1 = 6/1000      #Pasarela
R2 = 12/100      #soporte Pasarela
t2 = 6/1000      #soporte Pasarela
R3 = 12/100      #columnas
t3 = 6/1000      #columnas
R4 = 12/100      #diagonales
t4 = 6/1000      #diagonales
R5 = 12/100      #soporte columnas
t5 = 6/1000      #soporte columnas
```

Para esta estructura inicial se cumplió la combinación de carga 1 y combinación de carga 2,
obteniendo un Peso total = 900272.16652 [N].

Asi, se obtiene un diseño que cumple con las caracteristicas deseadas, pero debiendo optimizarla. 

Los factores de utilización del diseño inicial son valores bastantes lejanos a 1. La tendencia son números con exponenciales de -3 y -4. Además existe un factor de utilización con exponente -17.

Por otro lado, en las deformaciones resultantes para este primer diseño se obtuvo que en la mayoría de sus nodos los valores de sus deformaciones eran relativamente bajas, por lo que era posible seguir optimizando, sin incurrir a un riesgo de seguridad en la estructura.


Para optimizar la estructura, esta se dividió en cinco partes, para realizar cambios desde las barras que toman menos fuerzas hasta las que toman más. Las partes corresponden a las columnas de las torres que soportan el puente, las diagonales de estas, las abrazaderas, las pasarelas y las costaneras. Luego se disminuyó el área de las barras primero disminuyendo el radio y luego el espesor progresivamente. Esto para cada parte antes mencionadas, hasta alcanzar la falla de alguna de las barras de la misma. Esta sería la primera iteración.

# Diseño 1:

Para este diseño se utilizaron las siguientes propiedades

```
R = 12/100        #linea de soporte
t = 5/1000        #linea de soporte
R1 = 10/100       #Pasarela
t1 = 3/1000       #Pasarela
R2 = 8/100        #soporte Pasarela
t2 = 3/1000       #soporte Pasarela
R3 = 12/100       #columnas
t3 = 6/1000       #columnas
R4 = 6/100        #diagonales
t4 = 2/1000       #diagonales
R5 = 4/100        #soporte columnas
t5 = 2/1000       #soporte columnas
```

Para esta estructura, se mantuvo el diseño de la armadura original, cambiando solo las propiedades antes mencionadas. 
Se cumplió la combinación de carga 1 y combinación de carga 2.
Obteniendo un Peso total = 403539.9660369796 [N]

Luego se analiza la vecindad de la barra que falló en cada parte, subiendo el espesor y bajando el radio o viceversa según fuese conveniente para optimizar la estructura cumpliendo las condiciones, lo que corresponde a una segunda iteración.


# Diseño 2:

Para este diseño se utilizaron las siguientes propiedades:

```
R = 11.5/100       #linea de soporte
t = 5/1000         #linea de soporte
R1 = 9.5/100       #Pasarela
t1 = 3/1000        #Pasarela
R2 = 8/100         #soporte Pasarela
t2 = 3/1000        #soporte Pasarela
R3 = 11/100        #columnas
t3 = 5.5/1000      #columnas
R4 = 6/100         #diagonales
t4 = 2/1000        #diagonales
R5 = 4/100         #soporte columnas
t5 = 2/1000        #soporte columnas
```

Para esta estructura, se mantuvo el diseño de la armadura original, cambiando solo las propiedades antes mencionadas. 

Los factores de utilización finales son bastante más cercanos a 1 que los del diseño original, donde esta vez la tendencia son valores con exponenciales de -2 y -1.  Además, a diferencia del diseño original, ningún factor de utilización se escapa demasiado. El valor más lejano a 1 tiene un exponencial de -4.

Sin embargo, la optimización del diseño produce mayores deformaciones en la estructura, pero cumpliendo con la combinación de carga 1 y combinación de carga 2.
y finalmente obteniendo un Peso total = 380802.67067722726 [N]

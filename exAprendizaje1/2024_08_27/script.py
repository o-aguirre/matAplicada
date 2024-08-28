# importamos pyplot de matplotlib y numpy
import matplotlib.pyplot as plt
import numpy as np
# generaremos una tabla de datos usando numpy
# a la que aplicaremos la funci ́on, que es la misma del ejemplo
# tomaremos la variable independiente entre 0 y 6
# y haremos los elementos de la tabla separados en 0,01
x = np.arange(0, 6, 0.01)
# para cada elemento del dominio, aplicaremos la funci ́on
y = 120*x+2000
# le pedimos a matplotlib que genere un gr ́afico
plt.plot(x, y)
# cuyos ejes van de 0 a 6 en la x, de 0 a 2800 en la y
plt.axis([0, 6, 0, 2800])
# con un t ́ıtulo de eje x
plt.xlabel('Energia utilizada ({kWh})')
# y un t ́ıtulo de eje y
plt.ylabel('Costo para usuario ($)')
# y un titulo del grafico
plt.title('Costo para el usuario seg ́un uso de energia')
# pedimos mostrar una grilla para facilitar la lectura
plt.grid(True)
# y que nos muestre el gr ́afico
plt.show()
import sys
import modulo
def calcular_pi(n):
  pi35 = 3.1415926535897931159979634685441852
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0/float(n)
  for i in range(n):
    x_i = ((i+1)-1.0/2.0)/n
    #x_i = calcular_xi (n, n+1)
    fx_i = 4.0/(1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio/n
  return (valor_pi)
def error (nro_intervalos, nro_test, umbral):
  intervalo = nro_intervalos
  lista = []
  for i in range (nro_test):
    valor_pi = calcular_pi (intervalo)
    intervalo += nro_intervalos
    lista.append (valor_pi)
  pi35 = []
  for i in range (nro_test):
    pi35.append (PI35DT)
  dif35 = []
  for i in range (nro_test):
    dif35.append (abs(pi35[i] - lista [i]))
  correcto = 0
  for i in range (nro_test):
    if (dif35[i] <= umbral):
      correcto = correcto + 1
  porcentaje = 100.0 * (1.0 - (float(correcto) / float(nro_test)))
  return (porcentaje)

if (__name__ == "__main__"):
  argumentos = sys.argv[1:]
  if (len(argumentos) == 8):
    aproximaciones = int (argumentos[1])
    umbral = []
    for i in range (2,7):
      umbral.append(float (argumentos[i]))
    nombre_fichero = argumentos [7]
  else:
    print "Introduzca el numero de intervalos (n > 0):"
    n = int(raw_input())
    print "Introduzca el numero de aproximaciones:"
    aproximaciones = int(raw_input());
    print "Introduzca 5 umbrales de error:"
    umbral = []
    for i in range (5):
      print "Introduzca el umbral", i, ":"
      umbral.append(float (raw_input()));
    print "Introduzca el nombre del fichero para almacenar los resultados:"
    nombre_fichero = raw_input ();
  if (n>0):
    
  # Una forma de averiguar si un fichero existe o no puede ser esta
  # debemos de incluir el paquete os.path
  #  if os.patch.isfile(nombre_fichero):
  #	fichero = open (nombre_fichero, "a")
  #  else:
  #	fichero = open (nombre_fichero, "w")
  #Otra forma puede ser mediante excepciones, como vemos a continuacion
    try:
      fichero = open (nombre_fichero, "a")
    except:
      fichero = open (nombre_fichero, "w")
    fichero.write ("N* de intervalos: %d\n" % (aproximaciones))
    for i in range (5):
      porcentaje = modulo.error(n, aproximaciones, umbral[i])
      fichero.write("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
    fichero.close()
    #porcentaje = error (n, aproximaciones, umbral)
    #print "El porcentaje de fallos es del ", porcentaje
  else:
    print "El valor de los intervalos debe se mayor que 0"
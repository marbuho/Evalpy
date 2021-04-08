# Readme.md
En este repositorio se encuentra dos de las tres funcionalidades solicitadas en la evaluación.
- Calcular el cambio. 
- Analizar balance de corchetes.

## Requisitos
- Interprete Python.

## Installation
Descargue el archivo .zip y descomprimalo en algun sitio  ejem:`C:\user\Escritorio\carpeta`.
Ejecute la consola de comandos y coloquese en el directorio de la carpeta del proyecto
```bash
    > cd C:\user\Escritorio\carpeta\Evalpy 
```
### Calcular cambio $.
Para calcular el cambio a dar ejecute el scrip `evalpy.py` con el parametro `-c`.
```bash
    C:/> python evalpy.py -c  n1 n2
```
Donde:\
`n1`: Cantidad con la que se abona, debe ser un entero\
`n2`: Total a pagar, debe ser un entero.\
Devuelve un arreglo con los valores de cambio a dar.\
Ejemplo:
```bash
    C:/> python evalpy.py -c  500 120
    >>
    su cambio es:  [200, 100, 50, 20, 10]
```

### Balance de corchetes.
Para analizar balanceo de corchetes utilizar `-b`.
```bash
    C:/> python evalpy.py -b  <exp_corchetes>
``` 
Donde *<exp_corchetes>* se reemplaza por una expresión con corchetes, por ejemplo `[]]`, `[][[]]`,`[]`  etc.\
Devuelve `true` en el caso que exista balanceo, de lo contrario devuelve `false`.\
Ejemplo:
```bash
  C:/> python evalpy.py -b  [][]
  >>
  true
  
  C:/> python evalpy.py -b  [][
  >>
  false
	
``` 
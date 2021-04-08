def darcambio(pagacon, totalpago):
    cantidad = pagacon - totalpago
    denom_billetes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []
    
    #casos triviales:      
    if(cantidad == 0):
        result =  [0]
    elif(cantidad < 0):
        result.append(cantidad)
        print("pago insuficiente :(")

    #casos a calcular:
    i = 0; 
    while (cantidad > 0):
            cant_billete = cantidad // denom_billetes[i]
            for n in range(cant_billete):
                result.append(denom_billetes[i])
                cantidad = cantidad % denom_billetes[i]
            i += 1
    return result

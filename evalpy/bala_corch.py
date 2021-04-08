def bala_corch(textcorch):
    #caso trivial: cantidad impar  corchetes
    ok = True
    if len(textcorch) % 2 != 0:
        ok = False
        # print("caso trivial es impar")
    #caso trivial: cantidad nula corchetes
    elif len(textcorch) == 0:
        # print("caso trivial no hay corchetes")
        ok = True
        
    #caso trivial: comienza o finaliza desbalanceado 
    elif  (textcorch[0] == "]" ):
        # print("caso trivial arranca mal")
        ok = False      
    elif  (textcorch[-1] == "[" ):
        # print("caso trivial termina mal")
        ok = False
      
    #caso a analizar:
    else:
        # print("caso analizado")  
        nivel = 1
        j = 1
        while ((ok == True) and (j < len(textcorch))):
            if textcorch[j]== "[":
                nivel += 1
            elif textcorch[j]== "]":
                nivel-=1  
            ok = (nivel >= 0) #a la primera inconsistencia sale
            j+=1
            
           
    return ok

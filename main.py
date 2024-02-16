#Catalina Mulford
import json
file=("data.json","r")
datas=json.load 

file=("historila.json","r")
histo=json.load 
       
file=("pqr.json","r")
pqr=json.load

j=True
while j==True:
    
    qHacer=int(input("Bienvenido, que deseas hacer:\n 1. Perfiles Usuario\n 2. Historial usuarios\n 3. Personalización de Servicios\n 4. Gestión de Fidelización\n"))

    #Perfil usuario
    if qHacer==1:
        menuUsuario=int(input("Deseas: \n1.Crear usuario\n2.Actualizar\n3.Eliminar\n"))

        base={}

        #Crear
        if menuUsuario==1:
            t=datas["clientes"]
            nom=input("Pon el nombre entro, identificaciòn, direccion, numero de contacto y categoria (ejemplo: Nombre: Caro, ...)\n").split(",")
            t.append(nom)
            with open ("data.json","w") as file:
                json.dump(datas,file)
        
        #Actu
        elif menuUsuario==2:
            act=input("Pon el nombre de quien actualizar:\n")
            for llave, valor in datas:
                    for ser,nose in valor:
                        if nose==act:
                            qCambiar=input("Que cambiaras:\n")
                            if qCambiar==ser:
                                nuevo=input("Pon nuevo dato")
                                datas["sera"][ser]=nuevo
                                with open ("data.json","w") as file:
                                    json.dump(base,file)

        #Eliminar
        elif menuUsuario==3:
            el=input("Pon el nombre de quien actualizar:\n")
            if any(bus["nombre"] for bus in datas==el):
                for llave, valor in datas:
                    for ser,nose in valor:
                        if nose==el:
                            datas[el].plop()
                            with open ("data.json","w") as file:
                                    json.dump(base,file)

        y=input("Seguir: Si/no").lower
        if y=="si":
            j=False
    
    #Historial usuarios
    elif qHacer==2:
        
        UActu=int(input("Deseas:\n1.Crear un servicio\n2.Actualizar un servicio\n3.Eliminar un servicio\n4. Ver PQR\n"))
        bas=[]
        #Crear
        if UActu==1:
            nom=input("Pon la id, servivo(que posee), costo (ejemplo: id: 3110521, ...)\n").split(",")
            bas.append(nom)
            with open ("historila.json","w") as file:
                json.dump(bas,file)
        
        #Actu
        elif UActu==2:
            act=int(input("Pon el id de quien actualizar:\n"))
            for llave, valor in histo:
                    for ser,nose in valor:
                        if nose==act:
                            qCambiar=input("Que cambiaras:\n")
                            if qCambiar==ser:
                                nuevo=input("Pon nuevo dato")
                                histo[ser]=nuevo
                                with open ("historila.json","w") as file:
                                    json.dump(bas,file)

        #Eliminar
        elif UActu==3:
            el=input("Pon el id de quien elimnar:\n")
            if any(int(bus["id"] for bus in histo==el)):
                for llave, valor in histo:
                    for ser,nose in valor:
                        if nose==el:
                            histo[el].plop()
                            with open ("histo.json","w") as file:
                                    json.dump(bas,file)

        #Registro PQR
        elif UActu==4:
            apri=[]
            for i in pqr:
                apri.append(i)
            print(apri)
        
        y=input("Seguir: Si/no").lower
        if y=="si":
            j=True
        else:
            j=False

        

    #Personalización de Servicios
    elif qHacer==3:
        apri=[]
        estres=int(input("Deseasver:\n1.Patrones de un cliente\n2.Servicio màs vendido\n"))
        
        if estres==1:
            yes=int(input("Pon ID del cliente:\n"))
            for llave, valor in histo:
                for ser,nose in valor:
                    if nose==yes:
                        apri.append(nose)
                        print(apri)
        elif estres==2:
            apri=[]
            falling=input("Pon el registro que deseas buscar\n")
            
            for llave, valor in histo.itmes():
                        for nose in valor:
                            if nose["registro"].lower()==falling:
                                apri.append(nose)
                                print(apri)


        
        y=input("Seguir: Si/no").lower
        if y=="si":
            j=False
    
    #Gestión de Fidelización--pqr
    elif qHacer==4:
        file=("pqr.json","r")
        pqr=json.load

        tiempo=int(pqr["tiempo"])
        bermeja=[]
        for llave, valor in pqr:
            for tiempo in valor:
                if tiempo >=10:
                     bermeja.append(tiempo)
                    
                    
        print(bermeja)



        y=input("Seguir: Si/no").lower
        if y=="si":
            j=False
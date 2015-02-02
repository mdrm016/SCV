from django.shortcuts import render

# Create your views here.

def pagination(elementos, num_pagina):
    
    num_pagina = int(num_pagina)
    divisoria = 10
    cantidad = elementos.count()
    paginas = cantidad / divisoria
    if (cantidad % divisoria) == 0:
        num_pagina = int(num_pagina)-1
    if cantidad % divisoria > 0:
        paginas += 1
    pag = range(paginas+1)
    pag.remove(0)
    elemen=[]
    anterior = 'active'
    siguiente = 'active'
    
    if paginas == 1:
        anterior = 'disabled'
        siguiente = 'disabled'
        elemen = elementos
        
    elif paginas > 1:
        inicio = (num_pagina-1)*divisoria +1
        count = 0
        for elemento in elementos:
            count += 1
            if count >= inicio and count <= inicio+divisoria -1:
                elemen.append(elemento)

        if num_pagina == 1:
            anterior = 'disabled'
        if num_pagina == paginas:   
            siguiente = 'disabled'
            
    ctx = {'elementos': elemen, 'paginas': pag, 'pagina': num_pagina, 'anterior': anterior, 'siguiente': siguiente, 'sig': num_pagina+1, 'ant': num_pagina-1, 'infe': 0, 'supe': paginas+1}
    return ctx

def columnaRoles (permisos):
    
    elementCheck=[]
    count = 0
    control = 1
    columnas = 4
    cantidad = permisos.count()
    if (cantidad % columnas) > 0:
        div = cantidad/columnas + 1
    else:
        div = cantidad/columnas
    for permiso in permisos:
        count += 1
        if not count <= div:
            control += 1
            count = 1
        dic= {'columna': control, 'permiso':permiso}
        elementCheck.append(dic)
    return elementCheck
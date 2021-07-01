

def catalogacion_audiovisual(inventario: list) -> tuple:

    dvds = [x['id'] for x in inventario if x['tipo'] == 'DVD' and x['área'] == 'Tecnología' and x['año'] < 2006] 
    cds  = [x['id'] for x in inventario if x['tipo'] == 'CD' and ((x['área'] != 'Tecnología' and x['año'] < 2011) or (x['área'] == 'Tecnología' and x['año'] < 2013))] 

    mantener = [x for x in inventario if x['id'] not in dvds and x['id'] not in cds] 

    x = 0
    for lista in mantener:

        nombre = lista['autor']
        lista['autor'] = transformar_nombre(nombre)
        mantener[x] = lista
        x+=1
     
    return mantener,dvds,cds


def transformar_nombre(nombre: str) -> str:

    nuevo_nombre = ''

    if ',' in nombre:
        nombre_nuevo = nombre.split(',')
        for pos in range(len(nombre_nuevo)):
            nombre_separado = nombre_nuevo[pos].split(' ')
            if pos < len(nombre_nuevo)-1:
             nuevo_nombre += nombre_separado[1] +','+ nombre_separado[0] +';' 
            else:       
             nuevo_nombre += nombre_separado[1] +','+ nombre_separado[0]

    else:
        nuevo_nombre = nombre.split(' ')
        nuevo_nombre = nuevo_nombre[1] +','+ nuevo_nombre[0]

    return nuevo_nombre



print(catalogacion_audiovisual(inventario = [
    {'id': '10', 
    'titulo':'Administración de compras', 
    'tipo':'DVD', 
    'área': 'Administración',
    'autor': 'César Díaz,Andrés García',
    'año': 2005}, 
    {'id': '20',
     'titulo': 'Fundamentos de programación', 
     'tipo':'DVD', 
     'área': 'Tecnología', 
     'autor': 'César Díaz', 
     'año': 2003},
    {'id': '30',
     'titulo': 'Actualidad matemática',
     'tipo': 'CD',
     'área': 'Matemáticas',
     'autor': 'Pedro Navaja',
     'año': 1987},
    {'id': '40', 
    'titulo': 'Actualidad xormática', 
    'tipo': 'CD', 
    'área':'Tecnología', 'autor': 'Bill Gates',
    'año': 2019}, 
    {'id': '50',
     'titulo':'Atomic Physics for Dummies',
     'tipo':'DVD',
     'área': 'Física', 
     'autor': 'Albert Einstein',
     'año': 1955}]
))



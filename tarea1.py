import time
from random import seed
from random import randint

def reflex_agent(location, state):
    if state=="DIRTY":
        return 'CLEAN'
    elif location=='A':
        return 'RIGHT'
    elif location=='B':
        return 'LEFT'   

def getSystemState(state):
    location = state[0]
    stateA = state[1]
    stateB = state[2]
    if location == "A":
        if stateA == "DIRTY":
            return 1 if stateB == "DIRTY" else 2
        elif stateA == "CLEAN":
            return 3 if stateB == "DIRTY" else 4
    elif location == "B":
        if stateA == "DIRTY":
            return 5 if stateB == "DIRTY" else 6
        elif stateA == "CLEAN":
            return 7 if stateB == "DIRTY" else 8

visited = []
route = []

def dirty():
    seed()
	if(randint(0,1) == 1):
		return "DIRTY"
    else:
		return "CLEAN"

def recorrerTodo(state):

    while True:
        systemState = getSystemState(state)
        route.append(systemState)
        if systemState not in visited:
            visited.append(systemState)
        if len(visited) == 8:
            result = ""
            for s in route:
                result += "{0}->".format(s)
            print(result)
            break    
        
        stateA = state[1]
        stateB = state[2]
        location = state[0]
        locationState = (stateB, stateA)[location == 'A']
        action = reflex_agent(location, locationState)
        if action == "CLEAN":
            if location == 'A':
                state[1]="CLEAN"
            elif location == 'B':
                state[2]="CLEAN"
        elif action == "RIGHT":
            state[0]='B'
        elif action == "LEFT":
            state[0]='A'

        if stateA == "CLEAN":
            state[1] = dirty()
        if stateB == "CLEAN":
            state[2] = dirty()
        
        time.sleep(1)

recorrerTodo(['A','DIRTY','DIRTY'])


def sucesores(n):
    if n == 1: return [3]
    elif n == 2: return [4]
    elif n == 3: return [7]
    elif n == 4: return [8]
    elif n == 5: return [6]
    elif n == 6: return [2]
    elif n == 7: return [8]
    elif n == 8: return [4]
    else: return None


def anchura(nodo_inicio, nodo_fin):
    ruta = []
    lista = [nodo_inicio]
    while lista:
        actual = lista.pop(0)
        ruta.append(actual)
        if actual == nodo_fin:
            resultado = ""
            for r in ruta:
                resultado += "{0}->".format(r)
            return print(resultado)
        temp = sucesores(actual)
        if temp:
            lista.extend(temp)
    print ("NO-SOLUCIÓN")

def profundidad (nodo_inicio, nodo_fin):
    ruta = []
    lista = [nodo_inicio]
    while lista:
        actual = lista.pop(0)
        ruta.append(actual)
        if actual == nodo_fin:
            resultado = ""
            for r in ruta:
                resultado += "{0}->".format(r)
            return print(resultado)
        temp = sucesores(actual)
        temp.reverse()
        if temp:
            temp.extend(lista)
            lista = temp
    print ("NO-SOLUCIÓN")
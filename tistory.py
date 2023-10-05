#!pip install pyformlang
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import DeterministicFiniteAutomaton as DFA
import csv
import re

from pyformlang.cfg import CFG, Production, Variable, Terminal
import random

with open('docs/Story.csv',newline='') as pscfile:
    reader = csv.reader(pscfile)
    next(reader)
    nfaStates = dict(reader)


q0=State('q0')
q1=State('q1')
B_1_carulla=State('B_1_carulla')
B_2_nuevosAmigos=State('B_2_nuevosAmigos')
B_3_celular=State('B_3_celular')
B_4_cervezas=State('B_4_cervezas')
B_5_retirada=State('B_5_retirada')
B_6_vomito=State('B_6_vomito')
B_7_taxi=State('B_7_taxi')
B_8_dormir=State('B_8_dormir')
B_9_caminar=State('B_9_caminar')
B_10_montarse=State('B_10_montarse')
B_11_ignorado=State('B_11_ignorado')
B_12_robo=State('B_12_robo')
B_13_final=State('B_13_final')
B_14_amigo=State('B_14_amigo')
B_15_fifa=State('B_15_fifa')
B_16_partida=State('B_16_partida')
B_17_uber=State('B_17_uber')
B_18_solo=State('B_18_solo')
B_19_muerte=State('B_19_muerte')
A_1_Seleccion_de_transporte = State('A_1_Seleccion_de_transporte')
A_2_MIO = State('A_2_MIO')
A_3_Cupo = State ('A_3_Cupo')
A_3_1_Cupo = State ('A_3_1_Cupo')
A_3_2_Cupo = State ('A_3_2_Cupo')
A_3_3_Caminar = State ('A_3_3_Caminar')
A_4_Amigo = State ('A_4_Amigo')
A_4_1_1060 = State ('A_4_1_1060')
A_4_3_Sagsa =State('A_4_3_Sagsa')
A_4_4_Carulla = State ('A_4_4_Carulla')



dfa= DFA(
    states={q0, q1, B_1_carulla, B_2_nuevosAmigos, B_3_celular, B_4_cervezas, B_5_retirada, B_6_vomito, B_7_taxi, B_8_dormir, B_9_caminar, B_10_montarse, B_11_ignorado, B_12_robo, B_13_final, B_14_amigo, B_15_fifa, B_16_partida, B_17_uber, B_18_solo, B_19_muerte, A_1_Seleccion_de_transporte , A_2_MIO , A_3_Cupo , A_3_1_Cupo , A_3_2_Cupo , A_3_3_Caminar , A_4_Amigo , A_4_1_1060 , A_4_3_Sagsa , A_4_4_Carulla},
    input_symbols={'carulla', 'socializar', 'aceptar', 'negarse', 'retirarse', 'tomar', 'dormir', 'taxi', 'caminar', 'montarse', 'ignorar', 'golpear', 'saltar', 'seguir', 'celular', 'uber', 'amigo', 'dedo', 'fifa', 'revancha', 'transporte', 'MIO', 'cupo', '1060', 'sagsa', 'casa', 'fiesta', 'salir'},
    start_state=q0,
    final_states={B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_4_Carulla}
)

estados_perdedores=[B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_4_Carulla]
estados_ganadores=[B_13_final, A_3_3_Caminar]
estados_aceptacion=[]
estados_aceptacion.extend(estados_perdedores)
estados_aceptacion.extend(estados_ganadores)

dfa.add_transitions([(q0, 'a', q1), (q1, 'carulla', B_1_carulla), 
                     (B_1_carulla, 'socializar', B_2_nuevosAmigos), 
                     
                     (B_2_nuevosAmigos, 'aceptar', B_4_cervezas),
                     (B_4_cervezas, 'tomar', B_6_vomito),
                     
                     (B_4_cervezas, 'retirarse', B_5_retirada), 
                     (B_2_nuevosAmigos, 'negarme', B_5_retirada),
                     
                     (B_5_retirada, 'taxi', B_7_taxi),
                     (B_5_retirada, 'dormir', B_8_dormir),
                     
                     
                     (B_5_retirada, 'caminar', B_9_caminar),
                     (B_9_caminar, 'ignorar', B_11_ignorado),
                     (B_9_caminar, 'golpear', B_12_robo),
                     
                     (B_9_caminar, 'montarse', B_10_montarse),
                     (B_10_montarse, 'seguir', B_13_final), 
                     (B_10_montarse, 'saltar', B_19_muerte), 
                     
                     
                     
                     (B_1_carulla, 'celular', B_3_celular),
                     
                     (B_3_celular, 'uber', B_17_uber), 
                     (B_17_uber, 'caminar', B_9_caminar),
                     (B_17_uber, 'dedo', B_18_solo),
                     
                     (B_3_celular, 'amigo', B_14_amigo),
                     (B_14_amigo, 'fifa', B_15_fifa),
                     (B_14_amigo, 'revancha', B_16_partida),
                     
                     (B_16_partida, 'caminar', B_9_caminar), 
                     (B_16_partida, 'taxi', B_7_taxi),
                     
                     (q0, 'a', q1), 
                     (q1,'transporte',A_1_Seleccion_de_transporte),(A_1_Seleccion_de_transporte, 'MIO', A_2_MIO),(A_1_Seleccion_de_transporte, 'cupo', A_3_1_Cupo), (A_1_Seleccion_de_transporte, 'amigo', A_4_Amigo),
                    (A_2_MIO,'MIO', A_2_MIO),(A_2_MIO, 'cupo', A_3_1_Cupo),(A_3_1_Cupo, 'dormir', A_3_2_Cupo), (A_3_1_Cupo, 'amigo', A_4_Amigo),  (A_2_MIO, 'amigo', A_4_Amigo),
                    (A_4_Amigo, '1060', A_4_1_1060),(A_4_Amigo, 'sagsa', A_4_3_Sagsa), (A_4_Amigo, 'casa', A_4_4_Carulla),
                    (A_4_1_1060, 'fiesta', A_4_1_1060),(A_4_1_1060, 'salir', A_4_3_Sagsa), (A_4_3_Sagsa, 'fiesta', A_4_3_Sagsa), (A_4_3_Sagsa, 'casa', A_4_4_Carulla),
                    (A_3_2_Cupo, 'casa', A_3_3_Caminar), (A_3_2_Cupo, 'amigo', A_4_Amigo)
                     ])


def playStory(automaton = DFA, q0 = State, winning_states = [], acceptance_states = [], losing_states=[] , gic=CFG): 
    automatonDict=automaton.to_dict()
    
    
    actual_state = q0
    path=[]
    
    while(actual_state not in acceptance_states):
        options=automatonDict.get(actual_state)
        if (actual_state=='q0'):
            print('Como te llamas?')
        else:
            if((str(actual_state) + "x") in nfaStates):
                print(nfaStates.get(str(actual_state) + "x") +  generar_cadena(gic, S))
            print(nfaStates.get(actual_state))
        entry=input("entrada: ")

        for i in options: 
            if(re.search(rf"\b{i}\b", entry, re.IGNORECASE)): 
                actual_state=options.get(i)
                path.append(i)
        if(options==automatonDict.get(actual_state)): #verifica que el estado haya cambiado, de no ser asi es que la entrada no es correcta
            print("entrada erronea")       
        if(actual_state==q0): 
            print("volviste al inicio")
        elif(actual_state in losing_states): 
            print("no llegaste a tu casa")
        elif(actual_state in winning_states): 
            print("llegaste a tu casa")
    if((str(actual_state) + "x") in nfaStates):
        print(nfaStates.get(str(actual_state) + "x") +  generar_cadena(gic, S))
    print(nfaStates.get(actual_state))




#generador de historias a partir de una gramatica

# Definir una gramática independiente del contexto (CFG)
S = Variable("S")


#Gramatica para definir detalles:
gic = CFG.from_text("""
S -> FA 
FA -> Pi PA P
Pi -> SINi | PLURi
P -> SIN | PLUR
SINi ->  DetA NA VA
PLURi -> DetAs NAs VAs                   
SIN -> DetA NB
PLUR -> DetAs NBs
NAA -> NA | NB
DetA -> un 
DetAs -> unos
NA -> gato | perro | niño
NAs -> gatos | perros | niños
NB -> juguete | arbol | carro | balon | botellon | colchon
NBs -> juguetes | arboles | carros | balones | botellones | colchones
VA -> juega | corre | duerme | salta
VAs -> juegan | corren | duermen | saltan
PA -> sobre | bajo | cerca de | junto a | con
""")

# Generar una cadena de acuerdo con la CFG
def generar_cadena(cfg, simbolo_inicial):
    cadena = ""
    pila = [simbolo_inicial]

    while pila:

        simbolo_actual = pila.pop()

        if isinstance(simbolo_actual, Terminal):
            cadena += " " + simbolo_actual.value
        elif isinstance(simbolo_actual, Variable):
            producciones_posibles = [p for p in cfg.productions if p.head == simbolo_actual]
            if producciones_posibles:
                produccion = random.choice(producciones_posibles)
                pila.extend(reversed(produccion.body))

    return cadena


playStory(dfa, q0, estados_ganadores, estados_aceptacion, estados_perdedores, gic)
cadena_generada = generar_cadena(gic, S)
#print("Cadena generada:", cadena_generada)
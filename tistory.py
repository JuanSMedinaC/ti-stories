#!pip install pyformlang
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
q0=State('q0')
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

nfa = NondeterministicFiniteAutomaton()

nfa.add_transitions(
    [(q0,'transporte',A_1_Seleccion_de_transporte),(A_1_Seleccion_de_transporte, 'MIO', A_2_MIO),(A_1_Seleccion_de_transporte, 'cupo', A_3_1_Cupo), (A_1_Seleccion_de_transporte, 'amigo', A_4_Amigo),
     (A_2_MIO,'MIO', A_2_MIO),(A_2_MIO, 'cupo', A_3_1_Cupo),(A_3_1_Cupo, 'dormir', A_3_2_Cupo), (A_3_1_Cupo, 'amigo', A_4_Amigo),  (A_2_MIO, 'amigo', A_4_Amigo),
     (A_4_Amigo, '1060', A_4_1_1060),(A_4_Amigo, 'sagsa', A_4_3_Sagsa), (A_4_Amigo, 'casa', A_4_4_Carulla),
     (A_4_1_1060, 'fiesta', A_4_1_1060),(A_4_1_1060, 'salir', A_4_3_Sagsa), (A_4_3_Sagsa, 'fiesta', A_4_3_Sagsa), (A_4_3_Sagsa, 'salir', A_4_4_Carulla),
     (A_3_2_Cupo, 'casa', A_3_3_Caminar), (A_3_2_Cupo, 'amigo', A_4_Amigo)])

nfa.add_start_state(q0)
nfa.add_final_state(A_4_1_1060)
nfa.add_final_state(A_4_3_Sagsa)
nfa.add_final_state(A_4_4_Carulla)
nfa.add_final_state(A_3_3_Caminar)

dfa1=nfa.to_deterministic()

from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import DeterministicFiniteAutomaton as DFA
#AUTOMATA CARULLA

q0=State('q0')
q1=State('q1')
B_1_carulla=State('B1')
B_2_nuevosAmigos=State('B2')
B_3_celular=State('B3')
B_4_cervezas=State('B4')
B_5_retirada=State('B5')
B_6_vomito=State('B6')
B_7_taxi=State('B7')
B_8_dormir=State('B8')
B_9_caminar=State('B9')
B_10_montarse=State('B10')
B_11_ignorado=State('B11')
B_12_robo=State('B12')
B_13_final=State('B13')
B_14_amigo=State('B14')
B_15_fifa=State('B15')
B_16_partida=State('B16')
B_17_uber=State('B17')
B_18_solo=State('B18')
B_19_muerte=State('B19')


dfa= DFA(
    states={q0, q1, B_1_carulla, B_2_nuevosAmigos, B_3_celular, B_4_cervezas, B_5_retirada, B_6_vomito, B_7_taxi, B_8_dormir, B_9_caminar, B_10_montarse, B_11_ignorado, B_12_robo, B_13_final, B_14_amigo, B_15_fifa, B_16_partida, B_17_uber, B_18_solo, B_19_muerte},
    input_symbols={'carulla', 'socializar', 'aceptar', 'negarse', 'retirarse', 'tomar', 'dormir', 'taxi', 'caminar', 'montarse', 'ignorar', 'golpear', 'saltar', 'seguir', 'celular', 'uber', 'amigo', 'dedo', 'fifa', 'revancha'},
    start_state=q0,
    final_states={B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_13_final, B_15_fifa, B_18_solo, B_19_muerte} #solo el 13 es ganador
)

estados_perdedores=[B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte]
estado_ganador=B_13_final
estados_aceptacion=[]
estados_aceptacion.extend(estados_perdedores)
estados_aceptacion.append(estado_ganador)

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
                     (B_16_partida, 'taxi', B_7_taxi)
                     ])


estado_actual = q0

dfaDict=dfa.to_dict()

for i in dfaDict: 
    print(i) #printea la key. 
    print(dfaDict.get(i)) #printea el valor asociado a esa key
    
#print(dfaDict)
print()

estado_actual=q0
i=0
estados_perdedores=[A_4_4_Carulla,A_4_3_Sagsa,A_4_1_1060]
estado_ganador=A_3_3_Caminar
estados_aceptacion=[]
estados_aceptacion.extend(estados_perdedores)
estados_aceptacion.append(estado_ganador)


dfa1Dict= dfa1.to_dict()
ruta=[]
while(estado_actual not in estados_aceptacion):
    inter=dfa1Dict.get(estado_actual)
    print("opciones: ", inter)
    entrada=input("entrada: ")
    try:
        for i in inter: 
            if(i==entrada): 
                estado_actual=inter.get(i)
                print("nuevo estado: ", estado_actual)
                ruta.append(entrada)
            
    except: 
        print("entrada erronea")
        
    if(estado_actual==q0): 
        print("volviste al inicio")
    elif(estado_actual in estados_perdedores): 
        print("no llegaste a tu casa")
    elif(estado_actual==estado_ganador): 
        print("llegaste a tu casa")

print(ruta)
print("aceptacion de ruta: ", dfa1.accepts(ruta))
    
    
    
#!pip install pyformlang
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import DeterministicFiniteAutomaton as DFA



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
    final_states={B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_1_1060, A_4_3_Sagsa, A_4_4_Carulla}
)

estados_perdedores=[B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_1_1060, A_4_3_Sagsa, A_4_4_Carulla]
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
                    (A_4_1_1060, 'fiesta', A_4_1_1060),(A_4_1_1060, 'salir', A_4_3_Sagsa), (A_4_3_Sagsa, 'fiesta', A_4_3_Sagsa), (A_4_3_Sagsa, 'salir', A_4_4_Carulla),
                    (A_3_2_Cupo, 'casa', A_3_3_Caminar), (A_3_2_Cupo, 'amigo', A_4_Amigo)
                     ])


def playStory(automaton = DFA, q0 = State, winning_states = [], acceptance_states = [], losing_states=[]): 
    automatonDict=automaton.to_dict()
    
    actual_state = q0
    path=[]
    
    while(actual_state not in acceptance_states):
        options=automatonDict.get(actual_state)
        print("caminos: ", options)
        entry=input("entrada: ")
        
        for i in options: 
            if(i==entry): 
                actual_state=options.get(i)
                print("nuevo estado: ", actual_state)
                path.append(entry)   
 
            print("entrada erronea")
        if(actual_state==q0): 
            print("volviste al inicio")
        elif(actual_state in losing_states): 
            print("no llegaste a tu casa")
        elif(actual_state in winning_states): 
            print("llegaste a tu casa")

    print(path)
    print("aceptacion de ruta: ", dfa.accepts(path))




#generador de historias a partir de una gramatica

from pyformlang.cfg import CFG, Production, Variable, Terminal
import random

# Definir una gramática independiente del contexto (CFG)
S = Variable("S")


gramatica2 = CFG.from_text("""
  S -> A B
  A -> a A | a
  B -> b B | b
""")

#Gramatica para definir detalles:
gic = CFG.from_text("""
S -> FA 
FA -> DetA NA VA PA DetA NAA
NAA -> NA | NB
DetA -> 'el' | 'un' 
NA -> 'gato' | 'perro' | 'niño' 
NB -> 'juguete' | 'arbol' | 'carro' | 'balon' | 'botellon' | 'colchon'
VA -> 'juega' | 'corre' | 'duerme' | 'salta'
PA -> 'sobre' | 'bajo' | 'cerca de' | 'junto a' | 'en'
""")

# Generar una cadena de acuerdo con la CFG
def generar_cadena(cfg, simbolo_inicial):
    cadena = ""
    pila = [simbolo_inicial]

    while pila:

        simbolo_actual = pila.pop()
        print("simbolo actual: ", simbolo_actual)

        if isinstance(simbolo_actual, Terminal):
            cadena += simbolo_actual.value
            print("cadena hasta el momento: ", cadena)
        elif isinstance(simbolo_actual, Variable):
            producciones_posibles = [p for p in cfg.productions if p.head == simbolo_actual]
            print("producciones posibles: ", producciones_posibles)
            if producciones_posibles:
                produccion = random.choice(producciones_posibles)
                pila.extend(reversed(produccion.body))
                print("produccion escogida y anadida a la pila: ", produccion.body)
        print()

    return cadena


playStory(dfa, q0, estados_ganadores, estados_aceptacion, estados_perdedores)
cadena_generada = generar_cadena(gic, S)
print("Cadena generada:", cadena_generada)
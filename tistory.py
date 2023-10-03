#!pip install pyformlang
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

from pyformlang.finite_automaton import NondeterministicFiniteAutomaton

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
    [(A_1_Seleccion_de_transporte, 'El bus del MIO', A_2_MIO),(A_1_Seleccion_de_transporte, 'Esperar un cupo', A_3_1_Cupo), (A_1_Seleccion_de_transporte, 'Ir con amigo fiestero', A_4_Amigo),
     (A_2_MIO,'Esperar el siguiente bus', A_2_MIO),(A_2_MIO, 'Tomar el cupo', A_3_1_Cupo),(A_3_1_Cupo, 'Dormir en el cupo', A_3_2_Cupo), (A_3_1_Cupo, 'Bajar e ir con amigo', A_4_Amigo),  (A_2_MIO, 'Ir con amigo', A_4_Amigo),
     (A_4_Amigo, 'Ir a 1060', A_4_1_1060),(A_4_Amigo, 'Ir a Sagsa', A_4_3_Sagsa), (A_4_Amigo, ' Ir a casa', A_4_4_Carulla),
     (A_4_1_1060, 'Seguir en fiesta', A_4_1_1060),(A_4_1_1060, 'Intentar salir', A_4_3_Sagsa), (A_4_3_Sagsa, 'Seguir en la fiesta', A_4_3_Sagsa), (A_4_3_Sagsa, 'Intentar salir', A_4_4_Carulla),
     (A_3_2_Cupo, 'Caminar hasta casa', A_3_3_Caminar), (A_3_2_Cupo, 'Esperar amigo', A_4_Amigo)])

nfa.add_start_state(A_1_Seleccion_de_transporte)
nfa.add_final_state(A_4_1_1060)
nfa.add_final_state(A_4_3_Sagsa)
nfa.add_final_state(A_4_4_Carulla)
nfa.add_final_state(A_3_3_Caminar)
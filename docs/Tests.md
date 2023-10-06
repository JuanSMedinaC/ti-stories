# Unit tests


### Definitions
*DFA* = automaton( \
*STATES* = (q0, q1, B_1_carulla, B_2_nuevosAmigos, B_3_celular, B_4_cervezas, B_5_retirada, B_6_vomito, B_7_taxi, B_8_dormir, B_9_caminar, B_10_montarse, B_11_ignorado, B_12_robo, B_13_final, B_14_amigo, B_15_fifa, B_16_partida, B_17_uber, B_18_solo, B_19_muerte, A_1_Seleccion_de_transporte, A_2_MIO, A_3_Cupo, A_3_1_Cupo, A_3_2_Cupo, A_3_3_Caminar, A_4_Amigo, A_4_1_1060, A_4_3_Sagsa, A_4_4_Carulla)\
*INPUT_SYMBOLS* = ('carulla', 'socializar', 'aceptar', 'negarse', 'retirarse', 'tomar', 'dormir', 'taxi', 'caminar', 'montarse', 'ignorar', 'golpear', 'saltar', 'seguir', 'celular', 'uber', 'amigo', 'dedo', 'fifa', 'revancha', 'transporte', 'MIO', 'cupo', '1060', 'sagsa', 'casa', 'fiesta', 'salir') \
)
___
*WINNING_STATES* = [B_13_final, A_3_3_Caminar]
___
*LOSING_STATES* = [B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_4_Carulla]
___
*ACCEPTANCE_STATES* = [ B_13_final, A_3_3_Caminar, B_6_vomito, B_7_taxi, B_8_dormir, B_11_ignorado, B_12_robo, B_15_fifa, B_18_solo, B_19_muerte, A_4_4_Carulla]
____
*GIC* = \
S -> FA \
FA -> Pi PA P\
Pi -> SINi | PLURi\
P -> SIN | PLUR\
SINi -> DetA NA VA\
PLURi -> DetAs  NAs  VAs\                   
SIN -> DetA  NB\
PLUR -> DetAs  NBs\
NAA -> NA | NB\
DetA -> un \
DetAs -> unos
NA -> gato | perro | niño\
NAs -> gatos | perros | niños\
NB -> juguete | arbol | carro | balon | botellon | colchon\
NBs -> juguetes | arboles | carros | balones | botellones | colchones\
VA -> juega | corre | duerme | salta\
VAs -> juegan | corren | duermen | saltan\
PA -> sobre | bajo | cerca de | junto a | con

## Scenario for testing
| Nombre | Clase | Escenario |
|--------|-------|-----------|
|TestStory|tistory|*DFA*, *q0* = initial state, *WINNING_STATES*, *LOSING_STATES*, *ACCEPTANCE_STATES*, *GIC* |


## Tests for automatons
### Receives *DFA*, *q0*, *WINNING_STATES*, *LOSING_STATES* and *ACCEPTANCE_STATES* then it verifies that a path is valid

|Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| tistory | playStory | test| "Buscar transporte","esperar un cupo", "dormir en el cupo", "caminar hasta casa" | actualState = A_3_3_Caminar|
| tistory | playStory |  | "me presento y pongo conversacion", "aceptar", "retirarme", "pedir un taxi" | actualSate = B_7_Taxi |

## Tests for regular expressions
Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory | checkRegEx | TestStory | The user inputs "Buscar Uber" | The RE accepts and takes the one already defined |
| TiStory | chackRegEx | TestStory | The user inputs "Irte con fiestero" | The RE fails to recognize anything so it doesn´t accepts it |


## Test for transductor
Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory |  |  | |
| TiStory |  |  | 


## Test Grammars
Receives *GIC* and *S* = variable

Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory | generarCadena | TestPath3 | actual_state + ('x') |  |

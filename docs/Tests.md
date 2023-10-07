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



 grammar_phrases = [
        "un gato juega sobre un juguete",
        "un gato juega bajo un juguete",
        "un gato juega cerca de un juguete",
        "un gato juega junto a un juguete",
        "un gato juega con un juguete",
        "un gato juega sobre un arbol",
        "un gato juega bajo un arbol",
        "un gato juega cerca de un arbol",
        "un gato juega junto a un arbol",
        "un gato juega con un arbol",
        "un gato juega sobre un carro",
        "un gato juega bajo un carro",
        "un gato juega cerca de un carro",
        "un gato juega junto a un carro",
        "un gato juega con un carro",
        "un gato juega sobre un juguete",
        "un gato juega bajo un juguete",
        "un gato juega cerca de un juguete",
        "un gato juega junto a un juguete",
        "un gato juega con un juguete",
        "un gato juega sobre un arbol",
        "un gato juega bajo un arbol",
        "un gato juega cerca de un arbol",
        "un gato juega junto a un arbol",
        "un gato juega con un arbol",
        "un gato juega sobre un carro",
        "un gato juega bajo un carro",
        "un gato juega cerca de un carro",
        "un gato juega junto a un carro",
        "un gato juega con un carro",
        "un gato corre sobre un juguete",
        "un gato corre bajo un juguete",
        "un gato corre cerca de un juguete",
        "un gato corre junto a un juguete",
        "un gato corre con un juguete",
        "un gato corre bajo un arbol",
        "un gato corre cerca de un arbol",
        "un gato corre junto a un arbol",
        "un gato corre con un arbol",
        "un gato corre sobre un carro",
        "un gato corre bajo un carro",
        "un gato corre cerca de un carro",
        "un gato corre junto a un carro",
        "un gato corre con un carro",
        "un gato duerme sobre un juguete",
        "un gato duerme bajo un juguete",
        "un gato duerme cerca de un juguete",
        "un gato duerme junto a un juguete",
        "un gato duerme con un juguete",
        "un gato duerme sobre un arbol",
        "un gato duerme bajo un arbol",
        "un gato duerme cerca de un arbol",
        "un gato duerme junto a un arbol",
        "un gato duerme con un arbol",
        "un gato duerme sobre un carro",
        "un gato duerme bajo un carro",
        "un gato duerme cerca de un carro",
        "un gato duerme junto a un carro",
        "un gato duerme con un carro",
        "un gato salta sobre un juguete",
        "un gato salta bajo un juguete",
        "un gato salta cerca de un juguete",
        "un gato salta junto a un juguete",
        "un gato salta con un juguete",
        "un gato salta sobre un arbol",
        "un gato salta bajo un arbol",
        "un gato salta cerca de un arbol",
        "un gato salta junto a un arbol",
        "un gato salta con un arbol",
        "un gato salta sobre un carro",
        "un gato salta bajo un carro",
        "un gato salta cerca de un carro",
        "un gato salta junto a un carro",
        "un gato salta con un carro",
        "un gato juega sobre un balon",
        "un gato juega bajo un balon",
        "un gato juega cerca de un balon",
        "un gato juega junto a un balon",
        "un gato juega con un balon",
        "un gato corre sobre un balon",
        "un gato corre bajo un balon",
        "un gato corre cerca de un balon",
        "un gato corre junto a un balon",
        "un gato corre con un balon",
        "un gato duerme sobre un botellon",
        "un gato duerme bajo un botellon",
        "un gato duerme cerca de un botellon",
        "un gato duerme junto a un botellon",
        "un gato duerme con un botellon",
        "un gato salta sobre un botellon",
        "un gato salta bajo un botellon",
        "un gato salta cerca de un botellon",
        "un gato salta junto a un botellon",
        "un gato salta con un botellon",
        "un gato juega sobre un colchon",
        "un gato juega bajo un colchon",
        "un gato juega cerca de un colchon",
        "un gato juega junto a un colchon",
        "un gato juega con un colchon",
        "un gato corre sobre un colchon",
        "un gato corre bajo un colchon",
        "un gato corre cerca de un colchon",
        "un gato corre junto a un colchon",
        "un gato corre con un colchon",
        "un gato duerme sobre un colchon",
        "un gato duerme bajo un colchon",
        "un gato duerme cerca de un colchon",
        "un gato duerme junto a un colchon",
        "un gato duerme con un colchon",
        "un gato salta sobre un colchon",
        "un gato salta bajo un colchon",
        "un gato salta cerca de un colchon",
        "un gato salta junto a un colchon",
        "un gato salta con un colchon",
        "un gato duerme bajo un botellon",
        "un gato duerme cerca de un botellon",
        "un gato duerme junto a un botellon",
        "un gato duerme con un botellon",
        "un gato salta sobre un botellon",
        "un gato salta bajo un botellon",
        "un gato salta cerca de un botellon",
        "un gato salta junto a un botellon",
        "un gato salta con un botellon",
        "un gato juega sobre un botellon",
        "un gato juega bajo un botellon",
        "un gato juega cerca de un botellon",
        "un gato juega junto a un botellon",
        "un gato juega con un botellon",
        "un gato corre sobre un botellon",
        "un gato corre bajo un botellon",
        "un gato corre cerca de un botellon",
        "un gato corre junto a un botellon",
        "un gato corre con un botellon",
        "un gato duerme sobre un colchon",
        "un gato duerme bajo un colchon",
        "un gato duerme cerca de un colchon",
        "un gato duerme junto a un colchon",
        "un gato duerme con un colchon",
        "un gato salta sobre un colchon",
        "un gato salta bajo un colchon",
        "un gato salta cerca de un colchon",
        "un gato salta junto a un colchon",
        "un gato salta con un colchon",
        "un niño juega sobre un juguete",
        "un niño juega bajo un juguete",
        "un niño juega cerca de un juguete",
        "un niño juega junto a un juguete",
        "un niño juega con un juguete",
        "un niño juega sobre un arbol",
        "un niño juega bajo un arbol",
        "un niño juega cerca de un arbol",
        "un niño juega junto a un arbol",
        "un niño juega con un arbol",
        "un niño juega sobre un carro",
        "un niño juega bajo un carro",
        "un niño juega cerca de un carro",
        "un niño juega junto a un carro",
        "un niño juega con un carro",
        "un niño corre sobre un juguete",
        "un niño corre bajo un juguete",
        "un niño corre cerca de un juguete",
        "un niño corre junto a un juguete",
        "un niño corre con un juguete",
        "un niño corre sobre un arbol",
        "un niño corre bajo un arbol",
        "un niño corre cerca de un arbol",
        "un niño corre junto a un arbol",
        "un niño corre con un arbol",
        "un niño corre sobre un carro",
        "un niño corre bajo un carro",
        "un niño corre cerca de un carro",
        "un niño corre junto a un carro",
        "un niño corre con un carro",
        "un niño duerme sobre un juguete",
        "un niño duerme bajo un juguete",
        "un niño duerme cerca de un juguete",
        "un niño duerme junto a un juguete",
        "un niño duerme con un juguete",
        "un niño duerme sobre un arbol",
        "un niño duerme bajo un arbol",
        "un niño duerme cerca de un arbol",
        "un niño duerme junto a un arbol",
        "un niño duerme con un arbol",
        "un niño duerme sobre un carro",
        "un niño duerme bajo un carro",
        "un niño duerme cerca de un carro",
        "un niño duerme junto a un carro",
        "un niño duerme con un carro",
        "un niño salta sobre un balon",
        "un niño salta bajo un balon",
        "un niño salta cerca de un balon",
        "un niño salta junto a un balon",
        "un niño salta con un balon",
        "un niño salta sobre un botellon",
        "un niño salta bajo un botellon",
        "un niño salta cerca de un botellon",
        "un niño salta junto a un botellon",
        "un niño salta con un botellon",
        "un niño juega sobre un colchon",
        "un niño juega bajo un colchon",
        "un niño juega cerca de un colchon",
        "un niño juega junto a un colchon",
        "un niño juega con un colchon",
        "un niño corre sobre un colchon",
        "un niño corre bajo un colchon",
        "un niño corre cerca de un colchon",
        "un niño corre junto a un colchon",
        "un niño corre con un colchon",
        "un niño duerme sobre un colchon",
        "un niño duerme bajo un colchon",
        "un niño duerme cerca de un colchon",
        "un niño duerme junto a un colchon",
        "un niño duerme con un colchon",
        "un niño salta sobre un colchon",
        "un niño salta bajo un colchon",
        "un niño salta cerca de un colchon",
        "un niño salta junto a un colchon",
        "un niño salta con un colchon",
        "un niño duerme bajo un botellon",
        "un niño duerme cerca de un botellon",
        "un niño duerme junto a un botellon",
        "un niño duerme con un botellon",
        "un niño salta sobre un botellon",
        "un niño salta bajo un botellon",
        "un niño salta cerca de un botellon",
        "un niño salta junto a un botellon",
        "un niño salta con un botellon",
        "un niño juega sobre un botellon",
        "un niño juega bajo un botellon",
        "un niño juega cerca de un botellon",
        "un niño juega junto a un botellon",
        "un niño juega con un botellon",
        "un niño corre sobre un botellon",
        "un niño corre bajo un botellon",
        "un niño corre cerca de un botellon",
        "un niño corre junto a un botellon",
        "un niño corre con un botellon",
        "un niño duerme sobre un colchon",
        "un niño duerme bajo un colchon",
        "un niño duerme cerca de un colchon",
        "un niño duerme junto a un colchon",
        "un niño duerme con un colchon",
        "un niño salta sobre un colchon",
        "un niño salta bajo un colchon",
        "un niño salta cerca de un colchon",
        "un niño salta junto a un colchon",
        "un niño salta con un colchon"
___
## Scenario for testing
| Nombre | Clase | Escenario |
|--------|-------|-----------|
|TestStory|tistory|*DFA*, *q0* = initial state, *WINNING_STATES*, *LOSING_STATES*, *ACCEPTANCE_STATES*, *GIC* |


## Tests for automatons
Receives *DFA*, *q0*, *WINNING_STATES*, *LOSING_STATES* and *ACCEPTANCE_STATES* then it verifies that a path is valid

|Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| tistory | playStory | test| "Buscar transporte","esperar un cupo", "dormir en el cupo", "caminar hasta casa" | actualState = A_3_3_Caminar|
| tistory | playStory |  | "me presento y pongo conversacion", "aceptar", "retirarme", "pedir un taxi" | actualSate = B_7_Taxi |

## Tests for regular expressions
Receives *INPUT_SYMBOLS*

Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory | checkRegEx | TestStory | "Buscar Uber" | The RE searches for one of the input symbols in the input from the user |
| TiStory | chackRegEx | TestStory | "Irte con fiestero" | The RE fails to recognize anything so it doesn´t accepts it |

## Tests for gramatics
Receives *a phrase such as un gato salta sobre un colchon* and verifies that is in the list of gramatic generated phrases.

Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory | checkRegEx | TestStory | "un gato salta sobre un colchon" | Asserts on the test  |
| TiStory | chackRegEx | TestStory | "Un tigre corre sobre un avion" | The phrase can't be found on the list so it returns false. |


## Test for transductor
Default = "jugador123456789101112131415161718192021222324252627282930"
Clase|Métodos|Escenario|Valores de Entrada|Resultado|
|----|----|----|----|-----|
| TiStory | nameChanger |  | "Luis", "Default" | "Luis" |
| TiStory | nameChanger |  |"Juan", "Default" | "Juan" |
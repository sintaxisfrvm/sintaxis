from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.pda.dpda import DPDA
# DPDA which which matches zero or more 'a's, followed by the same
# number of 'b's (accepting by final state)
dpda = DPDA(
    states={'q0', 'q1'},
    input_symbols={'x', 'y'},
    stack_symbols={'0', '1'},
    transitions={
        'q0': {
            'x': {'0': ('q0', ('1', '0'))},  # transition pushes '1' to stack
            'x': {'1': ('q0', ('1', '1'))},  # transition pushes '1' to stack
             '': {'1': ('q1', ('1',))},
             '': {'0': ('q1', ('0',))}
            
        },
        
        'q1': {
            'y': {'1': ('q1', '')}
        }
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q1'}
)
#test = ["01001","10101","10100","10001","1000111110111","1110110","101010101","101","1010101111100","1111000011101010","1100001010101101","1011100001010","11111000101","11110001010","1111000000101","00111101","1101","0","","10010","1110","111100","0","1","00","11","111","11100","0011010","1100000000000000111111111","11001000110010110","111","000","1111100000","111110011"]

test= ["xyxyx","xyxyxyyx","xyx","xyxyxyxy","xyxyxyxyx","xyyyxx","xxxxyyy","xxxyyy","xy","","xxyy","xxxxxyyyyy"]
for i in range(0,len(test)):
    #print(i)
    if dpda.accepts_input(test[i]):
        print(test[i]+' =accepted')
    else:
        print(test[i]+' =rejected')
    

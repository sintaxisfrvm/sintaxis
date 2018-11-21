parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).

female(pam).
female(liz).
female(ann).
female(pat).
male(jim).
male(tom).
male(bob).

offspring(Y,X):-parent(X,Y).

mother(X,Y):-parent(X,Y),female(X).
grandparent(X,Z):-parent(X,Y),parent(Y,Z).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),different(X,Y).

different(X,Y):-X\=Y.

predecessor(X,Z):-parent(X,Z).
predecessor(X,Z):-parent(X,Y),predecessor(Y,Z).

member(X,[X|Tail]).
member(X,[Head|Tail]):-member(X,Tail).

conc([],L,L).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).


% gender
female(elizabeth).
female(ann).

male(charles).
male(andrew).
male(edward).

% order of birth
older(charles, ann).
older(ann, andrew).
older(andrew, edward).

is_older(X, Y):-
	older(X, Y).
is_older(A, B):-
	older(A, X),
	is_older(X, B).

% parent
offspring_of(charles, elizabeth).
offspring_of(ann, elizabeth).
offspring_of(andrew, elizabeth).
offspring_of(edward, elizabeth).

% old royal succession rule
quick_sort(List, Sorted) :- q_sort(List, [], Sorted).
q_sort([], Acc, Acc).
q_sort([H|T], Acc, Sorted):-
	pivoting(H,T,L1,L2),
	q_sort(L1, Acc, Sorted1),
	q_sort(L2, [H|Sorted1], Sorted).
   
pivoting(_, [], [], []).
pivoting(H, [X|T], [X|L], G) :- not(in_order(X, H)), pivoting(H, T, L, G).
pivoting(H, [X|T], L, [X|G]) :- in_order(X, H), pivoting(H, T, L, G).

in_order(X, Y) :-
	male(X),
	female(Y).

in_order(X, Y) :-
	male(X),
	male(Y),
	is_older(X, Y).

in_order(X, Y) :-
	female(X),
	female(Y),
	is_older(X, Y).

succession_list(SuccessionList):- 
    findall(Y, offspring_of(Y, elizabeth), OffspringList),
	quick_sort(OffspringList, SuccessionList).

company(sumsum).
comapny(appy).
competitor(sumsum, appy).
owns(sumsum, galacticas3).
smart_phone_technology(galacticas3).
stole(stevey, galacticas3).
boss(stevey).

unethical(X) :-
	boss(X),
	stole(X, Y),
	business(Y),
	owns(Z, Y),
	rival(Z),
	company(Z).

rival(X) :-
	competitor(X, appy).

business(X) :-
	smart_phone_technology(X).

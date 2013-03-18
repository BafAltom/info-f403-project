# Teste Erreur 3 : On teste le variable shadowing
# On vérifie que les fonctions n'ont pas accès aux variables définies dans le main (et inversément) ou dans d'autres fonctions
# En commentant alternativement certaines lignes, on voit qu'elles renvoyent tous une erreur
# L'erreur indique le nom de la variable qui pose problème

sub testFunct1 ($arg0, $arg1) {
	#$arg0 = $arg2;				# a décommenter pour le premier test
	$arg3 = 1;
	return $arg0;
}

sub testFunct3 ($arg0, $arg1) {
	#$arg0 = $arg3;			# a décommenter pour le deuxième test
	return $arg0;
}

sub testFunct2 ($arg0, $arg1) {
	$arg3 = 5;
	&testFunct3($arg0, $arg1);
	return $arg0;
}

# main
print ('teste erreur 3 : variable shadowing\n');

$arg0 = 6;
$arg1 = 2;
$arg2 = 2;

&testFunct1($arg0, $arg1);
&testFunct2($arg0, $arg1);
$arg0 = $arg3;			# a décommenter pour le troisième test

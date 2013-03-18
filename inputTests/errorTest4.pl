# Teste Erreur 4 : On teste le variable shadowing
# On vérifie que les conditions n'ont pas accès aux variables définies dans les autres conditions
# En commentant alternativement certaines lignes, on voit qu'ils renvoyent tous une erreur
# L'erreur indique le nom de la variable qui pose problème


# main
print ('teste erreur 4 : variable shadowing\n');

$arg0 = 6;
$arg1 = 2;
$arg2 = 2;


if $arg0 == 1 { } 
elsif $arg0 == 6 { 
	$arg4 = $arg1;
	if $arg1 > $arg0 { $arg3 = 5; $arg0 = $arg4;} # On peut appeler les variables définies aux niveaux supérieurs
	elsif $arg1 == $arg2 { #$arg2 = $arg3;		# a décommenter pour le premier test 
	}
	else {   } ;
} 
elsif $arg0 == 3 {   } 
else {   };

$arg0 = $arg3;									# a décommenter pour le deuxième test

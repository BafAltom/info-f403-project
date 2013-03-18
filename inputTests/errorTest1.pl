# Teste Erreur 1 : Vérification du nombre de paramètre
# On vérifie que notre programme renvoie bien une erreur lorsqu'on rentre le mauvais nombre de paramètres dans un appel de fonction
# En commentant alternativement un des appels de fonctions, on voit qu'ils renvoyent tout les deux une erreur
# L'erreur indique le nom de la fonction, et le nombre de paramètres qu'elle nécessite

sub testFunct ($arg1, $arg1) {
	$arg1 = 1;
	return $arg1;
}


# main
print ('teste erreur 1 : fonctions et nombre de paramètres\n');

$arg0 = 6;
$arg1 = 2;
$arg2 = 3;

&testFunct($arg0, $arg1, $arg2);
#&testFunct($arg0);

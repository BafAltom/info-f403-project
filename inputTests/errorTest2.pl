# Teste Erreur 2 : On vérifie que les fonctions ne prennent que des variables en argument
# La grammaire imposant que les fonctions ne prennent que des arguments en paramètres
# En commentant alternativement un des appels de fonctions, on voit qu'ils renvoyent tous une erreur
# L'erreur indique le nom de la fonction, et le type d'erreur

sub testFunct ($arg1, $arg1) {
	$arg1 = 1;
	return $arg1;
}


# main
print ('teste erreur 2 : fonctions et paramètres\n');

$arg0 = 6;
$arg1 = 2;

&testFunct($arg0, 4);
&testFunct($arg0, 'test');
#&testFunct($arg0, &testFunct($arg0, $arg1));

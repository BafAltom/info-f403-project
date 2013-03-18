# Teste 5 : Teste très simple
# C'est le code repris dans l'annexe du rapport, Fig 17 et suivantes
# Il a été conçu pour être simple mais assez complet afin de ne pas surcharger le rapport.

sub incr ($arg1) {
	return $arg1 +1;
}


# main
print ('teste compilateur\n'); # function call

$arg1 = 1;
$arg1 = &incr($arg1);
if $arg1 == 2 { print ('increment sucessfull\n'); } 
else { print ('erreur'); };	




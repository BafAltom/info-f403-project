# Teste 2 : Fonctions
# On teste un code contenant des fonctions
# On vérifie que les appels récursifs, les passages de paramètres et les retours de fonctions fonctionnent



sub metA1 ($arg1) {
	$arg1 = 1;
	return $arg1;
}

sub incr ($arg1) {
	return $arg1 +1;
}

sub metA2Util ($arg1) {
	return 2;
}

sub metA2 ($arg1) {
	return &metA2Util($arg1);
}

sub recursif ($arg1) {
	$arg1 = $arg1 +1;
	if($arg1 > 5){ 
		print ('funct recursive\n');}
	else { 
		$arg1 = &recursif($arg1);};
	
	return $arg1;
	
}

sub testFunct ($arg0, $arg1, $arg2) {	
	if $arg0 == 6 { 
		if $arg1 == 2 {
			if $arg2 == 3 { print ('passage param : ok\n'); }
			elsif $arg0 == 3 { print ('passage param : erreur'); } 
			else { print ('passage param : erreur'); };
		}
		else { print ('passage param : erreur'); }; }
	else { print ('passage param : erreur'); };
	
	$arg0 = &metA1($arg1);
	# Met $arg0 a 1
	
	if $arg0 == 1 { print ('assign funct : ok\n'); } 
	else { print ('assign funct erreur'); };
	
	$arg2 = &incr($arg2);
	# incrémente $arg2
	
	if $arg2 == 4 { print ('assign funct : ok\n'); } 
	else { print ('assign funct erreur'); };
	
	
	$arg0 = &metA2($arg1);
	# Met $arg0 a 2
	
	if $arg0 == 2 { print ('return funct : ok\n'); } 
	else { print ('return funct : erreur'); };	
	
	$arg0 = &metA1($arg1)+3;
	# Met $arg0 a 4
	
	if $arg0 == 4 { print ('assign funct et exp : ok\n'); } 
	else { print ('assign funct et exp : erreur'); };	
	
	$arg1 =1;
	$arg1 = &recursif($arg1);
	if $arg1 == 6 { print ('recursion : ok\n'); } 
	else { print ('recursion : erreur'); };
	
	return 4;
	
}

# main
print ('teste 2 : fonctions\n');

$arg0 = 6;
$arg1 = 2;
$arg2 = 3;
&testFunct($arg0, $arg1, $arg2);





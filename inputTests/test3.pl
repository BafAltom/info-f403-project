# Teste avec des fonctions

# function declaration
sub testCond ($number, $arg1, $arg2) {

	print ('funct0 : testCond\n');
	
	if $number == 1 { print ('premiere if : erreur'); } 
	elsif $number == 6 { 
		if $arg1 > $number { print ('deuxieme if : erreur'); } 
		elsif $arg1 == $arg2 { 	
			if $number == 6 { print ('troisieme if : ok\n'); } 
			elsif $number == 8 { print ('troisieme if : elsif : erreur');} 
			else { print ('troisieme if : else : erreur'); };
		}
		else { print ('deuxieme if : else : erreur'); } ;
	} 
	elsif $number == 3 { print ('premier if : elsif2 : erreur'); } 
	else { print ('premier if : else : erreur'); };

	$arg1 = $arg2 + 4;


	if $number == 1 { print ('premier if : erreur'); } 
	elsif $number == 6 { 
		if $arg1 == $number { print ('deuxieme if : ok\n'); } 
		elsif $arg1 == $arg2 { 	
			if $number == 6 { print ('troisieme if : erreur'); } 
			elsif $number == 8 { print ('troisieme if : elsif : erreur');} 
			else { print ('troisieme if : else : erreur'); };
		}
		else { print ('deuxieme if : else : erreur'); } ;
	} 
	elsif $number == 3 { print ('premier if : elsif2 : erreur'); } 
	else { print ('premier if : else : erreur'); };
	
	return 4;
	
}

sub testFunct ($number, $arg1, $arg2) {
	
	print ('funct1 : testFunct\n');
	
	if $number == 6 { 
		if $arg1 == 2 {
			if $arg2 == 3 { print ('passage param : ok\n'); } 
			else { print ('passage param : erreur'); };
		}
		else { print ('passage param : erreur'); }; }
	else { print ('passage param : erreur'); };
	
	$number = &metA1($arg1);
	# Met number a 1
	
	if $number == 1 { print ('assign funct : ok\n'); } 
	else { print ('assign funct erreur'); };
	
	
	$number = &metA2($arg1);
	# Met number a 2
	
	if $number == 2 { print ('return funct : ok\n'); } 
	else { print ('return funct : erreur'); };	
	
	$number = &metA1($arg1)+3;
	# Met number a 4
	
	if $number == 4 { print ('assign funct et exp : ok\n'); } 
	else { print ('assign funct et exp : erreur'); };	
	
	$arg1 =1;
	$arg1 = &recursif($arg1);
	if $arg1 == 6 { print ('recursion : ok\n'); } 
	else { print ('recursion : erreur'); };
	
	
	return 4;
	
}
sub metA1 ($arg1) {
	$arg1 = 1;
	print ('funct2\n');
	return $arg1;
}
sub metA2 ($arg1) {
	print ('funct3\n');
	return &metA2Util($arg1);
}
sub metA2Util ($arg1) {
	print ('funct4\n');
	return 2;
}
sub recursif ($arg1) {
	$arg1 = $arg1 +1;
	if($arg1 > 5){ 
		print ('funct5\n');}
	else { 
		$arg1 = &recursif($arg1);};
	
	return $arg1;
	
}
sub testExp ($arg1) {
	$arg2 =2;
	$number = 3;
	$arg1 = $arg1 * ($arg2 + ($number - $arg2));
	
	if $arg1 == 12 { print ('exp : ok\n'); } 
	else { print ('exp : erreur'); };	
	
	return $arg1;
}
# variable & string declaration



# main

$arg1 = 2;
$arg2 = 2;
$number = 6;
$arg8 = 9;



print ('teste cond + assign + funct + exp\n'); # function call


&testCond($number, $arg1, $arg2);

$arg1 = 2;
$arg2 = 3;
$number = 6;
&testFunct($number, $arg1, $arg2);

$arg1 = 2;
$number = 4;
&testExp($number);








$arg11 = 11;
	$arg12 = 12;
	$arg13 = 13;
	$arg14 = 14;
	$arg15 = 15;
	$arg16 = 16;
	$arg17 = 17;
	$arg18 = 18;
	$arg19 = 19;
	$arg20 = 20;
	$arg21 = 21;
	$arg22 = 22;
	$arg23 = 23;
	$arg24 = 24;
	$arg25 = 25;
	$arg26 = 26;
	$arg27 = 27;
	$arg28 = 28;
	$arg29 = 29;
	$arg30 = 30;
	$arg31 = 31;
	$arg32 = 32;
	$arg33 = 33;
	$arg34 = 34;
	$arg35 = 35;
	$arg36 = 36;
	$arg37 = 37;
	$arg38 = 38;
	$arg39 = 39;
	$arg40 = 40;
	$arg41 = 41;
	$arg42 = 42;
	$arg43 = 43;
	$arg44 = 44;
	$arg45 = 45;
	$arg46 = 46;
	$arg47 = 47;
	$arg48 = 48;
	$arg49 = 49;
	$arg50 = 50;
	$arg51 = 51;
	$arg52 = 52;
	$arg53 = 53;
	$arg54 = 54;
	$arg55 = 55;
	$arg56 = 56;
	$arg57 = 57;
	$arg58 = 58;
	$arg59 = 59;
	$arg60 = 60;

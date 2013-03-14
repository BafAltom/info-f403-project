# Teste avec des fonctions

# function declaration
sub println ($number, $arg1, $arg2) {
	
	print ('funct1\n');
	
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
	
	#$number = &test1($arg1); BUG, ????????
	$number = 1;
	&test1($arg1);
	
	if $number == 1 { print ('premier if : ok\n'); } 
	elsif $number == 6 { 
		if $arg1 == $number { print ('deuxieme if : erreur'); } 
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
sub test1 ($arg1) {
	$arg1 = 2;
	print ('funct2\n');
	return 1;
}
# variable & string declaration



# main

$arg1 = 2;
$arg2 = 2;
$number = 6;




print ('teste du main', '\n', 'cond + assign + funct\n'); # function call


if $number == 1 { print ('premier if : erreur'); } 
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


&println($number, $arg1, $arg2);


$arg1 = $arg1 * ($arg2 + ($number - $arg2));

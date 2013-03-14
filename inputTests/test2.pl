
	$arg1 = 2;
	$arg2 = 2;
	$number = 6;


# variable & string declaration

print ('teste du main', '\n', 'cond + assign\n'); # function call


if $number == 1 { print ('premier if : erreur'); } 
elsif $number == 6 { 
	if $arg1 > $number { print ('deuxieme if : erreur'); } 
	elsif $arg1 == $arg2 { 	
		if $number == 6 { print ('troisieme if : ok'); } 
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
	if $arg1 == $number { print ('deuxieme if : ok'); } 
	elsif $arg1 == $arg2 { 	
		if $number == 6 { print ('troisieme if : erreur'); } 
		elsif $number == 8 { print ('troisieme if : elsif : erreur');} 
		else { print ('troisieme if : else : erreur'); };
	}
	else { print ('deuxieme if : else : erreur'); } ;
} 
elsif $number == 3 { print ('premier if : elsif2 : erreur'); } 
else { print ('premier if : else : erreur'); };

# Teste 3 : conditions
# On teste un code contenant des conditions
# On vérifie que les conditions imbriquées fonctionnent


print ('teste 3 : conditions\n'); # function call

$arg0 = 6;
$arg1 = 2;
$arg2 = 2;


if $arg0 == 1 { print ('premiere if : erreur');} 
elsif $arg0 == 6 { 
	if $arg1 > $arg0 { print ('deuxieme if : erreur');} 
	elsif $arg1 == $arg2 { 	
		if $arg0 == 6 { print ('troisieme if : ok\n');} 
		elsif $arg0 == 8 { print ('troisieme if : elsif : erreur');} 
		else { print ('troisieme if : else : erreur'); };
	}
	else { print ('deuxieme if : else : erreur'); } ;
} 
elsif $arg0 == 3 { print ('premier if : elsif2 : erreur'); } 
else { print ('premier if : else : erreur'); };


$arg1 = $arg2 + 4;


if $arg0 == 1 { print ('premier if : erreur'); } 
elsif $arg0 == 6 { 
	if $arg1 == $arg0 { print ('deuxieme if : ok\n'); } 
	elsif $arg1 == $arg2 { 	
		if $arg0== 6 { print ('troisieme if : erreur'); } 
		elsif $arg0 == 8 { print ('troisieme if : elsif : erreur');} 
		else { print ('troisieme if : else : erreur'); };
	}
	else { print ('deuxieme if : else : erreur'); } ;
} 
elsif $arg0 == 3 { print ('premier if : elsif2 : erreur'); } 
else { print ('premier if : else : erreur'); };





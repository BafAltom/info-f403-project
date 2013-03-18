# Teste 1 : Expression
# On teste un code simple, sans fonctions, ne contenant que des expressions.


print ('teste 1 : expression\n');

$arg0 = 4;
$arg1 = 2;
$arg2 = 2 +1;
$arg3 = 'argument4';

if $arg1 > 1 { print ('exp : ok\n'); } 
else { print ('exp : erreur'); };


$arg1 = $arg1 * ($arg2 + ($arg0 - $arg2));
if $arg1 == 8 { print ('exp : ok\n'); } 
else { print ('exp : erreur'); };	

	
$arg1 = $arg1 * $arg2;
if $arg1 == 24 { print ('exp : ok\n'); } 
else { print ('exp : erreur'); };

	
$arg1 = 4 - $arg2;
if $arg1 == 1 { print ('exp : ok\n'); } 
else { print ('exp : erreur'); };






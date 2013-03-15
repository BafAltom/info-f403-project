#print 'The value is '.$myVar.'
#';

# function declaration
sub println ($message) {
	
	
	print ('funct1');
	&test1($message);
	return 4;
	
}
sub test1 ($arg1, $arg2, $arg3, $arg4) {
	$arg1 = 2;
	$arg2 = 9;
	#$argS1 = 'zuyefz';
	#$argS2 = 'zuyefetetzrtzz';
	$arg3 = 15;
	$arg5 = $arg3;
	#$argS3 = 'zuyefz';
	#$arg1 = $arg1 + 1;
	#$arg2 = $arg2 + 'sdhfg';
	#$arg4 = $arg2 - $arg1;
	#$arg4 = $arg2 - 'zuyefz';
	#return $arg1 * ($arg2 + ($arg3 + $arg4));
	#return $arg1;
	#return 4;
	#return 'qhdg';
	$number = 6;
	print ('funct2');
	return 4;
}
# variable & string declaration


#$message = 'Hello World';
#$truc = 4;
#$number = 4 - (3 + 2);
# if $number == 4 - (3 - 2)
# {
# 	print("Good")
# }
# function call
$message = 5;
print ('is equal to 2', '\n', 'shgdfjshfg\n'); # function call
&println($message, $message, $message);

#$arg4 = &println($message);
#return &test1($number, 3*$number, 2*$number, 4*$number);
#$arg4 = &println($message) + ($arg4 * &println($message));
#$arg4 = &println($message) + &println($message);

#if $number == 1 { print ($number); print('is equal to 1'); } 
#elsif $number == 2 { print ($number); print('is equal to 2'); } 
#elsif $number == 3 { print ($number); print('is equal to 3'); } 
#elsif $number == 4 { print ($number); print('is equal to 4'); } 
#elsif $number == 5 { print ($number); print('is equal to 5'); } 
#else { print ($number); print('is smaller than 5'); };

#if $number == 1 { $number = 6; } 
#elsif $number == 2 { 
#	if $number == 7 { $number = 6; } 
#	elsif $number == 8 { 	
#		if $number == 7 { $number = 6; } 
#		elsif $number == 8 { $number = 6;} 
#		else { $number = 6; };
#	}
#	else { $number = 6; } ;
#} 
#elsif $number == 3 { $number = 6; } 
#else { $number = 6; };



#print 'The value is '.$myVar.'
#';

# function declaration
sub println ($str) {
	return $str;
}
sub test1 ($arg1, $arg2, $arg3, $arg4) {
	$arg1 = $arg1 + 1;
	$arg2 = $arg2 + $arg3;
	$arg4 = $arg2 - $arg1;

	return $arg1 + ($arg2 + ($arg3 + $arg4));
}
# variable & string declaration


$message = 'Hello World';
$number = 4 - (3 - 2);
# if $number == 4 - (3 - 2)
# {
# 	print("Good")
# }
# function call
print ($number); # function call
&println($message);
&test1($number, 3*$number, 2*$number, 4*$number);

if $number == 1 { print ($number); print('is equal to 1'); } 
elsif $number == 2 { print ($number); print('is equal to 2'); } 
elsif $number == 3 { print ($number); print('is equal to 3'); } 
elsif $number == 4 { print ($number); print('is equal to 4'); } 
elsif $number == 5 { print ($number); print('is equal to 5'); } 
else { print ($number); print('is smaller than 5'); };

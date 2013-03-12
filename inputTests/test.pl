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
&println(&test1($number));
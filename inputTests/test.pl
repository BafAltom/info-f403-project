#print 'The value is '.$myVar.'
#';

# function declaration
sub println ($str) {
	$str = $str;
}
sub test1 ($arg1) {
	$arg1 = $arg1 + 1;
}
# variable & string declaration


$message = 'Hello World';
$number = 4 - 3 - 2;
# function call
print ($number); # function call
&println($message);
&println(&test1($number));



if $number>5 { print ($number); } 
elsif $number == 5 { print ($number);} 
else { print ($number); };

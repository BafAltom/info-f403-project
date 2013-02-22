# Remark : The Perl syntax allows ways to produce simpler codes than
# the one below , but to simplify your work we restrict the syntax
# print "Hello World\n ";
# an example o f how you must handle a function declaration :

sub println ( $str ) {
print $str ;
}

# an example o f how you must handle a variable and string declaration :
$message = ’Hello World’ ;
# an example of how you must handle a function call :
&println ( $message ) ;

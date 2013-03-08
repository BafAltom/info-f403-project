#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MESSAGE "Hellow World"
#define LENGTH 12

void println(char* ptr) {
	printf("%s\n", ptr);
}

static char * message;

int main(int argn, char args[]) {
	message = (char*)calloc(LENGTH+1, sizeof(char));
	strcpy(message, MESSAGE);
	println(message);
	free(message);
	return EXIT_SUCCESS;
}
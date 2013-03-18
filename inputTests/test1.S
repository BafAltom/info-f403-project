	.arch armv5te
	.fpu softvfp
	.eabi_attribute 20 , 1
	.eabi_attribute 21 , 1
	.eabi_attribute 23 , 3
	.eabi_attribute 24 , 1
	.eabi_attribute 25 , 1
	.eabi_attribute 26 , 2
	.eabi_attribute 30 , 6
	.eabi_attribute 18 , 4
 
	.data
 
str0:	.string "teste 1 : expression\n"
len0 = . - str0
str1:	.string "argument4"
len1 = . - str1
str2:	.string "exp : ok\n"
len2 = . - str2
str3:	.string "exp : erreur"
len3 = . - str3

 

 
	.text
 
	.global _start
_start :
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str0
	LDR 	R2, =len0
	MOV 	R7, #4
	SWI 	#0

	MOV 	R4, #4

	MOV 	R5, #2

	MOV 	R7, #2
	MOV 	R8, #1
	ADD	R9, R7, R8
	MOV 	R6, R9

	LDR 	R7, =str1

	MOV 	R8, #1
	CMP	R5, R8
		BLE else00
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end0
else00: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


end0:

	SUB	R8, R4, R6
	ADD	R9, R6, R8
	MUL	R8, R5, R9
	MOV 	R5, R8

	MOV 	R8, #8
	CMP	R5, R8
		BNE else10
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end1
else10: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


end1:

	MUL	R8, R5, R6
	MOV 	R5, R8

	MOV 	R8, #24
	CMP	R5, R8
		BNE else20
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end2
else20: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


end2:

	MOV 	R8, #4
	SUB	R9, R8, R6
	MOV 	R5, R9

	MOV 	R8, #1
	CMP	R5, R8
		BNE else30
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end3
else30: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


end3:


	/* syscall exit*/ 
	MOV     R0, #0
	MOV     R7, #1
	SWI     #0

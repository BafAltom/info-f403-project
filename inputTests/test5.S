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
 
str0:	.string "teste compilateur\n"
len0 = . - str0
str1:	.string "increment sucessfull\n"
len1 = . - str1
str2:	.string "erreur"
len2 = . - str2

 

 
	.text
 
.global incr
.type incr, %function
incr:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, #1
	ADD	R6, R4, R5
	MOV 	R0, R6


	POP	{R4-R11,R14}
	BX	LR
 
	.global _start
_start :
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str0
	LDR 	R2, =len0
	MOV 	R7, #4
	SWI 	#0

	MOV 	R4, #1

	MOV 	R0, R4
	BL	incr
	MOV 	R4, R0

	MOV 	R5, #2
	CMP	R4, R5
		BNE else00
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str1
	LDR 	R2, =len1
	MOV 	R7, #4
	SWI 	#0


	B end0
else00: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


end0:


	/* syscall exit*/ 
	MOV     R0, #0
	MOV     R7, #1
	SWI     #0

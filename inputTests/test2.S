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
 
str0:	.string "funct recursive\n"
len0 = . - str0
str1:	.string "passage param : ok\n"
len1 = . - str1
str2:	.string "passage param : erreur"
len2 = . - str2
str3:	.string "assign funct : ok\n"
len3 = . - str3
str4:	.string "assign funct erreur"
len4 = . - str4
str5:	.string "return funct : ok\n"
len5 = . - str5
str6:	.string "return funct : erreur"
len6 = . - str6
str7:	.string "assign funct et exp : ok\n"
len7 = . - str7
str8:	.string "assign funct et exp : erreur"
len8 = . - str8
str9:	.string "recursion : ok\n"
len9 = . - str9
str10:	.string "recursion : erreur"
len10 = . - str10
str11:	.string "teste 2 : fonctions\n"
len11 = . - str11

 

 
	.text
 
.global metA1
.type metA1, %function
metA1:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R4, #1

	MOV 	R0, R4


	POP	{R4-R11,R14}
	BX	LR
 
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
 
.global metA2Util
.type metA2Util, %function
metA2Util:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R0, #2


	POP	{R4-R11,R14}
	BX	LR
 
.global metA2
.type metA2, %function
metA2:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R0, R4
	BL	metA2Util


	POP	{R4-R11,R14}
	BX	LR
 
.global recursif
.type recursif, %function
recursif:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, #1
	ADD	R6, R4, R5
	MOV 	R4, R6

	MOV 	R5, #5
	CMP	R4, R5
		BLE else00
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str0
	LDR 	R2, =len0
	MOV 	R7, #4
	SWI 	#0


	B end0
else00: 
	MOV 	R0, R4
	BL	recursif
	MOV 	R4, R0


end0:

	MOV 	R0, R4


	POP	{R4-R11,R14}
	BX	LR
 
.global testFunct
.type testFunct, %function
testFunct:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, R1
	MOV 	R6, R2
	MOV 	R7, #6
	CMP	R4, R7
		BNE else10
	MOV 	R7, #2
	CMP	R5, R7
		BNE else20
	MOV 	R7, #3
	CMP	R6, R7
		BNE else30
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str1
	LDR 	R2, =len1
	MOV 	R7, #4
	SWI 	#0


	B end3
else30: 
	MOV 	R7, #3
	CMP	R4, R7
		BNE else31
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end3
else31: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


end3:


	B end2
else20: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


end2:


	B end1
else10: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


end1:

	MOV 	R0, R5
	BL	metA1
	MOV 	R4, R0

	MOV 	R7, #1
	CMP	R4, R7
		BNE else40
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


	B end4
else40: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


end4:

	MOV 	R0, R6
	BL	incr
	MOV 	R6, R0

	MOV 	R7, #4
	CMP	R6, R7
		BNE else50
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


	B end5
else50: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


end5:

	MOV 	R0, R5
	BL	metA2
	MOV 	R4, R0

	MOV 	R7, #2
	CMP	R4, R7
		BNE else60
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str5
	LDR 	R2, =len5
	MOV 	R7, #4
	SWI 	#0


	B end6
else60: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str6
	LDR 	R2, =len6
	MOV 	R7, #4
	SWI 	#0


end6:

	MOV 	R0, R5
	BL	metA1
	MOV 	R7, R0
	MOV 	R8, #3
	ADD	R9, R7, R8
	MOV 	R4, R9

	MOV 	R7, #4
	CMP	R4, R7
		BNE else70
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str7
	LDR 	R2, =len7
	MOV 	R7, #4
	SWI 	#0


	B end7
else70: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str8
	LDR 	R2, =len8
	MOV 	R7, #4
	SWI 	#0


end7:

	MOV 	R5, #1

	MOV 	R0, R5
	BL	recursif
	MOV 	R5, R0

	MOV 	R7, #6
	CMP	R5, R7
		BNE else80
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str9
	LDR 	R2, =len9
	MOV 	R7, #4
	SWI 	#0


	B end8
else80: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str10
	LDR 	R2, =len10
	MOV 	R7, #4
	SWI 	#0


end8:

	MOV 	R0, #4


	POP	{R4-R11,R14}
	BX	LR
 
	.global _start
_start :
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str11
	LDR 	R2, =len11
	MOV 	R7, #4
	SWI 	#0

	MOV 	R4, #6

	MOV 	R5, #2

	MOV 	R6, #3

	MOV 	R0, R4
	MOV 	R1, R5
	MOV 	R2, R6
	BL	testFunct


	/* syscall exit*/ 
	MOV     R0, #0
	MOV     R7, #1
	SWI     #0

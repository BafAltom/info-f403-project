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
 
str0:	.string "funct0 : testCond\n"
len0 = . - str0
str1:	.string "premiere if : erreur"
len1 = . - str1
str2:	.string "deuxieme if : erreur"
len2 = . - str2
str3:	.string "troisieme if : ok\n"
len3 = . - str3
str4:	.string "troisieme if : elsif : erreur"
len4 = . - str4
str5:	.string "troisieme if : else : erreur"
len5 = . - str5
str6:	.string "deuxieme if : else : erreur"
len6 = . - str6
str7:	.string "premier if : elsif2 : erreur"
len7 = . - str7
str8:	.string "premier if : else : erreur"
len8 = . - str8
str9:	.string "premier if : erreur"
len9 = . - str9
str10:	.string "deuxieme if : ok\n"
len10 = . - str10
str11:	.string "troisieme if : erreur"
len11 = . - str11
str12:	.string "funct1 : testFunct\n"
len12 = . - str12
str13:	.string "passage param : ok\n"
len13 = . - str13
str14:	.string "passage param : erreur"
len14 = . - str14
str15:	.string "assign funct : ok\n"
len15 = . - str15
str16:	.string "assign funct erreur"
len16 = . - str16
str17:	.string "return funct : ok\n"
len17 = . - str17
str18:	.string "return funct : erreur"
len18 = . - str18
str19:	.string "assign funct et exp : ok\n"
len19 = . - str19
str20:	.string "assign funct et exp : erreur"
len20 = . - str20
str21:	.string "funct2\n"
len21 = . - str21
str22:	.string "funct3\n"
len22 = . - str22
str23:	.string "funct4\n"
len23 = . - str23
str24:	.string "exp : ok\n"
len24 = . - str24
str25:	.string "exp : erreur"
len25 = . - str25
str26:	.string "teste cond + assign + funct + exp\n"
len26 = . - str26

 

 
	.text
 
.global testCond
.type testCond, %function
testCond:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, R1
	MOV 	R6, R2
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str0
	LDR 	R2, =len0
	MOV 	R7, #4
	SWI 	#0

	MOV 	R7, #1
	CMP	R4, R7
		BNE else00
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str1
	LDR 	R2, =len1
	MOV 	R7, #4
	SWI 	#0


	B end0
else00: 
	MOV 	R7, #6
	CMP	R4, R7
		BNE else01
	CMP	R5, R4
		BLE else10
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end1
else10: 
	CMP	R5, R6
		BNE else11
	MOV 	R7, #6
	CMP	R4, R7
		BNE else20
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


	B end2
else20: 
	MOV 	R7, #8
	CMP	R4, R7
		BNE else21
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


	B end2
else21: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str5
	LDR 	R2, =len5
	MOV 	R7, #4
	SWI 	#0


end2:


	B end1
else11: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str6
	LDR 	R2, =len6
	MOV 	R7, #4
	SWI 	#0


end1:


	B end0
else01: 
	MOV 	R7, #3
	CMP	R4, R7
		BNE else02
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str7
	LDR 	R2, =len7
	MOV 	R7, #4
	SWI 	#0


	B end0
else02: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str8
	LDR 	R2, =len8
	MOV 	R7, #4
	SWI 	#0


end0:

	MOV 	R7, #4
	ADD	R8, R6, R7
	MOV 	R5, R8

	MOV 	R7, #1
	CMP	R4, R7
		BNE else30
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str9
	LDR 	R2, =len9
	MOV 	R7, #4
	SWI 	#0


	B end3
else30: 
	MOV 	R7, #6
	CMP	R4, R7
		BNE else31
	CMP	R5, R4
		BNE else40
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str10
	LDR 	R2, =len10
	MOV 	R7, #4
	SWI 	#0


	B end4
else40: 
	CMP	R5, R6
		BNE else41
	MOV 	R7, #6
	CMP	R4, R7
		BNE else50
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str11
	LDR 	R2, =len11
	MOV 	R7, #4
	SWI 	#0


	B end5
else50: 
	MOV 	R7, #8
	CMP	R4, R7
		BNE else51
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


	B end5
else51: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str5
	LDR 	R2, =len5
	MOV 	R7, #4
	SWI 	#0


end5:


	B end4
else41: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str6
	LDR 	R2, =len6
	MOV 	R7, #4
	SWI 	#0


end4:


	B end3
else31: 
	MOV 	R7, #3
	CMP	R4, R7
		BNE else32
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str7
	LDR 	R2, =len7
	MOV 	R7, #4
	SWI 	#0


	B end3
else32: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str8
	LDR 	R2, =len8
	MOV 	R7, #4
	SWI 	#0


end3:

	MOV 	R0, #4


	POP	{R4-R11,R14}
	BX	LR
 
.global testFunct
.type testFunct, %function
testFunct:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, R1
	MOV 	R6, R2
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str12
	LDR 	R2, =len12
	MOV 	R7, #4
	SWI 	#0

	MOV 	R7, #6
	CMP	R4, R7
		BNE else60
	MOV 	R7, #2
	CMP	R5, R7
		BNE else70
	MOV 	R7, #3
	CMP	R6, R7
		BNE else80
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str13
	LDR 	R2, =len13
	MOV 	R7, #4
	SWI 	#0


	B end8
else80: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str14
	LDR 	R2, =len14
	MOV 	R7, #4
	SWI 	#0


end8:


	B end7
else70: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str14
	LDR 	R2, =len14
	MOV 	R7, #4
	SWI 	#0


end7:


	B end6
else60: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str14
	LDR 	R2, =len14
	MOV 	R7, #4
	SWI 	#0


end6:

	MOV 	R0, R5
	BL	metA1
	MOV 	R4, R0

	MOV 	R7, #1
	CMP	R4, R7
		BNE else90
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str15
	LDR 	R2, =len15
	MOV 	R7, #4
	SWI 	#0


	B end9
else90: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str16
	LDR 	R2, =len16
	MOV 	R7, #4
	SWI 	#0


end9:

	MOV 	R0, R5
	BL	metA2
	MOV 	R4, R0

	MOV 	R7, #2
	CMP	R4, R7
		BNE else100
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str17
	LDR 	R2, =len17
	MOV 	R7, #4
	SWI 	#0


	B end10
else100: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str18
	LDR 	R2, =len18
	MOV 	R7, #4
	SWI 	#0


end10:

	MOV 	R0, R5
	BL	metA1
	MOV 	R7, R0
	MOV 	R8, #3
	ADD	R9, R7, R8
	MOV 	R4, R9

	MOV 	R7, #4
	CMP	R4, R7
		BNE else110
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str19
	LDR 	R2, =len19
	MOV 	R7, #4
	SWI 	#0


	B end11
else110: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str20
	LDR 	R2, =len20
	MOV 	R7, #4
	SWI 	#0


end11:

	MOV 	R0, #4


	POP	{R4-R11,R14}
	BX	LR
 
.global metA1
.type metA1, %function
metA1:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R4, #1

	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str21
	LDR 	R2, =len21
	MOV 	R7, #4
	SWI 	#0

	MOV 	R0, R4


	POP	{R4-R11,R14}
	BX	LR
 
.global metA2
.type metA2, %function
metA2:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str22
	LDR 	R2, =len22
	MOV 	R7, #4
	SWI 	#0

	MOV 	R0, R4
	BL	metA2Util


	POP	{R4-R11,R14}
	BX	LR
 
.global metA2Util
.type metA2Util, %function
metA2Util:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str23
	LDR 	R2, =len23
	MOV 	R7, #4
	SWI 	#0

	MOV 	R0, #2


	POP	{R4-R11,R14}
	BX	LR
 
.global testExp
.type testExp, %function
testExp:
	PUSH	{R4-R11,R14}
	MOV 	R4, R0
	MOV 	R5, #2

	MOV 	R6, #3

	SUB	R7, R6, R5
	ADD	R8, R5, R7
	MUL	R7, R4, R8
	MOV 	R4, R7

	MOV 	R7, #12
	CMP	R4, R7
		BNE else120
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str24
	LDR 	R2, =len24
	MOV 	R7, #4
	SWI 	#0


	B end12
else120: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str25
	LDR 	R2, =len25
	MOV 	R7, #4
	SWI 	#0


end12:

	MOV 	R0, R4


	POP	{R4-R11,R14}
	BX	LR
 
	.global _start
_start :
	MOV 	R4, #2

	MOV 	R5, #2

	MOV 	R6, #6

	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str26
	LDR 	R2, =len26
	MOV 	R7, #4
	SWI 	#0

	MOV 	R0, R6
	MOV 	R1, R4
	MOV 	R2, R5
	BL	testCond

	MOV 	R4, #2

	MOV 	R5, #3

	MOV 	R6, #6

	MOV 	R0, R6
	MOV 	R1, R4
	MOV 	R2, R5
	BL	testFunct

	MOV 	R6, #4

	MOV 	R0, R6
	BL	testExp


	/* syscall exit*/ 
	MOV     R0, #0
	MOV     R7, #1
	SWI     #0

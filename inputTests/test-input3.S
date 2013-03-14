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
 
str0:	.string "funct1\n"
len0 = . - str0
str1:	.string "premier if : erreur"
len1 = . - str1
str2:	.string "deuxieme if : ok\n"
len2 = . - str2
str3:	.string "troisieme if : erreur"
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
str9:	.string "premier if : ok\n"
len9 = . - str9
str10:	.string "deuxieme if : erreur"
len10 = . - str10
str11:	.string "funct2\n"
len11 = . - str11
str12:	.string "teste du main"
len12 = . - str12
str13:	.string "\n"
len13 = . - str13
str14:	.string "cond + assign + funct\n"
len14 = . - str14
str15:	.string "troisieme if : ok\n"
len15 = . - str15

 

 
	.text
 
.global println
.type println, %function
println:
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
		BNE else10
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

	MOV 	R4, #1

	MOV 	R0, R5
	BL	test1

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
	LDR 	R1, =str3
	LDR 	R2, =len3
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
 
.global test1
.type test1, %function
test1:
	PUSH	{R4-R11,R14}
	MOV 	R7, R0
	MOV 	R7, #2

	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str11
	LDR 	R2, =len11
	MOV 	R7, #4
	SWI 	#0

	MOV 	R0, #1


	POP	{R4-R11,R14}
	BX	LR
 
	.global _start
_start :
	MOV 	R8, #2

	MOV 	R9, #2

	MOV 	R10, #6

	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str12
	LDR 	R2, =len12
	MOV 	R7, #4
	SWI 	#0
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str13
	LDR 	R2, =len13
	MOV 	R7, #4
	SWI 	#0
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str14
	LDR 	R2, =len14
	MOV 	R7, #4
	SWI 	#0

	MOV 	R11, #1
	CMP	R10, R11
		BNE else60
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str1
	LDR 	R2, =len1
	MOV 	R7, #4
	SWI 	#0


	B end6
else60: 
	MOV 	R11, #6
	CMP	R10, R11
		BNE else61
	CMP	R8, R10
		BLE else70
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str10
	LDR 	R2, =len10
	MOV 	R7, #4
	SWI 	#0


	B end7
else70: 
	CMP	R8, R9
		BNE else71
	MOV 	R11, #6
	CMP	R10, R11
		BNE else80
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str15
	LDR 	R2, =len15
	MOV 	R7, #4
	SWI 	#0


	B end8
else80: 
	MOV 	R11, #8
	CMP	R10, R11
		BNE else81
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


	B end8
else81: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str5
	LDR 	R2, =len5
	MOV 	R7, #4
	SWI 	#0


end8:


	B end7
else71: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str6
	LDR 	R2, =len6
	MOV 	R7, #4
	SWI 	#0


end7:


	B end6
else61: 
	MOV 	R11, #3
	CMP	R10, R11
		BNE else62
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str7
	LDR 	R2, =len7
	MOV 	R7, #4
	SWI 	#0


	B end6
else62: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str8
	LDR 	R2, =len8
	MOV 	R7, #4
	SWI 	#0


end6:

	MOV 	R11, #4
	ADD	R12, R9, R11
	MOV 	R8, R12

	MOV 	R11, #1
	CMP	R10, R11
		BNE else90
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str1
	LDR 	R2, =len1
	MOV 	R7, #4
	SWI 	#0


	B end9
else90: 
	MOV 	R11, #6
	CMP	R10, R11
		BNE else91
	CMP	R8, R10
		BNE else100
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str2
	LDR 	R2, =len2
	MOV 	R7, #4
	SWI 	#0


	B end10
else100: 
	CMP	R8, R9
		BNE else101
	MOV 	R11, #6
	CMP	R10, R11
		BNE else110
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str3
	LDR 	R2, =len3
	MOV 	R7, #4
	SWI 	#0


	B end11
else110: 
	MOV 	R11, #8
	CMP	R10, R11
		BNE else111
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str4
	LDR 	R2, =len4
	MOV 	R7, #4
	SWI 	#0


	B end11
else111: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str5
	LDR 	R2, =len5
	MOV 	R7, #4
	SWI 	#0


end11:


	B end10
else101: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str6
	LDR 	R2, =len6
	MOV 	R7, #4
	SWI 	#0


end10:


	B end9
else91: 
	MOV 	R11, #3
	CMP	R10, R11
		BNE else92
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str7
	LDR 	R2, =len7
	MOV 	R7, #4
	SWI 	#0


	B end9
else92: 
	/* syscall write	*/ 
	MOV 	R0, #1
	LDR 	R1, =str8
	LDR 	R2, =len8
	MOV 	R7, #4
	SWI 	#0


end9:

	MOV 	R0, R10
	MOV 	R1, R8
	MOV 	R2, R9
	BL	println

	SUB	R11, R10, R9
	ADD	R12, R9, R11
	MUL	R11, R8, R12
	MOV 	R8, R11


	/* syscall exit*/ 
	MOV     R0, #0
	MOV     R7, #1
	SWI     #0

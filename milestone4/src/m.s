	.data
	fmt_int: .string "%d\n" 
	fmt_char: .string "%c\n" 
	.text
	.global main
	.type main, @function
<<<<<<< HEAD
// gunint:
C_gunint:
	// BeginFunc12
	push %ebp
	mov %esp, %ebp
	sub $12, %esp
=======
// main:
main:
	// BeginFunc56
	push %ebp
	mov %esp, %ebp
	sub $56, %esp
>>>>>>> aba1b9314c881b372cb8a6d999f4add546d4191c
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// print_intr@2
	mov 12(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@2=10
	mov $10, %eax
<<<<<<< HEAD
	mov %eax , -8(%ebp)
	// +tmp@0this@20
	mov 8(%ebp), %eax
	mov $0 , %ebx
	add %ebx, %eax
	mov %eax , -4(%ebp)
	// tmp@1=tmp@2
	mov -8(%ebp), %eax
	mov -4(%ebp), %edi
	mov %eax, (%edi)
	// tmp@3=0
	mov $0, %eax
	mov %eax , -12(%ebp)
	// returntmp@3
	mov -12(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc
// main:
main:
	// BeginFunc48
	push %ebp
	mov %esp, %ebp
	sub $48, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@4=&p@3
	lea -12(%ebp), %eax
	mov %eax , -16(%ebp)
	// b@3=tmp@4
	mov -16(%ebp), %eax
	mov %eax , -4(%ebp)
	// tmp@7=5
	mov $5, %eax
	mov %eax , -24(%ebp)
	// -tmp@5124
	mov $12 , %eax
	mov $4 , %ebx
	sub %ebx, %eax
	mov %eax , -20(%ebp)
	// tmp@6=tmp@7
	mov -24(%ebp), %eax
	mov -20(%ebp), %edi
	neg %edi
	mov %eax, (%ebp , %edi, 1)
	// tmp@10=9
	mov $9, %eax
	mov %eax , -32(%ebp)
	// +tmp@8b@30
	mov -4(%ebp), %eax
	mov $0 , %ebx
	add %ebx, %eax
	mov %eax , -28(%ebp)
	// tmp@9=tmp@10
	mov -32(%ebp), %eax
	mov -28(%ebp), %edi
	mov %eax, (%edi)
	// tmp@11=7
	mov $7, %eax
	mov %eax , -36(%ebp)
	// PushParamtmp@11
	mov -36(%ebp), %eax
	push %eax
	// PushParamb@3
	mov -4(%ebp), %eax
	push %eax
	// tmp@12=FcallC:gunint
	call C_gunint
	mov %eax , -40(%ebp)
	// RemoveParams8
	// -tmp@13120
	mov $12 , %eax
	mov $0 , %ebx
	sub %ebx, %eax
	mov %eax , -44(%ebp)
	// print_inttmp@14
	mov -44(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
=======
	mov %eax , -4(%ebp)
	// tmp@1=4*tmp@0
	mov $4 , %eax
	mov -4(%ebp), %ebx
	imul %ebx, %eax
	mov %eax , -8(%ebp)
	// tmp@2=malloc(tmp@1)
	push %ebp
	mov %esp,%ebp
	mov -8(%ebp), %edi
	push %edi
	call malloc
	add $4, %esp
	mov %ebp, %esp
	pop %ebp
	mov %eax , -12(%ebp)
	// p@2=tmp@2
	mov -12(%ebp), %eax
	mov %eax , -16(%ebp)
	// tmp@3=0
	mov $0, %eax
	mov %eax , -20(%ebp)
	// i@3=tmp@3
	mov -20(%ebp), %eax
	mov %eax , -24(%ebp)
// for_begin10:
for_begin10:
	// tmp@4=10
	mov $10, %eax
	mov %eax , -28(%ebp)
	// tmp@5=i@3<tmp@4
	mov -24(%ebp), %eax
	mov -28(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -32(%ebp)
	// ifztmp@5goto->for_after10
	mov -32(%ebp), %eax
	cmp $0 , %eax 
	je for_after10
	// tmp@9=2
	mov $2, %eax
	mov %eax , -44(%ebp)
	// tmp@10=i@3*tmp@9
	mov -24(%ebp), %eax
	mov -44(%ebp), %ebx
	imul %ebx, %eax
	mov %eax , -48(%ebp)
	// tmp@7=p@2+i@3
	mov -16(%ebp), %eax
	mov -24(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -40(%ebp)
	// tmp@8=tmp@10
	mov -48(%ebp), %eax
	mov -40(%ebp), %edi
	mov %eax, (%edi)
	// tmp@11=p@2+i@3
	mov -16(%ebp), %eax
	mov -24(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -52(%ebp)
	// print_inttmp@12
	mov -52(%ebp), %esi
	mov  (%esi), %eax
>>>>>>> aba1b9314c881b372cb8a6d999f4add546d4191c
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
<<<<<<< HEAD
	// tmp@15=0
	mov $0, %eax
	mov %eax , -48(%ebp)
	// returntmp@15
	mov -48(%ebp), %eax
=======
// for_continue10:
for_continue10:
	// tmp@6=i@3
	mov -24(%ebp), %eax
	mov %eax , -36(%ebp)
	// i@3++
	mov -24(%ebp), %eax
	inc  %eax
	mov %eax , -24(%ebp)
	// goto->for_begin10
	jmp for_begin10
// for_after10:
for_after10:
	// freep@2
	push %ebp
	mov %esp,%ebp
	mov -16(%ebp), %edi
	push %edi
	call malloc
	add $4, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@13=0
	mov $0, %eax
	mov %eax , -56(%ebp)
	// returntmp@13
	mov -56(%ebp), %eax
>>>>>>> aba1b9314c881b372cb8a6d999f4add546d4191c
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc

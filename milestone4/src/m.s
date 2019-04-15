	.data
	fmt_int: .string "%d\n" 
	fmt_char: .string "%c\n" 
	.text
	.global main
	.type main, @function
// gunint:
C_gunint:
	// BeginFunc12
	push %ebp
	mov %esp, %ebp
	sub $12, %esp
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
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@15=0
	mov $0, %eax
	mov %eax , -48(%ebp)
	// returntmp@15
	mov -48(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc

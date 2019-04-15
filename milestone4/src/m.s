	.data
	print_fmt_int: .string "%d\n" 
	print_fmt_char: .string "%c\n" 
	scan_fmt_int: .string "%d" 
	scan_fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// fint:
func0:
	// BeginFunc36
	push %ebp
	mov %esp, %ebp
	sub $36, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@0=2
	mov $2, %eax
	mov %eax , -4(%ebp)
	// tmp@1=n@1<tmp@0
	mov 8(%ebp), %eax
	mov -4(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -8(%ebp)
	// ifztmp@1goto->single_if_after0
	mov -8(%ebp), %eax
	cmp $0 , %eax 
	je single_if_after0
	// returnn@1
	mov 8(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
// single_if_after0:
single_if_after0:
	// tmp@2=1
	mov $1, %eax
	mov %eax , -12(%ebp)
	// tmp@3=n@1-tmp@2
	mov 8(%ebp), %eax
	mov -12(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -16(%ebp)
	// PushParamtmp@3
	mov -16(%ebp), %eax
	push %eax
	// tmp@4=Fcallfint
	call func0
	mov %eax , -20(%ebp)
	// RemoveParams4
	// tmp@5=2
	mov $2, %eax
	mov %eax , -24(%ebp)
	// tmp@6=n@1-tmp@5
	mov 8(%ebp), %eax
	mov -24(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -28(%ebp)
	// PushParamtmp@6
	mov -28(%ebp), %eax
	push %eax
	// tmp@7=Fcallfint
	call func0
	mov %eax , -32(%ebp)
	// RemoveParams4
	// tmp@8=tmp@4+tmp@7
	mov -20(%ebp), %eax
	mov -32(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -36(%ebp)
	// returntmp@8
	mov -36(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
// main:
main:
	// BeginFunc16
	push %ebp
	mov %esp, %ebp
	sub $16, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@9=6
	mov $6, %eax
	mov %eax , -4(%ebp)
	// PushParamtmp@9
	mov -4(%ebp), %eax
	push %eax
	// tmp@10=Fcallfint
	call func0
	mov %eax , -8(%ebp)
	// RemoveParams4
	// g@3=tmp@10
	mov -8(%ebp), %eax
	mov %eax , -12(%ebp)
	// print_intg@3
	mov -12(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@11=0
	mov $0, %eax
	mov %eax , -16(%ebp)
	// returntmp@11
	mov -16(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 

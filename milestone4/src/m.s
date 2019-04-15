	.data
	fmt_int: .string "%d" 
	fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// main:
main:
	// BeginFunc32
	push %ebp
	mov %esp, %ebp
	sub $32, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@0=10
	mov $10, %eax
	mov %eax , -4(%ebp)
	// a@1=tmp@0
	mov -4(%ebp), %eax
	mov %eax , -8(%ebp)
	// tmp@1=17
	mov $17, %eax
	mov %eax , -16(%ebp)
	// tmp@2=a@1<tmp@1
	mov -8(%ebp), %eax
	mov -16(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -20(%ebp)
// ifelse_before0:
ifelse_before0:
	// ifztmp@2goto->ifelse_else_0
	mov -20(%ebp), %eax
	cmp $0 , %eax 
	je ifelse_else_0
	// tmp@3=1
	mov $1, %eax
	mov %eax , -24(%ebp)
	// b@1=tmp@3
	mov -24(%ebp), %eax
	mov %eax , -12(%ebp)
	// goto->ifelse_after0
	jmp ifelse_after0
// ifelse_else_0:
ifelse_else_0:
	// tmp@4=2
	mov $2, %eax
	mov %eax , -28(%ebp)
	// b@1=tmp@4
	mov -28(%ebp), %eax
	mov %eax , -12(%ebp)
// ifelse_after0:
ifelse_after0:
	// print_intb@1
	mov -12(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@5=0
	mov $0, %eax
	mov %eax , -32(%ebp)
	// returntmp@5
	mov -32(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc

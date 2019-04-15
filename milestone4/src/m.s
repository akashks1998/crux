	.data
	print_fmt_int: .string "%d\n" 
	print_fmt_char: .string "%c\n" 
	scan_fmt_int: .string "%d" 
	scan_fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// fintp:
func0:
	// BeginFunc4
	push %ebp
	mov %esp, %ebp
	sub $4, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// scan_inttmp@0
	mov 8(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $scan_fmt_int
	call scanf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@1=0
	mov $0, %eax
	mov %eax , -4(%ebp)
	// returntmp@1
	mov -4(%ebp), %eax
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
	// tmp@2=&g@2
	lea -4(%ebp), %eax
	mov %eax , -8(%ebp)
	// PushParamtmp@2
	mov -8(%ebp), %eax
	push %eax
	// tmp@3=Fcallfintp
	call func0
	mov %eax , -12(%ebp)
	// RemoveParams4
	// print_intg@2
	mov -4(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@4=0
	mov $0, %eax
	mov %eax , -16(%ebp)
	// returntmp@4
	mov -16(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 

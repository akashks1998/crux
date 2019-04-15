	.data
	fmt_int: .string "%d" 
	fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// main:
main:
	// BeginFunc12
	push %ebp
	mov %esp, %ebp
	sub $12, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@0=1256
	mov $1256, %eax
	mov %eax , -4(%ebp)
	// a@1=tmp@0
	mov -4(%ebp), %eax
	mov %eax , -8(%ebp)
	// scan_inta@1
	lea -8(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call scanf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// print_inta@1
	mov -8(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@1=0
	mov $0, %eax
	mov %eax , -12(%ebp)
	// returntmp@1
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

	.data
	print_fmt_int: .string "%d\n" 
	print_fmt_char: .string "%c\n" 
	scan_fmt_int: .string "%d" 
	scan_fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// xintp:
func0:
	// BeginFunc12
	push %ebp
	mov %esp, %ebp
	sub $12, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// z@3=t@3
	mov 8(%ebp), %eax
	mov %eax , -4(%ebp)
	// tmp@1=5
	mov $5, %eax
	mov %eax , -8(%ebp)
	// tmp@0=tmp@1
	mov -8(%ebp), %eax
	mov -4(%ebp), %edi
	mov %eax, (%edi)
	// tmp@2=4
	mov $4, %eax
	mov %eax , -12(%ebp)
	// returntmp@2
	mov -12(%ebp), %eax
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
	// tmp@3=&t@2
	lea -4(%ebp), %eax
	mov %eax , -8(%ebp)
	// PushParamtmp@3
	mov -8(%ebp), %eax
	push %eax
	// tmp@4=Fcallxintp
	call func0
	mov %eax , -12(%ebp)
	// RemoveParams4
	// print_intt@2
	mov -4(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@5=0
	mov $0, %eax
	mov %eax , -16(%ebp)
	// returntmp@5
	mov -16(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 

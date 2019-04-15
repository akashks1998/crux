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
	// BeginFunc8
	push %ebp
	mov %esp, %ebp
	sub $8, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@1=6
	mov $6, %eax
	mov %eax , -4(%ebp)
	// tmp@0=tmp@1
	mov -4(%ebp), %eax
	mov 8(%ebp), %edi
	mov %eax, (%edi)
	// tmp@2=0
	mov $0, %eax
	mov %eax , -8(%ebp)
	// returntmp@2
	mov -8(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
// xint:
func2:
	// BeginFunc4
	push %ebp
	mov %esp, %ebp
	sub $4, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@3=z@3*z@3
	mov 8(%ebp), %eax
	mov 8(%ebp), %ebx
	imul %ebx, %eax
	mov %eax , -4(%ebp)
	// returntmp@3
	mov -4(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
// aint:
func1:
	// BeginFunc4
	push %ebp
	mov %esp, %ebp
	sub $4, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// PushParamb@2
	mov 8(%ebp), %eax
	push %eax
	// tmp@4=Fcallxint
	call func2
	mov %eax , -4(%ebp)
	// RemoveParams4
	// returntmp@4
	mov -4(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
// xintp:
func3:
	// BeginFunc8
	push %ebp
	mov %esp, %ebp
	sub $8, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// z@5=t@5
	mov 8(%ebp), %eax
	mov %eax , -4(%ebp)
	// scan_inttmp@7
	mov -4(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $scan_fmt_int
	call scanf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@8=4
	mov $4, %eax
	mov %eax , -8(%ebp)
	// returntmp@8
	mov -8(%ebp), %eax
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
	// BeginFunc36
	push %ebp
	mov %esp, %ebp
	sub $36, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@5=&z@4
	lea -4(%ebp), %eax
	mov %eax , -12(%ebp)
	// l@4=tmp@5
	mov -12(%ebp), %eax
	mov %eax , -8(%ebp)
	// PushParaml@4
	mov -8(%ebp), %eax
	push %eax
	// tmp@6=Fcallxintp
	call func0
	mov %eax , -16(%ebp)
	// RemoveParams4
	// print_intz@4
	mov -4(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@9=&t@4
	lea -20(%ebp), %eax
	mov %eax , -24(%ebp)
	// PushParamtmp@9
	mov -24(%ebp), %eax
	push %eax
	// tmp@10=Fcallxintp
	call func3
	mov %eax , -28(%ebp)
	// RemoveParams4
	// PushParamt@4
	mov -20(%ebp), %eax
	push %eax
	// tmp@11=Fcallaint
	call func1
	mov %eax , -32(%ebp)
	// RemoveParams4
	// print_inttmp@11
	mov -32(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// print_intt@4
	mov -20(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@12=0
	mov $0, %eax
	mov %eax , -36(%ebp)
	// returntmp@12
	mov -36(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 

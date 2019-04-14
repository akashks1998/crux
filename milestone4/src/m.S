	 .data
	  fmt_int: .string '%d
' 
	  fmt_char: .string '%c
' 
	 .text
	 global main
	 .type main, @function
	 mov $4, %eax
main:
	 push %ebp
	 mov %esp, %ebp
	 sub $12, %esp
	 push %ebx
	 push %ecx
	 push %edx
	 push %esi
	 push %edi
	 mov $10, %eax
	 mov %eax , -4(%ebp)
	 mov -4(%ebp), %eax
	 mov %eax , -8(%ebp)
	 mov -8(%ebp), %eax
	 push %ebp
	 mov %esp,%ebp
	 push %eax
	 push $fmt_int
	 call printf
	 add  $8, %esp
	 mov %ebp, %esp
	 pop %ebp
	 mov $0, %eax
	 mov %eax , -12(%ebp)
	 mov -12(%ebp), %eax
	 pop %ebx
	 pop %ecx
	 pop %edx
	 pop %esi
	 pop %edi
	 mov %ebp, %esp
	 pop %ebp
	 ret 

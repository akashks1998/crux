	 .text
	 .global main
	 .type main, @function
	 mov $4, %eax
aint:
	 push %ebp
	 mov %esp, %ebp
	 sub $4, %esp
	 push %ebx
	 push %ecx
	 push %edx
	 push %esi
	 push %edi
	 mov $0, %eax
	 mov %eax , -4(%ebp)
	 mov -4(%ebp), %eax
	 pop %ebx
	 pop %ecx
	 pop %edx
	 pop %esi
	 pop %edi
	 mov %ebp, %esp
	 pop %ebp
	 ret 
main:
	 push %ebp
	 mov %esp, %ebp
	 sub $20, %esp
	 push %ebx
	 push %ecx
	 push %edx
	 push %esi
	 push %edi
	 mov -4(%ebp), %eax
	 mov (%ebp , %eax, 1), %eax
	 mov %eax , -8(%ebp)
	 mov -8(%ebp), %eax
	 push %eax
	 call aint
	 mov %eax , -12(%ebp)
	 mov -12(%ebp), %eax
	 mov %eax , -16(%ebp)
	 mov $0, %eax
	 mov %eax , -20(%ebp)
	 mov -20(%ebp), %eax
	 pop %ebx
	 pop %ecx
	 pop %edx
	 pop %esi
	 pop %edi
	 mov %ebp, %esp
	 pop %ebp
	 ret 

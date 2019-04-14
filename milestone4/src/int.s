	 .text
	 .global main
	 .type main, @function
main:
	 push %ebp
	 mov %esp, %ebp
	 sub $12, %esp
	 push %ebx
	 push %ecx
	 push %edx
	 push %esi
	 push %edi
	 mov $1256, %eax
	 mov %eax , -4(%ebp)
	 mov -4(%ebp), %eax
	 mov %eax , -8(%ebp)

    push %ebp
    mov %esp,%ebp
    push %eax
    push $form
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

.data
    form: .string "%d\n"

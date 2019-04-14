	 .text
	 .global main
	 .type main, @function
	 mov $4, %eax
main:
	 mov -4(%ebp), %eax
	 mov (%ebp , %eax, 1), %eax
	 mov %eax , -8(%ebp)
	 lea -8(%ebp), %eax
	 mov %eax , -12(%ebp)
	 mov -12(%ebp), %eax
	 mov %eax , -16(%ebp)
	 mov $0, %eax
	 mov %eax , -20(%ebp)

	 .data
	 fmt_int: .string "%d\n" 
	 fmt_char: .string "%c\n" 
	 .text
	 .global main
	 .type main, @function
	 mov $4, %eax
main:
	 push %ebp
	 mov %esp, %ebp
	 sub $88, %esp
	 push %ebx
	 push %ecx
	 push %edx
	 push %esi
	 push %edi
	 mov $10, %eax
	 mov %eax , -4(%ebp)
	 mov -4(%ebp), %eax
	 mov %eax , -8(%ebp)
	 mov $0, %eax
	 mov %eax , -12(%ebp)
	 mov -12(%ebp), %eax
	 mov %eax , -16(%ebp)
for_begin10:
	 mov $5, %eax
	 mov %eax , -20(%ebp)
	 mov -16(%ebp), %eax
	 mov -20(%ebp), %ebx
	 cmp %ebx, %eax
	 mov $0, %ecx
	 setne %cl
	 mov %ecx , -24(%ebp)
	 mov -24(%ebp), %eax
	 cmp $0 , %eax 
	 je for_after10
	 mov -8(%ebp), %eax
	 mov %eax , -32(%ebp)
	 mov -8(%ebp), %eax
	 inc  %eax
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
for_continue10:
	 mov -16(%ebp), %eax
	 mov %eax , -28(%ebp)
	 mov -16(%ebp), %eax
	 inc  %eax
	 mov %eax , -16(%ebp)
	 jmp for_begin10
for_after10:
	 mov $17, %eax
	 mov %eax , -40(%ebp)
	 mov -8(%ebp), %eax
	 mov -40(%ebp), %ebx
	 cmp %ebx, %eax
	 mov $0, %ecx
	 setl %cl
	 mov %ecx , -44(%ebp)
ifelse_before0:
	 mov -44(%ebp), %eax
	 cmp $0 , %eax 
	 je ifelse_else_0
	 mov $1, %eax
	 mov %eax , -48(%ebp)
	 mov -48(%ebp), %eax
	 mov %eax , -36(%ebp)
	 jmp ifelse_after0
ifelse_else_0:
	 mov $2, %eax
	 mov %eax , -52(%ebp)
	 mov -52(%ebp), %eax
	 mov %eax , -36(%ebp)
ifelse_after0:
	 mov -36(%ebp), %eax
	 push %ebp
	 mov %esp,%ebp
	 push %eax
	 push $fmt_int
	 call printf
	 add  $8, %esp
	 mov %ebp, %esp
	 pop %ebp
	 mov $7, %eax
	 mov %eax , -56(%ebp)
	 mov -8(%ebp), %eax
	 mov -56(%ebp), %ebx
	 cmp %ebx, %eax
	 mov $0, %ecx
	 setl %cl
	 mov %ecx , -60(%ebp)
ifelse_before1:
	 mov -60(%ebp), %eax
	 cmp $0 , %eax 
	 je ifelse_else_1
	 mov $2, %eax
	 mov %eax , -64(%ebp)
	 mov -64(%ebp), %eax
	 mov %eax , -36(%ebp)
	 jmp ifelse_after1
ifelse_else_1:
	 mov $1, %eax
	 mov %eax , -68(%ebp)
	 mov -68(%ebp), %eax
	 mov %eax , -36(%ebp)
ifelse_after1:
	 mov -36(%ebp), %eax
	 push %ebp
	 mov %esp,%ebp
	 push %eax
	 push $fmt_int
	 call printf
	 add  $8, %esp
	 mov %ebp, %esp
	 pop %ebp
	 mov $15, %eax
	 mov %eax , -72(%ebp)
	 mov -8(%ebp), %eax
	 mov -72(%ebp), %ebx
	 cmp %ebx, %eax
	 mov $0, %ecx
	 setl %cl
	 mov %ecx , -76(%ebp)
ifelse_before2:
	 mov -76(%ebp), %eax
	 cmp $0 , %eax 
	 je ifelse_else_2
	 mov $2, %eax
	 mov %eax , -80(%ebp)
	 mov -80(%ebp), %eax
	 mov %eax , -36(%ebp)
	 jmp ifelse_after2
ifelse_else_2:
	 mov $1, %eax
	 mov %eax , -84(%ebp)
	 mov -84(%ebp), %eax
	 mov %eax , -36(%ebp)
ifelse_after2:
	 mov -36(%ebp), %eax
	 push %ebp
	 mov %esp,%ebp
	 push %eax
	 push $fmt_int
	 call printf
	 add  $8, %esp
	 mov %ebp, %esp
	 pop %ebp
	 mov $0, %eax
	 mov %eax , -88(%ebp)
	 mov -88(%ebp), %eax
	 pop %ebx
	 pop %ecx
	 pop %edx
	 pop %esi
	 pop %edi
	 mov %ebp, %esp
	 pop %ebp
	 ret 

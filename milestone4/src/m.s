	.data
	print_fmt_int: .string "%d\n" 
	print_fmt_char: .string "%c\n" 
	scan_fmt_int: .string "%d" 
	scan_fmt_char: .string "%c" 
	.text
	.global main
	.type main, @function
// set_charint,char:
func0:
	// BeginFunc80
	push %ebp
	mov %esp, %ebp
	sub $80, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@0=0
	mov $0, %eax
	mov %eax , -4(%ebp)
	// i@3=tmp@0
	mov -4(%ebp), %eax
	mov %eax , -8(%ebp)
// for_begin10:
for_begin10:
	// tmp@1=8
	mov $8, %eax
	mov %eax , -12(%ebp)
	// tmp@2=i@3<tmp@1
	mov -8(%ebp), %eax
	mov -12(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -16(%ebp)
	// ifztmp@2goto->for_after10
	mov -16(%ebp), %eax
	cmp $0 , %eax 
	je for_after10
	// tmp@12=c@2
	mov 12(%ebp), %eax
	mov %eax , -48(%ebp)
	// c@2++
	mov 12(%ebp), %eax
	inc  %eax
	mov %eax , 12(%ebp)
	// +tmp@4this@28
	mov 8(%ebp), %eax
	mov $8 , %ebx
	add %ebx, %eax
	mov %eax , -24(%ebp)
	// tmp@7=0+i@3
	mov $0 , %eax
	mov -8(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -32(%ebp)
	// tmp@6=tmp@7*1
	mov -32(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -28(%ebp)
	// tmp@9=tmp@6*4
	mov -28(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -40(%ebp)
	// tmp@8=tmp@4
	mov -24(%ebp), %eax
	mov %eax , -36(%ebp)
	// tmp@10=tmp@8+tmp@9
	mov -36(%ebp), %eax
	mov -40(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -44(%ebp)
	// tmp@11=tmp@12
	mov -48(%ebp), %eax
	mov -44(%ebp), %edi
	mov %eax, (%edi)
	// tmp@21=d@2
	movb 16(%ebp), %al
	mov %eax , -76(%ebp)
	// d@2++
	movb 16(%ebp), %al
	inc  %eax
	movb %al , 16(%ebp)
	// +tmp@13this@20
	mov 8(%ebp), %eax
	mov $0 , %ebx
	add %ebx, %eax
	mov %eax , -52(%ebp)
	// tmp@16=0+i@3
	mov $0 , %eax
	mov -8(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -60(%ebp)
	// tmp@15=tmp@16*1
	mov -60(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -56(%ebp)
	// tmp@18=tmp@15*1
	mov -56(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -68(%ebp)
	// tmp@17=tmp@13
	mov -52(%ebp), %eax
	mov %eax , -64(%ebp)
	// tmp@19=tmp@17+tmp@18
	mov -64(%ebp), %eax
	mov -68(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -72(%ebp)
	// tmp@20=tmp@21
	mov -76(%ebp), %eax
	mov -72(%ebp), %edi
	movb %al, (%edi)
// for_continue10:
for_continue10:
	// tmp@3=i@3
	mov -8(%ebp), %eax
	mov %eax , -20(%ebp)
	// i@3++
	mov -8(%ebp), %eax
	inc  %eax
	mov %eax , -8(%ebp)
	// goto->for_begin10
	jmp for_begin10
// for_after10:
for_after10:
	// tmp@22=0
	mov $0, %eax
	mov %eax , -80(%ebp)
	// returntmp@22
	mov -80(%ebp), %eax
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
	// BeginFunc137
	push %ebp
	mov %esp, %ebp
	sub $137, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@23=&(H@4)
	lea -52(%ebp), %eax
	mov %eax , -56(%ebp)
	// tmp@24=10
	mov $10, %eax
	mov %eax , -60(%ebp)
	// tmp@25='a'
	mov $97,%eax
	movb %al , -61(%ebp)
	// PushParamtmp@25
	movb -61(%ebp), %al
	push %eax
	// PushParamtmp@24
	mov -60(%ebp), %eax
	push %eax
	// PushParamtmp@23
	mov -56(%ebp), %eax
	push %eax
	// tmp@26=Fcallhi:set_charint,char
	call func0
	mov %eax , -65(%ebp)
	// RemoveParams9
	// tmp@27=0
	mov $0, %eax
	mov %eax , -69(%ebp)
	// i@5=tmp@27
	mov -69(%ebp), %eax
	mov %eax , -73(%ebp)
// for_begin11:
for_begin11:
	// tmp@28=8
	mov $8, %eax
	mov %eax , -77(%ebp)
	// tmp@29=i@5<tmp@28
	mov -73(%ebp), %eax
	mov -77(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -81(%ebp)
	// ifztmp@29goto->for_after11
	mov -81(%ebp), %eax
	cmp $0 , %eax 
	je for_after11
	// -tmp@31528
	mov $52 , %eax
	mov $8 , %ebx
	sub %ebx, %eax
	mov %eax , -89(%ebp)
	// tmp@34=0+i@5
	mov $0 , %eax
	mov -73(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -97(%ebp)
	// tmp@33=tmp@34*1
	mov -97(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -93(%ebp)
	// tmp@36=tmp@33*4
	mov -93(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -105(%ebp)
	// tmp@35=tmp@31
	mov -89(%ebp), %eax
	mov %eax , -101(%ebp)
	// tmp@37=tmp@35-tmp@36
	mov -101(%ebp), %eax
	mov -105(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -109(%ebp)
	// print_inttmp@38
	mov -109(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// -tmp@39520
	mov $52 , %eax
	mov $0 , %ebx
	sub %ebx, %eax
	mov %eax , -113(%ebp)
	// tmp@42=0+i@5
	mov $0 , %eax
	mov -73(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -121(%ebp)
	// tmp@41=tmp@42*1
	mov -121(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -117(%ebp)
	// tmp@44=tmp@41*1
	mov -117(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -129(%ebp)
	// tmp@43=tmp@39
	mov -113(%ebp), %eax
	mov %eax , -125(%ebp)
	// tmp@45=tmp@43-tmp@44
	mov -125(%ebp), %eax
	mov -129(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -133(%ebp)
	// print_chartmp@46
	mov -133(%ebp), %esi
	neg %esi
	movb (%ebp , %esi, 1), %al
	push %ebp
	mov %esp,%ebp
	push %eax
	push $print_fmt_char
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
// for_continue11:
for_continue11:
	// tmp@30=i@5
	mov -73(%ebp), %eax
	mov %eax , -85(%ebp)
	// i@5++
	mov -73(%ebp), %eax
	inc  %eax
	mov %eax , -73(%ebp)
	// goto->for_begin11
	jmp for_begin11
// for_after11:
for_after11:
	// tmp@47=0
	mov $0, %eax
	mov %eax , -137(%ebp)
	// returntmp@47
	mov -137(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 

	.data
	fmt_int: .string "%d\n" 
	fmt_char: .string "%c\n" 
	.text
	.global main
	.type main, @function
// f:
f:
	// BeginFunc4
	push %ebp
	mov %esp, %ebp
	sub $4, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@0=80
	mov $80, %eax
	mov %eax , -4(%ebp)
	// returntmp@0
	mov -4(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc
// fint:
fint:
	// BeginFunc4
	push %ebp
	mov %esp, %ebp
	sub $4, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@1=g@3*g@3
	mov 8(%ebp), %eax
	mov 8(%ebp), %ebx
	imul %ebx, %eax
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
	// EndFunc
// main:
main:
	// BeginFunc680
	push %ebp
	mov %esp, %ebp
	sub $680, %esp
	push %ebx
	push %ecx
	push %edx
	push %esi
	push %edi
	// tmp@2=0
	mov $0, %eax
	mov %eax , -44(%ebp)
	// i@5=tmp@2
	mov -44(%ebp), %eax
	mov %eax , -48(%ebp)
// for_begin10:
for_begin10:
	// tmp@3=10
	mov $10, %eax
	mov %eax , -52(%ebp)
	// tmp@4=i@5<tmp@3
	mov -48(%ebp), %eax
	mov -52(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -56(%ebp)
	// ifztmp@4goto->for_after10
	mov -56(%ebp), %eax
	cmp $0 , %eax 
	je for_after10
	// tmp@12=2
	mov $2, %eax
	mov %eax , -84(%ebp)
	// tmp@13=tmp@12*i@5
	mov -84(%ebp), %eax
	mov -48(%ebp), %ebx
	imul %ebx, %eax
	mov %eax , -88(%ebp)
	// tmp@7=0+i@5
	mov $0 , %eax
	mov -48(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -68(%ebp)
	// tmp@6=tmp@7*1
	mov -68(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -64(%ebp)
	// tmp@9=tmp@6*4
	mov -64(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -76(%ebp)
	// tmp@8=40
	mov $40, %eax
	mov %eax , -72(%ebp)
	// tmp@10=tmp@8-tmp@9
	mov -72(%ebp), %eax
	mov -76(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -80(%ebp)
	// tmp@11=tmp@13
	mov -88(%ebp), %eax
	mov -80(%ebp), %edi
	neg %edi
	mov %eax, (%ebp , %edi, 1)
// for_continue10:
for_continue10:
	// tmp@5=i@5
	mov -48(%ebp), %eax
	mov %eax , -60(%ebp)
	// i@5++
	mov -48(%ebp), %eax
	inc  %eax
	mov %eax , -48(%ebp)
	// goto->for_begin10
	jmp for_begin10
// for_after10:
for_after10:
	// tmp@14=0
	mov $0, %eax
	mov %eax , -92(%ebp)
	// i@6=tmp@14
	mov -92(%ebp), %eax
	mov %eax , -96(%ebp)
// for_begin11:
for_begin11:
	// tmp@15=10
	mov $10, %eax
	mov %eax , -100(%ebp)
	// tmp@16=i@6<tmp@15
	mov -96(%ebp), %eax
	mov -100(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -104(%ebp)
	// ifztmp@16goto->for_after11
	mov -104(%ebp), %eax
	cmp $0 , %eax 
	je for_after11
	// tmp@19=0+i@6
	mov $0 , %eax
	mov -96(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -116(%ebp)
	// tmp@18=tmp@19*1
	mov -116(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -112(%ebp)
	// tmp@21=tmp@18*4
	mov -112(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -124(%ebp)
	// tmp@20=40
	mov $40, %eax
	mov %eax , -120(%ebp)
	// tmp@22=tmp@20-tmp@21
	mov -120(%ebp), %eax
	mov -124(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -128(%ebp)
	// tp@6=tmp@23
	mov -128(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	mov %eax , -132(%ebp)
	// print_inttp@6
	mov -132(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
// for_continue11:
for_continue11:
	// tmp@17=i@6
	mov -96(%ebp), %eax
	mov %eax , -108(%ebp)
	// i@6++
	mov -96(%ebp), %eax
	inc  %eax
	mov %eax , -96(%ebp)
	// goto->for_begin11
	jmp for_begin11
// for_after11:
for_after11:
	// tmp@31=6
	mov $6, %eax
	mov %eax , -160(%ebp)
	// tmp@33=0+tmp@31
	mov $0 , %eax
	mov -160(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -168(%ebp)
	// tmp@32=tmp@33*1
	mov -168(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -164(%ebp)
	// tmp@35=tmp@32*4
	mov -164(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -176(%ebp)
	// tmp@34=40
	mov $40, %eax
	mov %eax , -172(%ebp)
	// tmp@36=tmp@34-tmp@35
	mov -172(%ebp), %eax
	mov -176(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -180(%ebp)
	// tmp@24=5
	mov $5, %eax
	mov %eax , -136(%ebp)
	// tmp@26=0+tmp@24
	mov $0 , %eax
	mov -136(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -144(%ebp)
	// tmp@25=tmp@26*1
	mov -144(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -140(%ebp)
	// tmp@28=tmp@25*4
	mov -140(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -152(%ebp)
	// tmp@27=40
	mov $40, %eax
	mov %eax , -148(%ebp)
	// tmp@29=tmp@27-tmp@28
	mov -148(%ebp), %eax
	mov -152(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -156(%ebp)
	// tmp@30=tmp@37
	mov -180(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	mov -156(%ebp), %edi
	neg %edi
	mov %eax, (%ebp , %edi, 1)
	// tmp@38=5
	mov $5, %eax
	mov %eax , -184(%ebp)
	// tmp@40=0+tmp@38
	mov $0 , %eax
	mov -184(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -192(%ebp)
	// tmp@39=tmp@40*1
	mov -192(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -188(%ebp)
	// tmp@42=tmp@39*4
	mov -188(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -200(%ebp)
	// tmp@41=40
	mov $40, %eax
	mov %eax , -196(%ebp)
	// tmp@43=tmp@41-tmp@42
	mov -196(%ebp), %eax
	mov -200(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -204(%ebp)
	// tp@4=tmp@44
	mov -204(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	mov %eax , -208(%ebp)
	// print_inttp@4
	mov -208(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@58=500
	mov $500, %eax
	mov %eax , -500(%ebp)
	// tmp@45=2
	mov $2, %eax
	mov %eax , -452(%ebp)
	// tmp@47=0+tmp@45
	mov $0 , %eax
	mov -452(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -460(%ebp)
	// tmp@46=tmp@47*6
	mov -460(%ebp), %eax
	mov $6 , %ebx
	imul %ebx, %eax
	mov %eax , -456(%ebp)
	// tmp@48=2
	mov $2, %eax
	mov %eax , -464(%ebp)
	// tmp@50=tmp@46+tmp@48
	mov -456(%ebp), %eax
	mov -464(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -472(%ebp)
	// tmp@49=tmp@50*2
	mov -472(%ebp), %eax
	mov $2 , %ebx
	imul %ebx, %eax
	mov %eax , -468(%ebp)
	// tmp@51=1
	mov $1, %eax
	mov %eax , -476(%ebp)
	// tmp@53=tmp@49+tmp@51
	mov -468(%ebp), %eax
	mov -476(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -484(%ebp)
	// tmp@52=tmp@53*1
	mov -484(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -480(%ebp)
	// tmp@55=tmp@52*4
	mov -480(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -492(%ebp)
	// tmp@54=448
	mov $448, %eax
	mov %eax , -488(%ebp)
	// tmp@56=tmp@54-tmp@55
	mov -488(%ebp), %eax
	mov -492(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -496(%ebp)
	// tmp@57=tmp@58
	mov -500(%ebp), %eax
	mov -496(%ebp), %edi
	neg %edi
	mov %eax, (%ebp , %edi, 1)
	// tmp@59=2
	mov $2, %eax
	mov %eax , -504(%ebp)
	// tmp@61=0+tmp@59
	mov $0 , %eax
	mov -504(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -512(%ebp)
	// tmp@60=tmp@61*6
	mov -512(%ebp), %eax
	mov $6 , %ebx
	imul %ebx, %eax
	mov %eax , -508(%ebp)
	// tmp@62=2
	mov $2, %eax
	mov %eax , -516(%ebp)
	// tmp@64=tmp@60+tmp@62
	mov -508(%ebp), %eax
	mov -516(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -524(%ebp)
	// tmp@63=tmp@64*2
	mov -524(%ebp), %eax
	mov $2 , %ebx
	imul %ebx, %eax
	mov %eax , -520(%ebp)
	// tmp@65=1
	mov $1, %eax
	mov %eax , -528(%ebp)
	// tmp@67=tmp@63+tmp@65
	mov -520(%ebp), %eax
	mov -528(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -536(%ebp)
	// tmp@66=tmp@67*1
	mov -536(%ebp), %eax
	mov $1 , %ebx
	imul %ebx, %eax
	mov %eax , -532(%ebp)
	// tmp@69=tmp@66*4
	mov -532(%ebp), %eax
	mov $4 , %ebx
	imul %ebx, %eax
	mov %eax , -544(%ebp)
	// tmp@68=448
	mov $448, %eax
	mov %eax , -540(%ebp)
	// tmp@70=tmp@68-tmp@69
	mov -540(%ebp), %eax
	mov -544(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -548(%ebp)
	// print_inttmp@71
	mov -548(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@74=7
	mov $7, %eax
	mov %eax , -560(%ebp)
	// tmp@72=552+4
	mov $552 , %eax
	mov $4 , %ebx
	add %ebx, %eax
	mov %eax , -556(%ebp)
	// tmp@73=tmp@74
	mov -560(%ebp), %eax
	mov -556(%ebp), %edi
	neg %edi
	mov %eax, (%ebp , %edi, 1)
	// tmp@75=552+4
	mov $552 , %eax
	mov $4 , %ebx
	add %ebx, %eax
	mov %eax , -564(%ebp)
	// print_inttmp@76
	mov -564(%ebp), %esi
	neg %esi
	mov (%ebp , %esi, 1), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@77=2
	mov $2, %eax
	mov %eax , -568(%ebp)
	// z@4=tmp@77
	mov -568(%ebp), %eax
	mov %eax , -576(%ebp)
// switch_test0:
switch_test0:
	// tmp@82=1
	mov $1, %eax
	mov %eax , -596(%ebp)
	// tmp@83=z@4-tmp@82
	mov -576(%ebp), %eax
	mov -596(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -600(%ebp)
	// ifztmp@83goto->label0
	mov -600(%ebp), %eax
	cmp $0 , %eax 
	je label0
	// tmp@84=2
	mov $2, %eax
	mov %eax , -604(%ebp)
	// tmp@85=z@4-tmp@84
	mov -576(%ebp), %eax
	mov -604(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -608(%ebp)
	// ifztmp@85goto->label1
	mov -608(%ebp), %eax
	cmp $0 , %eax 
	je label1
	// tmp@86=3
	mov $3, %eax
	mov %eax , -612(%ebp)
	// tmp@87=z@4-tmp@86
	mov -576(%ebp), %eax
	mov -612(%ebp), %ebx
	sub %ebx, %eax
	mov %eax , -616(%ebp)
	// ifztmp@87goto->label2
	mov -616(%ebp), %eax
	cmp $0 , %eax 
	je label2
	// goto->label3
	jmp label3
// switch_body0:
switch_body0:
// label0:
label0:
	// tmp@78=2
	mov $2, %eax
	mov %eax , -580(%ebp)
	// print_inttmp@78
	mov -580(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
// label1:
label1:
	// tmp@79=4
	mov $4, %eax
	mov %eax , -584(%ebp)
	// print_inttmp@79
	mov -584(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
// label2:
label2:
	// tmp@80=6
	mov $6, %eax
	mov %eax , -588(%ebp)
	// print_inttmp@80
	mov -588(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// goto->switch_end0
	jmp switch_end0
// label3:
label3:
	// tmp@81=32
	mov $32, %eax
	mov %eax , -592(%ebp)
	// print_inttmp@81
	mov -592(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
// switch_end0:
switch_end0:
	// tmp@88=5
	mov $5, %eax
	mov %eax , -620(%ebp)
	// i@4=tmp@88
	mov -620(%ebp), %eax
	mov %eax , -624(%ebp)
// while_begin0:
while_begin0:
	// tmp@89=10
	mov $10, %eax
	mov %eax , -628(%ebp)
	// tmp@90=i@4<tmp@89
	mov -624(%ebp), %eax
	mov -628(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -632(%ebp)
	// ifztmp@90goto->while_after0
	mov -632(%ebp), %eax
	cmp $0 , %eax 
	je while_after0
	// tmp@91=8
	mov $8, %eax
	mov %eax , -636(%ebp)
	// tmp@92=i@4<tmp@91
	mov -624(%ebp), %eax
	mov -636(%ebp), %ebx
	cmp %ebx, %eax
	mov $0, %ecx
	setl %cl
	mov %ecx , -640(%ebp)
	// ifztmp@92goto->single_if_after0
	mov -640(%ebp), %eax
	cmp $0 , %eax 
	je single_if_after0
	// tmp@93=1
	mov $1, %eax
	mov %eax , -644(%ebp)
	// tmp@94=i@4+tmp@93
	mov -624(%ebp), %eax
	mov -644(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -648(%ebp)
	// i@4=tmp@94
	mov -648(%ebp), %eax
	mov %eax , -624(%ebp)
	// goto->while_begin0
	jmp while_begin0
// single_if_after0:
single_if_after0:
	// print_inti@4
	mov -624(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@95=1
	mov $1, %eax
	mov %eax , -652(%ebp)
	// tmp@96=i@4+tmp@95
	mov -624(%ebp), %eax
	mov -652(%ebp), %ebx
	add %ebx, %eax
	mov %eax , -656(%ebp)
	// i@4=tmp@96
	mov -656(%ebp), %eax
	mov %eax , -624(%ebp)
	// goto->while_begin0
	jmp while_begin0
// while_after0:
while_after0:
	// tmp@97=34
	mov $34, %eax
	mov %eax , -664(%ebp)
	// u@4=tmp@97
	mov -664(%ebp), %eax
	mov %eax , -668(%ebp)
	// tmp@98=&u@4
	lea -668(%ebp), %eax
	mov %eax , -672(%ebp)
	// p@4=tmp@98
	mov -672(%ebp), %eax
	mov %eax , -660(%ebp)
	// print_inttmp@99
	mov -660(%ebp), %esi
	mov (%esi), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@101=50
	mov $50, %eax
	mov %eax , -676(%ebp)
	// tmp@100=tmp@101
	mov -676(%ebp), %eax
	mov -660(%ebp), %edi
	mov %eax, (%edi)
	// print_intu@4
	mov -668(%ebp), %eax
	push %ebp
	mov %esp,%ebp
	push %eax
	push $fmt_int
	call printf
	add  $8, %esp
	mov %ebp, %esp
	pop %ebp
	// tmp@102=0
	mov $0, %eax
	mov %eax , -680(%ebp)
	// returntmp@102
	mov -680(%ebp), %eax
	pop %ebx
	pop %ecx
	pop %edx
	pop %esi
	pop %edi
	mov %ebp, %esp
	pop %ebp
	ret 
	// EndFunc

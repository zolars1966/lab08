	.build_version macos, 27, 2	sdk_version 27, 2
	.section	__TEXT,__text,regular,pure_instructions
	.globl	__Z8classifyi                   ; -- Begin function _Z8classifyi
	.p2align	2
__Z8classifyi:                          ; @_Z8classifyi
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	w0, [sp, #8]
	ldr	w8, [sp, #8]
	subs	w8, w8, #0
	b.le	LBB0_2
	b	LBB0_1
LBB0_1:
	mov	w8, #1                          ; =0x1
	str	w8, [sp, #12]
	b	LBB0_3
LBB0_2:
	mov	w8, #-1                         ; =0xffffffff
	str	w8, [sp, #12]
	b	LBB0_3
LBB0_3:
	ldr	w0, [sp, #12]
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols

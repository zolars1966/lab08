	.build_version macos, 27, 2	sdk_version 27, 2
	.section	__TEXT,__text,regular,pure_instructions
	.globl	__Z7abs_vali                    ; -- Begin function _Z7abs_vali
	.p2align	2
__Z7abs_vali:                           ; @_Z7abs_vali
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	w0, [sp, #12]
	ldr	w8, [sp, #12]
	str	w8, [sp, #8]
	ldr	w8, [sp, #12]
	tbz	w8, #31, LBB0_2
	b	LBB0_1
LBB0_1:
	ldr	w9, [sp, #12]
	mov	w8, #0                          ; =0x0
	subs	w8, w8, w9
	str	w8, [sp, #8]
	b	LBB0_2
LBB0_2:
	ldr	w0, [sp, #8]
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols

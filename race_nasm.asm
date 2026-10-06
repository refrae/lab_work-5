default rel

section .data
    global shared_counter
    shared_counter dq 0

section .text
    global thread_function

thread_function:
    mov rcx, 10000000
.loop:
    lock inc qword [shared_counter]
    loop .loop

    xor rax, rax
    ret

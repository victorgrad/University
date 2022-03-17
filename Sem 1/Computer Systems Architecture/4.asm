bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 27
    b db 14
    c db 32
    d dw 41
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AX, [d]
        mov BL, 2
        div BL ;AL=d/2
        mov BL, [c]
        add BL, [b]
        mul BL ;AX=(d/2)*(c+b)
        mov BX, AX ;BX=(d/2)*(c+b)
        mov Al, [a]
        mul byte [a] ; AX=a*a
        sub BX, AX ;BX=(d/2)*(c+b)-a*a
        mov AX, BX
        div byte [b] ; AL=[(d/2)*(c+b)-a*a]/b
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

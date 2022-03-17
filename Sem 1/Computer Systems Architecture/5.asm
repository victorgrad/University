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
    a db 15
    b db 65
    e dw 342
    f dw 152
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov BX, [e]
        add BX, [f] ; bx=(e+f)
        mov al, [a]
        mov cl, 2
        mul cl
        mov cx, ax ; cx=2*a
        
        mov al, [b]
        mov dl, 3
        mul dl ; ax= 3*b
        add AX, CX ; AX=(2*a+3*b)=8
        mul BX
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

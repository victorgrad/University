bits 32

; informam asamblorul ca dorim ca functia _hexa sa fie disponibila altor unitati de compilare
global _hexa

extern _printf

; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32
	format db "%xh ", 0
; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32


_hexa:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
	pushad
    
	mov eax, [ebp + 8] ;eax primeste nr in baza 10
	push eax
	push dword format  ;afisam folosind %x din limbajul de asamblare
	call _printf
	add esp, 4*2
	
	popad
    mov esp, ebp
    pop ebp

    ret
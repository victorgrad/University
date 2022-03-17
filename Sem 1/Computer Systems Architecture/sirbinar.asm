bits 32

; informam asamblorul ca dorim ca functia _binar sa fie disponibila altor unitati de compilare
global _binar

; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32

; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32


_binar:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
	pushad
    
    mov eax, [ebp+8]  ; eax<-nr in baza 10 (x)
	cld
	mov edi, [ebp+12] ;in edi punem adresa vectorului pentru a putea pune numerele
	conversie:
		cdq			 ;eax devine edx:eax pentru impartire
		mov ecx, 2
		idiv ecx     ;eax<- x/2       edx<- x%2
		mov ebx, eax
		mov eax, edx ;in eax punem restul impartirii (care se afla in edx) pentru al putea pune in vector 
		stosd        ;punem in vector doubleword-ul din eax, deoarece numere dintr-un vector din c de tip int sunt pe 32 biti
		mov eax, ebx ;punem inapoi catul impartirii pentru a putea face impartirile repetate
		
		cmp eax,0    ;daca eax e 0, nu mai avem ce imparti si sarim la final
		je fin
	jmp conversie
		
	fin:
	mov eax,2 
	stosd            ;punem un 2 la finalul vectorului pentru a ne putea da seama cand se termina vectorul
	
	popad
    mov esp, ebp
    pop ebp

    ret
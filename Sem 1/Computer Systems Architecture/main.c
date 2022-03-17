//4. Se da un sir de numere. Sa se afiseze valorile in baza 16 si in baza 2.
#include <stdio.h>

int hexa(int a);
int binar(int b,int v[]);

int main()
{
    // declaram variabilele
    int sir[101] = {10,20,30,2,4,6,8,543};
	int l=8;
	
	printf("Sir in baza 16 : ");
	for(int i=0;i<l;i++)
	{
		hexa(sir[i]);
	}
	
	printf("\n");
	printf("Sir in baza 2 : ");
	
	for(int i=0;i<l;i++)
	{
		int v[101];
		binar(sir[i],v);
		int j=0;  //vectorul returnat va avea numarul in baza 2 inversat si un 2 la final care marcheaza sfarsitul ex: 00012
		while(v[j]!=2)
			j++;
		j--; //in j va fi pozitia ultimei cifre a nr in baza 2, de la ex anterior j va fi 3
		for (j;j>=0;j--)
			printf("%d", v[j]); // afisam invers cifrele numarului, de la ex anterior se va afisa 1000b
		printf("b ");
	}
 
    return 0;
}
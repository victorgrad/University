#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int x,y;
}nod;

void dfs(char lab[][1001], nod curent, nod finish, int* drf) {
	lab[curent.y][curent.x] = 2; //il marcam ca vizitat
	if (curent.x == finish.x && curent.y == finish.y) {
		*drf = 1;
	}
	//cumva sa marcam drumul cu 3;

	//daca nu face parte din drumul final ii parcurgem vecinii
	if (*drf != 1) {
		int vx[4] = { 0, -1, 0, 1 }, vy[4] = { 1, 0, -1, 0 }, i;
		for (i = 0; i < 4; i++) {
			if(curent.y + vy[i]>=0 || curent.x + vx[i]>=0){
				if (lab[curent.y + vy[i]][curent.x + vx[i]] == ' ') {
					nod vecin=malloc(sizeof(nod));
					vecin.x = curent.x + vx[i];
					vecin.y = curent.y + vy[i];
					dfs(lab, vecin, finish, drf);
				}
			}
		}
	}
	else{
		lab[curent.y][curent.x] = 3;
	}
}

int main() {
	int i=0, j=0,m,n,drf=0;
	FILE* f;
	nod start, finish;
	char lab[1001][1001],line[1001]=" ";
	f = fopen("labirint_1.txt", "r");
	if (f == NULL)
		return 0;

	while (fgets(lab[i], 1000, f)) {
		i++;
	};

	m = strlen(lab[0])-2;
	n = --i;
	for(i=0;i<=n;i++)
		for (j = 0; j <= m; j++)
		{
			if (lab[i][j] == 'S') {
				start.x = j;
				start.y = i;
			}
			if (lab[i][j] == 'F') {
				finish.x = j;
				finish.y = i;
			}
		}


	dfs(lab, start, finish, &drf);

	for (i = 0; i <= n; i++)
		printf("%s\n", lab[i]);

}
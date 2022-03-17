#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;


typedef struct {
	int id;
	int p;
	int d;
}nod;

typedef struct {
	int a;
	int b;
	int flux;
}arc;

typedef struct {
	arc* arce;
	nod* noduri;
	int nr_arce;
	int nr_noduri;
}graf;

bool bfs(graf rG, int s, int t, int parinti[]) {
	int* viz = new int[rG.nr_arce + 1];


}

int ford_fulkerson(graf G, int s, int t) {

}

int main(int argc, char* argv[]) {
	ifstream in("in.txt");
	//ifstream in(argv[1]);

	//ofstream out(argv[2]);
	int V, E;
	graf* G = new graf;
	in >> V >> E;
	G->arce = new arc[E + 1];
	G->noduri = new nod[V + 1];
	G->nr_arce = E;
	G->nr_noduri = V;
	for (int i = 0; i < E; i++) {
		int a, b, c;
		in >> a >> b >> c;
		arc arcu;
		arcu.a = a;
		arcu.b = b;
		arcu.flux = c;
		G->arce[i] = arcu;
	}
	in.close();
	delete G;
	return 0;

}
#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <stdio.h>

const int n = 101;
const int INF = 1000000;


bool BFS(std::vector<int> vecini[], int** rflux, int sursa, int dest, int* tati, int N);
int ford_fulk(std::vector<int> vecini[], int** capacitate, int** rflux, int sursa, int dest, int N);

int main(int argc, char** argv)
{
    std::ifstream in(argv[1]);
    std::ofstream out(argv[2]);
    int N, C, D, flux_max = 0;
    int sursa, dest;
    in >> N >> C >> D;
    std::vector<int> *vecini=new std::vector<int>[D+1];
    int** capacitate = new int* [N + 1];
    int** rflux = new int* [N + 1];
    for (int i = 0; i < N + 1; ++i) {
        capacitate[i] = new int[N + 1];
        rflux[i] = new int[N + 1];
    }
    int a, b, c;
    for (int i = 0; i < D; i++) {
        in >> a >> b >> c;
        vecini[a].push_back(b);
        //vecini[b].push_back(a); drumurile au sens unic
        capacitate[a][b] = c;
        //setam fluxul rezidual ca fiind capacitatea
        rflux[a][b] = c;
    }
    //setam sursa
    sursa = N;
    //setam destinatia
    dest = N - 1;
    //setam capacitate infinita intre sursa imaginara si camine
    for (int i = 0; i < C; i++) {
        //setam vecinii sursei(caminele)
        vecini[sursa].push_back(i);
        capacitate[sursa][i] = INF;
        rflux[sursa][i] = INF;
    }
    flux_max = ford_fulk(vecini, capacitate, rflux, sursa, dest, N);
    out<<flux_max<<'\n';
    for (int i = 0; i < C; i++) {
        int suma = 0;
        for (int vecin : vecini[i]) {
            suma+= capacitate[i][vecin] - rflux[i][vecin];
        }
        out << suma << ' ';
    }
    for (int i = 0; i < N + 1; ++i) {
        delete[] capacitate[i];
        delete[] rflux[i];
    }
    delete[] vecini;
    delete[] capacitate;
    delete[] rflux;
}

int ford_fulk(std::vector<int> vecini[], int** capacitate, int** rflux, int sursa, int dest,int N) {
    //O(V*E^2);
    //ford fulkerson imbunatatit (Edmonds Karp)
    int* tati=new int[N+1];
    int flow_max = 0;

    while (BFS(vecini, rflux, sursa, dest, tati, N)) {
        int flow = INF;
        //parcurgem vectorul de tati pentru a gasi flow-ul minim
        for (int sf = dest; sf != sursa; sf = tati[sf]) {
            int tata = tati[sf];
            flow = std::min(flow, rflux[tata][sf]);
        }
        //scadem fluxul-ul din graful rezidual
        for (int sf = dest; sf != sursa; sf = tati[sf]) {
            int tata = tati[sf];
            rflux[tata][sf] -= flow;
            //rflux[sf][tata] += flow;
        }
        flow_max += flow;
    }
    delete[] tati;
    return flow_max;
}


bool BFS(std::vector<int> vecini[],int** rflux,int sursa,int dest,int* tati,int N) {
    //O(V+E)
    bool* vizitati = new bool[N+1];
    for (int i = 0; i < N; i++) {
        tati[i] = 0;
        vizitati[i] = false;
    }
    std::queue<int> coada;
    tati[sursa] = -1;
    vizitati[sursa] = true;
    coada.push(sursa);
    while (!coada.empty()) {
        int nod = coada.front();
        coada.pop();
        for (int vecin : vecini[nod]) {
            //daca nu e vizitat si daca arcul nu e saturat
            if (vizitati[vecin]==false && rflux[nod][vecin]>0) {
                //daca am ajuns la destinatie
                if (vecin == dest) {
                    tati[vecin] = nod;
                    delete[] vizitati;
                    return true;
                }
                tati[vecin] = nod;
                coada.push(vecin);
                vizitati[vecin] = true;
            }
        }
    }
    delete[] vizitati;
    //daca nu am mai gasit un drum de la sursa la dest
    return false;
}



// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

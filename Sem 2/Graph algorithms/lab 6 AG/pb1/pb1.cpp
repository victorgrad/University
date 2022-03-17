#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <stdio.h>
using namespace std;

int coloreaza(vector<int>* vec, int N,int* rez, int inc);

int main(int argc,char** argv)
{
    std::ifstream in(argv[1]);
    std::ofstream out(argv[2]);
    int N, M,minculori;
    in >> N >> M;
    minculori = N;
    int** graf = new int* [N + 1];
    int* rezf = new int[N + 1];
    int* reztmp= new int[N + 1];
    for (int i = 0; i < N + 1; ++i) {
        graf[i] = new int[N + 1];
    }

    vector<int>* vec = new vector<int>[N+1];

    for (int i = 0; i < M; i++) {
        int a, b;
        in >> a >> b;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    /*
    for (int i = 0; i < N; i++) {
        int nrculori = coloreaza(vec, N, reztmp, i);
        if (nrculori < minculori) {
            minculori = nrculori;
            for (int j = 0; j < N; j++) {
                rezf[j] = reztmp[j];
                reztmp[j] = -2;
            }
        }
    }
    */
    ///*
    int nrculori = coloreaza(vec, N, reztmp, 0);
    if (nrculori < minculori) {
        minculori = nrculori;
        for (int j = 0; j < N; j++) {
            rezf[j] = reztmp[j];
            reztmp[j] = -2;
        }
    }
    //*/
    out << minculori << '\n';
    for (int i = 0; i < N; i++) {
        out << rezf[i] << ' ';
    }

    for (int i = 0; i < N + 1; ++i) {
        delete[] graf[i];
    }
    delete[] graf;
    delete[] rezf;
    delete[] reztmp;

}

int coloreaza(vector<int>* vec, int N, int* rez,int inc) {
    //O(V^2+E)
    //coloram primul nod
    int culoaremax = 0;
    int nrculori = 1;
    rez[inc] = 0;
    for (int i = 0; i < N; i++) {
        //celelalte noduri sunt necolorate
        if(rez[i]!=0)
            rez[i] = -1;
    }
    //priority queue nu merge deoarece eu trebuie sa sustrag elemente specifice cand parcurg vecinii unui nod pentru a marca culorile lor ca fiind folosite
    bool* disponibil = new bool[N];
    for (int i = 0; i < N; i++) { //marcam toate culorile ca fiind utilizabile pentru a le marca dupa doar pe acelea indisponibile
        disponibil[i] = true;
    }
    for (int nod = 0; nod < N; nod++) {//gasim culorile pentru toate celelalte noduri
        if (nod != inc) {
            for (int vecin : vec[nod]) {//parcurgem vecinii nodului nod
                if (rez[vecin] != -1)//daca are o culoare
                    disponibil[rez[vecin]] = false;
            }
            int culoare;
            for (culoare = 0; culoare < N; culoare++) {
                if (disponibil[culoare])
                    break;
            }

            if (culoare > culoaremax) {//daca culoarea gasita e mai mare decat culoarea maxima folosita de pana acum o contorizam
                nrculori++;
                culoaremax = culoare;
            }
            rez[nod] = culoare;

            for (int vecin : vec[nod]) {//resetam valorile disponibilitatii nodurilor pentru urmatoarea parcurgere
                if (rez[vecin] != -1)
                    disponibil[rez[vecin]] = true;
            }
        }
    }
    delete[] disponibil;
    return nrculori;
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

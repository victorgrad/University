#include <iostream>
#include <fstream>
using namespace std;

ifstream in("input.txt");

void afisare(int mat[][101], int n)
{
    int i, j;
    for (i = 1; i <= n; i++)
    {

        for (j = 1; j <= n; j++)
        {
            cout << mat[i][j] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

void dfs(int nod, int mat_ad[][101],int viz[], int n)
{
    int i;
    viz[nod] = 1;
    for (i = 1; i <= n; i++)
        if (mat_ad[nod][i] == 1 and viz[i] == 0)
            dfs(i, mat_ad, viz, n);
}

int conex(int viz[], int n)
{
    int i;
    for (i = 1; i <= n; i++)
        if (viz[i] == 0)
            return 0;
    return 1;
}

int main()
{
    int mat_ad[101][101], i, j, n, a, b, mat_dis[101][101];
    in >> n;
    for (i = 0; i <= 100; i++)
        for (j = 0; j <= 100; j++)
        {
            mat_ad[i][j] = 0;
            mat_dis[i][j] = 0;
        }
    // din fisier in matrice de adiacenta
    while(in >>a)
    {

        in >>b;
        mat_ad[a][b] = 1;
        mat_ad[b][a] = 1;
        mat_dis[a][b] = 1;
        mat_dis[b][a] = 1;
    }

    //noduri izolate
    cout << "Nodurile izolate sunt: ";
    for (i = 1; i <= n; i++)
    {
        int ok = 1;
        for (j = 1; j <= n; j++)
        {
            if (mat_ad[i][j] == 1)
                ok = 0;
        }
        if (ok)
            cout << i << ' ';
    }
    cout << endl;

    //graf regular
    int ok = 1;
    int nr_n_1stline = 0;
    for (i = 1; i <= n; i++)
        if (mat_ad[i][1] == 1)
            nr_n_1stline++;
    for (i = 2; i <= n; i++)
    {
        int nr_n = 0;
        for (j = 1; j <= n; j++)
        {
            if (mat_ad[i][j] == 1)
                nr_n++;
        }
        if (nr_n != nr_n_1stline)
            ok = 0;
    }
    if (ok)
        cout << "Graful este regular\n";
    else
        cout << "Graful nu este regular\n";

    //matricea distantelor
    int k;
    for (i = 0; i <= 100; i++)
        for (j = 0; j <= 100; j++)
            if (mat_dis[i][j] == 0 && i!=j)
                mat_dis[i][j] = 101;

    for (k = 1; k <= n; k++)
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                if (mat_dis[i][j] > mat_dis[i][k] + mat_dis[k][j])
                    mat_dis[i][j] = mat_dis[i][k] + mat_dis[k][j];

    //graf conex
    int viz[101];
    for (i = 0; i < 101; i++)
        viz[i] = 0;
    dfs(1, mat_ad, viz, n);
    if (conex(viz, n))
        cout << "Graful este conex" << endl;
    else
        cout << "Graful nu este conex" << endl;
    cout << endl;

    //afisare
    cout << "Matricea de adiacenta:" << endl;
    afisare(mat_ad, n);
    cout<< "Matricea de distante:" << endl;
    cout << "(101 inseamna distanta infinita,adica nu exista un drum)" << endl;
    afisare(mat_dis, n);

    return 0;
}
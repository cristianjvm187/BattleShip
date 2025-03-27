#include <bits/stdc++.h>

using namespace std;

// Parametros constantes
const int gz = 50; // alto del tablero cuadrado
const int K = 4; // Cantidad de tipos de barcos
vector<int> b = {25, 50, 25, 25}; // Cantidad de barcos de cada tipo
vector<int> dim = {2, 3, 4, 5}; // Dimensiones de cada tipo en orden


//Para caso prueba de github
//const int K = 3; // Cantidad de tipos de barcos
//vector<int> b = {2, 3, 1}; // Cantidad de barcos de cada tipo


// player1() function
void Atk() {
    for (int i = 0; i < gz; ++i) {
        for (int j = 0; j < gz; ++j) {
            cout << i << " " << j << endl;
            cout.flush();

            int result;
            cin >> result;
            if (result == -1) {
                return;
            }
        }
    }
    return;
}

int main() {

    // Recogida de las partidas anteriores
    int N; // Cantidad de partidas anteriores
    cin >> N;

    vector<vector<vector<string>>> inp_def(N, vector<vector<string>>(K));
    vector<vector<int>> inp_atk(N);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < K; ++j) {
            inp_def[i][j].resize(b[j] * 3); // Allocate space for the expected input
            for (int k = 0; k < b[j]; ++k) {
                cin >> inp_def[i][j][k * 3] >> inp_def[i][j][k * 3 + 1] >> inp_def[i][j][k * 3 + 2];
            }
        }
    }

    for(int i = 0; i < N; ++i){
        // Read the number of attacks
        int A;
        cin >> A;

        inp_atk[i].resize(A * 2);
        for (int a = 0; a < A; ++a) {
            cin >> inp_atk[i][a * 2] >> inp_atk[i][a * 2 + 1];
        }
    }

    Atk();


    return 0;
}

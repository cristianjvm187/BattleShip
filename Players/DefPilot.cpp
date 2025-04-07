#include<bits/stdc++.h>
using namespace std;

// Parametros constantes
const int gz = 50; // alto del tablero cuadrado
const int K = 4; // Cantidad de tipos de barcos
vector<int> b = {25, 50, 25, 25}; // Cantidad de barcos de cada tipo
vector<int> dim = {2, 3, 4, 5}; // Dimensiones de cada tipo en orden

//Estas dimensiones del juego clasico del 10x10 son util para la posicion defensiva que damos como ejemplo
const int gr=5;
vector<int> bc = {1, 2, 1, 1}; // Cantidad de barcos de cada tipo(clasicas)

//Para caso prueba de github
//const int K = 3; // Cantidad de tipos de barcos
//vector<int> b = {2, 3, 1}; // Cantidad de barcos de cada tipo


// player1() function
void Def() {
    int aux=0;
    for(int i=0; i<K ; i++){
        string output="";
        for(int j=0; j<bc[i]; j++){
            for(int r=0; r<gr; r++){
                for(int c=0; c<gr; c++){
                    output+=(to_string(j * dim[i] + j + 10 * r) +" " +to_string(aux+10*c) +" V " );
                }
            }
        }
        aux++;
        cout<<output<<endl;
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

    Def();

    return 0;
}

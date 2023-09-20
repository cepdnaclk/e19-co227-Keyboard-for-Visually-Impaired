#include <iostream>
#include <unordered_map>
#include <map>
#include <list>
#include <string>
#include <cmath>
#include <array>

using namespace std;
map<int, int> mapdecoder; 

void addNewCharacterToMap(int code, char c){
    mapdecoder[code] = c-'a';

}
int encodeButtons(int arr[], int size){
    int code = 0;
    for (int i=0; i<size; i++){
        code += (1<<i)*arr[i];

    }
    return code;
}
void addNewCharacter(int arr[], char c){
    int code = encodeButtons(arr, 6);
    addNewCharacterToMap(code, c);
}
char getCharacter(int code){
    char c = mapdecoder[code] + 'a';
    return c;
}

map<char, array<int, 6>> keyPatterns;
int main()
{

    cout << "hello" << endl;
    return 0;
}
   
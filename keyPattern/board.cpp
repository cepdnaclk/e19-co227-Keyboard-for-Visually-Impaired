#include <iostream>

using namespace std;

int encodeButtons(int arr[], int size){
    int code = 0;
    for (int i=0; i<size; i++){
        code += (1<<i)*arr[i];

    }
    return code;
}
int main() {
    int buttonState[9];
    buttonState[0] = 1;
    buttonState[1] = 0;
    buttonState[2] = 0;
    buttonState[3] = 0;
    buttonState[4] = 0;
    buttonState[5] = 0;
    buttonState[6] = 0;
    buttonState[7] = 0;
    buttonState[8] = 0;
    
    
    int code = encodeButtons(buttonState, 9);
    cout << code << endl; 
    return 0;

    

}
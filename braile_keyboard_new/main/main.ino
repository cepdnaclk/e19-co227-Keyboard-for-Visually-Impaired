const int buttonPins[] = {2, 3, 4, 5, 6, 10, 11, 12, 13};
const int numButtons = sizeof(buttonPins) / sizeof(buttonPins[0]);    // the total size of the array divided by the size of a single element gives you the number of elements in the array.
int pressedKeys[3];                // declare an integer array pressedKeys with a size of 3 to store the currently pressed button values.
int numPressedKeys = 0; 

int sequences[37][9] = {
  {2, 3, 4}, {2, 3, 5}, {2, 3, 10}, {2, 3, 11}, {2, 3, 12}, {2, 3, 13},
  {2, 4, 5}, {2, 4, 10}, {2, 4, 11}, {2, 4, 12}, {2, 4, 13},
  {2, 5, 10}, {2, 5, 11}, {2, 5, 12}, {2, 5, 13},
  {2, 10, 11}, {2, 10, 12}, {2, 10, 13},
  {3, 4, 5}, {3, 4, 10}, {3, 4, 11}, {3, 4, 12}, {3, 4, 13},
  {3, 5, 10}, {3, 5, 11}, {3, 5, 12}, {3, 5, 13},
  {3, 10, 11}, {3, 10, 12}, {3, 10, 13},
  {4, 5, 10}, {4, 5, 11}, {4, 5, 12}, {4, 5, 13},
  {4, 10, 11}, {4, 10, 12}, {6}
};

const char* characters[37] = { 
  "A", "B", "C", "D", "E", "F", "G", "H", "I",
  "J", "K", "L", "M", "N", "O", "P", "Q", "R",
  "S", "T", "U", "V", "W", "X", "Y", "Z",
  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "
};

//used to compare the currently pressed keys to predefined sequences.
void checkPressedKeys() {

  for (int i = 0; i < 37; i++) {
    bool match = true;
    for (int j = 0; j < 3; j++) {
      if (pressedKeys[j] != sequences[i][j]) {  //currently pressed button at position j) is not equal to the value in the sequences array at position [i][j]. If there is a mismatch between the pressed key and the predefined sequence, match is set to false, and the loop breaks.
        match = false;                          //If there is a mismatch between the pressed key and the predefined sequence, match is set to false, and the loop breaks.
        break;
      }
    }
    if (match) {
      Serial.print("Matched Sequence ");
      Serial.print(i + 1);                    // displays the sequence number (i + 1, because array indices are zero-based)
      Serial.print(" => Character: ");
      Serial.println(characters[i]);

      for (int j = 0; j < 3; j++) {            //resets the pressedKeys array by setting all its elements to 0. This ensures that the code is ready to capture a new button sequence.
        pressedKeys[j] = 0;
      }
      numPressedKeys = 0;
      return;
    }
  }
}




void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 36; i++) {
    Serial.print("Sequence ");
    Serial.print(i + 1);
    Serial.print(": ");
    
    for (int j = 0; j < 3; j++) { 
      Serial.print(sequences[i][j]);
      Serial.print(" ");
    }
    
    Serial.print(" => Character: ");
    Serial.println(characters[i]);
  }
	
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {

  for (int i = 0; i < numButtons; i++) {
    if (digitalRead(buttonPins[i]) == LOW) {
      Serial.println(buttonPins[i]);
      pressedKeys[numPressedKeys] = buttonPins[i];
      numPressedKeys++;
      delay(500); 
    }
  }
  if (numPressedKeys == 3) {
	Serial.print(pressedKeys[0]);
  Serial.print(pressedKeys[1]);
  Serial.println(pressedKeys[2]);
  	checkPressedKeys();
    
}

}

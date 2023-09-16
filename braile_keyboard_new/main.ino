const int buttonPins[] = {2, 3, 4, 5, 6, 10, 11, 12, 13};
const int numButtons = sizeof(buttonPins) / sizeof(buttonPins[0]);

int sequences[36][9] = {
  {2, 3, 4}, {2, 3, 5}, {2, 3, 10}, {2, 3, 11}, {2, 3, 12}, {2, 3, 13},
  {2, 4, 5}, {2, 4, 10}, {2, 4, 11}, {2, 4, 12}, {2, 4, 13},
  {2, 5, 10}, {2, 5, 11}, {2, 5, 12}, {2, 5, 13},
  {2, 10, 11}, {2, 10, 12}, {2, 10, 13},
  {3, 4, 5}, {3, 4, 10}, {3, 4, 11}, {3, 4, 12}, {3, 4, 13},
  {3, 5, 10}, {3, 5, 11}, {3, 5, 12}, {3, 5, 13},
  {3, 10, 11}, {3, 10, 12}, {3, 10, 13},
  {4, 5, 10}, {4, 5, 11}, {4, 5, 12}, {4, 5, 13},
  {4, 10, 11}, {4, 10, 12}
};

const char* characters[36] = {
  "A", "B", "C", "D", "E", "F", "G", "H", "I",
  "J", "K", "L", "M", "N", "O", "P", "Q", "R",
  "S", "T", "U", "V", "W", "X", "Y", "Z",
  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 36; i++) {
    Serial.print("Sequence ");
    Serial.print(i + 1);
    Serial.print(": ");
    
    for (int j = 0; j < numButtons - 1; j++) { // Adjusted to numButtons - 1
      Serial.print(sequences[i][j]);
    }
    
    Serial.print(" => Character: ");
    Serial.println(characters[i]);
  }
}

void loop() {
  
}

import serial

ser = serial.Serial('COM3', 9600)

try:
    while True:
        # Read data from the Arduino
        data = ser.readline().strip()
        if data:
            button_number = int(data)
            print(f"Button {button_number} pressed")

            # Save the pressed key to a file
            with open('pressed_keys.txt', 'a') as file:
                file.write(f"{button_number}\n")

except KeyboardInterrupt:
    print("Program terminated.")
finally:
    ser.close()

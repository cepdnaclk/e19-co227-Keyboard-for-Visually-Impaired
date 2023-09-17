import serial
import pynput.keyboard as keyboard

ser = serial.Serial('COM3', 9600)
k = keyboard.Controller()

def send_char_to_input_buffer(c):
    """Sends a character to the keyboard input buffer."""
    k.press(c)
    k.release(c)

while True:
    try:
        data = ser.read().decode('utf-8')
        if data:
            # print(data)
            send_char_to_input_buffer(data)
    except KeyboardInterrupt:
        ser.close()
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")

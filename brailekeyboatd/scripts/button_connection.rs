use rppal::gpio::{Pin, InputPin};
use std::thread;

fn main() {
  //8 buttons
  let button_1 = Pin::new(12).into_input_pullup();
  let button_2 = Pin::new(13).into_input_pullup();
  let button_3 = Pin::new(14).into_input_pullup();
  let button_4 = Pin::new(15).into_input_pullup();
  let button_5 = Pin::new(26).into_input_pullup();
  let button_6 = Pin::new(27).into_input_pullup();
  let button_7 = Pin::new(28).into_input_pullup();
  let button_8 = Pin::new(29).into_input_pullup();
  

  //Listen for button presses
  thread::spawn(move || {
    loop {
      if button_1.is_high() 
        {
          println!("The number is {}", 1);
        } 
      else if button_2.is_high() 
        {
          println!("The number is {}", 2);
        } 
      else if button_3.is_high() 
        {
          println!("The number is {}", 3);
        } 
      else if button_4.is_high() 
        {
          println!("The number is {}", 4);
        } 
      else if button_5.is_high() 
        {
          println!("The number is {}", 5);
        } 
      else if button_6.is_high() 
        {
          println!("The number is {}", 6);
        } 
      else if button_7.is_high() 
        {
          println!("The number is {}", 7);
        } 
      else if button_8.is_high() 
        {
          println!("The number is {}", 8);
        }
    }
  });
  loop {}
}

// #include "LiquidCrystal_I2C.h";
// #include <Servo.h>
// #include <IRremote.h> 
// #include <Arduino.h>

// Servo myservo;
// int pos = 0;
// LiquidCrystal_I2C lcd(33,16,2);
// int data;
// int flag = 2;

// void setup() {
//   //Servo
//   myservo.attach(13);
//   //

//     //Initialize the LCD
//     lcd.begin();
//     // Turn on the blacklight
//     lcd.backlight();

//     lcd.setCursor(0, 0);
//     lcd.print("du ma may");
//     //serial init
//     Serial.begin(9600);
// }

// void loop() {
//     while( Serial.available() ){
//     //send flag
//     data = Serial.read();
//     if(data == '1'){
//       flag = 1;
//     }
//     else if(data == '0')
//     {
//       flag = 0;
//     }
//   }
//   serial flag processing
//   if(flag == 1)
//     {
//       lcd.setCursor (0,0);
//       lcd.print(" Welcome Boss!! ");
//       //servo activated
//       delay(200);
//     }
//      else if (flag == 0)
//     {
//       lcd.setCursor (0,0);
//       lcd.print("Face Unidentified ");
//     }
//   //   //SERVO
//   //     for (pos=0; pos<=180; pos++) { // từ 0 đến 180 độ
//   //     myservo.write(pos);
//   //     delay(5);
//   // }

//   // // Đảo ngược quá trình từ 180 đến 0 độ

// }

#include "LiquidCrystal_I2C.h";
#include <Servo.h>
#include "Adafruit_NeoPixel.h"

#include <Arduino.h>

Servo myservo;
int pos = 0;
LiquidCrystal_I2C lcd(33,16,2);
int data;
int flag = 0;

void setup() {
    //Servo
    myservo.attach(13);
    //Initialize the LCD
    lcd.begin();
    // Turn on the blacklight
    lcd.backlight();

    lcd.setCursor(0, 0);
    lcd.print("BACH KHOA");
    //serial init
    Serial.begin(9600);
}

void loop() {
    while( Serial.available() ){
    //send flag
    data = Serial.read();
    if(data == '1'){
      flag = 1;
    }
    else
    {
      flag = 0;
    }
  }
    // Serial flag processing
    if (flag == 1) {
        lcd.setCursor(0, 0);
        lcd.print(" Welcome Boss!! ");
        // Servo activated
        myservo.write(0);
        //

        flag = 0;
        delay(200);
    } else if (flag == 0) {
        lcd.setCursor(0, 0);
        lcd.print("Face Unidentified");
        // Servo activated
        myservo.write(100);
    }
}

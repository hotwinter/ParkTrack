/*
Laser Sensor 
VCC to Arduino 5V
GND to Arduino GND
Senser_1 2
Senser_2 3
*/

#define laser_1 2 // sensor 1
#define laser_2 3 // sensor 2
int sensor_1, sensor_2;
int cars, carsIn, carsOut, flag_1, flag_2;

void setup() {
  Serial.begin(9600);
  pinMode(laser_1,INPUT);
  pinMode(laser_2,INPUT);
  int setUp_1 = 0;
  int percentage_1 = 0; 
  int setUp_2 = 0;
  int percentage_2 = 0; 
  
  while (setUp_1 == 0 || setUp_2 == 0) {
    sensor_1 = digitalRead(laser_1);
    sensor_2 = digitalRead(laser_2);
    // Sensor 1
    if (percentage_1 == 100 && setUp_1 == 0) {
      setUp_1 = 1;
      Serial.println("Sensor 1 Setup Finished");
    } else if (sensor_1 == LOW && setUp_1 == 0){
      percentage_1++;
      if (percentage_1 % 10 == 0) {
        Serial.print(percentage_1);
        Serial.println(" / 100 SENSOR 1");
      }
    } else if (sensor_1 == HIGH && setUp_1 == 0){
      percentage_1 = 0;
      Serial.println("CHECK SENSOR 1");
    }
      
    // Sensor 2
    if (percentage_2 == 100 && setUp_2 == 0) {
      setUp_2 = 1;
      Serial.println("Sensor 2 Setup Finished");
    } else if (sensor_2 == LOW && setUp_2 == 0){
      percentage_2++;
      if (percentage_2 % 10 == 0) {
        Serial.print(percentage_2);
        Serial.println(" / 100 SENSOR 2");
      }
    } else if (sensor_2 == HIGH && setUp_2 == 0){
      percentage_2 = 0;
      Serial.println("CHECK SENSOR 2");
    }
    delay(100);
  }
  Serial.println("Setup Finished");
  Serial.println("====================================");  
}

void loop() {
  sensor_1 = digitalRead(laser_1);
  sensor_2 = digitalRead(laser_2);

  //*******************************************// Parking // LOW - No Object  HIGH - Object detected
  if ((flag_1 == 1) && (flag_2 == 1)) {
    if (sensor_1 == HIGH && sensor_2 == HIGH) {       // HIGH HIGH Object detected by both sensor
      //Serial.println("Car Blocking");
    } else if (sensor_1 == HIGH && sensor_2 == LOW) { // HIGH LOW Object detected by sensor 1
      carsIn++;
      cars++;
      //Serial.println("IN<=======");
      //Serial.print("Total cars in the Garage: ");
      Serial.print("CARS IN :");
      Serial.println(carsIn);
    } else if (sensor_1 == LOW && sensor_2 == HIGH) { // LOW HIGH bject detected by sensor 2
      carsOut++;
      cars--;
      //Serial.println("======>OUT");
      //Serial.print("Total cars in the Garage: ");
      Serial.print("CARS OUT :");
      Serial.println(carsOut);
    } else if (sensor_1== LOW && sensor_2 == LOW) {
      Serial.println("error");
    }
  }
  //********************************************// FLAG
  if (sensor_1 == HIGH && sensor_2 == HIGH){          // 1 1 HIGH HIGH Object detected by both sensor 
    flag_1 = 1;
    flag_2 = 1;
  } else if (sensor_1 == LOW && sensor_2 == HIGH){    // 0 1 LOW HIGH
    flag_1 = 0;
    flag_2 = 1;
  } else if (sensor_1 == HIGH && sensor_2 == LOW){    // 1 0 HIGH LOW
    flag_1 = 1;
    flag_2 = 0;
  } else if (sensor_1 == LOW && sensor_2 == LOW){     // 0 0 LOW LOW
    flag_1 = 0;
    flag_2 = 0;   
  }
  delay(50);
}






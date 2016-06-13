/*
HC-SR04 Ping distance sensor
VCC to Arduino 5V
GND to Arduino GND
Echo to Arduino pin 3, 5
Trig to Arduino pin 2, 4
*/

#define trigPin_1 8 // distance sensor 1
#define echoPin_1 9
#define trigPin_2 12 // distance sensor 2
#define echoPin_2 13

#define LED_1 6 // LED for distance sensor 1
#define LED_2 7 // LED for distance sensor 2

int MAX = 500;
int MIN = 0;
float TRIGER = 1.5; 
long duration, distance, duration_1, distance_1, duration_2, distance_2;
long counts, total_1, average_1, total_2, average_2, flag_1, flag_2, cars;


void setup() {
  Serial.begin (9600);
  pinMode(trigPin_1, OUTPUT);
  pinMode(echoPin_1, INPUT);
  pinMode(trigPin_2, OUTPUT);
  pinMode(echoPin_2, INPUT);
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);

  for (int setUp = 0; setUp < 101; setUp++) {
    //********************************************// DISTANCE SENSOR 1
    distance_1 = SonarSensor(trigPin_1,echoPin_1);
    digitalWrite(LED_1, HIGH);
    
    delay(50);
    //********************************************// DISTANCE SENOR 2
    distance_2 = SonarSensor(trigPin_2, echoPin_2);
    digitalWrite(LED_2, HIGH);
    
    counts++;
    total_1 += distance_1;
    average_1 = (total_1 + distance_1) / counts;
    total_2 += distance_2;
    average_2 = (total_2 + distance_2) / counts;
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, LOW);
    delay(50);
    Serial.print("Setup ");
    Serial.print(setUp);
    Serial.println(" / 100");
  }
  Serial.println("Setup Finished");
  Serial.print("Sensor 1: ");
  Serial.print(average_1);
  Serial.print(" cm // Sensor 2: ");
  Serial.print(average_2);
  Serial.println(" cm");
  Serial.println("====================================");
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  
}

void loop() {
  //********************************************// DISTANCE SENSOR 1
  distance_1 = SonarSensor(trigPin_1,echoPin_1);
  
  delay(50);
  //********************************************// DISTANCE SENOR 2
  distance_2 = SonarSensor(trigPin_2, echoPin_2);
  
  Serial.print(distance_1);
  Serial.print(" // ");
  Serial.println(distance_2);
  
  //*******************************************// Parking 
  if ((flag_1 == 1) && (flag_2 == 1)) {
    if ((distance_1 < (average_1 / TRIGER)) && (distance_2 < (average_2 / TRIGER))) {         // Object detected by both sensor
      Serial.println("Car Blocking");
    } else if  ((distance_1 < (average_1 / TRIGER)) && (distance_2 > (average_2 / TRIGER))) { // Object detected by sensor 1
      cars++;
      Serial.println("IN<=======");
      Serial.print("Total cars in the Garage: ");
      Serial.println(cars);
    } else if ((distance_1 > (average_1 / TRIGER)) && (distance_2 < (average_2 / TRIGER))) { // Object detected by sensor 2
      cars--;
      Serial.println("======>OUT");
      Serial.print("Total cars in the Garage: ");
      Serial.println(cars);
    } else if ((distance_1 > (average_1 / TRIGER)) && (distance_2 > (average_2 / TRIGER))) {
      Serial.println("error");
    }
  }
  //********************************************// FLAG
  if ((distance_1 < (average_1 / TRIGER)) && (distance_2 < (average_2 / TRIGER))){         // 1 1
    flag_1 = 1;
    flag_2 = 1;
    digitalWrite(LED_1, HIGH);
    digitalWrite(LED_2, HIGH);
  } else if ((distance_1 > (average_1 / TRIGER)) && (distance_2 < (average_2 / TRIGER))){  // 0 1
    flag_1 = 0;
    flag_2 = 1;
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, HIGH);
  } else if ((distance_1 < (average_1 / TRIGER)) && (distance_2 > (average_2 / TRIGER))){  // 1 0
    flag_1 = 1;
    flag_2 = 0;
    digitalWrite(LED_1, HIGH);
    digitalWrite(LED_2, LOW);
  } else if ((distance_1 > (average_1 / TRIGER)) && (distance_2 > (average_2 / TRIGER))){  // 0 0
    flag_1 = 0;
    flag_2 = 0;
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, LOW);    
  }
  delay(50);
}

//********************************************// DISTANCE SENSOR
long SonarSensor(int trigPin,int echoPin){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH,20000);
  distance = (duration/2) / 29.1;
  return distance;
}





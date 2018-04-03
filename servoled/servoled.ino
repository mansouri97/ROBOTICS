int incomingByte = 0;
int ledPin = 9;
String in; 
void setup(){
pinMode(ledPin, OUTPUT);
Serial.begin(9600);
}
 
void loop(){
 
if (Serial.available() > 0) {
// read the incoming byte:
incomingByte = Serial.read();
//in=Serial.readString();

 
// say what you got:
if(incomingByte == '1') { // ASCII printable characters: 49 means number 1
 digitalWrite(ledPin, HIGH);
 Serial.print("light on");
} else if(incomingByte == '0') { // ASCII printable characters: 48 means number 0
 digitalWrite(ledPin, LOW);
 Serial.print("light off");

}
}
 
}

  



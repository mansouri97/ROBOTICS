void setup() {
  pinMode(11,OUTPUT);
  pinMode(8,OUTPUT);
  digitalWrite(11,0); // put your main code here, to run repeatedly:
 digitalWrite(8,0);
}

void loop() {
 digitalWrite(11,1); // put your main code here, to run repeatedly:
 digitalWrite(8,0);
 delay(2000);
 digitalWrite(11,0); // put your main code here, to run repeatedly:
 digitalWrite(8,0);
 delay(5000);
 digitalWrite(11,0); // put your main code here, to run repeatedly:
 digitalWrite(8,1);
delay(2000);
}

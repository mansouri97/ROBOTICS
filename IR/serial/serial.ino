#define rel1 10   
#define rel2 12
#define npn 11

int dir1=0,dir2=0,sensorValue,outputValue;

void setup() {
  // put your setup code here, to run once:
pinMode(rel1,OUTPUT);
pinMode(rel2,OUTPUT);

pinMode(2,INPUT);
pinMode(3,INPUT);

digitalWrite(rel1,0);
digitalWrite(rel2,0);
}

void loop() {



dir1=digitalRead(2);
dir2=digitalRead(3);

sensorValue = analogRead(A0);
outputValue = map(sensorValue, 0, 1023, 0, 255);
analogWrite(npn,outputValue);
while(dir1==1)
  {
   
   digitalWrite(rel1,1);
   digitalWrite(rel2,0);
   dir1=digitalRead(2);
   }

while(dir2==1)
  {
    
   digitalWrite(rel1,0);
   digitalWrite(rel2,1);
   dir2=digitalRead(3);
   }
    

digitalWrite(rel1,0);
digitalWrite(rel2,0);
  




}

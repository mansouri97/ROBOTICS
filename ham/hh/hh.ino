#define in1 11
#define in2 12

int a,b;

void setup() {
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);  
  pinMode(5,INPUT);
  pinMode(4,INPUT);
  digitalWrite(in1,0);
  digitalWrite(in2,0);
  
}

void loop() {
a = digitalRead(4);
b = digitalRead(5);

while(a==1){ 
   
   digitalWrite(in1,1);
   digitalWrite(in2,0);
   a = digitalRead(4);
 }
     

while(b==1){ 
   
   digitalWrite(in1,0);
   digitalWrite(in2,1);
   b = digitalRead(5);
 }
   
digitalWrite(in1,0);
digitalWrite(in2,0);



}

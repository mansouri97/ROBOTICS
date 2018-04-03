

int in=0; 
int in2=0;
int in3=0; 
int in4=0;
int a=0;
int b=0;
int i;
void setup() {
 pinMode(2,INPUT);
 pinMode(3,INPUT);
 pinMode(4,INPUT);
 pinMode(5,INPUT); 
 pinMode(12,OUTPUT);
 pinMode(13,OUTPUT);
 pinMode(11,OUTPUT);
 Serial.begin(9600);
}

void loop() {
in=digitalRead(2);
in2=digitalRead(3);

 while(in==1)
 { digitalWrite(12,1);
   digitalWrite(13,0);
   a++; 
   Serial.println(a);
   delay(200);
   in=digitalRead(2);
   
 }
 while(in2==1)
 { digitalWrite(12,0);
   digitalWrite(13,1);
   a--; 
   Serial.println(a);
   delay(200);
   in2=digitalRead(2);
 }
 
digitalWrite(12,0);
digitalWrite(13,0);
in3=digitalRead(4);
in4=digitalRead(5);

if(in3==1) {digitalWrite(11,1);b=a; Serial.println("a is saved");delay(200);}else(digitalWrite(11,0));

if(in4==1) {
    if(b>a) {for(i=0;i<b-a;i++){    digitalWrite(12,1);digitalWrite(13,0); Serial.println(a+i);delay(200);}a=b;}
    if(b<a) {for(i=0;i<a-b;i++){    digitalWrite(12,0);digitalWrite(13,1); Serial.println(a-i-1);delay(200);}a=b;}
    if(a=b) {a=b;}
    
}







}



//
//#define up 16753245 
//#define dwn 16749165
//#define right 16756815
//#define left 16736925
//#define rep 4294967295

int incomingByte;


void setup()
{
  Serial.begin(9600);
 pinMode(8,OUTPUT);pinMode(9,OUTPUT);
}


void loop()
{
if (Serial.available() > 0) {
  incomingByte = Serial.read();
  
   if (incomingByte == 's') {
     bcws(500);
     stps(); 
    }
   if (incomingByte == 'z') {
     fwds(500);
     stps(); 
    }
   if (incomingByte == 'q') {
     bcw(80);
     stp(); 
    }
   if (incomingByte == 'd') {
     fwd(80);
     stp(); 
    }
  }

fwds(500);
stpsd(500);
bcw(80);
stpd(500);
bcws(500);
stpsd(500);
fwd(80);
stpd(500);
delay(2000);
bcw(80);
stpd(500);
fwds(500);
stpsd(500);
fwd(80);
stpd(500);
bcws(500);
stpsd(500); 
delay(2000);
}


void bcw(int x)
{
digitalWrite(8,1);
digitalWrite(9,0);
delay(x); 
}


void fwd(int x)
{
digitalWrite(8,0);
digitalWrite(9,1);
delay(x); 
}

void stp()
{
digitalWrite(8,0);
digitalWrite(9,0);

}
void stpd (int x)
{
digitalWrite(8,0);
digitalWrite(9,0);

delay(x);
}
void bcws(int x)
{
digitalWrite(10,0);
digitalWrite(11,1);
delay(x); 
}


void fwds(int x)
{
digitalWrite(10,1);
digitalWrite(11,0);
delay(x); 
}

void stps()
{
digitalWrite(10,0);
digitalWrite(11,0);
 
}
void stpsd(int x)
{
digitalWrite(10,0);
digitalWrite(11,0);
 delay(x);
}

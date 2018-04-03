#include <EEPROM.h>
int b,i,address,value,memval;
String input="",add="",val="";
char phrase[17];


void setup()
{ 
  Serial.begin(9600);

}


void loop() {  

while(Serial.available()){
  
  
  input=Serial.readString();
  b=input.length();


  input.toCharArray(phrase, b+1);

  char *token =strtok(phrase, " ");
  i=0;
  while(token != NULL)
    {
     i++;
     token = strtok(NULL, " ");
     if (i==1) add=token; 
     if (i==2) val=token;
    }

  address=add.toInt();
  value=val.toInt(); 


if (phrase[0]=='w') { EEPROM.write(address, value); Serial.print(String(memval)+ " is saved at " +String(address));Serial.print("\n");}
if (phrase[0]=='r') { memval = EEPROM.read(address);Serial.print("value at " + String(address) + " is " + String(memval));Serial.print("\n");}

}

} 








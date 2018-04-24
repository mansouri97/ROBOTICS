#include <stdio.h>
#include <stdlib.h>
#include<string.h>
struct automate
{
int nb_etats;
int etat_initial;
int etat_acceptant;
int matrice_transition[10][10];
};

void automate_data(struct automate *a)
{
   printf("donner le nombre d'états de l'automate : ");
   scanf("%d",&a->nb_etats);
   printf("\ndonner l'état initial : ");
   scanf("%d",&a->etat_initial);
   printf("\ndonner l'état acceptant : ");
   scanf("%d",&a->etat_acceptant);
   int i,j;
   printf("\nprenand (a=0,b=1)nombre colone et le num de l'etat courant E(0,1,2,etc..) comme\n");
   printf("ligne remplir le matrice avec les etat resultant de l'intersection entre \n");
   printf("linge et colone si il n'ya pas d'etat entrer(404)\n");
  for(i=0;i<(a->nb_etats);i++)
  {

    for(j=0;j<2;j++)
    {
      printf("\ndonner le etat [%d][%d] : ",i,j);
      scanf("%d",&a->matrice_transition[i][j]);
    }
     


  }
}



void print_automate(struct automate c)
{
printf("\nLe nombre d'états de l'automate est %d \n",c.nb_etats);
printf("\nL'état initial est E%d \n",c.etat_initial);
printf("\nl'état acceptant est E%d \n",c.etat_acceptant);
printf("\nLa matrice de transition est :\n");
printf("\ta\tb\n");
  int i,j;
  for(i=0;i<c.nb_etats;i++)
  {
    printf("E%d\t",i);
    for(j=0;j<2;j++)
       printf("E%d\t",c.matrice_transition[i][j]);
    printf("\n");
  }

}

int apply_transition(struct automate b,int etat_courant, char lettre)
{
int k;
if (lettre=='a') k=0;
if(lettre=='b') k=1;
return b.matrice_transition[etat_courant][k];
}
 
void word_test(struct automate d)
{
int i,k,c=0;
char word[20];
print_automate(d);
printf("\ngive me a word of a nd b ");
scanf("%s",word);
printf("\nvoici le parcours :\nE0 ");
for	(i=0;i<strlen(word);i++)
 {
 if (word[i]=='a') k=0; 
 if (word[i]=='b') k=1;
 
 
 printf("E%d ",d.matrice_transition[c][k]);
 if ((i==strlen(word)-1)&& (d.matrice_transition[c][k]!=d.etat_acceptant)) printf("\nle mot n'est pas accepté");
 if (d.matrice_transition[c][k]==404) {
 	printf("le parcour n'exicte pas donc le mot n'est pas accépte");
 	break;
 }
 c=d.matrice_transition[c][k];
 
 
 }
	
	
	
}
int main()
{
	int i,j,etat_courant,transition;
    struct automate m,*pointer;
    char lettre;
    pointer=(struct automate*)malloc(sizeof(struct automate ));
    automate_data(pointer);
    m.nb_etats=pointer->nb_etats;
    m.etat_initial=pointer->etat_initial;
    m.etat_acceptant=pointer->etat_acceptant;
    for(i=0;i<m.nb_etats;i++)
      for(j=0;j<2;j++)
         m.matrice_transition[i][j]=pointer->matrice_transition[i][j];
	 

word_test(m);


//print_automate(m);
//printf("donner un etat et une lettre de l'alphabet : ") ;
//scanf("%d %c",&etat_courant,&lettre) ;
//transition=apply_transition(m,etat_courant,lettre);
//printf("\n  E%d",transition);
  
return 0;
}

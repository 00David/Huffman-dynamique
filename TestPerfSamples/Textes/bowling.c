#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NBTOURS 5
#define NBLANCERS 2
#define NBQUILLES 10

/* Il sera probablement nécessaire de modifier les parametres et valeur de retour des fonctions 
  lancer, lancer_aleatoire, score et jeu */

/* Les declarations actuelles permettent de compiler et d'executer le programme */

int lancer(int *nb_quilles_debout) {
  int bon=0;
  int val;
  while (bon != 1) {
    printf("Combien de quilles vont tomber ? ");
    scanf("%d",&val);
    if ((val>=0) && (val<=*nb_quilles_debout)) {
      bon=1;
    }
  }
  return val;
}

int lancer_aleatoire() {
  return 0;
}

void score(int *score_jeu,int nb_quilles_lancer, int *spare, int *strike1, int *strike2) {

  *score_jeu=*score_jeu+nb_quilles_lancer;
  if ((*spare==1) && (*strike1==0) && (*strike2==0)) {
    *score_jeu=*score_jeu+nb_quilles_lancer;
  }
  if ((*spare==0) && (*strike1==1) && (*strike2==0)) {
    *score_jeu=*score_jeu+nb_quilles_lancer;
  }
  if ((*spare==0) && (*strike1==0) && (*strike2==1)) {
    *score_jeu=*score_jeu+nb_quilles_lancer;
  }



  if (*spare==1) {
    *spare=0;
  }
  if (*strike1==1) {
    *strike1=0;
  }
  if (*strike2==1) {
    *strike2=0;
    *strike1=1;
  }
}

void tour(int *score_jeu, int *spare, int *strike1, int *strike2,int nb_lancers){

  int nb_quilles_debout=10;

  int i;
  for (i=0;i<nb_lancers;i++) {
    int lanc=lancer(&nb_quilles_debout);
    nb_quilles_debout=nb_quilles_debout-lanc;
    printf("Quilles renversees : %d\n",lanc);

    score(score_jeu, lanc, spare, strike1, strike2);

    if ((nb_quilles_debout==0) && (i==0)) {
      *strike2=1;
      i=nb_lancers;
    }

    if ((nb_quilles_debout==0) && (i==1)) {
      *spare=1;
    }
  }


}

int jeu() {
  int nb_tours=1;
  int spare=0;
  int strike1=0;
  int strike2=0;
  int score_jeu=0;


  while (nb_tours<NBTOURS+1) {
    printf("\n");
    printf("TOUR ACTUEL : %d\n",nb_tours);
    printf("Score actuel : %d points\n",score_jeu);

    tour(&score_jeu, &spare, &strike1, &strike2,NBLANCERS);

    if ((spare==0) && (strike1==0) && (strike2==0)) {
      printf("Score apres tour %d : %d\n",nb_tours,score_jeu);
    }
    if (spare==1) {
      printf("Score apres tour %d : %d\n",nb_tours,score_jeu);
      printf("Score incomplet : spare en cours\n");
    }
    if (strike2==1) {
      printf("Score apres tour %d : %d\n",nb_tours,score_jeu);
      printf("Score incomplet : strike en cours\n");
    }
    nb_tours=nb_tours+1;

  }

  if ((nb_tours==NBTOURS+1) && (strike2==1)) {
    int spare=0;
    int strike1=0;
    int strike2=0;

    printf("\n");
    printf("TOUR ACTUEL : TOUR SUPPLEMENTAIRE\n");
    printf("Score actuel : %d points\n",score_jeu);

    tour(&score_jeu, &spare, &strike1, &strike2,2);
    nb_tours=nb_tours+1;
  }
  if ((nb_tours==NBTOURS+1) && (spare==1)) {
    int spare=0;
    int strike1=0;
    int strike2=0;

    printf("\n");
    printf("TOUR ACTUEL : TOUR SUPPLEMENTAIRE\n");
    printf("Score actuel : %d points\n",score_jeu);

    tour(&score_jeu, &spare, &strike1, &strike2,1);
    nb_tours=nb_tours+1;
  }


  printf("Score final : %d points\n",score_jeu);


  return 0;
}

int main() {
  srand(time(NULL));
  jeu(); 
  return 0;
}
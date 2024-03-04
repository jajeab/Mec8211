clc,clear all,close all
% But: ce code calcule l'expression du terme source à rajouter pour l'exemple sur la MMS en page 221 de Oberkapmf et Roy (ou voir aussi les diapos sur la MMS)
%
%
syms r t Ce Deff beta % Définition des variables symboliques
syms T(r,t) % Définition de la fonction symbolique et de ses variables

R = 0.5;
T(r,t)= beta*cos(pi*r)*(sin((1/t)+pi/2))+ Ce; %choix de la solution


dTdt=diff(T,t); % Dérivée temporelle de la solution choisie
d2Tdr2=diff(diff(T,r),r); % Laplacien de la solution choisie
dTdr=diff(T,r); % Calcul de la dérivée première pour l'évaluation de la condition de Neumann
dTdr_at_r0=dTdr(subs(0),t); % Si on souhaite tester une possible condition de Neumann (flux), permet d'obtenir l'expression de la condition de Neumann à x = 0.
T_at_L=T(subs(0.5),t); %
S = dTdt - Deff*(d2Tdr2 + (1/r)*dTdr);
T_at_0=T(subs(0),t); %

disp(' ');
disp('Resultats:');
disp(' ');
disp(['Dérivée temporelle de la solution choisie: ', char(dTdt)]);
disp(['Laplacien de la solution choisie: ', char(d2Tdr2)]);
disp(['Condition de dirichlet à r=L: ', char(T_at_L)]);
disp(['Condition de Neumann à r=0: ', char(dTdr_at_r0)]);
disp(['Terme source à ajouter: ', char(S)]);

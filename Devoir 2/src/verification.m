clc, clear all, close all;
tic
% Paramètres de simulation  
R = .5; % Rayon du pilier
Deff = 1E-10; % Coefficient de diffusion effectif
%S = 8e-9; % Terme source
Ce = 12; % Concentration à la surface
nbr_noeuds = [600 650 700 750 800]; % Nombre de nœuds pour les simulations
delta_r = R ./ (nbr_noeuds - 1); % pas en espace
%% DISCRÉTISATION EN ESPACE

% Initialisation des vecteurs d'erreur
erreur_L1 = zeros(1, length(nbr_noeuds));
erreur_L2 = zeros(1, length(nbr_noeuds));
erreur_Linf = zeros(1, length(nbr_noeuds));

% Création d'une grille fine pour l'interpolation et le calcul d'erreur
r_fine = linspace(0, R, 1000); % Grille fine allant de 0 à R

% Affichage des résultats
figure; % Crée une nouvelle figure pour les concentrations
hold on; % Garde la figure active pour le prochain tracé

for i = 1:length(nbr_noeuds)
    nbr = nbr_noeuds(i); % Nombre de nœuds pour la simulation courante
    [r, C, ref, temps] = transit_shema_2(nbr, R, Deff, Ce); % Appel de la fonction de calcul

    % Calcul des erreurs L1, L2 et Linf
    diff = abs(C' - ref);
    erreur_L1(i) = sum(diff) * (r_fine(2) - r_fine(1)); % Somme des erreurs absolues
    erreur_L2(i) = sqrt(sum(diff.^2) * (r_fine(2) - r_fine(1))); % Racine carrée de la somme des carrés des erreurs
    erreur_Linf(i) = max(diff); % Erreur maximale absolue

    % Tracé de la concentration
    plot(r, C, '.', 'MarkerSize', 18, 'DisplayName', ['MMS ' num2str(nbr) ' nœuds']);
end

% Tracé de la solution analytique de référence
plot(r, ref, 'k', 'LineWidth', 2, 'DisplayName', 'Solution Analytique');

xlabel('Distance (m)');
ylabel('Concentration de sel (mol/m^3)');
title('Comparaison entre une fonction et sa MMS');
legend('show');
grid on;
toc

% Calcul de l'ordre de convergence pour L1, L2, Linf
% Utiliser log10 pour le calcul sur une échelle logarithmique
pente_L1 = polyfit(log10(delta_r), log10(erreur_L1), 1);
pente_L2 = polyfit(log10(delta_r), log10(erreur_L2), 1);
pente_Linf = polyfit(log10(delta_r), log10(erreur_Linf), 1);

beta_L1 = 10^pente_L1(2);
beta_L2 = 10^pente_L2(2);
beta_Linf = 10^pente_Linf(2);

% Nouvelle figure pour les erreurs en échelle logarithmique
figure;
hold on; % Garde la figure active pour le prochain tracé

% Tracé des erreurs en échelle semi-logarithmique pour mieux visualiser
plot(delta_r, erreur_L1, 'b-o', 'LineWidth', 2, 'MarkerSize', 8, 'DisplayName', 'Erreur L1');
plot(delta_r, erreur_L2, 'g-s', 'LineWidth', 2, 'MarkerSize', 8, 'DisplayName', 'Erreur L2');
plot(delta_r, erreur_Linf, 'r-^', 'LineWidth', 2, 'MarkerSize', 8, 'DisplayName', 'Erreur Linf');

xlabel('Delta r');
ylabel('Erreur');
title('Erreur L1, L2 et Linf en fonction du pas d''espace');
legend('show');
set(gca,'xscale','log')
set(gca,'yscale','log')
grid on;

% Création des chaînes de texte pour les annotations
strL1 = ['\epsilon = ' num2str(beta_L1, 2) ' \Deltar^{' num2str(pente_L1(1), 2) '}'];
strL2 = ['\epsilon = ' num2str(beta_L2, 2) ' \Deltar^{' num2str(pente_L2(1), 2) '}'];
strLinf = ['\epsilon = ' num2str(beta_Linf, 2) ' \Deltar^{' num2str(pente_Linf(1), 2) '}'];

% Position des annotations sur le graphique pour chaque type d'erreur
% Ajustez les valeurs ci-dessous pour bien positionner vos annotations
offset = 1.1; % Offset pour élever le texte au-dessus des lignes
for i = round((length(nbr_noeuds))/2)
    delta_r = R / (nbr_noeuds(i) - 1);
    text(delta_r, erreur_L1(i) * offset, strL1, 'VerticalAlignment', 'bottom', ...
         'HorizontalAlignment', 'right', 'FontSize', 8);
    text(delta_r, erreur_L2(i) * offset, strL2, 'VerticalAlignment', 'bottom', ...
         'HorizontalAlignment', 'right', 'FontSize', 8);
    text(delta_r, erreur_Linf(i) * offset, strLinf, 'VerticalAlignment', 'bottom', ...
         'HorizontalAlignment', 'right', 'FontSize', 8);
end

% Affichage du graphique
hold off;

%% Erreur pas de temps

% resultats = simulation_adaptative(nbr_noeuds, R, Deff, Ce);
% [~, ~, ref] = transit_shema_2(nbr_noeuds, R, Deff, Ce, 2e3, 0.01, 1e9);
% ref_50 = ref(50); % Terme de référence au 50e noeud
% 
% % Initialisation des vecteurs d'erreur
% erreur_L1 = zeros(size(resultats, 1), 1);
% erreur_L2 = zeros(size(resultats, 1), 1);
% erreur_Linf = 0;
% 
% % Calcul des erreurs
% for i = 1:size(resultats, 1)
%     delta_t = resultats(i, 1);
%     C_50 = resultats(i, 2);
%     
%     erreur_L1(i) = abs(C_50 - ref_50); % Erreur L1
%     erreur_L2(i) = (C_50 - ref_50)^2; % Erreur L2 (à sommer puis racine carrée à la fin)
%     
%     if erreur_L1(i) > erreur_Linf
%         erreur_Linf = erreur_L1(i); % Erreur Linf
%     end
% end
% 
% % Calcul final de l'erreur L2
% erreur_L2 = sqrt(sum(erreur_L2));
% 
% 
% 
% % Affichage des erreurs en fonction du pas de temps sur le même graphique
% figure;
% 
% % Tracé des erreurs L1, L2, et Linf
% %plot(resultats(:, 1), erreur_L1, 'b-o', ...
% %     resultats(:, 1), repmat(erreur_L2, size(resultats, 1), 1), 'r-*', ...
% %     resultats(:, 1), repmat(erreur_Linf, size(resultats, 1), 1), 'g-x');
% plot(resultats(:, 1), erreur_L1, 'b-o');
% 
% % Ajout de la légende
% %legend('Erreur L^1', 'Erreur L^2', 'Erreur L^\infty');
% legend('Erreur L^1');
% 
% % Titre et labels
% title('Erreurs L^1 en fonction du temps');
% % title('Erreurs L^1, L^2, et L^\infty en fonction du temps');
% xlabel('temps');
% ylabel('Erreur');
% 
% 
% % Ajustement des graphiques pour une meilleure visualisation
% %set(gca,'xscale','log')
% set(gca,'yscale','log')
% grid on;
% 


% % MATLAB script to launch a fiber structure generation and the corresponding LBM simulation
% %
% %INPUT VARIABLES:
% %
% % SEED: integer representing the seed for initializing the random
% % generator. If seed=0, automatic seed generation. If you want to reproduce
% % the same fiber structure, use the same seed (fibers will be located at the same place). 
% %
% % MEAN_D: contains the mean fiber to be used
% %
% % STD_D: contains the standard deviation of the fiber diameters
% %
% % PORO: estimated porosity of the fiber structure to be generated
% % 
% % NX: domain lateral size in grid cell

seed = 101;
deltaP = 0.1; % Pression en Pa
NX_values = [50, 100, 200, 400]; % Différentes valeurs de NX à tester
poro = 0.9;
mean_fiber_d = 12.5; % en microns
std_d = 2.85; % en microns
%dx = 2e-6; % Taille de la grille en m
dx = [2*2e-6,2e-6,1/2*2e-6,1/4*2e-6];

filename = 'fiber_mat.tiff';

% Initialisation des vecteurs pour stocker les valeurs de perméabilité et les erreurs
permeabilite_values = zeros(size(NX_values));

% Génération de la structure des fibres et calcul de la perméabilité pour chaque valeur de NX
for i = 1:numel(NX_values)
    NX = NX_values(i);
    
    % Génération de la structure des fibres
    [d_equivalent] = Generate_sample(seed, filename, mean_fiber_d, std_d, poro, NX, dx(1,i));
    
    % Calcul de la perméabilité
    permeabilite = LBM(filename, NX, deltaP, dx(1,i), d_equivalent);
    
    % Enregistrement de la perméabilité
    permeabilite_values(i) = permeabilite;
end

% Tracé de la courbe de convergence
figure;
semilogx(NX_values, permeabilite_values, '-o', 'LineWidth', 2);
xlabel('NX');
ylabel('Permeabilité [micron^2]');
title('Courbe de convergence de la perméabilité en fonction de NX');


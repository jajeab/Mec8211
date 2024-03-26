% MATLAB script to launch a fiber structure generation and the corresponding LBM simulation
%
%INPUT VARIABLES:
%
% SEED: integer representing the seed for initializing the random
% generator. If seed=0, automatic seed generation. If you want to reproduce
% the same fiber structure, use the same seed (fibers will be located at the same place). 
%
% MEAN_D: contains the mean fiber to be used
%
% STD_D: contains the standard deviation of the fiber diameters
%
% PORO: estimated porosity of the fiber structure to be generated
% 
% NX: domain lateral size in grid cell

seed=0;
deltaP= 0.1 ; % pressure drop in Pa
nombre_echantillons = 1000;
NX= 100 ;
%poro= 0.9 ;
mean_poro= 0.9;
mean_fiber_d= 12.5 ; % in microns
poro_std = 7.5e-3; % ecart-type distribution porosite
std_d= 2.85 ; % in microns
dx= 2e-6 ; % grid size in m
filename= 'fiber_mat.tiff' ;
permeabilite = zeros(1,nombre_echantillons);
porosite = normrnd(mean_poro,poro_std,[1 nombre_echantillons]);

% generation of the fiber structure
for i = 1: nombre_echantillons
    
    [d_equivalent]=Generate_sample(seed,filename,mean_fiber_d,std_d,mean_poro,poro_std,porosite(1,i),NX,dx);
    
    % calculation of the flow field and the permeability from Darcy Law
    permeabilite(i) = LBM(filename,NX,deltaP,dx,d_equivalent);
    
end

% Tracé de l'histogramme et ajustement de la PDF gaussienne
figure;
histogram(permeabilite, 'Normalization', 'pdf', 'BinWidth', 1);
hold on;

% Ajustement de la PDF (distribution gaussienne)
mu = mean(permeabilite);
sigma = std(permeabilite);
x = linspace(min(permeabilite), max(permeabilite), nombre_echantillons);
pdf_gaussienne = (1 / (sigma * sqrt(2 * pi))) * exp(-(x - mu).^2 / (2 * sigma^2));
plot(x, pdf_gaussienne, 'r', 'LineWidth', 2);

% Tracé de la moyenne et de l'écart-type pour la distribution gaussienne
yl = ylim;
line([mu, mu], yl, 'Color', 'g', 'LineWidth', 1.5, 'LineStyle', '--');
text(mu, yl(2), sprintf('Mean: %.2f', mu), 'Color', 'g', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'center');

line([mu - sigma, mu - sigma], yl, 'Color', 'b', 'LineWidth', 1.5, 'LineStyle', '--');
line([mu + sigma, mu + sigma], yl, 'Color', 'b', 'LineWidth', 1.5, 'LineStyle', '--');
text(mu - sigma, yl(2), sprintf('Mean - Std: %.2f', mu - sigma), 'Color', 'b', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'center');
text(mu + sigma, yl(2), sprintf('Mean + Std: %.2f', mu + sigma), 'Color', 'b', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'center');

xlabel('Permeabilité');
ylabel('PDF');
title('Distribution de la perméabilité avec ajustement de la PDF (gaussienne)');
legend('Données expérimentales', 'PDF gaussienne', 'Mean', 'Mean ± Std');

figure;
histogram(permeabilite, 'Normalization', 'pdf', 'BinWidth', 1);
hold on;
% Ajustement de la PDF (log-normal)
param_lognormal = fitdist(permeabilite', 'lognormal');
pdf_lognormal = pdf(param_lognormal, x);
plot(x, pdf_lognormal, 'm', 'LineWidth', 2);


% Calcul de la médiane
median_lognormal = exp(param_lognormal.mu);

% Calcul du facteur de variation géométrique (FVG)
FVG = exp(param_lognormal.sigma);

%Affichage de la mediane et et FVG sur le graphe
x_median = (max(x) + log(median_lognormal)) / 2;
x_FVG = (max(x) + log(FVG)) / 2;
yl = ylim;
text(x_median, yl(2)*0.9, ['Median: ', num2str(log(median_lognormal))], 'Color', 'g', 'VerticalAlignment', 'middle', 'HorizontalAlignment', 'right');
text(x_FVG, yl(2) * 0.85, ['FVG: ', num2str(log(FVG))], 'Color', 'b', 'VerticalAlignment', 'middle', 'HorizontalAlignment', 'right');

% Autres configurations du tracé (étiquettes, titre, légende, etc.)
xlabel('Permeabilité [micron^2]');
ylabel('densite de probabilite');
title('Distribution de la perméabilité avec ajustement de la PDF (log-normale)');
legend('PDF log-normale', 'Location', 'best');

% Tracé de la CDF
cdf_values = cdf(param_lognormal, x);
figure;
plot(x, cdf_values, 'k', 'LineWidth', 2);
xlabel('Permeabilité [micron^2]');
ylabel('distribution cumulative de probalite');
title('Fonction de distribution cumulative (CDF) de la perméabilité');


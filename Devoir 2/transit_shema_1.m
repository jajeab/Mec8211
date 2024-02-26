function [r, C, ref] = transit_shema_1(nbr, R, Deff, S, Ce)

    % Le schéma semble contenir un problème à la condition de neumann
    %Initialisation
    delta_r = R / (nbr - 1);
    r = linspace(0, R, nbr); % points du domaine
    matrix = zeros(nbr);
    b = zeros(nbr, 1);
    C = zeros(nbr, 1);
    
    % Solution analytique
    ref = 0.25 * (S / Deff) * (R^2) * ((r / R).^2 - 1) + Ce;
    
    % paramètre de temps
    t = 0;
    t_station = 2e10;
    delta_t = 2000;
    
    % Construction de la matrice pour le schéma transitoire 1
    for i = 1:nbr
        if i == 1
            matrix(i, i) = 1; % Condition aux limites de Neumann modifiée
        elseif i == nbr
            matrix(i, i) = 1; % Condition de Dirichlet à la surface
        else
            matrix(i, i-1) = -Deff;
            matrix(i, i) = 2*Deff + (delta_r^2)/delta_t; % Terme de dérivée temporelle ajouté
            matrix(i, i+1) = -Deff;
        end
    end

    % Initialisation de b pour t=0 avec des conditions aux limites
    b(1) = 0; % Condition de Neumann à l'interface pilier-air
    b(nbr) = Ce; % Condition de Dirichlet à la surface du pilier

    % Boucle temporelle
    while t < t_station
        for i = 2:nbr-1
            b(i) = C(i) * (delta_r^2)/delta_t + S * (delta_r^2); % Mise à jour de b avec la source
        end

        C = matrix \ b; % Résolution du système à ce pas de temps

        t = t + delta_t;
    end
end



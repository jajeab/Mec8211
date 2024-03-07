function resultats = simulation_adaptative(nbr, R, Deff, Ce)
    % Paramètres initiaux
    t_initial = 0.01;
    t_final = 1e6;
    delta_t_initial = 2e3;
    facteur_augmentation = 10; % Facteur d'augmentation du temps
    nombre_augmentation = 2; % Nombre de fois que le temps est augmenté

    t = t_initial;
    delta_t = delta_t_initial;
    resultats = []; % Initialiser un tableau pour stocker les résultats


        c = 0;
        while c < nombre_augmentation + 1
            % Appel de votre fonction de calcul ici, par exemple :
            [r, C, ref] = transit_shema_2(nbr, R, Deff, Ce, delta_t, t, t_final);
            % Stockage ou traitement des résultats ici
            resultats = [resultats; t_final, C(50)]; % Exemple de stockage de temps et de la concentration au 50e nœud
            c = c+1;

        
            t_final = t_final * facteur_augmentation; % augmentation du temps
end
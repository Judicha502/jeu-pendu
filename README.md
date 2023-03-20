# jeu-pendu
projet groupe 1 TD02 L1 MIASHS
Liste des tâches

### Liste des tâches

**Conception et design du jeu**

- [x]  Définir le cahier des charges du jeu, ses règles et ses fonctionnalités.
    - cahier des charges
        1. Le joueur doit pouvoir deviner un mot aléatoire choisi par l'ordinateur.
        2. Lorsque le joueur choisit une lettre, le programme doit vérifier si la lettre est dans le mot et l'afficher dans le mot caché si elle est présente.
        3. Si la lettre choisie n'est pas dans le mot, le programme doit afficher une partie du dessin du pendu correspondant à la première erreur.
        4. Le joueur peut continuer à deviner des lettres jusqu'à ce qu'il trouve le mot ou atteigne le maximum d'erreurs autorisé.
        5. Si le joueur trouve le mot, le programme doit afficher un message de félicitations et demander si le joueur souhaite continuer ou quitter le jeu.
        6. Si le joueur atteint le maximum d'erreurs autorisé, le programme doit afficher un message de défaite et demander si le joueur souhaite continuer ou quitter le jeu.
        
        Le programme doit également permettre de  :
        
        1. recharger un autre mot à deviner
        2. proposer des indications 
        3. sauvegarder le score obtenu pour chaque partie. Le score représente le nombre de tentatives avant de retrouver le mot caché.
- [ ]  Concevoir les interfaces graphiques et les maquettes du jeu.
    - piste
        
        L'interface graphique du jeu doit contenir les éléments suivants :
        
        1. Une zone de texte pour afficher le mot caché avec des tirets pour chaque lettre non découverte.
        2. Une zone de texte pour afficher les lettres déjà devinées par le joueur.
        3. Un champ de saisie pour permettre au joueur de saisir une lettre.
        4. Un bouton "Devinez" pour valider la lettre saisie.
        5. Un dessin du pendu en fonction du nombre d'erreurs commises.
        6. Des boutons "Rejouer" et "Quitter" pour permettre au joueur de rejouer ou de quitter le jeu.
        
        L'interface graphique devra être claire et intuitive pour faciliter la prise en main du jeu. Les éléments devront être disposés de manière logique et lisible. Les couleurs utilisées devront également être choisies avec soin pour faciliter la lecture et l'utilisation du jeu.
        
- [ ]  Choisir la charte graphique du jeu.
    - c’est quoi la charte graphique du jeu ?
        
        La charte graphique d'un jeu ou d'une application désigne l'ensemble des choix graphiques qui vont définir l'apparence générale de l'interface utilisateur. Cela inclut notamment le choix des couleurs, des polices de caractères, des formes et des motifs qui vont être utilisés pour construire l'interface.
        
        Choisir une charte graphique pour un jeu est important car cela permet de donner une identité visuelle propre au jeu et de faciliter sa reconnaissance auprès des joueurs. La charte graphique doit être cohérente avec l'univers du jeu et refléter l'ambiance que l'on souhaite transmettre.
        
        Pour le jeu du pendu, la charte graphique pourrait par exemple utiliser des couleurs sombres pour évoquer le mystère et le suspense du jeu, ainsi que des formes arrondies pour apporter une touche de douceur et de convivialité. Il est important que les couleurs et les formes choisies soient en harmonie les unes avec les autres pour créer une ambiance cohérente et agréable à l'œil.
        
- [ ]  Planifier et répartir les tâches pour les différents membres de l'équipe.
    - Liste des membres du groupe 1:
        
        Lilian
        
        Evariste (chef de projet)
        
        Judicha
        
        Lounes
        

**Programmation des fonctions de base du jeu**

- [ ]  Générer un fichier contenant une liste de mots pour le jeu.
- [ ]  Écrire une fonction pour choisir un mot aléatoire dans la liste.
- [ ]  Écrire une fonction pour afficher le mot caché sous forme de tirets.
- [ ]  Écrire une fonction pour demander au joueur de saisir une lettre.
- [ ]  Écrire une fonction pour valider la lettre saisie par le joueur.
- [ ]  Si la lettre est présente dans le mot, modifier l'affichage du mot caché pour inclure la lettre à la place des tirets.
- [ ]  Si la lettre n'est pas présente dans le mot, afficher un message pour informer le joueur.
- [ ]  Écrire une fonction pour afficher les lettres déjà saisies par le joueur.

**Programmation de l'interface graphique**

- [ ]  Créer les fenêtres et les boutons nécessaires pour l'interface graphique.
- [ ]  Afficher le mot caché et les lettres déjà saisies par le joueur.
- [ ]  Créer un clavier virtuel pour que le joueur puisse saisir les lettres.
- [ ]  Programmer les interactions entre l'interface graphique et les fonctions du jeu.
- [ ]  Assurer la clarté et la propreté du code.

**Tests et débogage du jeu**

- [ ]  Tester le jeu pour s'assurer que toutes les fonctionnalités fonctionnent correctement.
- [ ]  Corriger les erreurs et les bogues détectés lors des tests.
- [ ]  Améliorer les performances du jeu.

**Déploiement du jeu sur Github**

- [ ]  Héberger le jeu sur Github.
- [ ]  Assurer la clarté et la propreté du code sur Github.
- [ ]  Documenter le code et le déploiement sur Github.

import pygame  # type: ignore
import os
import sys
from mod_loader import main as load_mods

# Initialisation de pygame
pygame.init()
pygame.display.set_caption("Re-world")

# Dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Vitesse du joueur et gravité
player_speed = 5

# Charger les assets du jeu (joueur et arrière-plan par défaut)
def load_image(path):
    try:
        if os.path.exists(path):
            return pygame.image.load(path)
        else:
            raise FileNotFoundError(f"Le fichier {path} est introuvable!")
    except Exception as e:
        print(f"Erreur lors du chargement de l'image {path}: {e}")
        sys.exit()

# Charger les assets du mod et exécuter son code dans un environnement contrôlé
def load_mod(mod_name):
    player_image = load_image('assets/player.png')
    background_image = load_image('assets/background.png')

    if mod_name is None:
        return player_image, background_image

    mod_path = os.path.join('mods', mod_name)
    mod_assets_path = os.path.join(mod_path, 'assets')
    
    if os.path.exists(mod_assets_path):
        try:
            player_mod_image = os.path.join(mod_assets_path, 'player.png')
            background_mod_image = os.path.join(mod_assets_path, 'background.png')

            if os.path.exists(player_mod_image):
                player_image = load_image(player_mod_image)

            if os.path.exists(background_mod_image):
                background_image = load_image(background_mod_image)
        except Exception as e:
            print(f"Erreur lors du chargement des assets du mod {mod_name}: {e}")

    mod_main_file = os.path.join(mod_path, 'main.py')
    if os.path.exists(mod_main_file):
        try:
            # Exécuter le code du mod dans un environnement contrôlé
            with open(mod_main_file) as file:
                mod_code = file.read()

            # Contexte limité pour l'exécution du code
            mod_context = {
                'pygame': pygame,
                'os': None,  # Interdit d'utiliser les fonctionnalités d'os
                'sys': None, # Interdit d'utiliser les fonctionnalités de sys
            }

            exec(mod_code, mod_context)
        except Exception as e:
            print(f"Erreur lors de l'exécution du mod {mod_name}: {e}")

    return player_image, background_image

# Charger les assets du mod sélectionné (ou ceux par défaut si aucun mod n'est sélectionné)
selected_mod = load_mods()
player_image, background_image = load_mod(selected_mod)

# Redimensionner le background pour qu'il occupe toute la fenêtre
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Obtenir les dimensions du joueur
player_rect = player_image.get_rect()

# Position initiale du joueur
player_x, player_y = 100, 100

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvements du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Empêcher le joueur de sortir des limites de l'écran
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_rect.width))
    player_y = min(player_y, SCREEN_HEIGHT - player_rect.height)

    # Effacer l'écran et dessiner les éléments
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Limiter la fréquence à 60 FPS
    clock.tick(60)

# Quitter pygame proprement après la fin de la boucle
pygame.quit()
sys.exit()

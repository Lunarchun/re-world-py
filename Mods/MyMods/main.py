
# Assurez-vous que la librairie est accessible en ajoutant le répertoire parent au sys.path
script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
libs_dir = os.path.join(parent_dir, 'libs')
sys.path.append(libs_dir)

# Importer la librairie
import RE_world_lib # type: ignore

# Initialisation de pygame et autres configurations via la librairie
game = RE_world_lib.Game()

# Charger les assets du mod sélectionné (ou ceux par défaut si aucun mod n'est sélectionné)
selected_mod = RE_world_lib.load_mods()  # Cette fonction doit être définie dans la librairie
player_image, background_image = game.load_mod(selected_mod)

# Redimensionner le background pour qu'il occupe toute la fenêtre
background_image = pygame.transform.scale(background_image, (game.screen_width, game.screen_height))

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
        player_x -= game.player_speed
    if keys[pygame.K_RIGHT]:
        player_x += game.player_speed

    # Empêcher le joueur de sortir des limites de l'écran
    player_x = max(0, min(player_x, game.screen_width - player_rect.width))
    player_y = min(player_y, game.screen_height - player_rect.height)

    # Effacer l'écran et dessiner les éléments
    game.screen.fill((0, 0, 0))
    game.screen.blit(background_image, (0, 0))
    game.screen.blit(player_image, (player_x, player_y))

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Limiter la fréquence à 60 FPS
    clock.tick(60)

# Quitter pygame proprement après la fin de la boucle
pygame.quit()
sys.exit()

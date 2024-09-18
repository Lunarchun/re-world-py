import pygame  # type: ignore
import os
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre de sélection des mods
MOD_LOADER_WIDTH = 400
MOD_LOADER_HEIGHT = 300
mod_loader_screen = pygame.display.set_mode((MOD_LOADER_WIDTH, MOD_LOADER_HEIGHT))
pygame.display.set_caption("MOD Loader")

# Charger une police pour le texte
font = pygame.font.SysFont(None, 36)

def set_icon():
    try:
        icon = pygame.image.load('assets/icon.png')  # Charge l'image d'icône
        pygame.display.set_icon(icon)  # Applique l'icône à la fenêtre
    except FileNotFoundError:
        print("Le fichier d'icône est introuvable.")

def draw_mod_loader(mods):
    mod_loader_screen.fill((200, 200, 200))  # Couleur de fond

    # Afficher le texte en haut
    text = font.render("Sélectionner un mod :", True, (0, 0, 0))
    mod_loader_screen.blit(text, (10, 10))

    # Afficher les boutons pour chaque mod
    button_height = 40

    # Ajouter une option par défaut
    pygame.draw.rect(mod_loader_screen, (0, 0, 255), (10, 50, MOD_LOADER_WIDTH - 20, button_height))
    mod_text = font.render("Par défaut", True, (255, 255, 255))
    mod_loader_screen.blit(mod_text, (20, 55))

    for i, mod in enumerate(mods):
        pygame.draw.rect(mod_loader_screen, (0, 0, 255), (10, 100 + i * (button_height + 10), MOD_LOADER_WIDTH - 20, button_height))
        mod_text = font.render(mod, True, (255, 255, 255))
        mod_loader_screen.blit(mod_text, (20, 105 + i * (button_height + 10)))

    pygame.display.flip()

def get_mods_list(mods_folder='mods'):
    mods = []
    if os.path.exists(mods_folder) and os.path.isdir(mods_folder):
        for mod in os.listdir(mods_folder):
            mod_path = os.path.join(mods_folder, mod)
            if os.path.isdir(mod_path):
                mods.append(mod)
    return mods

def main():
    set_icon()  # Définir l'icône avant de dessiner les mods
    mods = get_mods_list()
    selected_mod = None

    running = True
    while running:
        draw_mod_loader(mods)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                button_height = 40

                # Vérifier si "Par défaut" a été cliqué
                if 10 <= x <= MOD_LOADER_WIDTH - 10 and 50 <= y <= 50 + button_height:
                    selected_mod = None  # Aucune mod sélectionnée
                    running = False
                    break

                # Vérifier si un mod a été cliqué
                for i, mod in enumerate(mods):
                    if 10 <= x <= MOD_LOADER_WIDTH - 10 and 100 + i * (button_height + 10) <= y <= 100 + i * (button_height + 10) + button_height:
                        selected_mod = mod
                        running = False
                        break

    return selected_mod

if __name__ == "__main__":
    selected_mod = main()
    pygame.quit()
    sys.exit()

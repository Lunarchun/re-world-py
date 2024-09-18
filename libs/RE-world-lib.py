import pygame # type: ignore

class Game:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Re-world MODDED")
        self.clock = pygame.time.Clock()
        self.player_speed = 5
        self.player_image = None
        self.background_image = None

    def load_image(self, path):
        if pygame.image.get_extended():
            try:
                return pygame.image.load(path)
            except FileNotFoundError:
                print(f"Le fichier {path} est introuvable!")
                raise
        else:
            raise RuntimeError("Le support des images étendues n'est pas disponible.")

    def set_icon(self, icon_path='assets/icon.png'):
        try:
            icon = self.load_image(icon_path)
            pygame.display.set_icon(icon)
        except FileNotFoundError:
            print("Le fichier d'icône est introuvable.")

    def load_mod_assets(self):
        self.player_image = self.load_image('assets/player.png')
        self.background_image = self.load_image('assets/background.png')

    def run(self):
        self.set_icon()
        self.load_mod_assets()

        if self.background_image:
            self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        player_rect = self.player_image.get_rect()
        player_x, player_y = 100, 100

        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.player_image, (player_x, player_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player_y -= self.player_speed
            if keys[pygame.K_DOWN]:
                player_y += self.player_speed
            if keys[pygame.K_LEFT]:
                player_x -= self.player_speed
            if keys[pygame.K_RIGHT]:
                player_x += self.player_speed

            player_x = max(0, min(player_x, self.screen_width - player_rect.width))
            player_y = max(0, min(player_y, self.screen_height - player_rect.height))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

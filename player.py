from setting import*

class player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('image','chopper.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-30,0)
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self,dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")
        self.rect.center = self.hitbox_rect.center

    def collision (self,direction):
        for sprites in self.collision_sprites:
            if sprites.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprites.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprites.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprites.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprites.rect.top

    def update(self, dt):
        self.input()
        self.move(dt)
        

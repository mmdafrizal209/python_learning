import pygame
import random
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
lebar_layar = 400
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption('Game Balap Mobil')

# Warna
hitam = (0, 0, 0)
putih = (255, 255, 255)
merah = (255, 0, 0)
hijau = (0, 255, 0)

# Mobil pemain
mobil_pemain = pygame.Rect(lebar_layar // 2 - 25, tinggi_layar - 100, 50, 100)

# Mobil musuh
mobil_musuh_width = 50
mobil_musuh_height = 100
mobil_musuh_speed = 5
mobil_musuh = pygame.Rect(random.randint(0, lebar_layar - mobil_musuh_width), -mobil_musuh_height, mobil_musuh_width, mobil_musuh_height)

# Skor
skor = 0
font = pygame.font.Font(None, 36)

# Loop utama game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kontrol mobil pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mobil_pemain.left > 0:
        mobil_pemain.x -= 5
    if keys[pygame.K_RIGHT] and mobil_pemain.right < lebar_layar:
        mobil_pemain.x += 5

    # Gerakan mobil musuh
    mobil_musuh.y += mobil_musuh_speed
    if mobil_musuh.top > tinggi_layar:
        mobil_musuh.x = random.randint(0, lebar_layar - mobil_musuh_width)
        mobil_musuh.y = -mobil_musuh_height
        skor += 1  # Tambah skor saat mobil musuh melewati

    # Tabrakan
    if mobil_pemain.colliderect(mobil_musuh):
        print("Game Over! Skor Anda:", skor)
        pygame.quit()
        sys.exit()

    # Gambar objek
    layar.fill(hitam)
    pygame.draw.rect(layar, hijau, mobil_pemain)  # Mobil pemain
    pygame.draw.rect(layar, merah, mobil_musuh)   # Mobil musuh

    # Tampilkan skor
    skor_text = font.render(f"Skor: {skor}", True, putih)
    layar.blit(skor_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(30)
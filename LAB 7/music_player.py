import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

music_folder = "music"
music_files = sorted([f for f in os.listdir(music_folder) if f.endswith(".mp3")])
num_songs = len(music_files)
current_song = 0
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song]))

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % num_songs
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song]))
    pygame.mixer.music.play()

def prev_song():
    global current_song
    current_song = (current_song - 1) % num_songs
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_song]))
    pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_song()
                else:
                    play_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                prev_song()
    
    screen.fill((255, 255, 255))
    song_text = music_files[current_song]
    song_label = font.render(song_text, True, (0, 0, 0))
    screen.blit(song_label, (screen_width//2 - song_label.get_width()//2, screen_height//2 - song_label.get_height()//2))
    pygame.display.update()
    
    clock.tick(30)

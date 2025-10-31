import pygame
import pygame_gui
import random

pygame.init()
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Угадай число 🎯")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Элементы интерфейса
input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((20, 100), (200, 30)), manager=manager)
submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((230, 100), (100, 30)), text='Проверить', manager=manager)
output_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 150), (400, 30)), text='', manager=manager)

# Логика игры
secret = random.randint(1, 100)
attempts = 0

running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == submit_button:
            guess_text = input_box.get_text()
            try:
                guess = int(guess_text)
                attempts += 1
                if guess < secret:
                    output_label.set_text("📉 Слишком маленькое число.")
                elif guess > secret:
                    output_label.set_text("📈 Слишком большое число.")
                else:
                    output_label.set_text(f"🎉 Угадал {secret} за {attempts} попыток!")
            except ValueError:
                output_label.set_text("⚠️ Введи целое число!")

        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((240, 240, 255))
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()
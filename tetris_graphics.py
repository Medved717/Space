import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
SIDEBAR_WIDTH = 200
FULL_WIDTH = SCREEN_WIDTH + SIDEBAR_WIDTH

# Цвета (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Цвета фигур
COLORS = [
    (0, 255, 255),  # I - Циан
    (255, 255, 0),  # O - Желтый
    (128, 0, 128),  # T - Пурпурный
    (255, 165, 0),  # L - Оранжевый
    (0, 0, 255),  # J - Синий
    (0, 255, 0),  # S - Зеленый
    (255, 0, 0)  # Z - Красный
]

# Формы фигур
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]


class Piece:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0

    def rotate(self):
        # Поворот фигуры на 90 градусов
        rotated = list(zip(*self.shape[::-1]))
        return [list(row) for row in rotated]

    def get_rotated_shape(self):
        shape = self.shape
        for _ in range(self.rotation):
            shape = list(zip(*shape[::-1]))
            shape = [list(row) for row in shape]
        return shape


class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((FULL_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Тетрис")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.big_font = pygame.font.Font(None, 48)

        self.reset_game()

    def reset_game(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.score = 0
        self.lines = 0
        self.level = 1
        self.game_over = False
        self.fall_speed = 500  # миллисекунды
        self.last_fall = pygame.time.get_ticks()
        self.particles = []  # Эффекты частиц

    def new_piece(self):
        idx = random.randint(0, len(SHAPES) - 1)
        shape = [row[:] for row in SHAPES[idx]]
        color = COLORS[idx]
        x = GRID_WIDTH // 2 - len(shape[0]) // 2
        return Piece(x, 0, shape, color)

    def check_collision(self, piece, dx=0, dy=0):
        shape = piece.get_rotated_shape()
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = piece.x + x + dx
                    grid_y = piece.y + y + dy
                    if (grid_x < 0 or grid_x >= GRID_WIDTH or
                            grid_y >= GRID_HEIGHT or
                            (grid_y >= 0 and self.grid[grid_y][grid_x])):
                        return True
        return False

    def merge_piece(self):
        shape = self.current_piece.get_rotated_shape()
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = self.current_piece.x + x
                    grid_y = self.current_piece.y + y
                    if 0 <= grid_y < GRID_HEIGHT:
                        self.grid[grid_y][grid_x] = self.current_piece.color

        # Добавить эффект частиц при закреплении
        self.add_particles()

        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()

        if self.check_collision(self.current_piece):
            self.game_over = True

    def add_particles(self):
        # Эффект вспышки при закреплении фигуры
        for _ in range(20):
            self.particles.append({
                'x': self.current_piece.x * BLOCK_SIZE + random.randint(0, BLOCK_SIZE),
                'y': self.current_piece.y * BLOCK_SIZE + random.randint(0, BLOCK_SIZE),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-5, -1),
                'life': 30,
                'color': self.current_piece.color
            })

    def clear_lines(self):
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * GRID_WIDTH)
                lines_cleared += 1
            else:
                y -= 1

        if lines_cleared > 0:
            self.lines += lines_cleared
            # Подсчёт очков
            scores = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += scores.get(lines_cleared, 100)

            # Повышение уровня каждые 10 линий
            self.level = 1 + self.lines // 10
            self.fall_speed = max(100, 500 - (self.level - 1) * 40)

            # Анимация исчезновения линий
            pygame.time.wait(50)

    def move_left(self):
        if not self.check_collision(self.current_piece, -1, 0):
            self.current_piece.x -= 1

    def move_right(self):
        if not self.check_collision(self.current_piece, 1, 0):
            self.current_piece.x += 1

    def move_down(self):
        if not self.check_collision(self.current_piece, 0, 1):
            self.current_piece.y += 1
            return True
        else:
            self.merge_piece()
            return False

    def rotate_piece(self):
        old_rotation = self.current_piece.rotation
        self.current_piece.rotation = (self.current_piece.rotation + 1) % 4
        if self.check_collision(self.current_piece):
            self.current_piece.rotation = old_rotation

    def hard_drop(self):
        while not self.check_collision(self.current_piece, 0, 1):
            self.current_piece.y += 1
        self.merge_piece()

    def draw_grid(self):
        # Отрисовка сетки
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x], rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 1)
                else:
                    pygame.draw.rect(self.screen, DARK_GRAY, rect, 1)

    def draw_piece(self, piece, offset_x=0, offset_y=0):
        shape = piece.get_rotated_shape()
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        offset_x + (piece.x + x) * BLOCK_SIZE,
                        offset_y + (piece.y + y) * BLOCK_SIZE,
                        BLOCK_SIZE - 1, BLOCK_SIZE - 1
                    )
                    pygame.draw.rect(self.screen, piece.color, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_next_piece(self):
        # Заголовок
        title = self.font.render("Следующая:", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH + 20, 50))

        # Рисуем следующую фигуру
        shape = self.next_piece.shape
        block_size_small = 25
        start_x = SCREEN_WIDTH + (SIDEBAR_WIDTH - len(shape[0]) * block_size_small) // 2
        start_y = 100

        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        start_x + x * block_size_small,
                        start_y + y * block_size_small,
                        block_size_small - 1, block_size_small - 1
                    )
                    pygame.draw.rect(self.screen, self.next_piece.color, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_score(self):
        # Счёт
        score_text = self.font.render(f"Счёт: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH + 20, 200))

        # Линии
        lines_text = self.small_font.render(f"Линии: {self.lines}", True, WHITE)
        self.screen.blit(lines_text, (SCREEN_WIDTH + 20, 250))

        # Уровень
        level_text = self.small_font.render(f"Уровень: {self.level}", True, WHITE)
        self.screen.blit(level_text, (SCREEN_WIDTH + 20, 280))

        # Скорость
        speed_text = self.small_font.render(f"Скорость: {int(500 / self.fall_speed)}", True, WHITE)
        self.screen.blit(speed_text, (SCREEN_WIDTH + 20, 310))

    def draw_controls(self):
        controls = [
            "Управление:",
            "← → - движение",
            "↑ - поворот",
            "↓ - ускорение",
            "Пробел - вниз",
            "R - новая игра"
        ]

        y = 380
        for line in controls:
            text = self.small_font.render(line, True, GRAY)
            self.screen.blit(text, (SCREEN_WIDTH + 20, y))
            y += 25

    def draw_particles(self):
        for particle in self.particles[:]:
            pygame.draw.circle(self.screen, particle['color'],
                               (int(particle['x']), int(particle['y'])), 2)
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            if particle['life'] <= 0:
                self.particles.remove(particle)

    def draw_game_over(self):
        if self.game_over:
            overlay = pygame.Surface((FULL_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            # Текст GAME OVER
            text1 = self.big_font.render("GAME OVER", True, WHITE)
            text1_rect = text1.get_rect(center=(FULL_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(text1, text1_rect)

            # Финальный счёт
            text2 = self.font.render(f"Счёт: {self.score}", True, WHITE)
            text2_rect = text2.get_rect(center=(FULL_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text2, text2_rect)

            # Инструкция
            text3 = self.small_font.render("Нажми R для новой игры", True, GRAY)
            text3_rect = text3.get_rect(center=(FULL_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(text3, text3_rect)

    def run(self):
        running = True
        while running:
            current_time = pygame.time.get_ticks()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if not self.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.move_left()
                        elif event.key == pygame.K_RIGHT:
                            self.move_right()
                        elif event.key == pygame.K_DOWN:
                            self.move_down()
                        elif event.key == pygame.K_UP:
                            self.rotate_piece()
                        elif event.key == pygame.K_SPACE:
                            self.hard_drop()
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.reset_game()

            # Автоматическое падение
            if not self.game_over and current_time - self.last_fall > self.fall_speed:
                self.move_down()
                self.last_fall = current_time

            # Отрисовка
            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_piece(self.current_piece)
            self.draw_next_piece()
            self.draw_score()
            self.draw_controls()
            self.draw_particles()
            self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Tetris()
    game.run()
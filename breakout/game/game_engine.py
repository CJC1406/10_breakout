
"""
GameEngine: owns the paddle, ball, and bricks.

Task 1: Remove destroyed bricks.
Task 2: Lives, game over, and restart.
Task 3: Normal, strong, and unbreakable bricks.
Task 4: Score and combo multiplier.
"""

import pygame

from game.paddle import Paddle
from game.ball import Ball
from game.brick import Brick
from game.collision import handle_ball_brick_collision
from game.renderer import WIDTH, HEIGHT

BRICK_ROWS = 4
BRICK_COLS = 8
BRICK_WIDTH = 68
BRICK_HEIGHT = 22
BRICK_GAP = 6
BRICK_TOP_MARGIN = 50

STARTING_LIVES = 3
POINTS_PER_BRICK = 10


class GameEngine:
    def __init__(self):
        self.lives = STARTING_LIVES
        self.game_over = False
        self.score = 0
        self.combo_multiplier = 1
        self._reset_game()

    def _reset_game(self):
        self.paddle = Paddle(x=WIDTH / 2, y=HEIGHT - 30)
        self.ball = Ball(x=WIDTH / 2, y=HEIGHT - 50)
        self.bricks = self._build_bricks()

    def _build_bricks(self):
        bricks = []

        total_width = (
            BRICK_COLS * (BRICK_WIDTH + BRICK_GAP) - BRICK_GAP
        )
        start_x = (WIDTH - total_width) / 2

        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = start_x + col * (BRICK_WIDTH + BRICK_GAP)
                y = BRICK_TOP_MARGIN + row * (
                    BRICK_HEIGHT + BRICK_GAP
                )

                if row == 0 and col % 3 == 0:
                    brick_type = Brick.UNBREAKABLE
                elif (row + col) % 3 == 0:
                    brick_type = Brick.STRONG
                else:
                    brick_type = Brick.NORMAL

                bricks.append(
                    Brick(
                        x,
                        y,
                        BRICK_WIDTH,
                        BRICK_HEIGHT,
                        brick_type=brick_type,
                    )
                )

        return bricks

    def _reset_ball(self):
        self.ball = Ball(x=WIDTH / 2, y=HEIGHT - 50)

    def handle_input(self, keys_pressed):
        if self.game_over:
            return

        dx = 0

        if keys_pressed[pygame.K_LEFT]:
            dx -= self.paddle.speed

        if keys_pressed[pygame.K_RIGHT]:
            dx += self.paddle.speed

        self.paddle.move(dx, WIDTH)

    def handle_keydown(self, key):
        if self.game_over and key == pygame.K_r:
            self.lives = STARTING_LIVES
            self.game_over = False
            self.score = 0
            self.combo_multiplier = 1
            self._reset_game()

    def update(self):
        if self.game_over:
            return

        self.ball.update()
        self.ball.bounce_off_walls(WIDTH)

        if (
            self.ball.get_rect().colliderect(self.paddle.get_rect())
            and self.ball.vy > 0
        ):
            self.ball.bounce_off_paddle(self.paddle.get_rect())

        # Handle one brick collision per update.
        for brick in self.bricks[:]:
            if handle_ball_brick_collision(self.ball, brick):
                destroyed = brick.take_hit()

                if destroyed:
                    self.bricks.remove(brick)

                    # Award points using the current multiplier.
                    self.score += (
                        POINTS_PER_BRICK * self.combo_multiplier
                    )

                    # Increase the multiplier for the next destroyed brick.
                    self.combo_multiplier += 1

                break

        # Losing the ball resets the combo.
        if self.ball.is_below(HEIGHT):
            self.lives -= 1
            self.combo_multiplier = 1

            if self.lives <= 0:
                self.lives = 0
                self.game_over = True
            else:
                self._reset_ball()

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(
            surface,
            self.paddle,
            self.ball,
            self.bricks,
        )

        renderer.draw_text(
            surface,
            font,
            f"Bricks left: {len(self.bricks)}",
            (10, 10),
        )

        renderer.draw_text(
            surface,
            font,
            f"Lives: {self.lives}",
            (10, 35),
        )

        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}",
            (10, 60),
        )

        renderer.draw_text(
            surface,
            font,
            f"Combo multiplier: x{self.combo_multiplier}",
            (10, 85),
        )

        if self.game_over:
            renderer.draw_banner(
                surface,
                font,
                "GAME OVER - Press R to Restart",
            )

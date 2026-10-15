
"""
Brick: represents a normal, strong, or unbreakable block.
"""

import pygame


class Brick:
    NORMAL = "normal"
    STRONG = "strong"
    UNBREAKABLE = "unbreakable"

    COLORS = {
        NORMAL: (200, 90, 90),
        STRONG: (230, 150, 50),
        UNBREAKABLE: (120, 125, 135),
    }

    def __init__(
        self,
        x,
        y,
        width,
        height,
        hits_remaining=None,
        color=None,
        brick_type=NORMAL,
    ):
        if brick_type not in (
            self.NORMAL,
            self.STRONG,
            self.UNBREAKABLE,
        ):
            raise ValueError(f"Unknown brick type: {brick_type}")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.brick_type = brick_type

        if brick_type == self.UNBREAKABLE:
            self.hits_remaining = float("inf")
        elif hits_remaining is not None:
            self.hits_remaining = hits_remaining
        elif brick_type == self.STRONG:
            self.hits_remaining = 3
        else:
            self.hits_remaining = 1

        self.color = color or self.COLORS[brick_type]

    def get_rect(self):
        return pygame.Rect(
            int(self.x),
            int(self.y),
            self.width,
            self.height,
        )

    def take_hit(self):
        """Apply a hit and return True if this brick is destroyed."""
        if self.brick_type == self.UNBREAKABLE:
            return False

        self.hits_remaining -= 1
        return self.hits_remaining <= 0

    def get_color(self):
        """Show the strong brick's remaining durability visually."""
        if self.brick_type == self.STRONG:
            if self.hits_remaining == 3:
                return (230, 150, 50)
            if self.hits_remaining == 2:
                return (220, 110, 40)
            return (190, 70, 35)

        return self.color

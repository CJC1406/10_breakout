# Breakout Lab — Pygame

A Breakout/Brick Breaker game built using **Python and Pygame**. This project demonstrates collision detection, object-oriented programming, game state management, multiple brick types, lives, and combo scoring.

**Repository:** [CJC1406/10_breakout](https://github.com/CJC1406/10_breakout)

## Features Implemented

- **Paddle movement:** Control the paddle using the left and right arrow keys.
- **Ball physics:** The ball bounces off walls, the paddle, and bricks.
- **Brick collision fix:** Bricks are removed when their remaining hits reach zero.
- **Lives system:** Start with three lives. Losing the ball reduces the remaining lives.
- **Game over and restart:** The game ends when all lives are lost. Press `R` to restart.
- **Multiple brick types:** Normal, strong, and unbreakable bricks have distinct appearances and behaviors.
- **Combo scoring:** Destroying bricks consecutively increases the score multiplier.
- **Combo reset:** Missing the ball resets the multiplier to `x1`.
- **Live status display:** View the remaining bricks, lives, score, and current combo multiplier.

## Requirements

- Python 3.10 or later
- Pygame 2.5.0 or later

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/CJC1406/10_breakout.git
cd 10_breakout
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
pygame>=2.5.0
```

Then install the dependency:

```bash
python -m pip install -r requirements.txt
```

If the original Pygame package fails to install in your Python environment, you can try Pygame Community Edition:

```bash
python -m pip install pygame-ce
```

### 4. Run the game

```bash
python main.py
```

## Controls

| Key         | Action                  |
| ----------- | ----------------------- |
| Left Arrow  | Move the paddle left    |
| Right Arrow | Move the paddle right   |
| `R`         | Restart after game over |

## Implementation Details

### Task 1 — Ball–Brick Collision

**Problem:** Bricks remained on the board even after their hit counts were exhausted.

**Solution:** The game engine checks each brick's remaining hits and removes it from the brick list when its durability reaches zero.

[View collision-fix demonstration](https://github.com/user-attachments/assets/f0c5b7a2-4a9d-46d1-88db-0239ff42c5e0)

### Task 2 — Lives and Game Over

**Implementation:**

- The player starts with three lives.
- Missing the ball reduces the remaining lives by one.
- The ball resets while lives remain.
- The game displays a game-over message after the third miss.
- Pressing `R` starts a new game.

[View lives and game-over demonstration](https://github.com/user-attachments/assets/06170720-541b-461f-8359-d077d2a70657)

### Task 3 — Different Brick Types

Three brick types are implemented:

| Brick type  | Behavior                                  |
| ----------- | ----------------------------------------- |
| Normal      | Destroyed after one hit                   |
| Strong      | Requires multiple hits before destruction |
| Unbreakable | Remains on the board regardless of hits   |

Each type has a distinct appearance. Strong bricks change color as their durability decreases.

[View brick-types demonstration](https://github.com/user-attachments/assets/b003f387-466a-45f2-9f69-0b0dde497223)

### Task 4 — Combo Scoring

**Implementation:**

- Destroying a brick awards points.
- Consecutive brick destructions increase the combo multiplier.
- Each subsequent destroyed brick awards more points.
- Missing the ball resets the multiplier to `x1`.
- The score and multiplier are displayed on the screen.

[View combo-scoring demonstration](https://github.com/user-attachments/assets/24372b5b-e0fb-4f06-a8a5-19658617fc5c)

## Gameplay Recordings

The following recordings demonstrate the game before and after the changes.

- **Before:** Original gameplay showing the brick-collision bug.
- **After:** Updated gameplay demonstrating the completed features.

If the recordings are stored in a `videos/` directory in the repository, use these links:

- [Before gameplay](

https://github.com/user-attachments/assets/e5a22d47-c183-4c2e-bf18-0b76cc694673

)
- [After gameplay](

https://github.com/user-attachments/assets/91e95672-c811-4a01-9501-5035b0929661

)

Update these paths if your uploaded video files are stored elsewhere in the repository.

## Project Structure

```text
10_breakout/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── paddle.py
│   ├── ball.py
│   ├── brick.py
│   ├── collision.py
│   └── renderer.py
└── README.md
```

## Testing Checklist

- [x] Bricks disappear when their hit points are exhausted.
- [x] Normal bricks are destroyed after one hit.
- [x] Strong bricks require multiple hits.
- [x] Unbreakable bricks remain on the board.
- [x] Losing the ball reduces the number of lives.
- [x] The game ends after all three lives are lost.
- [x] Pressing `R` restarts the game.
- [x] Destroying consecutive bricks increases the score multiplier.
- [x] Missing the ball resets the multiplier.
- [x] The score, multiplier, lives, and bricks-left counter are displayed correctly.

## Git Commit History

Each task was committed separately:

| Commit    | Description                                |
| --------- | ------------------------------------------ |
| `bc579a5` | Fix ball-brick collision removal           |
| `4cd9361` | Add lives, game over, and restart          |
| `ffe2b86` | Add normal, strong, and unbreakable bricks |
| `a46a6ed` | Add combo scoring and multiplier           |

[View all commits](https://github.com/CJC1406/10_breakout/commits/main)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Configuration
NUM_BALLS = 6
RADIUS = 5
WIDTH, HEIGHT = 10, 10
BALL_RADIUS = 0.2
CORD_LENGTH = 1  # Not enforced spatially, just conceptual
TIME_STEPS = 500

# Initialize ball states
balls = []
for _ in range(NUM_BALLS):
    angle = random.uniform(0, 2 * np.pi)
    speed = 0.1
    vx = speed * np.cos(angle)
    vy = speed * np.sin(angle)
    x = RADIUS * np.cos(angle)
    y = RADIUS * np.sin(angle)
    balls.append({
        'pos': np.array([x, y]),
        'vel': np.array([vx, vy]),
        'cords': 1,
        'alive': True
    })

# Function to update ball positions and simulate rules
def update_positions():
    for i, ball in enumerate(balls):
        if not ball['alive']:
            continue

        # Move ball
        ball['pos'] += ball['vel']

        # Bounce on circle wall
        if np.linalg.norm(ball['pos']) >= RADIUS - BALL_RADIUS:
            normal = ball['pos'] / np.linalg.norm(ball['pos'])
            ball['vel'] -= 2 * np.dot(ball['vel'], normal) * normal
            ball['cords'] += 1  # Gain a cord on bounce

    # Check for cord crossings and apply cut rule
    for i, ball1 in enumerate(balls):
        if not ball1['alive']:
            continue
        for j, ball2 in enumerate(balls):
            if i != j and ball2['alive']:
                # Random chance of crossing
                if np.random.rand() < 0.05:
                    ball2['cords'] -= 1
                    if ball2['cords'] <= 0:
                        ball2['alive'] = False

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-WIDTH / 2, WIDTH / 2)
ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
circle = plt.Circle((0, 0), RADIUS, fill=False)
ax.add_artist(circle)
ball_artists = [plt.Circle((0, 0), BALL_RADIUS, color='blue') for _ in range(NUM_BALLS)]
for artist in ball_artists:
    ax.add_patch(artist)

# Animation update function
def animate(frame):
    update_positions()
    for i, ball in enumerate(balls):
        if ball['alive']:
            ball_artists[i].center = ball['pos']
            ball_artists[i].set_color('blue')
        else:
            ball_artists[i].set_color('red')
            ball_artists[i].center = (-100, -100)  # Hide

    return ball_artists

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=TIME_STEPS, interval=50, blit=True)
plt.close(fig)
ani.save("EulerP/cord_cutting_balls_simulation.gif", writer='pillow')
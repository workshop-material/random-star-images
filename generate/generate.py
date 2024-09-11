import numpy as np
import matplotlib.pyplot as plt

width, height = 1024, 1024
num_stars_min, num_stars_max = 200, 600
num_images = 20


def random_star_color():
    colors = [
        (1.0, 1.0, 1.0),  # white
        (1.0, 0.9, 0.8),  # Warm white
        (0.9, 0.8, 0.7),  # Yellowish
        (0.8, 0.8, 1.0),  # Cool blue
        (1.0, 0.8, 0.8),  # Slightly reddish
    ]
    return colors[np.random.randint(0, len(colors))]


for image_index in range(num_images):
    # create a black canvas with 3 color channels (r, g, b)
    image = np.zeros((width, height, 3))

    num_stars = np.random.randint(num_stars_min, num_stars_max)

    # random positions for stars
    x_positions = np.random.randint(0, width, num_stars)
    y_positions = np.random.randint(0, height, num_stars)

    # random star sizes
    sizes = np.random.uniform(0.5, 3.0, num_stars)

    # create the starry sky
    for x, y, s in zip(x_positions, y_positions, sizes):
        color = random_star_color()
        for i in range(3):  # apply color to each channel (r, g, b)
            image[
                max(0, y - int(s)) : min(height, y + int(s)),
                max(0, x - int(s)) : min(width, x + int(s)),
                i,
            ] += color[i]

    # clip pixel values to valid range (0, 1)
    image = np.clip(image, 0, 1)

    # generate and save the image
    plt.figure(figsize=(6, 6))
    plt.axis("off")
    plt.imsave(f"stars-{image_index:03}.png", image, dpi=300)

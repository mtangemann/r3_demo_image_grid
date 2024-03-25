"""Displays a grid of images."""

import matplotlib.pyplot as plt
import numpy as np


def save_image_grid(output_file: str, images: np.ndarray, labels: np.ndarray) -> None:
    """Saves a grid of images to a file.

    Args:
        output_file: The file to save the image grid to.
        images: A numpy array of shape (num_images, height, width, num_channels).
        labels: A numpy array of shape (num_images,) containing the labels for each image.
    """
    plt.figure(figsize=(5, 5))
    num_images = images.shape[0]
    grid_size = int(np.ceil(np.sqrt(num_images)))
    for i in range(num_images):
        plt.subplot(grid_size, grid_size, i + 1)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.axis("off")
        plt.title(f"Predicted: {labels[i]}")
    plt.savefig(output_file)
    plt.close()

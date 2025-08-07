import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def display_npy_animation():
    # ==== MANUAL PARAMETERS ====
    folder_path = '../depth_map'   # <- Change this
    start_idx = 30
    end_idx = 90
    colormap = 'viridis'
    interval = 100  # milliseconds per frame
    # ===========================

    file_list = [os.path.join(folder_path, f"{i:06d}_depth.npy") for i in range(start_idx, end_idx + 1)]
    file_list = [f for f in file_list if os.path.exists(f)]

    if not file_list:
        print("No valid .npy files found in the given range.")
        return

    # Load first image to initialize
    first_depth = np.load(file_list[0])
    first_depth = np.squeeze(first_depth)  # Remove dimensions of size 1
    norm_first = (first_depth - np.min(first_depth)) / (np.max(first_depth) - np.min(first_depth) + 1e-8)

    fig, ax = plt.subplots()
    im = ax.imshow(norm_first, cmap=colormap)
    ax.set_title(f"Frame {start_idx}")
    plt.axis('off')

    def update(frame_idx):
        depth = np.load(file_list[frame_idx])
        depth = np.squeeze(depth) 
        print("Depth shape after squeeze:", depth.shape)
        norm_depth = (depth - np.min(depth)) / (np.max(depth) - np.min(depth) + 1e-8)
        im.set_array(norm_depth)
        ax.set_title(f"Frame {start_idx + frame_idx}")
        return [im]

    ani = animation.FuncAnimation(
        fig, update, frames=len(file_list), interval=interval, blit=True, repeat=True
    )

    plt.show()

if __name__ == '__main__':
    display_npy_animation()

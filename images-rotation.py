from PIL import Image

# Load the images
image1 = Image.open('C:\\Users\\Nitheesh kumar\\PycharmProjects\\images-rotation-folder\\image1.png').convert("RGBA")
image2 = Image.open('C:\\Users\\Nitheesh kumar\\PycharmProjects\\images-rotation-folder\\image2.png').convert("RGBA")
image3 = Image.open('C:\\Users\\Nitheesh kumar\\PycharmProjects\\images-rotation-folder\\image3.png').convert("RGBA")
image4 = Image.open('C:\\Users\\Nitheesh kumar\\PycharmProjects\\images-rotation-folder\\image4.png').convert("RGBA")

# Resize images for consistent sizes
size = (650, 650)  # Set a standard size for all images
image1 = image1.resize(size)

# Resize image2 to be slightly bigger than image1
image2_size = (650, 650)  # Slightly larger size for image2
image2 = image2.resize(image2_size)

# Resize image3 to fit inside image1 and image2
image3_size = (300, 350)  # Adjusted size for image3 to fit in the center
image3 = image3.resize(image3_size)

# Resize image4 to fit inside image3
image4_size = (150, 150)  # Adjusted size for image4
image4 = image4.resize(image4_size)

# Number of frames and rotation settings
num_frames = 60  # Total frames in the GIF
rotation_angle_per_frame = 360 / num_frames

# Create frames for the GIF
frames = []
for frame_index in range(num_frames):
    # Rotate image1 and image2 simultaneously
    rotated_image1 = image1.rotate(-rotation_angle_per_frame * frame_index, expand=False)
    rotated_image2 = image2.rotate(-rotation_angle_per_frame * frame_index, expand=False)

    # Composite image2 on top of image1
    combined = Image.alpha_composite(rotated_image1, rotated_image2)

    # Paste image3 in the center of the combined image
    combined.paste(image3, (175, 150), image3)

    # Flip image4 horizontally every alternate frame and paste it in the center of image3
    if frame_index % 2 == 0:
        flipped_image4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        flipped_image4 = image4
    combined.paste(flipped_image4, (250, 230), flipped_image4)

    # Append the frame to the list
    frames.append(combined)

# Save the GIF with disposal=2 and expand=False
output_gif_path = "C:\\Users\\Nitheesh kumar\\PycharmProjects\\images-rotation-folder\\image-rotation.gif"
frames[0].save(
    output_gif_path,
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=100,
    loop=0,
    disposal=2  # Prevent frame expansion
)

print(output_gif_path)

from PIL import Image
import os

fps = 10
duration = 2
angle_per_frame =  360 // (fps * duration)

image_path = "C:\\Users\\Nitheesh kumar\\PycharmProjects\\turtleproject\\Prabodh-Technologies-LLP-FINAL_0000s_0001s_0000s_0000_Group-4.png"
file_path = os.path.join(image_path)
image = Image.open(file_path)
output_path = "rotating_gear.gif"
frames = []

for i in range(fps * duration):
    angle = ( i * angle_per_frame)
    rotated_frame = image.rotate(-angle)

    frames.append(rotated_frame)

if frames:
    frames[0].save(
        output_path,
        save_all = True,
        append_images = frames[1:],
        duration = 700 // fps,
        loop = 0,
        disposal = 2
        )

print(output_path)

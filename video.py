from moviepy.editor import VideoFileClip
import os
from natsort import natsorted

folder_path = "С:\\PATH\\"
output_file = "output.txt"  # Specify the name of the output text file

# Get a list of all MKV files in the folder and sort them naturally
mkv_files = natsorted([file for file in os.listdir(folder_path) if file.endswith(".mkv")])

total_duration = 0

# Open the output file in write mode
with open(output_file, "w") as output:
    # Loop through each MKV file
    for file_index, file_name in enumerate(mkv_files):
        # Create the full file path
        file_path = os.path.join(folder_path, file_name)

        # Load the video clip
        clip = VideoFileClip(file_path)

        # Get the duration in seconds
        duration = clip.duration

        # Format the total duration as HH:MM:SS
        formatted_total_duration = str(total_duration).split(".")[0]

        # For the first file, set formatted_total_duration to 0
        if file_index == 0:
            formatted_total_duration = "0"

        # Add the duration to the total duration
        total_duration += duration

        filename2 = file_name.replace('.mkv', '')
        # Write the file name and total duration to the output file
        print(
            f'{filename2}{formatted_total_duration}')
        output.write(f'{filename2}{formatted_total_duration}')

        # Release the video clip from memory
        clip.close()
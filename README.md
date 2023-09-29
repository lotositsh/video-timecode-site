# video-timecode-site
  The code extracts the duration of video clips in a specified folder and writes the file name and total duration to an output file. It uses the `moviepy` library to load the video clips and `natsort` to sort the MKV files in a natural order. The duration is calculated in seconds and then formatted as HH:MM:SS. 
  

To use this code, make sure it is placed in the folder with the video clips. Also, ensure that the `folder_path` variable is set to the correct folder path containing the videos. If your video files have a different format than MKV, you can modify the code to match your file format. 
  

The output will be written to the `output_file` variable, so make sure to specify the desired name for the output text file.

# if ERROR infos = error.decode('utf8')

'''pip install moviepy==2.0.0.dev2'''


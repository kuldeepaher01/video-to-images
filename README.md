
# Video to Image Converter :movie_camera: :camera_flash:

This python script is used to extract images from a video file. It can extract images in two ways:

1.  Frame by Frame :camera_flash:
2.  Based on time delay :alarm_clock:

## Requirements :computer:

-   Python 3.x
-   OpenCV (cv2)

## How to Use :question:

1.  Clone this repository or download the zip file.
2.  Navigate to the downloaded directory and open a terminal.
3.  Run the following command: `python video_to_image_converter.py`
4.  Modify the `dir_path`, `folder`, `delay`, `name` parameters to fit your requirements.
5.  Run the script and wait for the images to be extracted.

## Parameters :gear:

-   `dir_path` : The path of the directory containing the video files.
-   `folder` : The folder where the extracted images will be stored. If no folder is specified, it will save the images in the current working directory.
-   `delay` : The time delay (in seconds) for the extraction of images when using the time-based method.
-   `name` : The prefix for the extracted image names.

## Example Usage :rocket:


    dir_path = "C:\\Users\\xxx\\Downloads\\dataset\\Videos"
    folder = "C:\\Users\\xx\\Downloads\\dataset\\images\\"
    extract_frame_by_frame(os.path.join(dir_path, "video.mp4"), folder, 10, name="img") 

This will extract images from the "video.mp4" file, every 10th frame, and save them in the "C:\Users\xx\Downloads\dataset\images\" folder with the prefix "img".

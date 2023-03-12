# video-to-images
The packages that are necessary to install in order to run the functions are OpenCV.
## functions take some arguments: 
<li>image_delay, to decide how much time between the screenshots
delete_video, to decide if the videos are deleted after being used
num_urls, to decide how many videos to (try to) download
max_images, to fix a maximum number of images to extract for each video
name, to change the names of the files, which are of the form "name_##.jpg", the folder called name will contain the images
max_duration, to decide the maximum length of the videos to download (in minutes)
silent, to decide if messages about the saved images are printed, messages about the videos downloaded are always printed
The other functions in the library can be useful separately as well.

extract_images_from_video: uses a .mp4 file to exract images
download_video: takes the url of the video and downloads it
get_urls: search for a specific word and returns a list of urls for the videos
max_label: find the maximum label for files called "name_##.jpg" in a folder

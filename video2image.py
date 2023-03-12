
import cv2
import os
import glob

    

def max_label(name, folder):
    '''Look at a folder and check the files with pattern "name_###.jpg" to extract the
    largest label present.'''
    
    path_pattern = os.path.join(folder, name + "_*.jpg")
    existing_files = glob.glob(path_pattern)
    if not existing_files:
        biggest_label = 0
    else:
        existing_labels = map(lambda s: int(s.split('_')[-1].split('.')[0]), existing_files)
        biggest_label = max(existing_labels)
    return biggest_label

def extract_frame_by_frame(video, folder=None, delay=10, name="img"):
    '''Read a downloaded video from its path and extract screenshots every few frames, set by the delay parameter.
        Images are saved in the specified folder or the cwd if none is specified and a maximum number of
        screenshots can be specified. The files are named "img##.jpg" and the labelling starts where it already stops
        in the folder.'''
    cap = cv2.VideoCapture(video)
    #############Set resolution acc to ur dataset. I'm extracting fruits from video so increasing res################
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    success = True
    count = 1
    if not folder:
        folder = os.getcwd()
    label = max_label(name, folder)

    while success:
        success , image = cap.read()
        if success == True:  
            # i want every 5th frame from video
            if count%delay == 0:
                # specify the output path and file name
                # i used count as a file name
                # you can use any
                label += 1
                file_name = name + "_" + str(label) + ".jpg"
                path = os.path.join(folder, file_name)
                try:
                    cv2.imwrite(path, image)
                    if cv2.imread(path) is None:
                        os.remove(path)
                    else:
                        print(f'Image successfully written at {path}')
                except:
                    pass
            count += 1
        else:
            break

    
def extract_images_from_video(video, folder=None, delay=1, name="img"):
    '''Read a downloaded video from its path and extract screenshots every few seconds, set by the delay parameter.
        Images are saved in the specified folder or the cwd if none is specified and a maximum number of
        screenshots can be specified. The files are named "name_##.jpg" and the labelling starts where it already stops
        in the folder.'''
    
    vidcap = cv2.VideoCapture(video)
    #############Set resolution acc to ur dataset. I'm extracting fruits from video so increasing res################
    vidcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vidcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    count = 0
    num_images = 0
    if not folder:
        folder = os.getcwd()
    label = max_label(name, folder)
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    
    while success:
        success, image = vidcap.read()
        num_images += 1
        label += 1
        file_name = name + "_" + str(label) + ".jpg"
        path = os.path.join(folder, file_name)
        try:
            cv2.imwrite(path, image)
            if cv2.imread(path) is None:
                os.remove(path)
            else:
                print(f'Image successfully written at {path}')
        except:
            pass
        count += delay*fps
        vidcap.set(1, count)



def rename_files(folder, name=""):
        # Get a list of all the files in the folder
    files = os.listdir(folder)

    # Loop through all the files in the folder
    i=0
    for file in files:
        # Construct the new file name
        new_file_name = name +str(i)+".jpg"
        print(".",i)
        # Rename the file using the new file name
        os.rename(os.path.join(folder, file), os.path.join(folder, new_file_name))
        i+=1

if __name__ == "__main__":
# set the directory path where the video files are present
    dir_path = "C:\\Users\\xxx\\Downloads\\dataset\\Videos"

    # loop over all the files present in the directory
    folder = "C:\\Users\\xx\\Downloads\\dataset\\images\\"
    # rename_files(folder)
    for file_name in os.listdir(dir_path):
        # separate the filename and extension of the file
        name, extension = os.path.splitext(file_name)
        video = (os.path.join(dir_path, file_name))
        # extract_frame_by_frame(video, folder, 10, name="img")

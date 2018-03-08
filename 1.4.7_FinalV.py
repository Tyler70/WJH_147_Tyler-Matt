import PIL
import os.path
import PIL.ImageDraw

def logoPlacement(original_image, logo_size, logo, st):
#places the logo in our desired place
    width, height = original_image.size
    position = int(logo_size * min(width, height))
    rlogo = logo.resize((position, position))
    result = original_image.copy()
    result.paste(rlogo, (0,0), rlogo)
    return result
    
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd()
    image_list = []
    file_list = []
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    return image_list, file_list
    
def logo_all_images(directory=None,size=0.5, st = False):
    
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)
    logo = PIL.Image.open('/Users/227205/Desktop/RF.png')
    for n in range(len(image_list)):
        print n
    filename, filetype = file_list[n].split('.')
    new_image = image_list[n]
    new_image = logoPlacement(image_list[n], size, logo, st)
    new_image_filename = os.path.join(new_directory, filename + '.png')
    new_image.save(new_image_filename)
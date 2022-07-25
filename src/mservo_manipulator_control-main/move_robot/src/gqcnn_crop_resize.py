import cv2
import numpy as np

def crop_and_resize(rgb_path, depth_path, inplace=True):
    img = cv2.imread(rgb_path)
    depth = np.load(depth_path)

    depth = cv2.resize(depth, (1823, 1041))
    depth = depth[162:1041-(878-720)-1,233:1823-(1590-1280)]

    img = center_crop(img, (856, 720))
    depth = center_crop(depth, (856, 720))

    img = cv2.resize(img, (640, 480))
    depth = cv2.resize(depth, (640, 480))

    if not inplace:
        rgb_path = new_file_path(rgb_path)
        depth_path = new_file_path(depth_path)

    cv2.imwrite(rgb_path, img)
    np.save(depth_path, depth)

def center_crop(img, size):
    w, h = size
    try:
        oh, ow = img.shape
    except:
        oh, ow, _ = img.shape
    return img[oh//2 - h//2:oh//2 + h//2, ow//2 - w//2:ow//2 + w//2]

def new_file_path(path):
    return '.'.join(path.split('.')[:-1]) + '_new.' + path.split('.')[-1]

if __name__ == '__main__':
    rgb_path = './sample/figure_rgb0.png'
    depth_path = './sample/figure_depth0.npy'
    crop_and_resize(rgb_path, depth_path, inplace=False)
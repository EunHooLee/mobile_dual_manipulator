import os
import os.path as path

def calc_grasping_point(rgb_path, depth_path, result_path='./results', docker_container='gqcnn'):
    workspace = '/root/Workspace'
    deeplab = path.join(workspace, 'pytorch-deeplab-xception')
    gqcnn = path.join(workspace, 'gqcnn')

    work_rgb_path = path.join(workspace, 'sample_rgb.jpg')
    work_depth_path = path.join(workspace, 'sample_depth.npy')
    work_depth_mask_path = path.join(workspace, 'sample_depth_mask.npy')
    work_segmask_path = path.join(workspace, 'sample_segmask.jpg')
    work_result_txt_path = path.join(workspace, 'sample_grasping_result.txt')
    work_result_image_path = path.join(workspace, 'sample_grasp.jpg')

    if not path.exists(result_path):
        os.makedirs(result_path)

    result_txt_path = path.join(result_path, 'grasping_result.txt')
    result_image_path = path.join(result_path, 'grasping_result.jpg')
    result_segmask_path = path.join(result_path, 'segmask.jpg')

    os.system('docker cp {} {}:{}'.format(
        rgb_path, docker_container, work_rgb_path
    ))
    os.system('docker cp {} {}:{}'.format(
        depth_path, docker_container, work_depth_path
    ))

    os.system('docker exec -it -w {} {} python3 test.py --in-path {} --depth-path {}'.format(
        deeplab, docker_container, work_rgb_path, work_depth_path
    ))

    os.system('docker exec -it -w {} {} python3 examples/policy.py GQCNN-4.0-PJ --depth_image {} --segmask {} --camera_intr data/calib/phoxi/phoxi.intr > /dev/null'.format(
        gqcnn, docker_container, work_depth_mask_path, work_segmask_path
    ))

    os.system('docker cp {}:{} {}'.format(
        docker_container, work_result_txt_path, result_txt_path
    ))
    os.system('docker cp {}:{} {}'.format(
        docker_container, work_result_image_path, result_image_path
    ))
    os.system('docker cp {}:{} {}'.format(
        docker_container, work_segmask_path, result_segmask_path
    ))

    return parse_txt_file(result_txt_path)

def parse_txt_file(txt_path):
    data = open(txt_path).read()
    data = data.strip().split('\n')
    data = [parse_line(d) for d in data]
    return dict(data)

def parse_line(line):
    name, value = line.split(' : ')
    name = ''.join(name.split(' ')[1:])
    if name == 'depth':
        value = value.replace('m', '')
    value = eval(value)
    return (name, value)

if __name__ == '__main__':
    rgb_path = 'sample/ham2_nip_snap_rgb_0.jpg'
    depth_path = 'sample/ham2_nip_snap_depth_0.npy'
    grasping_point = calc_grasping_point(rgb_path, depth_path, result_path='./results', docker_container='gqcnn')
    print(grasping_point)

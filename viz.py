import open3d as o3d
import numpy as np
import os


#pcd = o3d.geometry.PointCloud()

cam = o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
#cam.intrinsic_matrix =  [[914, 0.00, 640] , [0.00, 274.2, 192], [0.00, 0.00, 1.00]]

#img = o3d.io.read_image("D:/8th_Avenue_Stereo/Depth/R/img_000001.jpeg")
##color_raw = o3d.io.read_image("D:/8th_Avenue_Stereo/RGB/R/img_000300.jpeg")
##depth_raw = o3d.io.read_image("D:/8th_Avenue_Stereo/Depth/R/img_000300.jpeg")
color_raw = o3d.io.read_image("C:/Users/Ibrahim/Pictures/000196.jpeg")
depth_raw = o3d.io.read_image("C:/Users/Ibrahim/Projects/AdaBins/sim2/000196.png")
depth_raw = o3d.io.read_image("C:/Users/Ibrahim/Projects/AdaBins/sim2/X196.png")
#depth_raw = o3d.io.read_image("sim1/img_000300.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=False)
print("hellow")
print(rgbd_image.color)
pcdx = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image, cam)

o3d.io.write_point_cloud("satya.pcd", pcdx)


vis = o3d.visualization.Visualizer()
vis.create_window()

# geometry is the point cloud used in your animaiton
#geometry = o3d.geometry.PointCloud()
vis.add_geometry(pcdx)
#ctr = vis.get_view_control()

pcdx.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcdx])


exit()

imgs = [file for file in os.listdir("D:/8th_Avenue_Stereo/RGB/R/") if file.endswith(".jpeg")]

for n, i in enumerate(imgs):
    # now modify the points of your geometry
    # you can use whatever method suits you best, this is just an example
    color_raw = o3d.io.read_image("D:/8th_Avenue_Stereo/RGB/R/"+i)
    depth_raw = o3d.io.read_image("sim1/"+i.split(".")[0]+".png")
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=False)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, cam)
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    pcdx.points = pcd.points
    pcdx.colors = pcd.colors
    #o3d.visualization.draw_geometries([pcd])
    vis.update_geometry(pcdx)
    #ctr.set_zoom(0.01)
    vis.poll_events()
    vis.update_renderer()
    print(n)

###pcd.points = o3d.utility.Vector3dVector(np.random.randn(500,3))
#pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
#o3d.visualization.draw_geometries([pcd])


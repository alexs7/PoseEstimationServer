class HomeController < ApplicationController

  protect_from_forgery with: :null_session

  def index

  end

  def frame
    byte_array = request.raw_post

    File.open("arcore.JPG", 'w') { |file| file.write(byte_array.force_encoding('UTF-8'))}

    # run the script here
    system("./get_pose_server_script.sh")
    points3D = File.read("../../Python/results/arcore/3D_points_direct.txt")
    colmap_pose_translation = File.read("../../Python/results/arcore/pnp_ransac_translation_vector_direct.txt")
    colmap_pose_rotation_as_quat = File.read("../../Python/results/arcore/rotation_direct_matching_as_quaternion.txt")

    data = points3D + colmap_pose_rotation_as_quat + colmap_pose_translation

    render json: data
  end

  def pose


    render text: "foo"
  end

end

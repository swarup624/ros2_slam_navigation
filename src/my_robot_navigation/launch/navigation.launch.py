from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    nav2_bringup = PathJoinSubstitution([
        FindPackageShare("nav2_bringup"),
        "launch",
        "bringup_launch.py"
    ])

    map_file = PathJoinSubstitution([
        FindPackageShare("my_robot_navigation"),
        "maps",
        "warehouse_map.yaml"
    ])

    params_file = PathJoinSubstitution([
        FindPackageShare("my_robot_navigation"),
        "config",
        "nav2_params.yaml"
    ])

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_bringup),
            launch_arguments={
                "slam": "False",
                "use_sim_time": "True",
                "autostart": "True",      # <-- Add this
                "map": map_file,
                "params_file": params_file,
            }.items(),
        ),

    ])
#!/usr/bin/env python3

import rclpy
import tf_transformations

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult


# ============================================================
# Initial Robot Pose (AMCL)
# ============================================================

INITIAL_X = 0.1060
INITIAL_Y = -0.0175
INITIAL_YAW = 0.0


# ============================================================
# Waypoints
# Format:
# (x, y, yaw_in_radians)
# ============================================================

WAYPOINTS = [

    (-12.0618, -13.1170, 0.0),

    (-7.7551, -12.6137, 0.0),

    (3.6422, -14.7130, 0.0),

]


# ============================================================
# Create PoseStamped
# ============================================================

def create_pose(navigator, x, y, yaw):

    qx, qy, qz, qw = tf_transformations.quaternion_from_euler(
        0.0,
        0.0,
        yaw
    )

    pose = PoseStamped()

    pose.header.frame_id = "map"
    pose.header.stamp = navigator.get_clock().now().to_msg()

    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 0.0

    pose.pose.orientation.x = qx
    pose.pose.orientation.y = qy
    pose.pose.orientation.z = qz
    pose.pose.orientation.w = qw

    return pose


# ============================================================
# Main
# ============================================================

def main():

    rclpy.init()

    navigator = BasicNavigator()

    print("\n===================================")
    print("   Waypoint Navigation Started")
    print("===================================\n")

    # --------------------------------------------------------
    # Set Initial Pose
    # --------------------------------------------------------

    initial_pose = create_pose(
        navigator,
        INITIAL_X,
        INITIAL_Y,
        INITIAL_YAW
    )

    navigator.setInitialPose(initial_pose)

    print("Initial pose set.")

    # --------------------------------------------------------
    # Wait for Nav2
    # --------------------------------------------------------

    print("Waiting for Nav2...")

    navigator.waitUntilNav2Active()

    print("Nav2 is Active!\n")

    # --------------------------------------------------------
    # Create waypoint list
    # --------------------------------------------------------

    poses = []

    for wp in WAYPOINTS:

        x, y, yaw = wp

        poses.append(
            create_pose(
                navigator,
                x,
                y,
                yaw
            )
        )

    print(f"Total Waypoints : {len(poses)}")

    # --------------------------------------------------------
    # Start Navigation
    # --------------------------------------------------------

    navigator.followWaypoints(poses)

    current_waypoint = 1

    while not navigator.isTaskComplete():

        feedback = navigator.getFeedback()

        if feedback:

            print(
                f"Navigating to waypoint {current_waypoint}/{len(poses)}",
                end="\r"
            )

            if feedback.current_waypoint != current_waypoint - 1:

                current_waypoint = feedback.current_waypoint + 1

                print(
                    f"\nReached waypoint {current_waypoint-1}"
                )

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    result = navigator.getResult()

    print()

    if result == TaskResult.SUCCEEDED:

        print("Mission Completed Successfully!")

    elif result == TaskResult.CANCELED:

        print("Mission Cancelled!")

    elif result == TaskResult.FAILED:

        print("Mission Failed!")

    else:

        print("Unknown Result!")

    rclpy.shutdown()


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()
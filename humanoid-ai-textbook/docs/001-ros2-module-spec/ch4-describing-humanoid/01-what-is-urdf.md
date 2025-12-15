# What is URDF?

URDF, or Unified Robot Description Format, is an XML-based file format in ROS 2 that is used to describe a robot's kinematic and dynamic properties. Essentially, it's a blueprint that tells ROS 2 (and other tools) exactly what your robot looks like, how its parts are connected, and how it moves. For humanoid robots, URDF is fundamental because it provides a standardized way to represent their complex structure.

A URDF file defines:
1.  **Links**: These are the rigid bodies of the robot, such as a torso, an upper arm, or a foot. Each link has its own visual properties (shape, color, texture) and collision properties (used for physics simulation).
2.  **Joints**: These define how links are connected to each other and how they can move relative to one another. Joints can be fixed, revolute (rotating), prismatic (sliding), or other types, representing the robot's degrees of freedom.

By providing a comprehensive description of the robot, URDF enables various ROS 2 tools to:
*   **Visualize the robot**: Display a 3D model of the robot in simulation or visualization tools.
*   **Perform kinematics**: Calculate the position and orientation of different parts of the robot.
*   **Detect collisions**: Identify potential collisions between robot parts or with the environment.
*   **Control the robot**: Provide a common interface for motion planning and control software.

URDF is thus an indispensable tool for designing, simulating, and controlling humanoid robots in the ROS 2 ecosystem.
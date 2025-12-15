# Key Elements of a URDF File: Links, Joints, and Transmissions

A URDF (Unified Robot Description Format) file is structured around several key elements that collectively define the robot.

1.  **`<link>` (Links)**:
    *   Represent the physical segments or rigid bodies of the robot (e.g., torso, thigh, forearm).
    *   Each link has an associated `<visual>` element (describes its appearance) and a `<collision>` element (describes its geometry for collision detection).
    *   A `<inertial>` element defines the link's mass, center of mass, and inertia tensor, crucial for physics simulation.

2.  **`<joint>` (Joints)**:
    *   Define the kinematic and dynamic connection between two links (a parent and a child link).
    *   Specify the type of joint (e.g., `revolute` for rotation, `prismatic` for linear movement, `fixed` for rigid connections).
    *   Includes attributes like `origin` (relative position and orientation), `axis` (direction of movement), and `limit` (range and velocity constraints).

3.  **`<transmission>` (Transmissions)**:
    *   Describe the relationship between actuators (e.g., motors) and joints.
    *   This element maps the effort applied by an actuator to the resulting motion in a joint.
    *   Essential for control systems, as it defines how a motor's command translates into joint movement.

These elements, when combined in a hierarchical structure, paint a complete picture of the robot's physical form, enabling sophisticated simulation, control, and visualization within the ROS 2 ecosystem.
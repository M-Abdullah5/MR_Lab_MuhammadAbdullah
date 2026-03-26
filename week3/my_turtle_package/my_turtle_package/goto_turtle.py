import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
import math

class GotoGoalNode(Node):
    def __init__(self):
        super().__init__('goto_turtle')
        self.publisher_ = self.create_publisher(Twist, 'turtle4/cmd_vel', 10)
        
        # Subscriber 1: Listens to where the turtle currently is
        self.pose_subscriber = self.create_subscription(Pose, 'turtle4/pose', self.update_pose, 10)
        
        # Subscriber 2: Listens to rqt for a new target location
        self.goal_subscriber = self.create_subscription(Point, 'turtle4/goal', self.update_goal, 10)
        
        self.pose = Pose()
        self.timer = self.create_timer(0.1, self.move2goal)
        
        # Default starting goal
        self.goal_x = 5.5
        self.goal_y = 5.5
        self.tolerance = 0.1

    def update_pose(self, data):
        self.pose = data

    def update_goal(self, msg):
        # When rqt sends a message, update the target variables
        self.goal_x = msg.x
        self.goal_y = msg.y
        self.get_logger().info(f'New target received! Hunting down X: {self.goal_x}, Y: {self.goal_y}')

    def move2goal(self):
        distance = math.sqrt((self.goal_x - self.pose.x)**2 + (self.goal_y - self.pose.y)**2)
        msg = Twist()
        
        if distance >= self.tolerance:
            # 1. Calculate raw angle
            angle_to_goal = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x)
            
            # 2. Normalize the angle to always take the shortest turn [-pi, pi]
            raw_angle_error = angle_to_goal - self.pose.theta
            angle_error = math.atan2(math.sin(raw_angle_error), math.cos(raw_angle_error))
            
            # 3. Apply control loop (with a speed limit so it doesn't overshoot)
            msg.angular.z = 4.0 * angle_error
            msg.linear.x = min(1.5 * distance, 2.0) # Drives fast but never exceeds 2.0 speed
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GotoGoalNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

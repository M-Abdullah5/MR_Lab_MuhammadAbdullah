import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import math

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')

        self.spawn_client = self.create_client(Spawn, 'spawn')
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for spawn service...')
        
        req = Spawn.Request()
        req.x = 2.0
        req.y = 2.0
        req.theta = 0.0
        req.name = 'turtle2'
        self.spawn_client.call_async(req)

        self.sub_leader = self.create_subscription(Pose, 'turtle1/pose', self.leader_callback, 10)
        self.sub_follower = self.create_subscription(Pose, 'turtle2/pose', self.follower_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

        self.leader_pose = Pose()
        self.follower_pose = Pose()
        self.timer = self.create_timer(0.1, self.timer_callback)

    def leader_callback(self, msg):
        self.leader_pose = msg

    def follower_callback(self, msg):
        self.follower_pose = msg

    def timer_callback(self):
        dist = math.sqrt((self.leader_pose.x - self.follower_pose.x)**2 + (self.leader_pose.y - self.follower_pose.y)**2)
        msg = Twist()
        
        # Reduced tolerance so it gets closer to the leader
        if dist > 0.5: 
            # 1. Calculate the shortest angle to the leader
            angle_to_leader = math.atan2(self.leader_pose.y - self.follower_pose.y, self.leader_pose.x - self.follower_pose.x)
            angle_error = angle_to_leader - self.follower_pose.theta
            angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

            # 2. Always turn towards the leader aggressively
            msg.angular.z = 6.0 * angle_error
            
            # 3. THE FIX: Only drive forward IF mostly facing the leader (within ~0.2 radians)
            if abs(angle_error) < 0.2:
                msg.linear.x = min(2.0 * dist, 2.5) # Fast catch-up speed, capped at 2.5
            else:
                msg.linear.x = 0.0 # Stop driving and focus on turning!
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = FollowerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

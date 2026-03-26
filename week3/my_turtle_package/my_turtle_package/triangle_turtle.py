import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TriangleNode(Node):
    def __init__(self):
        super().__init__('triangle_turtle')
        # This node controls turtle3
        self.publisher_ = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.state = 0  
        self.ticks = 0

    def timer_callback(self):
        msg = Twist()
        self.ticks += 1
        
        if self.state == 0:
            msg.linear.x = 1.0  
            msg.angular.z = 0.0
            if self.ticks >= 20:  
                self.state = 1
                self.ticks = 0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 2.0 * math.pi / 3.0  # 120 degrees
            if self.ticks >= 10:  
                self.state = 0
                self.ticks = 0
                
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TriangleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

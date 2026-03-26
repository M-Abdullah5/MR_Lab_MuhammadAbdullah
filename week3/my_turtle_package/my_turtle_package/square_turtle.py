import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class SquareNode(Node):
    def __init__(self):
        super().__init__('square_turtle')
        # This node controls turtle2
        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
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
            msg.angular.z = math.pi / 2.0  # 90 degrees
            if self.ticks >= 10:  
                self.state = 0
                self.ticks = 0
                
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SquareNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

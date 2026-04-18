import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        # Create publisher for /cmd_vel using Twist message type
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        # Timer calls the callback every 2.0 seconds
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.is_moving = False

    def timer_callback(self):
        msg = Twist()
        if self.is_moving:
            msg.linear.x = 0.0  # Stop
            self.get_logger().info('State: Stopping...')
        else:
            msg.linear.x = 0.15  # Move forward at 0.15 m/s
            self.get_logger().info('State: Moving Forward...')
        
        # Publish the message and toggle the state
        self.publisher_.publish(msg)
        self.is_moving = not self.is_moving

def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        # 1. Declare the parameter with an empty string as the default
        self.declare_parameter('student_name', '')
        
        # 2. Retrieve the parameter's value
        student_name = self.get_parameter('student_name').get_parameter_value().string_value
        
        # 3. Apply the conditional logic required by the lab
        if student_name:
            self.get_logger().info(f'{student_name}')
        else:
            self.get_logger().info('student_name not set')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

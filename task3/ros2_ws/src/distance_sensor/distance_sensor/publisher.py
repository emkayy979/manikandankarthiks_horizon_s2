import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

# this is the part that sends the distance numbers
class distancesender(Node):
    def __init__(self):
        super().__init__('distance_sender')
        # make the publisher thing here
        self.p = self.create_publisher(Int32, '/rover_distance', 10)
        # run every 1 second
        self.t = self.create_timer(1.0, self.send)

    # this function sends a random number
    def send(self):
        val = Int32()
        val.data = random.randint(5, 150)  # random distance value
        self.p.publish(val)
        self.get_logger().info(f'sending: {val.data}')

def main(args=None):
    rclpy.init(args=args)
    # start the node
    x = distancesender()
    rclpy.spin(x)
    x.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

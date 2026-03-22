import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# this one receives the numbers from the other node
class distancereceiver(Node):
    def __init__(self):
        super().__init__('distance_receiver')
        #subscribe to the incoming.
        self.s = self.create_subscription(
            Int32, '/rover_distance', self.getdata, 10)

 #this runs when a new message comes in
    def getdata(self, msg):
        print(f'Received distance: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    # create and run the node
    y = distancereceiver()
    rclpy.spin(y)
    y.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

from std_msgs.msg import String

import rclpy
from rclpy.node import Node

class InterfaceWhiteList(Node):

    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f">>><<<")

        self.pub = self.create_publisher(String, "test/one", 10)
        # self.sub = self.create_subscription(String, "test/one", self.cb, 10)

        self.timer = self.create_timer(2.0, self.timer_cb)
    
    def cb(self, msg):
        print(f">> We Got Msg: {msg}")

    def timer_cb(self):
        msg = String()
        msg.data = "ass"

        print("Sending Message>>")
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    inter_node = InterfaceWhiteList("interface_whitelist_node")

    rclpy.spin(inter_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
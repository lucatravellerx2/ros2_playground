from tester_interfaces.msg import LogStrArray

import rclpy
from rclpy.node import Node


class LoggerNode(Node):

    def __init__(self, file_name):
        super().__init__("logger_node")

        self.file_name = file_name
        self.log_sub = self.create_subscription(LogStrArray, "/logger/data/write", self.log_data_cb, 10)
    
    def log_data_cb(self, msg):
        if len(msg.data_to_write) == len(msg.time_strings):
            data_str = ""

            with open(self.file_name, "a+") as log_file:
                for index in range(len(msg.data_to_write)):
                    data_str = msg.time_strings[index] + ":   " + msg.data_to_write[index] + "\n"
                    log_file.write(data_str)
    
def main(args=None):
    rclpy.init(args=args)

    logger_node = LoggerNode("log_file_report.txt")

    rclpy.spin(logger_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
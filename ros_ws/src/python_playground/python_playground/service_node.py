from tester_interfaces.srv import StringTesterService

import rclpy
from rclpy.node import Node
import time

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(StringTesterService, 'test_service1', self.tester_callback)
        self.rate = self.create_rate(4)

    def tester_callback(self, request, response):
        time.sleep(4)
        self.get_logger().info('Incoming request\nparam1: %s param2: %s param3 %s' % (request.param1, request.param2, request.param3))        
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
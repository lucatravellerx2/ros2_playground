import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup, MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from tester_interfaces.srv import StringTesterService
from tester_interfaces.msg import LogStrArray
import time

class TestGroups(Node):

    def __init__(self, executor):
        super().__init__('test_group_node')
        timer_period = 1
        
        self.executor = executor

        self.lister = []

        timer_cb_group = MutuallyExclusiveCallbackGroup()
        service_cb_group = MutuallyExclusiveCallbackGroup()
        timer2_cb_group = MutuallyExclusiveCallbackGroup()

        self.log_pub = self.create_publisher(LogStrArray, "/logger/data/write", 10)

        self.timer = self.create_timer(0.2, self.timer_callback, callback_group=timer_cb_group)
        # self.timer2 = self.create_timer(1, self.timer2_callback, callback_group=timer2_cb_group)
        # self.timer2.cancel()
        # self.timer2.cancel()
        # self.get_logger().info(str(self.timer2.is_ready()))
        # self.get_logger().info(str(self.timer2.is_canceled()))
        # self.service_client = self.create_client(StringTesterService, "test_service1", callback_group=service_cb_group)

        self.num = 0
    def timer_callback(self):
        self.get_logger().info(str(self.timer.is_ready()))
        self.get_logger().info(str(self.timer.is_canceled()))
        self.lister.append(self.num)
        self.num += 1

        timestamp = time.time()

        log_msg = LogStrArray()
        log_msg.data_to_write = [str(self.num)]
        log_msg.time_strings = [str(timestamp)]

        self.log_pub.publish(log_msg)

        self.get_logger().info(f"{self.num}")
    
    def timer2_callback(self):
        self.get_logger().info("TIMER 2")
        
        # self.get_logger().info("We Are In Timer Callback")

        srv_request = StringTesterService.Request()
        srv_request.param1 = "myvalue1"
        srv_request.param2 = "myvalue2"
        srv_request.param3 = "myvalue3"

        while not self.service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        future = self.service_client.call_async(srv_request)

        self.executor.spin_until_future_complete(future)
        # self.get_logger().info("Making Service Request")
        # # future = self.service_client.call(srv_request)

        response =  future.result()
        self.get_logger().info("GOT RESPONSE: " + str(response.success))


def main():
    rclpy.init()
    executor = MultiThreadedExecutor()
    group_cb_testing = TestGroups(executor)
    executor.add_node(group_cb_testing)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        group_cb_testing.destroy_node()
        executor.shutdown()
        rclpy.shutdown()
    
    # try:
    #     rclpy.spin(group_cb_testing)
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     # group_cb_testing.destroy_node()
    #     # executor.shutdown()
    #     rclpy.shutdown()




if __name__ == '__main__':
    main()

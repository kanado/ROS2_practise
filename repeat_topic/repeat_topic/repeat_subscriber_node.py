import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RepeatSubscriber(Node):
    def __init__(self):
        super().__init__('repeat_Subscriber_node')
        self.sub = self.create_subscription(String,'topic',self.callback,10)

    def callback(self,msg):
        self.get_logger().info(f'サブスクライブ:{msg.data}')

def main():
    rclpy.init()
    Node = RepeatSubscriber()
    rclpy.spin(Node)
    rclpy.shutdown()

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

repeat_count = int(input('How many time repeat:'))

class RepeatPublisher(Node):
    def __init__(self):
        super().__init__('repeat_publish_node')
        self.pub = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        msg = String()
        if self.i <= repeat_count:
            msg.data = f'送信回数ー＞{self.i}'
        else:
            msg.data = f'終わり'
            self.destroy_timer(self.timer)
        self.pub.publish(msg)
        self.get_logger().info(f'パブリッシュ:{msg.data}')
        self.i += 1


def main():
    rclpy.init()
    node = RepeatPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('キャンセルします')
    rclpy.shutdown()
    print('終了しました')

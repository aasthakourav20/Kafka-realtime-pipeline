from confluent_kafka.admin import AdminClient, NewTopic

from asyncio import Future
from typing import List

from confluent_kafka.admin import AdminClient, NewTopic, ListConsumerGroupsResult, ConsumerGroupListing


class KafkaAdminHelper:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.admin_client = AdminClient({"bootstrap.servers": self.bootstrap_servers})

    def topic_exists(self, topic_name):
        topics_metadata = self.admin_client.list_topics()

        if topic_name in topics_metadata.topics.keys():
            print(f"Topic '{topic_name}' already exists.")
            return True

        return False

    # def create_topic_if_not_exists(self, topic_name, num_partitions=5, replication_factor=3):
    #     """Create a topic if it doesn't exist"""
    #     if self.topic_exists(topic_name):
    #         return

    #     new_topic = NewTopic(topic=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
    #     self.admin_client.create_topics([new_topic])
    #     print(f"Topic '{topic_name}' created.")

    def create_topic_if_not_exists(self, topic_name, num_partitions=1, replication_factor=1):
        """Create a topic if it doesn't exist"""
        topic_metadata = self.admin_client.list_topics(topic=topic_name)
        print(topic_metadata)
        if topic_metadata:
            print(f"Topic '{topic_name}' already exists.")
            return
        new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        self.admin_client.create_topics([new_topic])
        print(f"Topic '{topic_name}' created.")

    def delete_topic(self, topic_name):
        if not self.topic_exists(topic_name):
            print(f"topic {topic_name} doesn't exist")
            return

        res = self.admin_client.delete_topics([topic_name])
        res[topic_name].result()
        if not self.topic_exists(topic_name):
            print(f"topic {topic_name} deleted successfully")

    def group_exists(self, group_name):
        groups: Future = self.admin_client.list_consumer_groups()

        groups: ListConsumerGroupsResult = groups.result()
        groups: List[ConsumerGroupListing] = groups.valid
        group_names = list(map(lambda x: x.group_id, groups))
        return group_name in group_names
    def delete_consumer_group(self, group_name: str):

        if not self.group_exists(group_name):
            print('consumer group doesn\'t exist')
            return

        res = self.admin_client.delete_consumer_groups([group_name])
        res[group_name].result()
        if not self.group_exists(group_name):
            print(f"consumer group {group_name} deleted successfully")
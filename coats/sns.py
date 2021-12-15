import logging
import boto3

class publisher:
    
    def publish_message(self, topic_name, my_message):
        
        try:
           sns_client = boto3.client('sns')
           print('\npublishing the message {} to the SNS topic {}...\n'.format(my_message, topic_name))
           # recall that if the topic already exists, the create_topic() method returns that topic's ARN
           response = sns_client.create_topic(Checkout_title = topic_name)
           topic_arn = response[TopicArn]
           
           response = sns_client.publish(topic_arn = 'arn:aws:sns:us-east-1:032882127517:Checkout_title',  my_message = 'Your order has been placed' )    
           print(response)
           
    

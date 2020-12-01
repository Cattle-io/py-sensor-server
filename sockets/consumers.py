import json


from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class PacketsSocketsConsumer(WebsocketConsumer):

    def connect(self):
        """
        Join channel group by chatname.
        """
        self.group_name = 'chat_{0}'.format(self.scope['url_route']['kwargs']['chatname'])
        
        print(' ')
        print(' ')
        print('group_name ')
        print( self.group_name )
        print(' ')
        print('channel_name')
        print(self.channel_name)
        print(' ')
        print(' ')
        
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )

        self.accept()
        self.send('{"message":"Welcome Back Angular 1 , we are in '+ self.group_name +' room "}')
       
    def disconnect(self, close_code):
        """
        Leave channel by group name.
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        self.close()

    def receive(self, text_data):
        """
        Receive message from websocket and send message to channel group.
        """

    def chat_message(self, event):
        """
        Receive message from channel group and send message to websocket.
        """
        print(event["message"])
        self.send(text_data=event["message"])
        

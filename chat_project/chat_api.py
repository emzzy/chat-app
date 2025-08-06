# from rest_framework.response import Response
# from rest_framework.views import APIView
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync


# class ChatView(APIView):
#     def get(self, request):
#         return Response({'message': 'Hello, World!'})

#     def post(self, request):
#         message = request.data['message']
#         async_to_sync(self.channel_layer.group_send)(
#             'chat_group',
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#         return Response({'message': 'Message sent!'})
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from agent_service import agent_executor

class AgentInvokeView(APIView):
    """
    API view to handle requests to the LangChain agent.
    """
    def post(self, request, *args, **kwargs):
        user_input = request.data.get('input')

        if not user_input:
            return Response(
                {"error": "No 'input' provided"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            response = agent_executor.invoke({"input": user_input})

            return Response(
                {"output": response.get('output')},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
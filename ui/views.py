import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from agent.agent_runner import run_agent
from django.shortcuts import render

def index(request):
    return render(request, "chat.html")


@csrf_exempt

def chat_view(request):
    import json
    data = json.loads(request.body)
    user_message = data.get("message", "")

    session_memory = request.session.get("memory", [])

    response, memory = run_agent(user_message, session_memory=session_memory)

    # Save updated memory in session
    request.session["memory"] = memory.messages
    request.session.modified = True

    return JsonResponse({"response": response})

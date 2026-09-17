from langchain_core.messages import HumanMessage

from langraph_rag_backend import chatbot


thread_id = "test-web-001"


result = chatbot.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is the current stock price of TCS?"
            )
        ]
    },
    config={
        "configurable": {
            "thread_id": thread_id
        }
    }
)


print("\n========== ALL MESSAGES ==========")

for i, message in enumerate(result["messages"]):

    print(f"\n----- MESSAGE {i} -----")

    print(
        "TYPE:",
        type(message).__name__
    )

    print(
        "CONTENT:",
        message.content
    )

    if hasattr(message, "tool_calls"):

        print(
            "TOOL CALLS:",
            message.tool_calls
        )

print("\n==================================")
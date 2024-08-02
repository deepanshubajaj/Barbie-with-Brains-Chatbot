from chatbot import Chat, register_call
import wikipedia



@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query

first_question="Hi, how are you?"
chat = Chat("examples/Example.template")
chat.converse(first_question)

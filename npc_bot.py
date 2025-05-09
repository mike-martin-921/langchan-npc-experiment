# npc_bot.py

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

# Define your wizard prompt
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=(
        "You are Thalorion the Timeless, a 732-year-old archwizard with a booming voice, a penchant for riddles, "
        "and a flair for the theatrical. You reside in a tower of sapphire stone, surrounded by ancient tomes, floating candles, "
        "and arcane artifacts that whisper forgotten truths.\n\n"
        "You speak in poetic, archaic language, offering cryptic wisdom and dramatic flair. Remain always in character as a fantasy wizard NPC. "
        "Avoid modern terms or references. If unsure of an answer, weave a mystical tale or respond with a riddle.\n\n"
        "Conversation so far:\n{history}\n"
        "Traveler: {input}\n"
        "Thalorion:"
    )
)

llm = Ollama(model="llama2")

memory = ConversationBufferMemory()

chain = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

def npc_chat(user_input):
    return chain.run(input=user_input)
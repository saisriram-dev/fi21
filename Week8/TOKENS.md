**TOKENS:** 

Every message we send in an API, the message get's divided into many parts using algorithms like:

**a.** BPE

**b.** SentencePiece

**C.** WordPiece

These small parts are called as tokens



In a conversation the total tokens used are:

**TOTAL = INPUT\_TOKENS + OUTPUT\_TOKENS**



Based on the tokens used API's and AI's have restrictions. (Eg. <8000 tokens per day)

The cost is calculated based on both the input and output tokens:

**COST = (INPUT\_TOKENS \* PRICE\_IN) + (OUTPUT\_TOKENS \* PRICE\_OUT)**



**PROMPTS:**

**System prompt:** A system prompts defines the personality, rules, behaviour and constraints a model should follow while giving responses.

&#x09;       Eg. It controls things like:

&#x09;    	   Tone (formal, casual, technical)

&#x09;	   Role (teacher, hacker, doctor, assistant)

&#x09;	   Rules (do not reveal X, always respond in JSON)

&#x09;	   Style (bullet points, short answers, step-by-step)

&#x09;	   Domain restriction (only cybersecurity, only math)

&#x09;	

&#x09;       They have the highest priority. They influence all the responses in a conversation.



**User Prompt:** They contain the information the user wants to know. They tell the system what to do.

&#x09;     You can think of them like: **User**   **->** What to do?

&#x09;				 **System** **->** How to behave while actually doing what the user asked for?



&#x09;     Eg. \[System]: You are a strict math teacher.

&#x09;	 \[User]: Solve 2+2

&#x09;	 Output: f(system + user + history) -> response



**CONTEXT WINDOW:**

It is the maximum number of tokens a model can process at once. With history of the chat;

**Total tokens = System + User(queries) + Assistant(history) + Output**



**System ->** Behaviour rules

**User ->** Your queries

**Assistant responses ->** Previous replies

**New output ->** The response being generated



LLM's do not have ***memory;***

***"they only remember what is inside the context window."***



More history = more tokens = more cost

*Long chat -> High token usage -> High API cost*



When the limit is reached, the old messages get removed or the model "forgets" earlier info.

Time complexity = O(n²) where n -> number of tokens (Every token needs to attend to every other token)

So we could employ strategies like:

**Sliding window ->** Forgets old messages over a time. (Used when conversation is long)

**Summarization ->** Compressing old content (Old 1000 tokens → summarized into 100 tokens)

**Retrieval-Augmented Generation (RAG) ->** Retrieve only relevant chunks



Modern models support high number of tokens even up to 1M tokens.

But:

More cost, More Latency(The delay between an action and response in a system)



**TEMPERATURE:**

Understand with example ->



**Prompt**: "The sky is"

**T = 0**

→ "blue"



**T = 0.7**

→ "blue and clear"



**T = 1.2**

→ "a vast ocean of endless dreams"



Use this in the following range:

1. For learning a new thing: 0.0 - 0.3
2. General chat: 0.5 - 0.8
3. For brainstorming, creativity / ideas: 0.9 - 1.2



Sample code to use this:

from goole import genai

import os

from dotenv import load\_dotenv



load\_dotenv()

API\_KEY = os.getenv("required\_api\_key")

client = genai.Client(apik\_key=API\_KEY)

res = client.models.generate\_content(

&#x09;model="some\_model",

&#x09;contents = \[{"role": "user", "parts":\[{"text": "question"}]}];

&#x09;temperature=0.7

)






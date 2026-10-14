We tried out the new OpenAI Decisions API in my Python + AI office hours today!

The API returns typed answers with probabilities (yes/no, multiple choice, or a score) instead of generated text, so it can be a fast and cheap solution for routing, classification, and LLM-as-a-judge.

The good:

📚 Huge context window: It's based on GPT-6 Luna, so it should support about 1M tokens. A 256K-token file worked fine, while our 1M test file was just over the limit.

🖼️ Multimodal: It accepts image inputs, unlike most other decision models (like Jev or Decision-1).

The bad:

🦎 It fails my "alligator vs crocodile" test, which most OpenAI models pass. Asked as two yes/no questions, it said 91% alligator and 67% crocodile. Asked as one multiple-choice question, with descriptions of each snout, it still chose alligator (73%). They're crocodiles!

Remember: Evaluate the Decisions API on your *own* scenarios, since it may work great for yours even if it fails mine.

Watch the full office hours here: (Or jump to that demo at 24:46)
https://www.youtube.com/watch?v=wrw9xA541Fk

I posted links to all our experiments in the OH thread:
https://github.com/orgs/microsoft-foundry/discussions/280#discussioncomment-18915761

Join us live every week: http://aka.ms/pythonai/oh
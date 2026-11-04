🎉 We now have the Decisions API in Azure OpenAI!

It uses the GPT-6 Luna model behind the scenes, which means it's multimodal and has a 1 million token context window.

For example, I sent the input "I was charged twice for order 123. Please refund the duplicate charge" and asked three questions of the API:

❓ Is a refund requested?
➡️ Yes, with probability 1.0

❓ Which department should handle this request?
➡️ "billing", with confidence 1.0

❓ What's the severity?
➡️ A score of 1.05 on a 0 (Low) to 2 (High) scale, with confidence 0.9 (93% probability for Medium)

This is how decision models work: you get back a value for each question, plus a probability or confidence. For choices and scores, you also get the probability for every option. And since it doesn't generate text, the whole request used only 406 input tokens and ZERO output tokens!

So now you actually have two decision models in Foundry:

💸 Microsoft Decision-1: Smaller context window and not multimodal, but price-wise it's going to be your cheaper option, and it might be faster.

🖼️ Azure OpenAI Decisions API: If you need the longer context and the multimodal support, use this one instead.

There are so many places where I'm starting to bring in decision models, like routing, classification, and LLM-as-a-judge evaluation. Just make sure you calibrate them and check that they're working well for your scenario.

Docs:
https://learn.microsoft.com/azure/foundry/openai/how-to/decisions

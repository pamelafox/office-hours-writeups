# October 13, 2026 Office Hours Q&A

## Announcement: Microsoft-Decision-1 in Microsoft Foundry

📹 [00:30](https://www.youtube.com/watch?v=wrw9xA541Fk&t=30)

[Microsoft-Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) is Microsoft's new decision model, now available in the [Foundry model catalog](https://ai.azure.com/catalog/models/Microsoft-Decision-1). Like [Jev from TypeSafe AI](https://docs.typesafe.ai/introduction), it returns typed decisions with probabilities instead of generated text. It is [post-trained from Qwen3.5-9B](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/), and Microsoft plans to rebase it on other models, including MAI and OpenAI models.

### Using Decision-1 to choose a reasoning level

📹 [01:55](https://www.youtube.com/watch?v=wrw9xA541Fk&t=115)

Justin uses Decision-1 to choose a reasoning level before running a task. He previously always used extra-high reasoning. Some people say extra-high reasoning is mostly for benchmarks, and Pamela has seen it overthink in some of her evaluations. Justin also wants to use Decision-1 to decide when a task can run on a local model, although he noted that this only saves tokens sometimes.

### Latency, calibration, and accuracy

📹 [02:42](https://www.youtube.com/watch?v=wrw9xA541Fk&t=162)

The announcement post has interactive charts. Latency is Decision-1's strongest result. The post reports calibration and benchmark accuracy separately. Calibration measures whether the returned probabilities match how often the answers are correct, while accuracy measures how often the answers are correct on benchmarks. In the post's comparison, Decision-1 had higher accuracy than Jev, but Jev had higher calibration. Benchmarks are useful signals, but watch out for models optimized to score well on them.

### Comparison to the OpenAI Decisions API

📹 [03:30](https://www.youtube.com/watch?v=wrw9xA541Fk&t=210)

The Decision-1 announcement does not compare it with the [OpenAI Decisions API](https://developers.openai.com/api/docs/guides/decisions), another decision model option that is now available on the OpenAI platform. The Decisions API uses a version of GPT-6 Luna that has been optimized for faster response times.

The biggest difference is image support. Decision-1 accepts only text or JSON, no images. The Decisions API accepts image inputs, so use it if you need multimodal decisions. The Decisions API is not available in Azure yet, likely because supporting a brand new API endpoint takes more work than adding a new model to an existing API.

### Calling the Decision-1 API

📹 [05:44](https://www.youtube.com/watch?v=wrw9xA541Fk&t=344)

The [Decision-1 documentation](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision) shows that it uses a separate decision endpoint, so you cannot swap it into existing LLM code. Each request sends a `state` and one or more typed questions:

* **`noul`:** A Bernoulli probability, which works like a boolean with a probability. You can optionally define criteria for true and false. Decision-1 appears to use the same question types as Jev.
* **`choice`:** Selects one option from a fixed set, like a multiple-choice question.
* **`score`:** Places an item on an ordered, labeled scale. The returned score is the probability-weighted average of the level indexes, so it can fall between levels. Validate scores against your own labeled examples.

Every answer comes back with probabilities, so you can set thresholds for when your application acts. Decision-1 is available as a Global Standard deployment and in selected regions. There is no SDK yet, so the documentation calls the endpoint with Python's `urllib` package. One request can include multiple questions about the same state. Low latency and support for multiple questions in one request are what people like most about Jev, and Decision-1 offers both.

## When should you use a decision model?

📹 [08:14](https://www.youtube.com/watch?v=wrw9xA541Fk&t=494)

Decision models make many scenarios that people already use smaller LLMs for more practical because they are so fast and cheap. Good candidates include:

* **Routing:** Many people avoid putting a router before a step because it adds latency, but a fast decision model makes routing more practical. Make sure the router performs well. A bad router may be worse than no router at all. The same applies to model routing, so evaluate whether adding a routing step is worth it.
* **Classification:** Use cases include spam detection, intent analysis, and ticket classification. Some people simply call Jev a classifier model. If your structured outputs contain only booleans, choices, or scores, you can move them to a decision model. If they also include free text, you cannot.
* **LLM-as-a-judge:** Many people are switching evaluation pipelines to decision models for much faster evaluations. This helps when you need to evaluate hundreds of ground truth examples. Calibrate the scores against human ratings.
* **Recommendations and search relevance:** A decision model can work much like a reranker. For example, Azure AI Search's semantic ranker gives each result a score. Dedicated reranker models are trained for that task, while decision models are generic, but you could try implementing a reranker with one. An upcoming Ignite session will reimplement Azure AI Search from scratch and may compare that approach.
* **Safety and security screening:** A coding agent could use a decision model to assess risk levels. In a [Latent Space interview](https://www.youtube.com/watch?v=cFx9Z3ZXca0), the founder of Jev's company argued that safety screening should be more deterministic than a prompt.
* **Robotics:** OpenAI connected the Decisions API to the [Microduck](https://pollen-robotics.com/microduck/) from Pollen Robotics. The OpenAI team reported that it quickly chose the robot's next action.

### Can it classify support tickets?

📹 [12:48](https://www.youtube.com/watch?v=wrw9xA541Fk&t=768)

Justin plans to test Decision-1 for classifying tickets in his professional services automation (PSA) tool. Classification is one of the clearest use cases for a decision model.

## What context window do decision models support?

📹 [13:08](https://www.youtube.com/watch?v=wrw9xA541Fk&t=788)

Pablo asked how relevant the context window is for these use cases and how Decision-1 compares with other models:

* **Microsoft-Decision-1:** Up to 32,768 input tokens, according to its model catalog details.
* **Jev 1.13:** 64K on OpenRouter, according to Pablo.
* **OpenAI Decisions API:** No context window was listed on the Decisions documentation. The API uses GPT-6 Luna, which has a 1 million-token context window, so the Decisions API most likely supports about 1 million tokens too. Pablo found that GPT-6 Luna Decisions has a 1,050,000-token context window, and testing confirmed it accepts at least 256K tokens.

### Demo: Measuring the Decisions API's token limit

📹 [16:35](https://www.youtube.com/watch?v=wrw9xA541Fk&t=995)

To find the limit, increasingly large text files were sent to the Decisions API. A 64K-token file pasted into the [Decisions playground](https://platform.openai.com/decisions?lang=python) went through, but the playground does not show token usage. The [run_decision.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/run_decision.py) script sends a test file with a single predicate question and prints the full response, which includes the input token count. It requires the latest `openai` package, which includes the Decisions API.

The results:

* [test_120k_tokens.txt](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/test_120k_tokens.txt) reported 95,000 input tokens. The generated files only roughly estimate their token counts.
* [test_256k_tokens.txt](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/test_256k_tokens.txt) succeeded.
* [test_1m_tokens.txt](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/test_1m_tokens.txt) exceeded the token limit, so it was probably slightly over 1 million tokens.

## Demo: Testing image decisions with the OpenAI Decisions API

📹 [24:46](https://www.youtube.com/watch?v=wrw9xA541Fk&t=1486)

Justin asked whether the API can recognize what is in an image, such as a dog. The first image test, [check_image.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_image.py), checked a product photo for visible damage and worked.

The [chat vision notebook](https://github.com/Azure-Samples/openai-chat-vision-quickstart/blob/main/notebooks/chat_vision.ipynb) in the OpenAI chat vision quickstart has many image examples that can be rewritten as decision questions. GitHub Copilot ported them to separate Python scripts based on the image-check example, with shared helpers in [image_utils.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/image_utils.py), and copied the images.

| Script | Question | Type | Result |
| --- | --- | --- | --- |
| [check_image.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_image.py) | Does the product have visible damage? | Predicate | Worked as expected |
| [check_unicorn_url.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_unicorn_url.py) | Is this a unicorn? | Predicate | 0 (correct) |
| [check_reptile.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_reptile.py) | Are the reptiles alligators? Are they crocodiles? | Two predicates | Alligator 0.91, crocodile 0.67 (wrong) |
| [check_reptile.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_reptile.py) | Are the reptiles alligators or crocodiles? | Choice with descriptions | Alligator 0.73, crocodile 0.26, other 0.01 (wrong) |
| [check_menu_vegan.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_menu_vegan.py) | Is anything on this menu suitable for vegans? | Predicate | 0.45 |
| [check_insurance_claim.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_insurance_claim.py) | Is the damage consistent with a hail claim? | Predicate | 0 (correct) |
| [check_tree_cover_loss.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_tree_cover_loss.py) | Which zone is losing the most trees? | Choice | Tropical 1.0 (correct) |
| [check_plant_table.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_plant_table.py) | Is any plant priced under $10? | Predicate | 1.0 (correct) |
| [check_architecture_diagram.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_architecture_diagram.py) | Is this an architecture diagram, and does it need alt text? | Two predicates | Not run |
| [check_dishwasher.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_dishwasher.py) | Does the dishwasher have a visible quick wash option? | Predicate | Not run |

Notes on the results:

* **Vegan menu:** A yes-or-no question like this is not a great test because the menu probably has at least one vegan item.
* **Insurance claim:** The photo shows a very dented car. Hail would have to be massive to cause that damage, so the correct answer is no. The first run failed because the script used a system message (see below).
* **Tree cover loss graph:** Copilot ported every example as a predicate because the example script it started from used one. This question works better as a choice among four climate zones. Pick the question type that fits each decision.
* **Reptiles:** The mystery reptile photo trips up many models. The reptiles are crocodiles, so both approaches were wrong. With two predicates, the probabilities do not add up to 1 because each predicate is scored independently. When two mutually exclusive predicates both score above 50%, the model is not very confident. As Nnamdi noted, it is easy to assume that the probabilities would add up to 1.

![Comparison of two Decisions API approaches for the mystery reptile photo: two predicate questions returned 91% alligator and 67% crocodile, while one choice question chose alligator at 73%, crocodile at 26%, and other at 1%](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/alligators_crocs.png?raw=true)

### Can you run the same code multiple times?

📹 [30:35](https://www.youtube.com/watch?v=wrw9xA541Fk&t=1835)

Repeated runs returned very similar results. Jev is not deterministic because it is optimized for speed, performance, and cost, but its team has said it is open to adding a seed parameter. The new OpenAI models do not have a seed parameter either, although their results were very predictable here.

### The Decisions API doesn't accept system messages

📹 [33:35](https://www.youtube.com/watch?v=wrw9xA541Fk&t=2015)

The insurance claim script failed with an invalid value error saying that the role must be `user`. Every input example in the Decisions API documentation uses the `user` role, so put any system-style instructions in the user input or question instructions instead.

### Choice questions with descriptions

📹 [35:53](https://www.youtube.com/watch?v=wrw9xA541Fk&t=2153)

Choice options can include description fields that give the model more information. The rewritten reptile check used a choice question with descriptions of alligator and crocodile snouts, plus an `other` option. When you give a model a fixed set of choices, always include an option for unexpected input.

Even with those hints, the model still chose alligator, with 73% probability versus 26% for crocodile. Do not rely on GPT-6 Luna decisions to identify animals. This was surprising because GPT-4o mini handled this kind of check much earlier. The cause is unclear. Test decision models on your own use case.

### Questions that need free-text answers

📹 [38:01](https://www.youtube.com/watch?v=wrw9xA541Fk&t=2281)

The original notebook asked, "What is the cheapest plant?" A decision model cannot answer directly because the answer requires reading every plant in the table and returning one as free text. The port, [check_plant_table.py](https://github.com/pamelafox/office-hours-writeups/blob/main/office-hours/2026_10_13/check_plant_table.py), instead asked whether any plant cost less than $10, and the API correctly returned 1.0.

To answer the original question, build a multistep workflow. First extract the plant names with an LLM or OCR model, then send them as choices to the decision model.

## Discussion: Choosing a decision model

📹 [39:41](https://www.youtube.com/watch?v=wrw9xA541Fk&t=2381)

The OpenAI Decisions API's context window is most likely about 1 million tokens, matching GPT-6 Luna. That is much larger than Decision-1's or Jev's. Choose a model based on your inputs:

* **Image inputs or long context:** Use the OpenAI Decisions API. Hopefully it will come to Azure soon.
* **Text-only inputs under 32K tokens:** Try Microsoft-Decision-1.

In every case, test the model on your own examples because model behavior differs.

## Announcement: HydraFusion in VS Code and the GitHub Copilot app

📹 [41:34](https://www.youtube.com/watch?v=wrw9xA541Fk&t=2494)

[HydraFusion is now available in VS Code and the GitHub Copilot app](https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app/). It was previously available only in Copilot CLI. 

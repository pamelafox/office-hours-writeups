🔁 Have you tried dynamic workflows in the GitHub Copilot app or CLI yet?

Dynamic workflows let you define in code how Copilot carries out a task. You can split work into phases, fan it out to subagents in parallel, and get structured results back. Because the orchestration is JavaScript instead of a Markdown skill, it's much more deterministic: you can read exactly what will happen.

In my office hours today, we asked Copilot to make a "review-changed" workflow that:

1️⃣ Lists every changed file on the branch with git
2️⃣ Starts one reviewer subagent per file, each returning findings in a JSON schema (severity, line, title, explanation)
3️⃣ Sorts the findings by severity and has an agent write a summary report

My branch had ~300 changed files, so it spun up ~300 subagents. 😅 Lesson learned: tell it to skip data files!

The Copilot app makes it easy to follow along: a workflow panel shows each phase, AI credits used, how many agents are live, and the status of every subagent. You can pause or cancel the run, and click into any subagent's session to inspect its prompt and results.

You can check out the workflow code here:
https://gist.github.com/pamelafox/dd6c3ad66933105affcaf838f6a02f92

Watch the demo:
https://www.youtube.com/watch?v=M9IF-ymn5sU&t=1037

Docs:
https://docs.github.com/en/copilot/concepts/agents/dynamic-workflows

Join us live every week: http://aka.ms/pythonai/oh

#GitHubCopilot #AIAgents #DeveloperTools #AI

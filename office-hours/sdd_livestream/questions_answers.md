# Spec Kit (Spec-Driven Development) Livestream

This livestream demonstrates building a printable charades card generator using Spec Kit, a tool for spec-driven development (SDD).

## What is Spec Kit and how do you get started?

📹 [0:03](https://youtube.com/watch?v=8PjRfFluB2g&t=3)

Spec Kit is a way of doing **spec-driven development (SDD)** - you start with a specification which becomes executable. It's from GitHub and uses a structured approach with multiple agents for different phases of development.

To get started:

1. Install the Specify CLI using `uv tool install specify`
2. Create a new project with the CLI - it will ask you to choose your AI assistant (like Copilot) and script type
3. Open the project in VS Code - the slash commands are available in the assistant

The workflow follows these steps: constitution → specify → plan → tasks → implement. Each step is implemented as an agent with potential handoffs to other agents.

Links shared:

* [Spec Kit on GitHub](https://github.com/github/spec-kit)

## What does the constitution step do?

📹 [4:51](https://youtube.com/watch?v=8PjRfFluB2g&t=291)

The constitution creates project governing principles and development guidelines that guide all subsequent development. It focuses on code quality and testing standards.

However, you might want to point to your own existing best practices (like Python best practices, Bicep best practices) rather than having the LLM generate generic ones from scratch for every project.

## How does the specify step work?

📹 [8:18](https://youtube.com/watch?v=8PjRfFluB2g&t=498)

The specify step is where you describe what you want to build. The agent then:

1. Creates a numbered git branch (like `001-charade-cards`)
2. Writes a spec using user stories in "given/when/then" format (similar to behavioral testing)
3. Creates a checklist to validate the specification completeness
4. Shows potential handoffs (build technical plan or clarify spec requirements)

For the demo, the spec was: "Make a static app that generates printable charade cards across different themes, with words and emojis/Wikipedia images, easy to cut into squares."

## How does the plan step work?

📹 [15:56](https://youtube.com/watch?v=8PjRfFluB2g&t=956)

After specifying what you want, the plan step creates a technical implementation plan. You can provide constraints like:

- Using vanilla HTML and web components (no React)
- No build system
- No backend - all cards precomputed and stored in JSON
- Deploying to GitHub Pages

The plan agent:

1. Generates research.md with technology decisions
2. Creates data models and contracts (JSON schemas)
3. Determines testing approach (Vitest for unit tests, Playwright for E2E)

One caveat: the agent may add features you don't need (like service worker caching). You should read through the plan and provide feedback to remove unnecessary items.

## What does the tasks step produce?

📹 [24:43](https://youtube.com/watch?v=8PjRfFluB2g&t=1483)

The tasks step breaks down the plan into actionable items. For this project, it generated:

- 55 total tasks
- 16 parallel opportunities
- 6 phases (Phase 0-5 plus future features)

The tasks are organized in `task.md` with checkboxes. Features that aren't needed immediately (like Wikipedia image support) get moved to a "future" section.

## How does implementation work with Spec Kit?

📹 [32:11](https://youtube.com/watch?v=8PjRfFluB2g&t=1931)

When you run `speckit.implement`, the agent:

1. Reads the task.md file and implements features phase by phase
2. Marks tasks with X's as they're completed
3. Creates the actual files (HTML, CSS, JavaScript, JSON data for themes)

For this demo, phases 0-3 were implemented first to create a working MVP with an animals theme. The agent created:

- Custom HTML elements (web components) for cards
- CSS with print styles
- JSON files for themes (animals, food, actions, holidays, occupations)
- A basic static app structure

## What do colleagues think about Spec Kit?

📹 [47:19](https://youtube.com/watch?v=8PjRfFluB2g&t=2839)

Feedback from colleagues:

- **Overkill for small products** - you have to iterate over and over especially in the task phase
- **Works well with strong PRDs combined with a few skills.md files** - a more lightweight alternative approach
- Spec Kit was made when models weren't as good and needed more handholding; current models are quite capable

The key takeaway: use Spec Kit as **inspiration** for what might work for your organization. Maybe you don't need all the steps but you like the idea of having a plan file with tasks that get marked off.

### Will this approach work for a project we already started?

📹 [48:16](https://youtube.com/watch?v=8PjRfFluB2g&t=2896)

You could potentially use it for a big new feature. The options are:

1. **Bring in the directories** - Copy the `.specify` and `.agents` directories into your repo. You can use `specify init` in the current directory (with `--no-git` flag) instead of creating a new one.
2. **Adopt a similar lightweight approach** - Have an agent that writes out a product plan, then another agent that turns that into an implementation plan. This is similar to the approach Nicholas Zakas uses.

Links shared:

* [Nicholas Zakas' approach](https://humanwhocodes.com/blog/2025/01/creating-github-copilot-extension-part-1/)

## How do you see the context window usage in VS Code?

📹 [32:56](https://youtube.com/watch?v=8PjRfFluB2g&t=1976)

VS Code automatically compacts (summarizes) the conversation when approaching the context window limit. You can view context window usage by:

1. Looking for the context indicator in the chat
2. Clicking to see breakdown: system instructions, tool definitions, user context, tool results, messages, files

In the demo, after summarization the context was at 72%:
- System instructions: 5.8%
- Tool definitions: 12%
- User context: 31%
- Tool results: 18%
- Messages: largest portion

## What's the recommended approach for testing?

📹 [46:19](https://youtube.com/watch?v=8PjRfFluB2g&t=2779)

For front-end apps, **end-to-end tests are more useful** than unit tests because there's so much mocked out in unit tests. Kent C. Dodds argues we should start with E2E tests as you learn more from them.

However, **if you're still actively figuring out what you want**, writing tests early can be annoying because every change requires rewriting tests. It's better to wait until you know you like something before adding tests, to speed up development time.

## Pro tip: Use ASCII diagrams for UI feedback

📹 [1:05:40](https://youtube.com/watch?v=8PjRfFluB2g&t=3940)

When looking for UI feedback on component design, ask the AI to generate ASCII mockups. For example, when deciding how to implement a difficulty filter (easy/medium/hard), the AI generated ASCII diagrams showing:

- Checkbox pills
- Toggle buttons
- Slider
- Dropdown options

This gives a quick visual comparison without implementing anything.

## How does the task-to-issues feature work?

📹 [1:07:44](https://youtube.com/watch?v=8PjRfFluB2g&t=4064)

Spec Kit can convert incomplete tasks to GitHub issues automatically. The agent:

1. Checks for a git remote origin
2. Reads through task.md
3. Creates issues for incomplete tasks in the repository

This is useful for handing off work or delegating to Copilot coding agent. Note: The agent needs terminal access and the GitHub MCP server tools to work properly.

### Do you code in Rust?

📹 [58:20](https://youtube.com/watch?v=8PjRfFluB2g&t=3500)

No, but Rust is very popular in the Python community - UV, Ruff, and Ty (type checker) are all written in Rust, along with many other Python packages. With LLMs, it's easier to dip in and out of different languages even if you're not an expert in them.

## Final project

Links shared:

* [pamelafox/speckit-project](https://github.com/pamelafox/speckit-project) - The completed charades card generator

[00:01] Okay, welcome to our last office hours
[00:04] in the Python agents live stream series.
[00:08] Uh so this office hours is after the
[00:10] talk I just gave about adding a human in
[00:12] the loop to workflows. Uh so if you do
[00:16] have any questions just put them in the
[00:18] chat um about today or about everything
[00:21] we've covered or just Python and AI
[00:24] generally.
[00:27] All right, so we have the first
[00:28] question. What are some realw world use
[00:30] cases for the handoff with interaction
[00:33] pattern? Um, you know, some points
[00:35] regarding the human being potentially
[00:39] offline.
[00:40] Yeah. So, the example I showed, I mean,
[00:42] this one was a um was, you know, is
[00:46] designed to to be a real world use case
[00:49] where you're um, you know, you're you're
[00:52] chatting at multiple potential agents
[00:54] that can help you out. Now there the
[00:57] checkpoint storage here I think is just
[01:00] in memory. So I don't think this one
[01:02] does resuming
[01:04] um like at least not like across
[01:06] sessions. Um but uh what you c you could
[01:09] do is um you know basically if you're
[01:13] using like a database checkpoint storage
[01:16] and if you associate the checkpoints
[01:18] with the user then um you know then when
[01:23] the user revisits the the site you could
[01:25] imagine pop like checking to see like
[01:28] okay um you know is there a flow
[01:32] associated with this user? In this case,
[01:35] I think you could just scope it to the
[01:36] user. Uh I don't think the user would
[01:38] have like multiple conversations going.
[01:39] You could even if you had chat like if
[01:41] this had chat history, right? Um if
[01:43] there was a history of your
[01:44] conversations and you could actually
[01:45] resume any of the in the conversations,
[01:48] right? Because it's kind of a similar in
[01:51] this case to um to like a chat history.
[01:54] Um so
[01:58] so yeah so the for the handoff uh I I
[02:01] think it's designed for cases like this
[02:04] um where you you have like multiple
[02:07] potential people like kind of like it's
[02:10] say like this is like a what do we call
[02:11] a phone tree. We used to have these
[02:13] customer well we still have them where
[02:15] you're getting customer service you call
[02:17] and it's like do you want help with this
[02:19] this and this right and you get directed
[02:20] to that particular person and then they
[02:22] like pass you around from one to the
[02:24] other and the most annoying thing there
[02:25] is that you spend like 20 minutes on the
[02:27] line waiting to get passed to the next
[02:29] person and the next person like forgets
[02:30] everything. This is like better because
[02:32] you know that the whole conversation
[02:33] gets passed off between each agent and
[02:36] the handoff is a lot faster. So even if
[02:38] they are going back and forth like they
[02:39] did a couple times in the the demo, it's
[02:42] a lot faster because uh we're not, you
[02:44] know, waiting on the line for an actual
[02:45] human to be available. So I think of
[02:47] this as like the phone tree um scenario
[02:50] where you you have these like specialist
[02:53] agents because um you you know generally
[02:57] specialist agents can be a little more
[02:59] successful at their task because they're
[03:01] you know scoped down. So if you're able
[03:03] but the tricky thing there is like you
[03:05] have to make sure that they have the
[03:06] flexibility to handle everything. So if
[03:08] you can you know map the domains of the
[03:12] task it's like and break them down into
[03:16] specialist agents and it's very clear
[03:18] what the boundaries are like the example
[03:19] I gave actually was not a very good um
[03:23] example where was the this one order
[03:25] agent and return agent. I was doing so
[03:27] much like prompt engineering this
[03:29] morning to like get the triage agent to
[03:32] go to the right agent because orders and
[03:34] returns are too similar. Like they
[03:37] overlap too much and there's just not
[03:38] enough information here. Um I think the
[03:41] banking assistant is much clearer in um
[03:45] like first of all it's like triage uh
[03:47] orchestrator is like much more verbose
[03:49] right? So, it has all these, you know,
[03:52] um, you know, really specific things
[03:55] like, okay, you're going to do here.
[03:59] Um,
[04:02] and then I bet the agents themselves
[04:04] have clear descriptions on them, right?
[04:07] So, if you are using handoff, it is very
[04:09] important that it's really, really
[04:11] clear, you know, who's handling what
[04:14] because otherwise you just get too much
[04:16] like too much uh weird back and forth.
[04:21] Okay. Um, so yeah, so I would I would
[04:24] try it for snares like this, but just
[04:25] keep all that in mind.
[04:28] All right. So, Honor says, "When
[04:30] building agents, does it make sense to
[04:32] use an MCP or just use the underlying
[04:34] Python message uh methods?" Uh, yeah. I
[04:37] think this is an architectural decision
[04:39] and I think MCP just like it's useful
[04:42] for reusability. Um, I I don't I
[04:45] wouldn't I wouldn't necessarily make
[04:47] something
[04:49] an MCP
[04:51] server unless you're going to use it in
[04:55] multiple contexts. And also maybe if
[04:56] you're going to use like if you if you
[04:59] ever intend to use that MCP server like
[05:01] in a you know a generic application like
[05:04] VS Code then you know then you might as
[05:06] well make it an actual server right
[05:08] because one thing that's worth pointing
[05:09] out is that MCP is is actually more than
[05:12] just tools. I know I always talk about
[05:14] the tools part of MCP, but it it does
[05:16] involve a lot more um a lot more
[05:20] capabilities um that are useful when
[05:22] it's used inside something like uh you
[05:24] know cloud or VS code where it can
[05:26] actually like go back and forth with the
[05:28] user and it can be like more
[05:31] collaborative, right? Because an API or
[05:34] just a tool like you know it can do the
[05:36] thing and return the value. MCP has
[05:39] tools, but it also has stuff like
[05:41] elicitations where you can ask for more
[05:43] information from the user. So that all
[05:44] matters when an MCP server is being used
[05:46] in the context of something like VS Code
[05:48] or Claude. Uh but if you're just using
[05:50] it from your own agents, well then
[05:52] you're, you know, you're probably just
[05:53] using it like tools. So if your agent
[05:55] just needs access to some functionality
[05:58] some you know some API calls and you you
[06:01] don't have any other uh reasons to turn
[06:05] those into MCP server then I think you
[06:08] can just just keep them as tools right
[06:11] uh I would I would only go as far as an
[06:13] MCP server when you want additional
[06:16] portability and reusability like within
[06:18] your organization or across different
[06:20] MCP clients.
[06:25] Um,
[06:26] okay. So, KA says the way to create a
[06:31] human in the loop workflow in an API is
[06:34] to use
[06:36] checkpoints, right? Um,
[06:40] so generally, you know, well, you can it
[06:44] depends, right? like if it's if it's
[06:46] like a durable like you need checkpoints
[06:48] for being able to resume workflows like
[06:52] over time between uh you know a process
[06:55] exiting. Um if everything is happening
[06:59] at once and the human is there the whole
[07:01] time, you don't necessarily need need
[07:03] checkpoints. Um but if you want to like
[07:06] run a workflow and sometimes that
[07:09] workflow is going to um you know going
[07:12] to need human intervention then you can
[07:16] uh you know detect that and um you know
[07:20] when when there's no human there you can
[07:22] just exit and then you can have a way of
[07:26] finding all the workflows that need
[07:27] resuming. Uh, one thing I wanted to do
[07:29] that I didn't have time to do was to
[07:31] implement um, agent inbox for agent
[07:35] framework. So this is it's just a react
[07:37] application that's built on top of lang
[07:39] chains um, linksmith which finds looks
[07:43] basically for all the what they call
[07:45] them interrupted
[07:47] um, agent threads right and say okay
[07:49] this one's you know all these agents
[07:50] have been interrupted and they require
[07:52] action from you. So I think this is a
[07:54] nice uh this is a nice kind of interface
[07:57] for
[07:59] uh surfacing paused workflows that that
[08:03] require additional intervention to keep
[08:06] going. So you can imagine if I was going
[08:08] to reimplement this I would uh be
[08:10] looking through I'd be storing the
[08:12] checkpoints like in my database. I'd be
[08:14] looking through to find the latest
[08:16] checkpoint for each workflow. check to
[08:17] see and I'd probably have another table
[08:19] like keeping track of workflows and just
[08:21] saying like oh this workflow is not
[08:23] complete maybe something like that I
[08:24] have to think through exactly how I want
[08:26] to uh implement it um and then you you
[08:29] know you would just you know you log in
[08:30] in the morning you check your uh you
[08:33] know workflow inbox and say oh okay
[08:35] these workflows are paused they need my
[08:38] further action let me take the action
[08:40] and then you know and then the the code
[08:42] in the background would resume so that's
[08:45] that's one um potential way working with
[08:48] workflows like the kind of workflows
[08:49] that might you know be running in the
[08:51] background but occasionally need human
[08:53] input. Uh that would be a way of doing
[08:55] it. There's another version of agent
[08:57] inbox
[08:59] uh human in the loop. So this is for
[09:02] this durability.

[00:00] Let's get started with this week's
[00:04] Python AI weekly office hours.
[00:07] Uh, and uh, this week is a little bit of
[00:10] a funny week for me since I am in the
[00:12] Microsoft Redmond office. I'm here for
[00:15] MVP summit. So, I don't know if any of
[00:17] you are here right now, which would be
[00:19] funny. Um, but, uh, yeah, MVC summit is
[00:22] bringing together lots of MVPs and also
[00:24] just generally lots of folks from
[00:27] Microsoft product team. So I'm actually
[00:29] in the office of the AZD team, the Azure
[00:32] developer CLI, and it's fantastic
[00:34] because I'm getting all my bugs fixed.
[00:37] Uh so I love getting to sit with the
[00:39] product teams and just directly uh uh
[00:43] you know debugging things with them. So
[00:45] what is going on right now? Um uh there
[00:49] is a new release candidate for agent
[00:52] framework. So if any of you are you know
[00:54] very eager to for agent framework to go
[00:57] GA generally available. So as a reminder
[00:59] agent framework is the successor to
[01:02] semantic kernel and autogen. So if you
[01:04] were using autogen or semantic kernel we
[01:06] would recommend moving over to agent
[01:08] framework. You can see that March 19th
[01:11] there's this new release candidate RC5
[01:14] and um we're currently bug bashing it.
[01:16] So I actually tested it out this morning
[01:18] and started porting all of our examples
[01:22] to use this latest version instead. Uh
[01:25] so that means we are getting closer to
[01:27] GA. So hoping for GA to happen you know
[01:31] I was told originally like end of March
[01:33] early April and uh yeah and I think
[01:37] they're they're feeling pretty good
[01:38] about this release candidate. Uh that
[01:40] that's why they're doing a big bug bash
[01:42] right now internally. Uh but and you can
[01:44] also test it yourself if you are already
[01:47] developing with agent framework. So
[01:49] that's cool. Uh let's see there's this
[01:51] blog post that I was just going through
[01:52] this morning with the AZD team and uh
[01:56] this just came out yesterday
[01:59] and here let me post it in the chat.
[02:04] So this blog post is about how you can
[02:08] deploy your own agents using either
[02:11] agent framework or lang chain deploy
[02:14] them to Microsoft foundry so they become
[02:16] what's known as a foundry hosted agent.
[02:19] Now I actually have not yet um done
[02:23] this. I I'm I'm working my way through
[02:25] this currently and working through
[02:27] various um issues with my ACD. Um but um
[02:32] but I'm excited about it because it
[02:34] means you can we can use agent
[02:35] frameworks that we like uh but then get
[02:38] the benefits of of foundry right so I do
[02:41] have this uh example checked out here so
[02:44] you can see this one I think this one is
[02:46] using was using this one's using agent
[02:48] framework right so you can do agent
[02:49] framework um or or do lang chain so
[02:55] what's exciting is that I'm going to
[02:57] have a good excuse to get really um deep
[03:00] into this because we are working on our
[03:02] next hosted series and our next our next
[03:06] live stream series, right? Because you
[03:07] know we love to do the live stream
[03:08] series. So this is going to be a
[03:10] three-part live stream series from April
[03:12] 28th to April 30th and it is going to be
[03:14] all about foundry hosted agents. Uh so
[03:17] we're going to do one day on Microsoft
[03:18] agent framework, one day on link chain
[03:20] and lingraph and then one day on um
[03:24] quality and safety evaluations.
[03:26] And um actually that's what I really
[03:28] like about Foundry is that if you're
[03:30] using Foundry agent service or Foundry
[03:32] hosted agents then you get online you
[03:35] get online evaluations meaning that like
[03:37] a sample of the traces from your agents
[03:40] are actually evaluated as they come
[03:42] through like you know real time like
[03:44] from actual users. You can set that up
[03:46] and you also get scheduled evaluations.
[03:48] So you can actually uh say hey every day
[03:51] we're going to run this evaluation and
[03:52] make sure that things are good. And the
[03:54] same thing with red teaming.
[03:57] Uh so yeah, so that's what we'll be
[03:59] talking about. So you can if you if you
[04:01] want to get started today, you can you
[04:03] know there is already documentation.
[04:04] There's this blog post here. That's the
[04:06] one I was going through, but there's
[04:07] also um another the other one is
[04:13] this one. Um,
[04:16] so you can you can try either of these
[04:20] uh you know either of these, but you can
[04:22] also wait uh until there's some
[04:24] improvements to the service because not
[04:26] like not everything works yet that you
[04:28] know that I talk about in this
[04:29] description, but it will all work by you
[04:32] know April 28th. So um yeah, so just
[04:36] stay tuned. We will start having
[04:38] registration pages open for this uh for
[04:42] this series.
[04:45] Uh, so there we go. So that's cool.
[04:48] And what else am I working on right now?
[04:51] I've been working on a big effort to
[04:53] port chat completions API to responses
[04:55] API. I mentioned that last week and I've
[04:58] made a lot of progress since then. Uh,
[05:00] let me me open up my
[05:04] uh my repo where I'm keeping track of
[05:07] this.
[05:12] Okay.
[05:14] So here,
[05:19] all right. So you can see what I've done
[05:20] is uh I went through well me I I GitHub
[05:25] Copilot go through all of my repos and
[05:27] check to see what API flavor they're
[05:30] using right now and you know marked
[05:32] whether they're using chat completions
[05:34] or responses. Now originally these all
[05:36] said chat completions
[05:38] um and then you know uh also whether
[05:41] you're using GitHub models. This is an
[05:42] issue since GitHub models only support
[05:44] chat completion. So whenever I port from
[05:47] chat completions to responses API, we
[05:48] will no longer have a path to use GitHub
[05:51] models, which is a shame, but there's so
[05:54] many benefits to responses API. So we
[05:56] decided it's worth it to port to
[05:57] responses API because then you get the
[06:00] built-in uh you know code interpreter
[06:02] and web search tool and it's just you
[06:04] know it's just a much more powerful API.
[06:07] Um so we are but yeah it does mean you
[06:10] lose support for GitHub models which is
[06:12] nice for our you know live stream series
[06:15] and uh and yeah and then you know
[06:17] there's some other things. So I'm going
[06:18] through them and pointing them to
[06:20] responses API. Now I'm I'm not doing it.
[06:22] I'm having co-pilot do it using this um
[06:26] basically you know custom agent that
[06:29] we're we're working on. Uh so here's the
[06:32] repo for that. So if you do have any
[06:36] repos right now that are using chat
[06:38] completions and you're feeling ready to
[06:40] port them to responses API then
[06:45] uh you can go and you you basically
[06:49] you add it to your you know to your to
[06:52] your repo and then
[06:54] um and then yeah it'll just it'll do the
[06:56] port for you. Am I sharing my screen?
[06:59] Oh, stream just ended. Thank you. All
[07:01] right, we'll go back to Discord and we
[07:04] will restart the stream. Thank you. Here
[07:07] we go. Lost. Yep. Yeah, Discord likes to
[07:10] kill it sometimes.
[07:12] It does not bounce back. Discord does
[07:14] not bounce back. Discord doesn't believe
[07:17] in bouncing back. That would be too
[07:19] easy. Um, so, okay. But we have it back.
[07:22] Let me also check the the uh Streamyard.
[07:29] Oh my gosh.
[07:34] Okay, let me go to Streamyard and see
[07:37] Streamyard still looks good. It didn't
[07:39] lose it. Okay, great. Okay, so yeah, so
[07:41] this is a uh this repo here. What you
[07:45] can do, the easiest thing to do is
[07:47] actually open your repo in VS Code that
[07:50] is using track completions and then just
[07:53] add like check out this repo and add it
[07:55] to the workspace because this repo has
[07:57] all these like skills in it. Uh, and
[07:59] then you just put this in co-pilot chat
[08:02] and then it'll just do everything. Um,
[08:06] which is cool. Uh, I've I've only had to
[08:09] do like a little bit of followup and
[08:10] only because a lot of my repos had a lot
[08:12] of other kind of old issues in it. But
[08:13] yeah, you can see here we've got skills.
[08:16] So, it knows it's got various like
[08:18] scripts in here and documentation.
[08:22] And then it has an agent and that agent,
[08:24] you know, knows how to
[08:27] um, you know, use the skills here.
[08:32] So, so there we go. So, I do recommend
[08:34] moving to responses API if you can. Um,
[08:39] you know, let me know if there's any
[08:40] blockers for you. We're we're trying to
[08:42] get more people over. And then also if
[08:44] you're if you're not using it yet and
[08:45] you you know you just want to get um
[08:48] started with it then the repo I
[08:51] recommend is this one and this one um
[08:57] has it it just starts you off with
[09:00] responses API and it's got the infra in
[09:03] it to deploy things the right way and so
[09:07] this way and the nice thing about
[09:08] responses API is that once you move to
[09:10] it then your code can support deep sea
[09:13] and llama like basically all of the
[09:15] Azure direct models it's going to
[09:17] support.
[09:19] Uh can I explain the difference between
[09:21] chat completion API and responses API?
[09:24] Yeah, so I mean they look actually
[09:26] really similar like I can show you um
[09:30] uh let me look for the
[09:34] uh a recent PR.
[09:37] Okay. Right. So this was
[09:40] uh like here. Okay,
[09:44] so the actual code is pretty minimal,
[09:48] right? So, you know, instead of
[09:50] chat.comp completions.create,
[09:52] we have responses.create
[09:55] and it takes an input. Now, one thing
[09:57] that's interesting here is this store
[10:00] parameter. And that actually is a
[10:02] potential difference is that the
[10:04] responses API, so chat completions API
[10:08] is always stateless. So that if you want
[10:11] to do a multi-turn conversation with the
[10:13] chat completions API, you do need to
[10:16] pass in
[10:18] all the previous messages, right? And
[10:20] you basically build back up the history
[10:21] and say, "Hey, this is what we talked
[10:23] about before. Here it is, right?" And
[10:24] normally that's pretty easy to do,
[10:25] right? You've got it either stored in
[10:27] your front end, like you you just pass
[10:28] along pretty easily. But the responses
[10:30] API does have this feature um where you
[10:33] can say store equals true and then it
[10:35] will actually basically create like an
[10:38] ID that identifies your your current
[10:40] thread and then if you're doing
[10:42] multi-turn you can just reference that
[10:44] ID and it will be stored. Uh but you can
[10:47] turn this off as well if like because
[10:49] some people have issues with that from
[10:50] like a privacy and logging perspective
[10:53] right. Um so you can turn it off with
[10:56] store equals false as well. So here I'm
[10:58] using store equals false just because
[10:59] that's you know chat completion never
[11:02] had the ability to store. So the easiest
[11:04] when I'm porting over it's easiest just
[11:05] to to have store equals false. But
[11:08] that's definitely something you can take
[11:09] advantage of. Let me find our
[11:10] documentation about it because there's
[11:12] some more details about like encryption
[11:14] um when you're actually uh using it. Let
[11:18] me find the docs. Yeah. Does it store on
[11:20] the OpenAI server? So for Azure OpenAI
[11:23] it would store on the Azure servers,
[11:26] right?
[11:27] um
[11:29] uh retrieve. Okay. So, here you can see
[11:31] like when you um you know when you use
[11:34] it, you'll you'll get like a response uh
[11:38] a response ID and you can actually
[11:41] you know you can retrieve you can
[11:43] retrieve it based off ID. So, this would
[11:45] be stored on Azure servers, right? Um
[11:48] and let's see it's retained for 30 days
[11:50] by default. Um you can have it
[11:52] explicitly delete it. Um, presumably you
[11:54] could extend that because I would think
[11:57] that you'd want to be able to
[11:58] potentially keep some of them forever.
[12:00] But here you can see this is how you do
[12:01] multi uh a multi-turn conversation. If
[12:04] you wanted to take advantage of this,
[12:06] you'd say, okay, client.responses create
[12:08] previous response ID equals response ID,
[12:10] right? And that's going to bring in all
[12:12] the previous responses and tool calls
[12:14] and stuff like that. Um, so now it gets
[12:17] the full context. Um
[12:22] but then this is like this would be your
[12:24] more manual way of doing it, right?
[12:25] Where you can build back up the inputs.
[12:26] So you can do it either way. Uh there is
[12:29] compa you can do compaction. Uh let's
[12:32] see. Okay. I haven't messed with that at
[12:34] all yet. Oh, there's
[12:36] client.responses.compact.
[12:37] Okay. Didn't know about that. Uh oh,
[12:40] there's also server side compaction.
[12:42] More things to play with here. And then
[12:44] I wanted to show Oh, but this is what I
[12:46] really like about it is that you can
[12:47] just, you know, with one line of code,
[12:50] you can enable our code interpreter and
[12:52] that will run code in a sandbox
[12:55] environment on Azure container apps. And
[12:58] but this is all you have to do. All you
[12:59] have to do is say, hey, you now have the
[13:01] ability to use code interpreter. And
[13:03] then boom, you have the ability to use
[13:04] code interpreter. So that is what I'm
[13:06] like super excited about, right? So you
[13:08] can see it runs on container container
[13:10] apps. Uh, it has lots of file inputs and
[13:13] outputs. It can generate, you know,
[13:15] graphs for you with like metplot lib.
[13:17] That's what I use it for a lot. Um,
[13:19] let's see. We've got multimodal blah
[13:21] blah blah blah blah. Uh, you can also
[13:23] point it at remote MCP servers. So, it
[13:25] does have built-in support for remote
[13:27] MCP. So, that's really nice as well. Um,
[13:31] and then the other thing I want to show
[13:34] background tasks. Oh, that's uh 01
[13:36] models. Okay. All right. And then I want
[13:38] to show encrypted reasoning atoms. So
[13:40] this is one thing that's interesting. So
[13:42] when you're using responsive AI in
[13:43] stateless mode, you want you still want
[13:46] to preserve the reasoning context and
[13:48] that's quite that's that's that's
[13:51] tricky. So you have to include the
[13:53] encrypted reasoning items. So you have
[13:54] to like you have to first retrieve those
[13:58] by saying hey I need the reasoning the
[14:00] encrypted content and then once you
[14:03] retrieve that you have to like pass it
[14:05] back. Um so yeah so if you are doing
[14:08] stateless mode then and you're using a
[14:10] reasoning model and most of us these
[14:12] days are using reasoning models then you
[14:14] do want to um think about this aspect
[14:18] here. Uh once again if you if you use
[14:20] this the the you know the skill that
[14:23] ports it it should it should know about
[14:25] this.
[14:27] Uh so there we go. So let me also share
[14:29] this doc here because this is useful.
[14:35] All right. Uh, okay. So, we see a
[14:37] question from Lubis22.
[14:40] Would you be able to briefly explain why
[14:41] skills MD files can be a replacement for
[14:43] MCP approach? Not sure if this is fake
[14:45] news. Um, no, it's not fake news. Like,
[14:49] okay, so here's the whole thing. So,
[14:50] there's this whole thing about whether
[14:51] like, you know, MCP is dead. So, first
[14:54] of all, I have to share the best um the
[14:57] best thing. Uh, let me find it. Uh,
[15:01] okay. Here we go. All right. So, there
[15:05] was this whole thing on Twitter like two
[15:06] weeks ago, right? Which everyone's like,
[15:08] "Oh, MCB is dead. MCB is dead." And uh
[15:11] so, of course, there's going to be a
[15:12] funeral for MCP. So, if any of you are
[15:14] in New York City on April 1st, uh do
[15:17] come to the funeral for MCP. It is being
[15:20] put on by the Fast MCP maintainers. And
[15:23] of course, Fam Fast MCP is downloaded
[15:26] two million times a day. So, obviously,
[15:29] MCP is not dead. um because it's, you
[15:32] know, it's incredibly uh you know,
[15:34] popular uh technique. Now, um yeah, this
[15:39] you have to read this. This is it's so
[15:40] well done. I wish I could come. I
[15:42] thought I was going to be going, but I'm
[15:44] I'm not going to be there. Um hopefully
[15:46] my colleagues can go. I do encourage you
[15:48] to go and wear black. And in in order to
[15:50] RSVP, you actually send an MCP uh call,
[15:55] I believe. Um, and so anyway, so okay,
[15:59] but here's the deal is that when you are
[16:02] doing agentic coding, when you're using
[16:04] a coding agent with like GitHub copilot,
[16:07] MCP servers can be um, you know, a bit
[16:12] sometimes they're a bit overkill, right?
[16:13] Like they're a bit heavy. Like if you
[16:16] want to like load in lots of MTB
[16:18] servers, then there's lots of potential
[16:19] tools to pick from that can overwhelm
[16:21] your context. um because the like
[16:24] there's a lot of tool descriptions that
[16:26] goes in there. Whereas like with a
[16:28] skill, it's like you can be a lot more
[16:29] selective about it. Only the tool name
[16:32] and description gets put in the context.
[16:33] So it's it's easier to do kind of
[16:35] progressive loading with skills
[16:38] sometimes depending on what you're
[16:40] doing. So I would say that for if you
[16:43] when you're doing coding agents locally,
[16:46] you may find that actually it's more
[16:48] effective for you to just write a skill
[16:50] that you know knows how to do the thing
[16:52] that you're going to do a lot, right?
[16:54] And it's very easy to ask co-pilot to
[16:56] write a skill. Like what I always do,
[16:58] like if I need a new skill, um what I do
[17:00] is I I point it at the docs and I say,
[17:02] "Hey co-pilot, um you know, write me a
[17:06] skill." And I also here's the other
[17:08] thing I do. I say, "Write me a skill."
[17:10] and use you know for any scripts write a
[17:13] Python script that uses Python inline
[17:16] dependencies so that it can be run with
[17:19] UV run. Okay, so that is that is the
[17:21] prompt I do. Um, and a lot of times a
[17:23] good thing to do is like after you've
[17:24] successfully done something, you can
[17:26] tell the agent like, "Hey, you know,
[17:28] let's make a skill based off of this,
[17:30] you know, this conversation we just had
[17:32] that, you know, encapsulates that all
[17:34] right." Um, so then it's, you know, it's
[17:37] very good at doing that and it'll add it
[17:38] to either your GitHubskills or
[17:40] agent/skills, either one. And then, you
[17:43] know, it'll make it'll make your skills.
[17:45] So, you'll have your skill.mdb and it'll
[17:48] just have instructions and if there's
[17:49] any Python files, you know, can see how
[17:50] to run them. And then with the Python
[17:52] file, like once again, I recommend that
[17:54] you have it use um inline dependencies.
[17:58] That's a standard in the Python world.
[18:00] There's a PEP that explains it and the
[18:03] agents know how to know how to do it.
[18:05] So, you just tell it to use inline
[18:06] dependencies and it'll stick this at the
[18:08] top and that way it's super easy for the
[18:12] agent to run. You don't have to worry
[18:13] about your environment.
[18:15] Um, oh yeah. So, we see on awesome
[18:18] co-pilot there are a bunch of skills on
[18:21] there that you can use. Let's find the
[18:23] skills directory. Uh, skills, right? So,
[18:28] you can see here
[18:31] um you know, lots of good ideas for for
[18:34] skills. There's so many um
[18:38] I don't know if these all I don't know
[18:40] which of these are are um Python stuff.
[18:43] Let's see which one looks fun. Uh,
[18:46] Python. Let's find Python. Python.
[18:48] Python. Pi test coverage. Okay, this one
[18:51] is just a skilled MD because it didn't
[18:53] need a custom one. Most of mine do end
[18:55] up having Python scripts along with
[18:58] them, right? Um, so I have the two main
[19:02] places. Actually, I've started using
[19:04] skills in a lot of my repos and most of
[19:07] them are just like custom for me. Um, so
[19:09] I use it there. I use it um in my
[19:12] presentation writeups. One that has a
[19:15] bunch bunch of skills now.
[19:20] Uh so definitely if you're not, you
[19:23] know, already doing skills, you know,
[19:24] you definitely want to get in the habit
[19:26] of it. Um because there's you know it's
[19:29] just a you're doing some as soon as
[19:31] you're doing something multiple times
[19:32] and if you ever notice like that you
[19:34] know maybe the agent struggles a little
[19:36] bit to do it you know use the best API
[19:39] or use the best CLI or whatever like you
[19:42] know if you put in a skill then you have
[19:44] more confidence that it's going to use
[19:45] the right flow later. So I really like
[19:47] it for like functionality right I to me
[19:50] like I use MCP for like data access
[19:52] because MCP does have really nice
[19:54] authentication. So if I'm trying to
[19:56] access authenticated data, I would
[19:58] rather use an MCP server because MCP
[20:01] knows all about authentication. It's
[20:03] built in. VS Code knows how to
[20:04] authenticate using using OOTH, right? So
[20:06] I do prefer still using the GitHub MCP
[20:09] server versus the GitHub CLI. Some
[20:11] people prefer the GitHub CLI. Um but I
[20:14] will generally prefer the GitHub MCP
[20:15] server because it handles authentication
[20:17] better. Um but for functionality like
[20:20] all this stuff where it's like oh
[20:21] convert slides to images, extract a
[20:23] transcript you know like anything that
[20:25] is um you know like something you would
[20:28] do with a Python script uh then uh you
[20:32] know then I I I like using skills for
[20:34] that. So uh yeah so I would say um
[20:39] certainly for local coding
[20:42] uh you know people are reappreciating
[20:45] that skills plus you know Python scripts
[20:48] and CLI commands are very powerful and
[20:52] um you know it's just giving like the LM
[20:54] a little hint a little nudge like oh
[20:56] yeah here's like the good way of doing
[20:57] it but there's still a huge um need for
[21:02] MCP
[21:03] uh for all this like agent to agent um
[21:07] you know like communication like when
[21:08] you're setting up like if you're in a
[21:09] big organization
[21:11] people in these organizations like you
[21:13] know the way organizations work is they
[21:15] set up MCP servers and say okay we have
[21:17] all these common MCP servers that is
[21:20] going to expose data from different
[21:21] services in a structured way with
[21:24] authentication done the way it should be
[21:25] done right so we see so much interest
[21:28] for MCP from uh from organizations as a
[21:31] way of exposing especially a way of
[21:33] exposing service data
[21:35] And uh so I don't think MCP is going
[21:37] away there uh because I think there's
[21:40] like skills is not a replacement for it.
[21:42] But I also did talk with MCP maintainers
[21:45] a few weeks ago and there is an MCP
[21:47] skills working group where they're
[21:49] figuring out like how can MCP servers
[21:51] expose skills, right? So you are going
[21:54] to see MCP start to I think embrace
[21:57] skills to in in however way it can. Um,
[22:00] so that if MCP server wanted to include
[22:02] skills that there'd be a standard way of
[22:04] of doing that.
[22:07] Uh, let's see. Oh, um, I see that
[22:09] request to speak. I usually don't do
[22:11] audio on these because of how I'm doing
[22:13] the recording. So, you can put your like
[22:15] question in the chat and then we'll
[22:17] we'll see it there because recording
[22:19] only hears me.
[22:21] Um, let me check also. So, we have
[22:23] everything still running. Okay, good.
[22:25] Uh, yeah, that was a great question.
[22:27] Thank you. Thank you for asking that. Uh
[22:30] yeah, if you have not written a skill
[22:31] yet, do it. Uh you can either store
[22:35] them. I have some of my skills stored in
[22:36] my repos. And then uh you can also store
[22:39] so if you go here uh let's see like in
[22:42] VS code you can be like new skill file
[22:45] and here you can see that you can first
[22:47] in your repo you can pick
[22:49] from.github/skills.agent/skills.
[22:51] So aentskills is like the standard
[22:54] location. Now, I heard like Claude
[22:56] doesn't support it yet, which would be
[22:57] crazy, but Claude I guess they can be a
[23:00] little strangely as the authors of MCP,
[23:02] they can somehow be strangely slow to
[23:04] adopt stuff like agents.md and
[23:06] agent/skills.
[23:08] Uh, but anyway, um, so right now I think
[23:10] mine are on github/skills, but I'll
[23:12] probably move them to agentskills and
[23:15] then you can, but also that's inside the
[23:17] repo, right? If you have if you want
[23:18] skills that are just um you know at the
[23:21] global layer like let me check what's in
[23:23] my agents
[23:25] um agents slashsklls.
[23:29] Yeah. So you can see I have a few here
[23:32] that were um let me make this like way
[23:34] bigger. Some of these were added by
[23:36] extensions. So it looks like these two
[23:38] were added by extensions. And then this
[23:40] is um one that I added because it's this
[23:43] really common flow that I use is that
[23:45] whenever I get comments on APR, I use
[23:50] the agent to go through those comments
[23:52] and we collaborate on, you know, on
[23:54] reviewing those comments. And at first I
[23:56] was just putting it in every single
[23:57] repo, but then I was like, h I just want
[24:00] to have it, you know, always available
[24:02] on every single repo I'm on, right?
[24:04] Because for me, I've got like dozens,
[24:06] hundreds of repos. And um you know I I
[24:11] want to be able to do this flow on all
[24:12] of them.
[24:14] So yeah so you can you know you can
[24:15] store them personally you can store them
[24:17] in the repo. Um if you are in an
[24:20] organization what you might do is make a
[24:23] uh you know make a repo that has all the
[24:26] skills and so that's easy for people to
[24:28] pull from there. We have a we have a
[24:30] couple repos like that. Um, we have the
[24:34] uh let me find the Azure co-pilot skills
[24:39] GitHub repo.
[24:41] Find this. Okay, unfortunately we
[24:44] haven't quite all decided on exactly
[24:47] where
[24:49] um this one. Okay, this is I think this
[24:52] is the one one hour ago. That looks
[24:54] good. Azure skills plugin
[24:57] and
[24:59] I think this comes with right this I
[25:02] think comes with the co-pilot for Azure
[25:05] extension. So this comes with various
[25:07] things and this has a lot of skills. So
[25:10] if you're doing Azure stuff you know
[25:12] it's got a bunch of stuff baked in here
[25:14] that it already knows about um
[25:18] and it you know kind of has all this
[25:19] like bundled up stuff. So,
[25:22] uh, so that's that's one to check out if
[25:26] you're doing a lot of, um, a lot of
[25:29] Azure stuff there.
[25:31] Another thing that's cool actually, uh,
[25:33] and this is from somebody who is just
[25:36] like 10 feet away from me right now. H,
[25:38] so he made Waza, which is a CLI that
[25:44] evaluates your skills to see how good
[25:46] they are. So if you want to like really,
[25:48] you know, see like, hey, am I have I
[25:50] done a good job on this skill? And then
[25:53] the other thing he made was a sensei.
[25:58] Let me find this one. Here we go.
[25:59] Sensei.
[26:02] Uh, so this one is a skill for
[26:04] iteratively improving a skill using the
[26:07] Ralph loop pattern.
[26:10] Uh, so both these help you improve
[26:12] skills. Okay. Yeah, great point from
[26:14] Zach. I'm super concerned about this. I
[26:17] did post this on all my Oh, I didn't put
[26:19] on LinkedIn, but I put it on my other uh
[26:21] social media accounts this morning.
[26:24] Um yeah, if any of you using light LLM
[26:27] and if you didn't pin it, then you you
[26:30] really got to check um you know, check
[26:33] your environment because it's been
[26:35] compromised. So, light LLM is this
[26:37] popular gateway and it is a Python
[26:39] package. I actually have contributed to
[26:41] it in the past. I I was not a big fan of
[26:45] the codebase when I saw it. Um so I
[26:48] didn't keep contributing but uh yeah so
[26:51] this is really concerning. Lite LM was
[26:53] incredibly popular. I'm this has
[26:55] probably affected like like 100,000
[26:58] machines I would guess. I don't know.
[26:59] It's like it was it's super popular and
[27:01] a lot of people do not pin their
[27:03] dependencies and it's so important
[27:05] especially with something like this that
[27:06] you pin it. So if any of you are using
[27:08] my LLM, definitely do
[27:11] um check out whether your environment
[27:14] has been has been compromised. Um and
[27:18] ideally I would say to move off light
[27:20] LLM because um I think there's probably
[27:24] better ways of doing it. Like for
[27:27] example, if you're an Azure user, you
[27:28] know, I would move off of light LLM and
[27:30] instead uses the responses API because
[27:32] that basically is a common gateway to
[27:34] all the Azure models. Uh, so I think
[27:36] that would be a better approach, but I'm
[27:38] curious if there's something that light
[27:40] LLM is doing for you
[27:42] um that you can't do. Uh, yeah. Yeah. By
[27:46] pinning I mean pinning to a pi version
[27:48] number, right? Because you can see the
[27:49] ones that were compromised. Um, because
[27:53] usually like, right, so this was
[27:55] published, right? So if you had it
[27:56] pinned to 1.82 Oh. Oh, it was seven.
[28:00] When was seven published? All right,
[28:01] let's check the history. Um,
[28:07] okay. LM release history. Oh, they've
[28:12] taken down. They're already down. Okay.
[28:14] So, I don't know when I saw another
[28:16] timeline earlier today. I forget where
[28:18] that timeline was. Um,
[28:21] this is also in hacker news, too. So,
[28:23] yeah. So, anyway, so if you had 8 point,
[28:25] you know, if you had it pinned at
[28:26] 1.882.6,
[28:28] then you should be fine, right? So, both
[28:31] were published today. Okay. Yeah. So you
[28:32] should be okay if it's 1.82.6,
[28:35] right? Um, but if if you didn't have it
[28:37] pinned and you're in an environment
[28:39] where you like, you know, where it where
[28:41] you pulled the latest today without
[28:43] having a pin, then it would have pulled
[28:45] in, you know, 7 or 08 and not anymore
[28:48] thankfully because it's uh looks like Pi
[28:51] has has taken it down. But if you were
[28:53] within that, you know, hour period uh
[28:55] however many hours there was a good
[28:56] timeline. What was the let me see if I
[28:58] can find the timeline now. Somebody has
[29:00] it. This one may No,
[29:04] had a funny name. I don't know if anyone
[29:07] remembers what that time. There was a
[29:09] good time timeline website. Um,
[29:13] yeah. So, you should always be pinning.
[29:15] Um, so you know what is pinning? What is
[29:18] pinning look like? Where's one where
[29:19] I've got it pinned? Right. So, you can
[29:21] pin with UV or with pip. Um, but for
[29:24] like this example, you can see here in
[29:26] my pi project.l normal. Uh these ones
[29:29] don't look pinned. Um well some some of
[29:31] them have like minor version
[29:32] constraints. Some of them he these ones
[29:34] I do have exact constraints because um
[29:37] just of how the these are all release
[29:39] candidates. Um but um then when I use UV
[29:43] sync it makes a lock file, right? So the
[29:45] lock file is what I'm actually syncing
[29:47] based off of. So it's you know it's it's
[29:50] going to have to I would have to
[29:51] explicitly update this lock file. So
[29:53] with UV that's what you're you know
[29:55] relying on. And then for my other repos
[29:58] where I'm um you know not using that
[30:01] then I'm usually doing like um a a pip
[30:05] install and and a pip compile. Sorry. So
[30:09] for the other ones and I'll do like a
[30:10] pip compile. Uh let me find a more
[30:14] recent one. What was I doing earlier
[30:17] this week? Okay. So like this one.
[30:22] Uh
[30:24] okay. So this one I have a pi projectl
[30:26] that has no version numbers in it and
[30:29] then I have this thing which is
[30:31] requirements.ext and I use pip compile
[30:34] and say hey take this pi projectl
[30:36] compile requirements.ext and so then I
[30:38] know whenever I install I'm going to do
[30:41] a pip install-r requirements.ext text
[30:44] and it's only going to install these
[30:45] versions, right? And you can see I I've
[30:47] got this extension that shows me the
[30:48] latest version. So, you know, so I'm
[30:50] like behind on the versions, but it's
[30:52] better generally it's it's good be it's
[30:55] generally better to be behind than to be
[30:56] grabbing the latest. Now, that being
[30:58] said, sometimes you'll find out about
[30:59] security issues in like one that you
[31:02] have pinned. And that you'll find out
[31:04] because of GitHub, right? So, if you
[31:05] look at um let's look at the the actual
[31:10] repo. So you you know you just want to
[31:12] install make sure you have code alerts
[31:15] in on your repository right because then
[31:18] you'll find out. So here you can see
[31:20] that I get a dependabot that says hey um
[31:24] you know this will merge a high severity
[31:26] dependabot alert on cryptography and
[31:29] that's in my security. Okay, obviously I
[31:32] I need to pull some uh PRs usually like
[31:35] you know Yeah. So this is what will
[31:37] happen is that there's there's so many
[31:39] like of these CVES and even though they
[31:42] say hi like a lot of times we're not
[31:44] using the features that are affected by
[31:46] them. Um but um you know so that's
[31:49] what'll happen is that when you pin it
[31:51] you'll get told like hey this version of
[31:54] Azure core has this CVE
[31:57] and um you know and then and then you'll
[32:00] get this dependabot update here and um
[32:02] and yeah and so when you get anything
[32:04] from dependabot that's because of a CVE
[32:06] a vulnerability then you do want to take
[32:08] action on them um fairly quickly.
[32:12] Uh, I just have so many demo repos that
[32:14] I tend to be um behind on them because
[32:17] there's so many CVEs now because it's so
[32:18] much easier for people to use a agents
[32:20] to find CVEes and some of them are real
[32:23] vulnerabilities. Um, I know a lot of the
[32:25] ones like for Flask like are, you know,
[32:28] they're like just really low severity,
[32:30] but you know, people, you know, we fix
[32:32] them anyway. All right, here is the nice
[32:34] timeline. John found it. Thank you,
[32:36] John. Um yeah, so apparently there's
[32:39] this like team that is a team PCP that's
[32:42] attacking multiple
[32:44] uh you know multiple things. Uh so
[32:46] where's the
[32:48] uh the most recent one? Okay. Yeah. So
[32:51] here you can see the timeline when it
[32:55] was published 1039. So they were
[32:57] published really close to each other and
[33:01] um they harvest SSHs cloud rentals and
[33:04] bars and crypto wallets. It's crazy. Um,
[33:08] and then it spanned a bunch of comments
[33:11] and it defaced the repos because it it
[33:14] got the compromised account of the
[33:16] person who runs all these repos. Um,
[33:20] and then pipe quarantined them. So,
[33:21] there's a three-hour exposure window. Um
[33:24] but during that window if anybody had an
[33:26] unpinned light LLM that they pulled in
[33:29] their prod environment or their local
[33:31] environment then
[33:33] uh it would have been
[33:35] bad bad news.
[33:38] And here's the official
[33:41] advisory.
[33:45] All right. So yeah,
[33:48] exciting exciting times there. Good
[33:52] reminder to always pin your requirements
[33:59] and also just to
[34:02] only use packages from people that you
[34:04] know well and trust that are using like
[34:07] best practices. Like usually you can
[34:09] like let's see if you go
[34:12] if you looked at light LLM what would it
[34:14] look like here? So you can see all right
[34:16] so these are unverified details blah
[34:19] blah blah and then those are the
[34:22] verified details okay all right and then
[34:25] but if we look at uh agent framework
[34:29] it's this one verified details so you
[34:32] can see all these are the verified ones
[34:34] okay and all right so it doesn't look
[34:37] that dissimilar but one thing you'll
[34:39] notice is that if it is an official
[34:40] Microsoft package then Microsoft will be
[34:43] list as the maintainer
[34:45] And uh if Microsoft is listed as a
[34:48] maintainer then the package does have to
[34:50] go through pretty strict
[34:52] requirements to make sure that it's
[34:55] following all the best practices so that
[34:57] you know it doesn't get compromised uh
[34:59] as easily or hopefully at all.
[35:02] Uh, so that's something to look for. If
[35:03] you're ever wondering if a package comes
[35:05] from Microsoft or is like officially
[35:07] part of the Python maintenance strategy,
[35:11] then you know, look for Microsoft under
[35:14] the maintainers.
[35:17] All right, let's see. Okay. Um, okay.
[35:20] So, yeah. So, I so we talked about
[35:22] responses API. Uh, I've also been
[35:24] working with Foundry agent service. So,
[35:26] I did do a demo at Nvidia GTC last week.
[35:30] That's the Nvidia conference and it's
[35:33] all the code for the demo is in this
[35:36] repo here.
[35:38] Um so this uh you know if you ever just
[35:42] want to see like so this will do a few
[35:44] things. It'll create 20 different
[35:46] Foundry prompt agents. So these are like
[35:48] you know agents that are just a prompt.
[35:50] They don't really have any tools. It'll
[35:51] create an agent that's grounded in a
[35:53] foundry IQ um knowledge base which is an
[35:56] Azure AI search like a gentic knowledge
[35:58] base and then it can run evaluations. It
[36:01] can run red teaming scans. It can set up
[36:03] continuous evaluation, set up daily
[36:04] scheduled evaluation, daily scheduled
[36:06] renting rings, and then I even use
[36:08] Locust to send a bunch of user traffic
[36:11] to the agents because I wanted to um
[36:14] populate the the the charts for my demo
[36:17] so I could like make it look like real,
[36:19] you know, real things are happening. Let
[36:21] me see if I can open it up now.
[36:23] Uh so yeah and that's all with the this
[36:26] is the agent service which is different
[36:27] from bit different from the foundry
[36:29] hosting agents because the agent service
[36:31] there you're using you know the their
[36:34] agent SDK and everything is going
[36:37] through their agent runtime right so you
[36:39] can see um the create foundry agents uh
[36:42] right you you create a you create a
[36:45] foundry project agent you know with your
[36:47] prompt and then boom you've got an agent
[36:50] um and then with the the one that's
[36:53] grounded in a knowledge base. That one's
[36:54] a little fancier because it's a rag,
[36:56] right? And we give it an MCP tool and we
[36:58] point it at the MCP endpoint of that uh
[37:02] agentic knowledge base. So that's how
[37:05] that's how we connect them. And let me
[37:07] find
[37:09] my uh
[37:13] let me find
[37:19] project. Maybe this one.
[37:22] Now I have so many foundry projects.
[37:24] Okay,
[37:29] let's check on build agents. No, it's
[37:32] not that one. All right, let me actually
[37:33] just open up this this repo here.
[37:37] Uh,
[37:40] okay.
[37:43] Foundry agent.
[37:46] Foundry agent demos. Here we go.
[37:51] Henb.
[37:54] Okay. Don't look at No, I have to do my
[37:56] fix my key again. All right. I don't
[37:58] know why we're using keys in this one.
[38:00] Boundary TF. Okay. All right. I'll
[38:03] change that to not use keys. Um. All
[38:06] right. So, now I'm going to look for
[38:11] find
[38:14] my agent.
[38:23] Uh, let me just do a show.
[38:29] Okay. And then there we go. That's the
[38:32] one I was looking for. All right.
[38:36] Models
[38:38] build. Okay. You got to go to build.
[38:41] Here we go. All right. So, here you can
[38:43] see I've got 21 agents. Most of these
[38:46] are just you know boring prompt only.
[38:47] But then we've got more exciting one. Uh
[38:50] this is the one that's grounded. So you
[38:52] can see that it is grounded in this
[38:53] knowledge base and like okay what are
[38:55] our vacation
[38:57] policies? Okay. Uh so it should it
[39:01] should go out. Oo that's exciting.
[39:05] Did I take it down? Connection Canada.
[39:09] Okay. All right. I'll have to see if I
[39:11] took that one down.
[39:13] Otherwise, that might be okay. All
[39:15] right. And then we can see um
[39:19] you know, we can make new knowledge
[39:21] bases. We've got tools.
[39:24] Uh let me see if I can show you. I
[39:26] haven't run the the load. Okay, let's do
[39:30] evaluation. All right. So, you can see
[39:32] there's um we've got like the scheduled
[39:34] evaluation and then under red team um we
[39:38] can set up red teaming scans as well.
[39:42] So yeah, there's a lot of cool stuff you
[39:45] do. I really like the online evaluation
[39:46] and the scheduled evaluations because
[39:48] it's especially with online evaluation,
[39:50] it's like hard to
[39:52] hard to set up. Um, so I'm trying to
[39:54] make it so that we can set up everything
[39:56] from code. Um, but uh I'm still still
[40:00] working through a couple things. All
[40:02] right, I see there's some questions.
[40:04] Let's tackle the questions here. Uh, is
[40:07] there a way to host agents in AKS
[40:11] and use the Azure AI foundry
[40:12] orchestrations just for no code
[40:14] orchestrations alone? Only hosted agents
[40:17] are supported right now and self-hosted
[40:18] agents are not available in no code
[40:20] orchestrator.
[40:22] Well, what is the noode orchestration?
[40:25] What if you can clarify what you mean by
[40:27] the no code orchestration? So when you
[40:29] do foundry hosted agents um the thing I
[40:32] was talking about here they are um
[40:36] currently deployed to Azure container
[40:38] apps behind the scenes um the this AZD
[40:41] takes care of that uh they are not
[40:43] deployed to AKS um but container apps is
[40:47] pretty similar um but you have to you
[40:52] have to like deploy it using you know
[40:54] using this very specific way so that it
[40:56] gets wrapped in the instrumentation so
[40:59] that it can because the the goal is with
[41:02] Foundry Hosted agents is that then you
[41:03] could do stuff like online evaluations,
[41:06] right? Because online evaluations is
[41:08] like you know actually like you know
[41:09] pretty cool the fact that you could
[41:11] potentially
[41:13] um you know set that up. Let me see
[41:14] settings right. So continuous evaluation
[41:18] the ability that every time a request
[41:21] goes through the agent that you could um
[41:23] say you're going to sample like here
[41:25] I've got saying like oh sample like you
[41:27] know I could say like 10 runs per hour
[41:29] right uh but in order to be able to do
[41:31] that like we foundry has to understand
[41:34] what is an agent request in your you
[41:37] know in your environment and so it it
[41:39] has to have like an adapter so they have
[41:42] two adapters right now one for agent
[41:44] framework and one for uh lang chain and
[41:46] lang graph because basically it can say
[41:49] hey we know you know we know what a link
[41:51] chain agent looks like we know what an
[41:52] agent framework thing looks like we're
[41:54] going to adapt it so that then we can
[41:57] hook in and we can do tracing um with
[41:59] app insights we can do this continuous
[42:01] evaluation uh and you know the
[42:03] evaluation alerts so yeah so that but
[42:06] that does mean that they have to have a
[42:08] particular setup where you deploy it a
[42:10] certain way and it wrapped it a certain
[42:12] way so um but there is actually wait
[42:14] that being said, I did get linked
[42:19] um
[42:20] something that would be potentially
[42:23] useful. Let me see if I can find it.
[42:25] Learn
[42:27] uh it would be under
[42:30] Let's see if I can find it. Um oh man,
[42:33] everything says foundry. Okay,
[42:37] agent.
[42:38] The agent is going to be a lot of
[42:40] answers.
[42:42] Uh oh, maybe this one. create a hosted.
[42:46] All right. So, there's roles and
[42:49] permissions.
[42:50] So, you can use the Azure AI um
[42:58] is it going to be this one? Nope.
[43:05] Okay. Azure AI projects. Create hosted
[43:11] agent.
[43:18] Nope.
[43:26] Because basically you have to like point
[43:27] at the image. There's like an image for
[43:29] it. Um okay.
[43:33] Uh so
[43:36] can't find it right now. There there's a
[43:38] third way of doing it because here it
[43:39] lists two different ways of doing it. It
[43:41] says like oh you can do add or um or you
[43:45] can do a um AI toolkit but there's a
[43:48] third way where you can actually
[43:49] directly use the
[43:53] uh the Azure AI project SDK. Let's see
[43:56] if it's under here.
[43:58] Code custom code interpreter custom
[44:01] custom. All right, let's look here.
[44:04] Main. py.
[44:07] Okay.
[44:13] Creeper.
[44:16] No,
[44:18] doesn't look good.
[44:43] Okay, see this one's got like this
[44:45] custom adapter. So, it is I think
[44:47] possible that if you're not using those
[44:50] frameworks, you can write this like
[44:51] custom adapter.
[44:55] So
[44:58] yeah um oh okay so Desh said I meant the
[45:01] workflow options that we have in new
[45:03] foundry
[45:05] um the problem with hosted agents it's a
[45:07] managed service for Microsoft build
[45:08] separately as part of foundry project
[45:10] okay so looking back at okay but if
[45:14] you're doing the workflows option
[45:15] sequential and group chat those are all
[45:16] from agent framework so
[45:20] um could you could you just use the
[45:23] agent framework um you know workflows
[45:27] because
[45:28] and just write the code um because when
[45:31] you do like yeah if you're doing a
[45:33] foundry it'll like make a YAML but that
[45:34] YAML is just uh it's it's just part of
[45:38] agent framework like it's probably this
[45:40] one workflow samples right it's math
[45:41] chat right and says oh okay we're going
[45:43] to you know do this um you know this
[45:47] workflow here or like deep research
[45:50] right but these are really just using
[45:53] agent framework
[45:55] um you know workflows behind the scenes.
[45:57] Uh so I I guess I would personally write
[45:59] it in Python and then you know run that
[46:01] on on AKS. Um but there's if you do you
[46:05] can do the YAML as well. Um
[46:10] okay foundry workflows. Right. But if
[46:12] you're doing if it's a foundry I'm
[46:15] getting confused. Okay. because you're
[46:16] saying you want foundry work. So you
[46:18] don't want to pay for foundry workflows,
[46:19] but you want foundry workflows
[46:22] to scale.
[46:24] Um so I'm trying to figure out what you
[46:26] do and don't want there.
[46:29] Uh so the orchestrations you're talking
[46:31] about are under here. There is
[46:33] uh sequential and then group chat and
[46:36] then there's a couple others as well.
[46:38] Um, but I'm presuming that you're you're
[46:42] doing uh if you're doing no code, then
[46:44] it's probably generating the YAML and
[46:47] running the YAML.
[46:53] Let me see if I can find the workflows.
[46:55] We're doing agents foundry.
[46:59] Um, I don't even remember where to do
[47:01] workflows here. Oh, there we go. Yeah,
[47:03] workflows preview. Okay, here we go.
[47:05] you want your agents.
[47:08] Okay. But if you want your agents to be
[47:10] in AKS,
[47:12] could you instead of Mark 7?
[47:16] Um,
[47:19] okay. So, I mean, if you wanted to be
[47:22] AKS, then you could use agent framework
[47:25] with the workflow.yaml,
[47:27] right? Like, so you make your workflow
[47:29] here and then, oh, where was it? So,
[47:32] make the workflow here. Blah blah blah.
[47:34] create. Oh, here you go. Group chat.
[47:36] Yeah, great. So, we create that and then
[47:39] um you get the YAML, right? So, this is
[47:40] the YAML. I was just showing you this
[47:42] this YAML in the agent framework um
[47:45] repository. So, you can use that YAML
[47:48] with agent framework. Um and then you
[47:50] could just run that with agent framework
[47:53] on AKS
[47:56] and uh and yeah and then you would get
[47:58] you know this this kind of no code
[48:00] experience but you could you could run
[48:01] this YAML
[48:03] run this YAML yourself um from here you
[48:06] but then you don't necessarily get the
[48:08] thing is there you don't necessarily get
[48:09] continuous evaluation right because
[48:11] you're running it you know you're not
[48:13] using the foundry hosted agent service
[48:14] so I think that would be you know that's
[48:17] what you're missing really is that
[48:19] continuous evaluation but um you know
[48:22] but you can get the other stuff right
[48:24] because here you you have limited
[48:26] publish options but you can grab the
[48:28] YAML and run that with markup agent
[48:30] framework
[48:32] that work
[48:36] okay cool
[48:39] um all right so John V said do I have
[48:42] recommendations for evals
[48:44] um you know what you want eval 101 one.
[48:48] Um I mean we've we've we we do have uh
[48:51] you know we talked about evals in I try
[48:55] to talk about evals in every one of our
[48:57] our um sessions that we have right so
[49:01] you know uh we talked about AI quality
[49:03] and safety in our Python AI survey um
[49:06] one and then in the most recent
[49:10] uh thing we talked about uh monitoring
[49:13] and evaluation and evaluating agents but
[49:16] maybe you already saw those and want
[49:19] more
[49:21] information. But also with both of these
[49:23] I was um I didn't show the new way of
[49:25] doing eval. So the new way of doing
[49:27] evals if you want to take full example
[49:29] full sorry full advantage of foundry
[49:32] then um
[49:35] so then you need the new way of doing
[49:36] it. So in the in the next series I will
[49:38] show the newest way of doing eval
[49:41] there's two different SDKs. So there's
[49:42] the Azure AI valuation SDK and that's
[49:44] the old array of doing it and then the
[49:47] new way is using openAI.ebal. So here if
[49:51] we look at this one quality eval py um
[49:57] you can see that we
[50:00] uh let's see we just set up um a test
[50:03] data set here and then we put so here
[50:06] we've got our criteria. So we say okay
[50:08] and this is using a built-in evaluator.
[50:09] So you can use built-in evaluators and
[50:11] these are like really generic evalu
[50:13] evaluators that we hope are going to
[50:15] work you know for you know many people.
[50:18] This is kind of like your first your
[50:20] first attempt is using these right like
[50:22] task adherence intent resolution. These
[50:24] are both overall evaluators that are
[50:25] just looking at hey this was the user's
[50:27] request and how well did we adhere right
[50:30] so you can start off with these built-in
[50:32] ones and then I did groundedness because
[50:33] I was doing a rag one and relevance. So,
[50:35] ground instance and relevance are the
[50:36] two best ones if you're doing um rag of
[50:39] the built-in ones. But as a best
[50:41] practice, uh you don't want to just use
[50:44] the built-in evaluators. What you want
[50:46] to do is, you know, look start looking
[50:48] through the data and have a human tell
[50:50] you like this is an example of a good or
[50:52] a bad. And what you should see is that
[50:54] you should see certain ways in which
[50:55] your agent fails. And then you can get
[50:57] much more specific and say, hey, you
[50:59] know, how's it failing? And then you
[51:01] also want to distinguish between evals
[51:03] that you're running on data where you
[51:05] have ground truth because if you have
[51:07] ground truth then you can say exactly
[51:08] like hey here's my multi- aent system
[51:10] and at this point I want the agent to
[51:12] call this tool with you know these
[51:14] arguments and then then it's going to
[51:15] call this tool with these arguments and
[51:16] then this tool with these arguments
[51:18] right so if you have the ground truth
[51:19] for that then you can get super duper
[51:21] specific and just um you know run your
[51:24] evals on that ground truth and just
[51:26] check every single point of the way like
[51:28] hey did it do exactly what I wanted to
[51:30] do. Um, but if you don't have ground
[51:33] truth, like you're running evals on uh
[51:35] live data as it's coming in, then you
[51:37] need to have an idea for what generally
[51:39] are the kind of failure cases that you
[51:41] see. And you only are going to figure
[51:42] that out by looking at your looking at
[51:44] your data and um and then you can build
[51:47] custom evaluators which are basically
[51:49] like you know they can either a lot of
[51:51] times that's going to be an LLM as a
[51:52] judge that's going to like say hey did
[51:54] it you know do fail in this particular
[51:56] way or succeed in this particular way.
[51:58] Um or you know you could even use a
[52:00] regular I have some rejax based
[52:02] evaluators as well right depends what
[52:03] you're looking for. Um but uh yeah and
[52:06] what I generally recommend is um
[52:09] subscribing to ham.dev. Uh he runs
[52:11] courses about evals but uh he's like
[52:14] everything he writes is really really
[52:16] helpful and even just the memes are um
[52:20] god
[52:23] h the memes are great. Um,
[52:28] types of headaches spilling LM as a
[52:30] judge. Uh, no, but let me get
[52:35] they just crack me up so much. Um, but
[52:38] let me find the actual more useful
[52:39] thing. I just love that those memes. Uh,
[52:42] here we go. LM eviles everything. You
[52:44] know, this is everything. Um, so you may
[52:47] not want to, you know, necessarily start
[52:48] with this, but you know, I, so you can
[52:50] check my, you know, what I've said about
[52:52] evaluations like in the last series. Um,
[52:55] but, you know, really,
[52:58] uh, Hamela is the expert and, uh, I
[53:01] always learn more from him when I watch
[53:03] his talks and read his blog posts.
[53:07] Uh but yeah, and then also check out the
[53:08] new way of doing uh doing eval uh in
[53:13] this if you're if you're trying to take
[53:14] advantage of foundry like for continuous
[53:16] evals.
[53:20] Okay. And we got a suggestion here about
[53:22] using agents in AKS for a more no code
[53:24] approach. Okay. Thank you. Yeah, I
[53:26] haven't actually used any and or logic
[53:29] apps. Uh, I know that logic apps are
[53:31] like the tools now. Like all of those um
[53:34] logic apps got added as tools here. Like
[53:37] when you uh oh discover tools, you go
[53:40] here and the types um a lot of them are
[53:45] these I think are all uh logic app
[53:48] connectors. Yeah, if you go down here
[53:49] the registry
[53:51] the vast majority of tools actually come
[53:53] from logic apps connectors. So when you
[53:55] are building like foundry agents uh then
[53:57] it's easy to add these in in theory.
[54:00] Haven't tried it yet. Uh hopefully we'll
[54:02] soon.
[54:04] Do they confuse you? Okay. I haven't
[54:06] tried it yet. Um you know I'm I'm
[54:08] actually pretty new to Microsoft stuff.
[54:10] So I know logic apps have been around
[54:11] for a while but uh just not something
[54:13] I've used yet but they are um they've
[54:16] made them into tools that are built in
[54:18] so that you can easily add them to
[54:20] Foundry agents and Foundry hosted
[54:22] agents.
[54:24] All right, it is now 12 o'clock. Uh, we
[54:28] made it through our
[54:31] uh weird office hours with me being in
[54:33] the office. I think we still Great and
[54:35] all the recording is still going. So,
[54:37] that's good. That means I'll be able to
[54:38] do a write up that has everything we
[54:40] talked about and I will, you know, post
[54:43] that in the usual thread and we'll have
[54:45] a YouTube uh recording. So, it'll be
[54:48] posted here um you know, probably at the
[54:52] end of the day sometime.
[54:55] All right, that's that's all for today.
[55:00] I'm going to go wander around Microsoft
[55:02] campus and get ready for a lab. And I
[55:07] hope you all have a nice rest of your
[55:08] day. Bye, everyone.
or a lab. And I
[55:07] hope you all have a nice rest of your
[55:08] day. Bye, everyone.

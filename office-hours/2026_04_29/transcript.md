[00:00] Uh so welcome everyone. Um if you
[00:02] wandered in and have no idea what's
[00:04] going on, we just had our live stream um
[00:07] from the host your foundry agent series
[00:10] and today's live stream was about lang
[00:13] chain and langraph. Um and uh this is
[00:17] the office hours afterwards. So, uh, if
[00:20] you have questions, um, just put them in
[00:25] the chat and we'll, uh, go through the
[00:29] questions. Oh, or the news. Great. So,
[00:32] Anorog says that PIP, the new version of
[00:35] Pep has dependency cooldowns. I think I
[00:37] saw, did Seth Larson add this? Oh,
[00:40] Richard C. Okay. All right. Well, that
[00:41] maybe that's just who's writing about
[00:42] it, but um yeah, because like Pipi has a
[00:47] security engineer like in residence now
[00:50] and they've been trying to improve
[00:51] security. So that's very cool.
[00:53] Dependency cool downs. Um
[00:56] so uploaded prior to accepts a relative
[00:59] duration and is the number of days.
[01:01] Interesting.
[01:05] I wonder if UV then also UV dependency.
[01:08] I didn't even know the name for it. So
[01:09] now we have a name for it. UV dependency
[01:12] cooldown.
[01:15] Dependency cool down. Okay. Yeah. So, UV
[01:18] has exclude newer. That looks like what
[01:22] they're calling it. Exclude newer.
[01:26] Uh
[01:29] where I just want the UV docs
[01:35] exclude newer. Okay. Oh, yeah. They also
[01:37] call dependency cool down.
[01:40] Nice.
[01:44] Um, all right. So, it said the
[01:46] equivalent if you use exclude newer. Oh,
[01:49] so cool down. All right. Dependabot
[01:51] itself. Dependabot's the GitHub thing,
[01:54] right? Dependabot has a cool down
[01:55] option, too. Okay. All right. So, we
[01:58] should use the pip. We've got pip cool
[01:59] down. We got dependabot cool down. And
[02:02] we've got UV um exclude newer. Um, so,
[02:07] so, uh, cool. So, we've got three
[02:11] different ways. I feel like this is a
[02:12] blog post now.
[02:15] Um,
[02:16] so this is, wait, this date
[02:19] uh, accepts. Oh, you can do a friendly
[02:21] duration like one week, 30 days, etc.
[02:27] Nice.
[02:30] All right. Very cool.
[02:34] So now every now we all have to go and
[02:36] add a cool down
[02:39] uh or um you know update your pip or
[02:42] your UV as well.
[02:45] Okay, so I see um some questions coming
[02:48] in.
[02:50] So Patrick says, "I really like the
[02:52] foundry manage conversations. Um is this
[02:56] feature limited to prompt agents and
[02:57] hostage? You'd love to use it with a
[02:58] langup agent that's hosted and as your
[03:00] web app." Oh, this good question. You're
[03:02] basically asking whether foundry memory
[03:04] can be used standalone.
[03:06] Uh, you know, um, I don't know, but
[03:09] we're going to try and figure it out.
[03:10] Um, let's see. Production
[03:16] production production. I'm just trying
[03:19] to find Okay, so I know that the launch
[03:22] blog post talked about
[03:26] memory.
[03:27] Um, so this was the this was the blog
[03:31] post um for last week's launch of the
[03:34] new Foundry hosted agent service. Um, so
[03:37] so this isn't answering your question
[03:38] yet. Um, but for both Foundry hosted
[03:41] agents
[03:43] um you could use the Foundry
[03:46] memory provider
[03:49] um and that memory provider
[03:53] uh should work. So let's see. So you can
[03:55] do it's n so it's natively integrated
[03:59] but there's also a CRUD API. So if
[04:01] there's a CRUD API
[04:03] then um I feel like you could you should
[04:07] be able to bring it into anything right?
[04:09] Um
[04:11] it's maybe going to be harder. Uh but it
[04:15] seems like
[04:19] let's see you do need like a open eye
[04:22] model. um
[04:26] memory related content create and use
[04:29] memory.
[04:31] Uh so in Python, how are they doing in
[04:34] Python?
[04:36] Um oh and there's also so the Azure AI
[04:38] projects SDK
[04:40] has has it um has support for it. So,
[04:46] um, and you would just need to you would
[04:48] you would need to authenticate to your
[04:50] Foundry project in order to to use it,
[04:52] but it looks like you could
[04:55] you could use this anywhere.
[04:58] Is this what you're looking for? Are you
[04:59] looking for something else?
[05:02] Add memories to memory store.
[05:06] Looks pretty cool.
[05:11] Um, oh, long-term memory only. Oh, okay.
[05:14] All right. Um H. Wait, what is the
[05:18] short-term memory then? Uh that probably
[05:20] means I don't know what the short-term
[05:21] memory is. Um
[05:25] so you're saying do we have boundary
[05:27] short-term memory? Wouldn't a short-term
[05:29] memory just be like a session?
[05:38] Okay, that's so you foundry manage
[05:41] conversations. Okay. Yeah. So, you
[05:43] basically mean like the sessions. Um,
[05:47] I don't think that
[05:51] that would be I don't Yeah, as far as I
[05:53] know, I don't think that's
[05:56] available
[05:58] separately. Um,
[06:00] if it was anywhere, it probably would be
[06:02] in the Azure AI projects SDK. So, that
[06:04] would be,
[06:06] you know, where to look for it.
[06:10] Okay. Yeah. The session history. Yeah.
[06:13] Okay, I get what you're saying now. Um,
[06:15] so let's just go let's check the um,
[06:21] uh, projects SDK.
[06:23] If it's going to be anywhere,
[06:27] it's going to be in here. Um,
[06:31] is my theory at least.
[06:35] Models, operations.
[06:37] Oh, this might not be the easiest to see
[06:39] what's in here.
[06:48] Yeah. Okay. I as far as I know, we're
[06:51] gonna I'm gonna say no and I will I will
[06:53] follow up and and and double check that
[06:56] there's now standalone access to
[06:58] sessions.
[07:03] All right, let's see. It's a good
[07:05] question. Um
[07:07] okay, so this one, um I should be able
[07:10] to answer. So for the knowledge
[07:12] retrieval MCV server is that something
[07:13] that is part of Microsoft Foundry? Yeah.
[07:16] So that is Foundry
[07:18] um IQ also known as Azure AI search um
[07:21] depending who you talk to. Um so uh you
[07:26] know you can also just in the Azure
[07:28] portal this is you know if you make an
[07:31] Azure search in the Azure portal like so
[07:34] you don't have to go through Foundry for
[07:35] it. Um but when you use it with Foundry,
[07:37] there's like built-in ways of connecting
[07:39] to the the you know, Foundry IQ. Um so
[07:45] yeah, so this is Azure AI search
[07:47] knowledge base. Let me get the the
[07:48] standalone documentation about um the
[07:52] MCP retrieval. Here we go. How to
[07:54] retrieve. Okay.
[07:57] Um so we're using the MCP endpoint
[08:03] for it. Um so you see this it's it's
[08:06] Azure AI search. Um you know there's
[08:08] some built-in it's you know more tightly
[08:12] integrated into Foundry and that's where
[08:14] it's called Foundry IQ. Um but it is
[08:17] basically Azure AI search and you can
[08:20] you know call the MCP endpoint and
[08:22] that's what we often do in Foundry um
[08:25] because it's compatible with MCP uh but
[08:27] you can also use it over REST you can
[08:29] use it via the Python SDK uh just uh
[08:32] however you want to do it. So for
[08:34] example like if you didn't want to um
[08:36] point your agent at the MCP endpoint you
[08:38] can also just write a tool and that tool
[08:41] can do a retrieval request u so I have
[08:44] implemented this as well I had it like
[08:46] in a branch um for the day one session
[08:49] actually so you know there's many ways
[08:51] that you can point your agent at um you
[08:55] know at uh knowledge so you can point it
[08:58] at the MCP endpoint you can use the SDK
[09:02] Um you can yeah I don't know you have a
[09:05] lot of options. So
[09:07] uh so there we go. Um
[09:12] uh and it'll like the knowledge bases
[09:14] support quite a few different sources.
[09:16] Um so
[09:19] here's the knowledge sources currently.
[09:21] So you can have a search index blob
[09:23] index one late index shareepoint remote
[09:25] shareepoint and Microsoft Bing. So those
[09:27] are the currently supported knowledge
[09:29] sources for knowledge bases.
[09:32] In my case, I just pointed it at two
[09:33] different search indexes. Um, but you
[09:36] can, you know, you can get fancier than
[09:37] that,
[09:41] right? So, you can have it. Yeah, you
[09:42] can make your own tool that wraps it.
[09:45] You could have a sub agent. Uh, you got
[09:47] lots of options.
[09:49] And then the knowledge base itself is
[09:50] like different effort levels, so you can
[09:53] you can have it do more work as well.
[09:57] Uh, let's see. Okay,
[10:00] so Quentyn's
[10:03] question um when deploying Langraph and
[10:06] Langchen and host agent, how should I
[10:08] imagine short-term memory, long-term
[10:10] memory, and compaction?
[10:13] Um well, for the memory, uh looks like
[10:17] we really got to add memory to this uh
[10:20] to this series next time. I don't know
[10:22] if uh Gwen's around, but um okay, so
[10:25] let's just check uh Azure AI link chain.
[10:29] I want to see if um
[10:33] do we have
[10:39] chain AI?
[10:41] Yeah. Okay. I'm just checking to see
[10:46] if we've got support in here
[10:50] for memory.
[10:54] Um, looks like no.
[10:59] Let's just search memory
[11:07] chat history.
[11:10] Well, that looks promising. All right.
[11:12] So, Azure AI
[11:15] chat history,
[11:17] chat history, Azure AI memory and Cosmos
[11:20] DB.
[11:22] All right. So, there is
[11:25] a
[11:27] some code here. Azure AI chat message
[11:30] history. It updates Azure AI foundry
[11:32] memory per term.
[11:35] Okay.
[11:38] Um
[11:44] All right. So, this actually
[11:47] try Yeah. So, this tries to make it
[11:49] easier to store. So, this is about like
[11:52] this isn't like what I think of as like
[11:53] kind of dynamic memories, but this is
[11:55] storing at least your chat history,
[11:56] right? So, if you're trying to just, you
[11:58] know, for each user, you're trying to
[12:00] remember what that, you know, those
[12:02] users previous chats. So, you can do
[12:04] like a list of the chats and then
[12:06] restore from those chats. Um, then this
[12:08] should
[12:10] This should work for for that. Um,
[12:14] you might want like something more a
[12:16] more d like that's this is this issue
[12:18] with memory is that we use it in so many
[12:20] different ways. Um, so this is yeah,
[12:23] this is like the chat history memory.
[12:25] Um, if you're looking for like the agent
[12:27] like seeing like, oh, I should remember
[12:29] that this person likes dark chocolate.
[12:31] Uh, I don't see that. I don't
[12:35] particularly see um an implementation of
[12:38] that here right now. Uh you could build
[12:40] it yourself on top of uh you know on top
[12:43] of these services but I I don't see
[12:46] something like dynamic memory as I would
[12:48] call it. Um, oh, does link chain have
[12:51] its own? Okay, so if lang chain has its
[12:53] own framework for memory, uh, right
[12:56] threads go memory,
[12:58] long-term memory.
[13:00] Um, yeah, I think the thing is, yeah, I
[13:04] don't know. You'd have to check the
[13:05] stores to see
[13:08] uh what are the so the in-memory store.
[13:10] So yeah, you would want to
[13:13] implement
[13:14] um
[13:16] you'd probably want to do
[13:19] can you subclass or how do you do your
[13:22] own memory store? Memory store.
[13:27] Um wait, what did this one subclass?
[13:32] We go here. Chat history. Azure AI
[13:35] memory.
[13:38] Just going to check. Okay. So, base chat
[13:40] messages history.
[13:47] So, that's that's doing it a bit
[13:49] differently.
[13:53] Short-term memory in memory.
[13:58] H.
[14:01] Yeah, these are uh it's it's a good
[14:03] question.
[14:05] Um, I think there's some options here,
[14:08] but I'm not sure what the number one
[14:09] best option is here.
[14:12] Uh, so you could take a look at at this
[14:14] one.
[14:15] Uh, but I'll I'll ask um our colleague
[14:18] who's, you know, working on this if if
[14:21] they can share what they think the best
[14:23] practices.
[14:25] Um, oh, use Reddus. Yeah. Well, you can
[14:28] use Reddus is on um you use Reddus on
[14:31] Azure. So you don't have if you're using
[14:33] Reddus, you could use Azure Reddus. Um,
[14:37] but you could you could also like port
[14:39] that to Cosmos.
[14:41] Well, everybody wants to know about
[14:43] Foundry Memory. Okay. All right. For the
[14:45] record, haven't used Foundry Memory yet.
[14:48] Um, I now know that there's a lot of
[14:50] questions about it, so I shouldn't use
[14:52] it. Um, but this is why I do these
[14:54] office hours in order to find out what
[14:56] things like what my knowledge gaps are
[14:58] so that then I can go and fill in those
[15:00] knowledge gaps. Uh so clearly a lot of
[15:03] interest in foundry memory and so I I
[15:07] need to actually um try that out.
[15:13] Um let's see.
[15:16] Okay. So
[15:22] all right so oh compaction. Sorry your
[15:24] other question was on compaction. So for
[15:25] that one I would I mean my first step
[15:27] would I would just use the link chain
[15:29] summarization middleware. they have it
[15:31] built into lang chain that's one of
[15:32] their built-in middleares right and
[15:34] because it just needs a model so you can
[15:37] just pass in your foundry model for it
[15:39] so um so for compaction that's at least
[15:42] what I would start off with and it's
[15:43] open source so like you can also just
[15:44] write your own summarization middleware
[15:46] so like I've totally looked at the code
[15:48] for this before and just made my own
[15:50] version of it um so for cont yeah yeah
[15:54] for for compaction that that's what I
[15:58] would start off with
[16:00] and um and then see and see how well
[16:03] that's working for you.
[16:06] The agent service uh the agent service
[16:09] as far as I know it should not be doing
[16:11] compaction. Um trying to think if any of
[16:15] the models would be doing so responses
[16:18] API itself like the OpenAI responses API
[16:22] and Azure I think does have maybe some
[16:25] degree of compaction.
[16:28] Let me check. But that would be
[16:30] different from, you know, we're exposing
[16:32] the responses API layer ourselves. So um
[16:36] yeah, as far as I know, we are not doing
[16:40] any sort of compaction oursel. But some
[16:42] if anyone knows otherwise, you should
[16:43] you should um cl Yeah. So if you're
[16:46] using Azure OpenAI for your model,
[16:49] right? So on the model side, when using
[16:51] responses API, um there is actually
[16:55] compaction options. um on the model side
[16:59] um but that's on the model itself right
[17:02] so if you wanted to you can actually
[17:04] make a call to this compaction endpoint
[17:06] that's one way of doing compactions I
[17:09] feel like they can also yeah there's
[17:11] different ones there's server side okay
[17:14] um server side directly you can do
[17:17] context manage with a compact threshold
[17:19] that way you don't have to call the
[17:20] endpoint separately
[17:23] um so you do yeah so assuming you're
[17:25] using a foundry model like I showed um
[17:29] and if it's an Azure OpenAI model so
[17:31] let's say you're using like GBD55
[17:34] then um in theory you can set this
[17:37] context management
[17:39] um option here uh let's see context
[17:44] management type compaction compact
[17:46] threshold so then every time it's going
[17:50] to do something it'll do that but then
[17:52] this is at the this is in the me in the
[17:54] actual create all.
[17:56] Um, so you'd have to figure out how to
[17:58] do that in your agent code as well. Oh,
[18:02] I see we got a link. Let's see.
[18:05] Compaction man. Yeah, compaction applies
[18:08] only to agents and manage agents that
[18:10] really do not benefit. Okay.
[18:16] For these.
[18:19] Okay.
[18:23] Wait, this is from the agent framework.
[18:25] Okay.
[18:27] Oh, yeah. So, this is for agent
[18:28] framework. So, yeah. So, similarly,
[18:30] agent framework has some built-in
[18:32] compaction. Um,
[18:37] so check this out if you're using agent
[18:40] framework.
[18:46] Uh, okay. Let's see. All right. So, that
[18:49] was so, okay, compaction.
[18:51] Compaction. Compaction. Um just
[18:54] scrolling up to see everything. Uh
[19:01] okay. So Pablo asks is there a place to
[19:03] check for the features that are not
[19:05] available
[19:06] in relation to interacting with other
[19:08] Microsoft services in the tenant when
[19:11] the agents are created with link chain
[19:12] lane graph instead of agent framework?
[19:15] Um well really to me the big difference
[19:19] between agent framework and lang chain
[19:22] is the fact that agent framework has the
[19:24] responsive server built into agent
[19:26] framework and that responsive server
[19:29] works quite well. Uh with lang chain
[19:31] it's not built in to lang chain um
[19:35] because langchain you know is not from
[19:38] foundry um so they have no particular
[19:42] desire to build it in um and it's also
[19:44] not even built into the lchain Azure AI
[19:46] package. So here so here the let's go
[19:49] back to that langchain Azure AI GitHub
[19:54] where was it? Okay here. Uh so the code
[19:57] that I showed today is actually based
[19:59] off of a pull request from Fukundo.
[20:04] So this pull request has all the code
[20:06] that we copied into the repo for today
[20:11] and it tries to you know take care of
[20:14] all the complexities of multimodal and
[20:17] tool calls and all of that stuff. Um
[20:19] there are still some bugs with it. So I
[20:21] was saying like today I actually was
[20:23] struggling and that's why I was using
[20:24] Gwen's version of it and that's also why
[20:26] I encouraged you to file reports. So the
[20:28] the big issue with lang chain is that
[20:30] you basically have to maintain your own
[20:33] responses adapter. I mean you can start
[20:34] with our code here and copy this code in
[20:39] um but um it's it's there's like there's
[20:42] no official for lingchain. there's a PR
[20:45] into link chain Azure AI, but uh it's
[20:48] not clear that it's going that we're
[20:50] actually going to merge it. Um I'm we're
[20:53] we're so we're trying to get the Foundry
[20:56] hosted agents team to agree to maintain
[20:58] it. Um but uh they're not sure that they
[21:02] want to maintain it because link chain
[21:04] is like not for Microsoft. So,
[21:07] uh, you know,
[21:09] if I were you, I don't know that I would
[21:11] actually
[21:12] deploy, uh, to host it like my LinkedIn
[21:15] stuff to host agents using the responses
[21:17] API because I think it's actually really
[21:20] hard to make a responses adapter.
[21:23] Um, and you know, we we've tried in this
[21:26] PR and in the code, but it's like it's a
[21:29] it's a complex API. And um you know if
[21:32] if you're going to be exposing your link
[21:35] chain agents using the responses API uh
[21:38] then you have to have an adapter that
[21:40] works for all the things that your
[21:41] agents might be doing and all the
[21:42] complexities of the responses API and
[21:44] streaming and tool calls and you know
[21:46] all that stuff. Uh and that's hard. Um
[21:49] so I would say like if we don't merge
[21:51] this I I don't actually think that I
[21:55] don't actually think you should do it.
[21:58] Sorry I now I'm just being honest. Um,
[22:00] so I would say instead to use like if
[22:03] you want to host, you could host with
[22:04] the invocations API, but then if you
[22:06] host with invocations, then you don't
[22:07] get all the benefits of response to the
[22:09] API, right? So you can try using this
[22:11] code, the code we showed today, and if
[22:12] it works for you, great. Or if you can,
[22:14] you know, make it work, great. Um, and
[22:17] then if you if as long if if it's fully
[22:19] working with responses API, then you
[22:21] should get everything you get from agent
[22:22] framework, right? Like because what
[22:24] matters is whether you are fully
[22:26] supporting the responses API because
[22:28] that's what everything is based off of
[22:30] right the playground is based off
[22:32] responses API the evaluation is based
[22:34] off responses API traces monitor all of
[22:37] that is based off responsive API so if
[22:39] you can get whatever agent framework to
[22:41] be working with the responses API layer
[22:44] then as far as I know you should you
[22:46] know be able to to use everything um I
[22:48] guess there's integrations like memory
[22:51] or something that might be an agent
[22:52] framework but Listen, if you can find I
[22:54] mean that's the other thing is that like
[22:56] if you can find I think the hardest part
[22:59] is the responses adapter because you
[23:01] have to understand both lane chain and
[23:04] responses API at the same time in order
[23:06] to make a great adapter. Um, if there's
[23:08] something else in agent framework that
[23:09] you like, like if they have a nice
[23:10] memory class that you like, you could
[23:13] just, you know, point your lang chain
[23:15] code at it, point cop at it and say,
[23:17] "Hey, I want this memory class, but make
[23:19] it link chain compatible." And probably
[23:20] you can make it work, right? Because
[23:21] agent framework code is just open
[23:23] source. Um, to me, the hardest thing is
[23:25] this responses layer. And that's why I'm
[23:28] really hoping that we decide to merge
[23:31] this PR and officially support this
[23:34] responses adapter for lang chain. um
[23:36] because there's just so much complexity
[23:37] about that. Um but if you can get that
[23:39] responsive layers working layer, then
[23:42] you should in theory um have everything
[23:46] available that we would have for agent
[23:48] framework.
[23:54] Um okay. All right. So that was
[23:58] um Pablo's
[24:00] question,
[24:04] right? So, oh, and so we have some
[24:05] followup. Quite hard to make Foundry the
[24:07] enterprise project for custom enterprise
[24:09] agents because link chain isn't is
[24:13] is allowed to be what response API is
[24:15] compatible with it and math
[24:17] math doesn't allow you to manage what
[24:19] comes into the context.
[24:22] Uh what do you mean by that? Math
[24:24] doesn't allow you to come what's into
[24:25] the to manage what comes into the
[24:27] context because with math we've got like
[24:28] middleware and context providers and all
[24:30] that stuff. So, I'm surprised.
[24:33] Uh, I'd be interested to hear what the
[24:35] limitation is with math.
[24:39] Um, okay. So, let's see.
[24:45] All right. So, we have this question
[24:46] about scaling. How does the scaling work
[24:49] with stateful hosted agents? So, you
[24:52] have three four replicas of host agents.
[24:55] How is the state shared between agents
[24:57] when each of them have their own file
[25:00] system?
[25:03] Well,
[25:05] I think that the state wouldn't be
[25:07] shared. Um, right.
[25:11] Um, I'm not sure, you know, uh, let's
[25:14] see. Let's see if we can get more
[25:17] insights into that. These are all really
[25:19] good questions, by the way. like
[25:22] um so let you know like I'm I'm pretty
[25:26] new to this platform as well so I
[25:29] apologize that I'm not able to answer
[25:31] everything um but let me see
[25:34] create and manage sessions sessions
[25:36] manage isolated sandbox compute
[25:40] uh
[25:42] invoke an agent through a session
[25:45] list sessions get session details upload
[25:48] a file
[25:50] So, you can upload files. That's
[25:52] interesting. That would be a way of
[25:53] potentially sharing state. Um,
[25:57] I'm just trying to get like an idea by
[25:59] from the docs of how how you might do
[26:02] that. Oh, you can also do this in
[26:04] Python. That's nice. Lists, get session
[26:06] details, delete a session, session file,
[26:09] upload file.
[26:11] Um,
[26:14] so you could share state that way. That
[26:16] seems kind of weird. Um, I think you'd
[26:19] probably want to like set up like a
[26:20] Reddus or a Cosmos. Um, I don't know if
[26:23] there's I don't know. Yes. Is there any
[26:25] other way that you can kind of share
[26:28] state amongst them besides using like a
[26:31] database or or copying files around
[26:36] um
[26:41] isolation model. Okay. Hosted agents run
[26:44] in per session VM isolated sandbox. Each
[26:46] session gets a dedicated sandbox with a
[26:48] persistent file system enabling scale
[26:49] zero with stateful resume for that one
[26:52] and predictable codes sessions are
[26:54] isolated from each other and state is
[26:55] automatically restored when a session
[26:57] resumes right the state is restored for
[26:58] that session but not across sessions.
[27:01] Um additional protocols
[27:06] uh
[27:08] sessions
[27:10] lifetime session management APIs.
[27:16] Okay.
[27:19] Yeah. So as far as I can see, you know,
[27:21] saying the state is isolated. If you did
[27:23] want to share state across the sessions,
[27:26] um I think you'd have to use something
[27:28] outside of the session, whether that was
[27:30] like a um you know, a fast database or
[27:33] something like that. That's my best idea
[27:35] so far. I don't know if people have
[27:36] other ideas. Um your first message goes
[27:39] the first agent replica. Wait, what do
[27:41] you mean by replicas? Um,
[27:45] so you're scaling up like so you're
[27:48] you're you're creating
[27:50] um you're you're cuz if you're the it
[27:54] should be that all your responses go to
[27:56] the same session.
[27:59] Uh oh, maybe maybe I don't understand
[28:01] how you're interacting with your agents.
[28:10] First called agent. Oh, for Yeah. Okay.
[28:12] Right. First call agent. Great. Thank
[28:13] you, Patrick. So, the first call agent
[28:15] gives you back the conversation ID.
[28:16] Second call has to include the ideas
[28:17] session history. Yeah, we should
[28:19] probably add that to the um
[28:22] the example that calls it. Okay. Pull
[28:25] for version. All right. So, we do invoke
[28:28] the agent. Pull for version. Invoke.
[28:32] Invoke the agent.
[28:41] Um, so when we call it, right? So call
[28:44] it here.
[28:46] So this one,
[28:50] so we'd get back a response
[28:53] and the response
[28:55] would have an ID in it. So, what we
[28:58] should do is add um we should add a a
[29:02] followup to this so you can see how we
[29:06] would do a multi-turn one um when
[29:09] calling from here because in the
[29:10] playground it like takes care of it for
[29:12] you. That's this is a great point. Thank
[29:13] you all. Um response response. I'm just
[29:17] trying to get back
[29:19] or
[29:20] ID
[29:22] conversation
[29:25] that this belongs to. Okay. All right.
[29:27] So,
[29:29] uh we should add a followup to this, but
[29:33] um
[29:35] maybe it works similar to how the uh
[29:37] Azure OpenI works, right? So, we do
[29:39] let's see chaining responses together.
[29:44] Um
[29:46] does it work like this? I should know. I
[29:49] haven't tried this actually. This is a
[29:51] great question.
[29:54] Um, this is how we do it with like
[29:56] standard like OpenAI responsive API. Um,
[29:59] I haven't checked to see I if I would
[30:02] assume we would basically do it the same
[30:04] way and it would find it based off the
[30:07] response ID.
[30:09] Um,
[30:11] yeah. Uh, so that would be that is that
[30:14] would be my my assumption. Um but
[30:18] uh we should we should really to do
[30:20] let's see to do add
[30:23] followup
[30:26] question to this to demonstrate using uh
[30:31] previous response ID to send to same
[30:34] session. Yeah,
[30:36] good point. All right, Patrick links to
[30:40] here. Okay. Oh. Oh, it's a lot more
[30:44] work. How did you find this? build your
[30:46] Okay. Runtime components. I don't even
[30:47] think I've seen this one. Okay. Is that
[30:51] So that's This one has like a whole Did
[30:53] Did we do the agent reference here too?
[30:56] Agent reference. I think this actually
[30:58] got updated recently because I remember
[31:02] because here we're doing because now the
[31:04] agent name is it's I think this must be
[31:07] for maybe this is for prompt agents
[31:09] because for these ones I don't think we
[31:11] have to do the agent name because it's
[31:13] in the um it's in the URL. Um, so what
[31:16] does this do? Response output.
[31:19] Um,
[31:21] oh, but it doesn't fall past in the
[31:23] response ID. Conversation conversations
[31:25] items.
[31:27] Uh, we have the conversations create.
[31:32] Oh, use a conversation when you want
[31:33] multi-turn continuity. Well, okay, that
[31:35] would that'd be a way of doing it, but
[31:37] really you want to know what is it doing
[31:38] behind the scenes. So, you get this
[31:40] conversation ID.
[31:45] Um,
[31:47] yeah. So, we could look at I I feel like
[31:50] we need to have an example because this
[31:52] is is this foroundary agent service?
[31:57] Um,
[31:59] because in our code here,
[32:02] uh, we do wait responses.create.
[32:05] Uh, where do we do it?
[32:11] Responses.create. Um, so you see here we
[32:14] don't do the the reference.
[32:17] Um, we just uh in this one we passed it
[32:20] in.
[32:21] Um, oh, actually even here I did it
[32:23] differently. Oh my gosh. Okay, we've got
[32:25] three different ways of doing it. Oh, we
[32:27] got to figure this out. All right, I I'm
[32:30] just going to put everything here. Say,
[32:32] okay, we got to figure this out. um to
[32:35] do
[32:37] because I remember trying the one in the
[32:39] docs and it wasn't why didn't the docs
[32:41] version work?
[32:47] Uh and then also to do
[32:52] to do why um
[32:57] do we need agents reference for
[33:00] followup?
[33:03] I it feels like things have changed and
[33:05] our docs are not quite up to date.
[33:11] Um
[33:14] right. Uh yeah. So, yeah, conversations
[33:17] and responses.
[33:19] Um, yeah, I was thinking that if but we
[33:23] if we were using it this way, you could
[33:25] do um the
[33:28] uh this right the response to ID, right?
[33:32] And then you would do a followup uh
[33:34] second response equals,
[33:38] you know, client.responses.create
[33:40] create
[33:42] and
[33:44] um you know previous
[33:47] response equals response ID.
[33:51] Uh so the question is does will this
[33:53] work with hosted agents when you know
[33:56] we're setting it up this way um or do we
[33:59] have to use that um or do we have to use
[34:03] conversations.create?
[34:05] I would think I would hope hope maybe
[34:07] they would both or do but you know maybe
[34:10] not.
[34:21] Okay. Um
[34:23] there. Okay. So there we go. Uh yeah, we
[34:27] need some clarity on that. Wow, we're
[34:29] getting really good questions here.
[34:31] Okay.
[34:33] Um,
[34:38] can all right so we have this question
[34:42] can we connect elastic search as a
[34:44] knowledge source to the foundry agent
[34:45] service um you wouldn't do it using
[34:48] foundry IQ but you can you know you can
[34:50] connect everything as long as you can
[34:52] authenticate to it and either do it as a
[34:54] tool um or as an MCP server so you know
[34:58] generally anything you can connect
[35:00] anything
[35:03] Um,
[35:09] all right. Uh, pricing. Yeah, we just
[35:11] had the p pricing page. Well, the
[35:13] pricing page is it's also in the blog
[35:15] post. U, so I think this has we were
[35:18] looking at pricing yesterday. So,
[35:20] pricing pricing pricing.
[35:23] There's a couple. Okay, that's the
[35:24] memory pricing. All right, so pricing.
[35:28] Um, what happens for 20 parallel agent
[35:31] API calls? All right, so you pay only
[35:32] for active execution. This is the
[35:34] compute. And so remember, it's like
[35:36] really fast um spin up time and go down
[35:40] time. Uh so it should just basically be
[35:42] like how long did your thing take to go?
[35:44] How much CPU uh how much compute and
[35:46] memory did that use? Um so I think the
[35:50] pricing is similar to before, but the
[35:51] difference is now with the new platform,
[35:53] it's you know, uh it's much faster to
[35:56] you're not wasting time, right? So we've
[35:58] got this zero. So faster startup, so
[36:01] under 100 milliseconds and then zero
[36:03] idle idle cost. So the agents are
[36:05] suspended between conversation turns. Um
[36:08] so that should mean that overall end
[36:11] ends up being, you know, cheaper. Uh so
[36:14] here's the pricing, right? So you could
[36:16] calculate based off of if you did 20
[36:18] parallel agent API calls, you know, how
[36:20] long do they take, how much memory do
[36:22] they take? Um and then then you have
[36:25] your pricing.
[36:29] Uh,
[36:33] okay.
[36:39] All right. Uh, let's see. I see some
[36:41] folks typing. Yeah, I think those are
[36:42] all the
[36:44] questions. I I feel like we have more
[36:46] questions than we have answers.
[36:49] Um, okay. For the demonstration the
[36:51] series, how much have I spent on Azure?
[36:54] Uh, probably pennies. Um, let's see.
[36:59] Uh, you can watch me try. So, the
[37:02] problem is that my my uh computer kicks
[37:05] me out all the time. You can watch my
[37:06] very lovely process for trying to log
[37:09] back into Azure and seeing if I can get
[37:11] back into my portal. I didn't want to do
[37:13] this during the stream because it's not
[37:14] very fun. Um, but let me try to do it.
[37:18] Uh, I'm I'm in the process of getting a
[37:20] new Mac because this Mac is just done
[37:23] done with being a computer. Um, it's too
[37:27] hard. Uh, everything's wrong. All right.
[37:31] So, let me try to off back in,
[37:34] do my 10 factors of authentication,
[37:40] and see if I can get back into the
[37:41] portal.
[37:46] Let's see.
[37:49] What was the Okay, so what was the code
[37:52] mode tool I mentioned on Monday that is
[37:54] similar to Monty?
[37:56] Um well the code interpreter is you know
[38:00] is one thing similar. I can't remember
[38:01] what I was talking about on Monday, but
[38:02] like um you know the code interpreter is
[38:06] is similar in that it's being able to
[38:09] run code and it's much more, you know,
[38:11] much more powerful than Monty because
[38:14] it's got access to pandas and pillow. It
[38:17] can make all these nice charts. Um I'm
[38:19] trying to think if I
[38:22] if I talked about any other code modes
[38:25] be behind beside that like code like
[38:27] sandboxes code sandboxes are such a big
[38:29] thing right now. Everybody's coming out
[38:32] with different ones. I think lane chain
[38:34] actually lang chain just asked added a
[38:36] um like a a code sandbox thing as well.
[38:39] I don't know if they're just hosted or
[38:40] not.
[38:42] Um
[38:45] yeah, and then let me try and get
[38:48] compliant. Okay. Uh, and I also got I
[38:52] linked Yeah, on the on the Monty note,
[38:54] like I was chatting about Monty with
[38:56] folks and and Drew made this cool server
[39:02] for just having like lots and lots of
[39:04] Monty sandboxes.
[39:06] Oh, code interpreter is what you're
[39:07] looking for. Yeah. So, code interpreter,
[39:10] you know, that's just built in. So, is
[39:12] as long as you're using um, you know,
[39:14] the Foundry tools or even just responses
[39:16] API, you can use it. Like I've got it
[39:19] enabled.
[39:22] Uh do I have it enabled here? Yeah. So I
[39:23] can be like, okay, make a Matt plot lib
[39:29] chart
[39:30] showing
[39:32] average rainfall in SF. I don't know.
[39:35] Let's try
[39:40] um Oh yeah, I I just just make a pretend
[39:46] data. just use pretend data
[39:50] and monthly.
[39:52] All right, I just want to get it to use
[39:54] code interpreter so we can see it. Okay,
[39:56] there we go. So, this is using code
[39:58] interpreter. And with code interpreter,
[40:00] we get access to map plot lib. Um, which
[40:03] means that we can make cool charts and
[40:05] it can even like if you upload an image,
[40:07] I've had it like annotate the image, you
[40:10] know, with with shapes on it to like
[40:12] highlight stuff.
[40:14] And then I can download
[40:16] uh my chart. Um
[40:19] and then boom,
[40:23] this is not correct data at all, but I
[40:25] did say it to be pretend. Uh so yeah,
[40:27] code interpreter is pretty powerful. All
[40:30] right, let's see. I don't think I can
[40:32] log into Azure yet. Well, I'll check. Um
[40:39] so then we have other questions. Let's
[40:41] see. You have an app locally using
[40:42] Foundry local models. Can you host it as
[40:44] a hosting agent keeping the fi models in
[40:47] the container?
[40:49] Um, well, the problem is you'd have to
[40:51] run like you need to like I don't think
[40:54] that the the fi models
[40:57] would would run
[41:00] I don't think they'd run very well in
[41:02] the container. I don't I doubt they
[41:03] would run at all because I don't think
[41:04] these containers are like GPU
[41:06] containers, right? I would be very
[41:08] surprised. So I think if you wanted to
[41:11] use
[41:13] a um local uh small language models, you
[41:16] would probably want to do like a
[41:17] container apps serverless GPU and run it
[41:21] on that and then put like point at that
[41:24] endpoint. Um but then at that point I
[41:26] don't know if you'd be saving money or
[41:28] not. Uh it depends kind of on the number
[41:31] of calls you're making and whatnot
[41:32] because with serverless GPUs you you
[41:35] still they're pretty expensive. Um
[41:39] well you can theoretically do scale down
[41:40] to zero but it depends on the model. So
[41:43] you could try you could try that. Um
[41:46] uh yeah it's not happy.
[41:50] Um
[41:52] but here's like this was a example we
[41:54] did with running NIM on a serverless
[41:56] GPU. Um here's the like a tutorial.
[42:02] Um
[42:05] there's probably one Oh yeah, there's
[42:07] also let's see opening IGBT will oss
[42:10] llama. Yeah, I don't actually see one.
[42:12] It's a good question. I don't see any
[42:14] one about doing like deploying with
[42:16] foundry local itself. But um
[42:20] yeah, you so those might be options, but
[42:22] I don't know that you I think I feel
[42:24] like at that point you wouldn't end up
[42:26] saving any money,
[42:28] but you might. Depends. Uh I know some
[42:31] people that run, you know, some
[42:32] companies do run small language models
[42:34] in production and because they have so
[42:36] much scale uh then it's you know it's
[42:39] fine for them to run a serverless GPU
[42:40] because it's it's going to be running
[42:42] you know they're they're using so much
[42:44] scale that um you know they make good
[42:46] money off of it. So, I know some people
[42:48] did move like um there was a great
[42:50] Shopify talk where they moved from
[42:52] OpenAI model to Quen uh like a a small
[42:57] Gwen model and they saved like it was
[42:59] like 75x cost savings. Um and they're
[43:03] they actually got their accuracy even
[43:05] better due to a prompt optimization
[43:06] process they use. So, uh yeah, if it's
[43:09] practical, you could use it. All right,
[43:12] I see lots of interesting cost. So, I
[43:14] think we also have to figure out cost
[43:15] because everyone's asking about cost. Uh
[43:17] I can't log into
[43:20] uh Azure right now so I can't show you
[43:21] cost but um that did seem to be a big
[43:24] question that we're getting um is more
[43:26] insight in cost. I'm trying to remember
[43:28] was there costs on that agents
[43:30] dashboard.
[43:32] Uh
[43:34] I'm just going to look at the
[43:35] screenshot.
[43:37] Uh I don't think it necessarily had cost
[43:40] here. I think you'd have to look at the
[43:43] cost in the Azure portal. Um, I don't
[43:46] know. Foundry
[43:48] does the new foundry have it's not under
[43:52] here. It could be under operate. Maybe
[43:54] if they were going to have costs, maybe
[43:56] we'd find under operate. These are great
[43:59] questions.
[44:02] Uh, any inputs using the keyword
[44:04] classification pattern before burning
[44:08] tokens in a multi- aent environment? Uh,
[44:11] you mean like basically doing like
[44:12] structured outputs to on your input to
[44:16] route something to the best like sub
[44:19] agent for it? Is that kind of what
[44:20] you're thinking of doing?
[44:23] Routing. Um, yeah. I mean, I think that
[44:27] it I think if if the use cases are
[44:31] discreet enough, uh, then then you could
[44:36] you could do that. Um it it really
[44:38] depends like you know if the if you can
[44:42] if you can have discrete enough use
[44:44] cases. Um,
[44:48] so it's, you know, certainly example
[44:50] that we show is like, oh, okay, you you
[44:52] you get in this input, you're going to
[44:53] decide, is it going to go to this agent,
[44:54] this agent, or this agent. But your
[44:56] agents do need to be really really
[44:58] distinct from each other, right? If
[44:59] there's any sort of ambiguity,
[45:02] uh, you know, it's it's it's hard. Um,
[45:05] so yeah, I think that's only going to
[45:07] work if you have really really distinct
[45:09] use cases. If it's not really distinct,
[45:11] then I think you just got to have an
[45:13] agentic loop. um that's can recover if
[45:17] it made the wrong selection.
[45:21] Um okay so LPK thinks that you want more
[45:26] documentation on tracing for the
[45:28] different frameworks.
[45:30] Um
[45:33] yeah. So for lang for lang graph um I
[45:38] you're going to want to use the lang
[45:39] chain Azure AI package like we showed
[45:41] with the um
[45:43] the enable autoracing ability.
[45:47] That would be as far as I know that's
[45:49] the the the best way of doing it. Um
[45:51] with the OpenAI SDK
[45:54] uh yeah we we you're right we don't
[45:56] really document that for the OpenAI SDK
[45:58] itself. I use
[46:01] um if you're just using that directly
[46:04] then I use a different package
[46:08] um
[46:11] called
[46:14] uh this one I use this one open
[46:16] telemetry instrumentation open AI
[46:20] and it's not like an official Microsoft
[46:21] one it's from this random company
[46:26] um but I use that And then uh and then
[46:30] where do we set it up? Uh
[46:34] way at the bottom here, right? And then
[46:37] I just instrument it.
[46:40] Uh I don't know if there's a newer way
[46:42] of doing that, but it's it seems to work
[46:44] fairly well uh in in my experiment
[46:47] experiments. Uh so yeah, it's good. We
[46:50] should document things better. Um we can
[46:52] let me check the lingshine on Azure docs
[46:54] to see if we have open telemetry called
[46:57] out there. Hopefully we do because there
[46:59] is
[47:00] like a whole portal now
[47:03] um dedicated to ling chain. No, I don't
[47:07] think it's this one.
[47:09] Get started with link chain and
[47:11] lingraph.
[47:13] Um
[47:15] connect with product endpoints. Use
[47:17] found on default.
[47:20] Use foundry. Here we go. Use foundry
[47:22] observability to trace apps. Okay. So,
[47:25] check out this.
[47:29] Um,
[47:32] and hopefully this says what we said to
[47:34] do. Yeah, it looks looks like
[47:38] um Oh, you also Well, this one is like
[47:40] manually creating the the tracers. Um,
[47:44] so you have different options here. But
[47:46] what did we use the enable in? What did
[47:50] we do? Enable auto tracing. enable auto.
[47:54] Oh, interesting. That's not even
[47:57] documented here. Okay.
[48:00] All right. That that's another question
[48:04] I should write for the team. Um I got to
[48:06] have so many questions to bring back to
[48:08] the team after this.
[48:10] Um
[48:12] yeah, so uh those let me get also the pi
[48:17] URL for that package that I use. Um,
[48:20] what was it called?
[48:24] This one. This one.
[48:30] All right.
[48:35] And then also lang chain enable
[48:37] instrumentation.
[48:40] No, it was enable
[48:42] enable
[48:44] auto tracing. Okay. enable
[48:49] auto tracing from link chain as your AI.
[48:54] Okay.
[48:56] Um Pablo says, "Would it make sense to
[48:58] use Cosmos DB for link chain link graph
[49:01] hosted agents?" Um I mean depends what
[49:04] you're using it for, right? Like are you
[49:06] going to use it for your database? um
[49:10] use it for
[49:13] so I mean I think like saying you can
[49:14] you like you can certainly use Azure
[49:16] Cosmos D um the thing to keep in mind
[49:19] with the hosted agents is that the agent
[49:21] has its own identity so when you're if
[49:24] it if you're going to have the agent
[49:25] authenticated Cosmos DB you do need to
[49:28] assign the um assign the arbback role if
[49:33] you're doing you know keyless uh keyless
[49:36] authentication
[49:37] uh so you can just take the the approach
[49:40] I use for search service. Um we're going
[49:43] to do infra
[49:46] post deploy. Okay. So you got first you
[49:49] have to find the agent's principal ID
[49:51] and then you need to assign whatever
[49:53] role. So if you were going to have your
[49:54] agent use Cosmos then you would assign
[49:57] the Cosmos role here. Oh the question
[50:00] was for short and long-term memories. Um
[50:05] yeah. Okay. So when we say short-term
[50:08] memory, if we mean like the session,
[50:10] then um that we should already be able
[50:13] to do the session um by using the the
[50:17] conversation ID. Um we'll we'll verify
[50:20] that by adding that to our sample. Uh so
[50:23] I wouldn't I wouldn't want to I don't
[50:25] think you necessarily want to go through
[50:26] the effort of reimplementing that if
[50:28] that's already working for you. Although
[50:29] I do think that they said like don't the
[50:32] sessions run off run out after like 30
[50:35] days I think. So that might be a reason
[50:37] to use Cosmos to be because I've I I
[50:39] feel like there was something about them
[50:42] running out after 30 days. Um
[50:47] yeah, so that might be a reason to use
[50:49] it. Uh yeah, and I certainly we use
[50:51] Cosmos DB for chat history in our other
[50:54] repos and it it works quite well for it
[50:56] and I have some talks about that because
[50:58] that's what we use in the rag repo. Um
[51:01] so if you wanted to use it and have that
[51:04] persistence, you could do that. Uh and
[51:07] it could you work for long-term as well,
[51:09] it does have vector search and full text
[51:12] search now, so you can like search the
[51:14] memories pretty decently. So yeah, I
[51:17] think it could work well for both. Um
[51:19] there was that didn't we have that in
[51:22] yesterday's blog post? Yeah, we had that
[51:23] blog post about the Cosmos DB memory
[51:26] patterns right and we were talking
[51:28] yesterday about how
[51:31] uh how to
[51:33] you know how to implement those for
[51:35] agent framework but you can do something
[51:36] similar
[51:38] for link chain.
[51:41] Um okay, Colleen asks any
[51:42] recommendations or documents to handle
[51:44] vector drift over the long term long
[51:46] run. All right. First, I'm gonna
[51:48] remember what vector drift is. Nope.
[51:51] Vector drift lighter. No.
[51:55] Oh, look at this. We have a a blog post
[51:57] about vector drift in Azure AI search.
[52:00] Um, who is okay
[52:03] no longer actually represents semantic
[52:05] intent.
[52:08] Um,
[52:11] but why do we get Wait, why do we get
[52:14] vector drift models? Well, the model
[52:17] wouldn't change because you're going to
[52:18] use the same models before.
[52:21] Um,
[52:24] well, no, this would never happen. You
[52:27] can't like this is impo. I don't
[52:29] understand because if you're if you
[52:31] index it with one embedding model and
[52:33] you generate your embeddings with the
[52:34] other like you just physically cannot I
[52:37] mean I guess you could do a query but
[52:38] you're not going to get any it's going
[52:40] to be a nonsense result. Um so I guess I
[52:43] would say here like this should never
[52:44] happen. You should always be using the
[52:47] same embedding model for your embedding
[52:49] step as your query step. Um, one thing
[52:52] you can do is like store that in your
[52:54] environment u variables or even when I'm
[52:56] doing like if I'm storing in like a
[52:57] database column, I put the embedding
[52:59] model name in that column name. Um,
[53:02] because you're going to get such bad
[53:04] results if you attempt to even do a
[53:06] query with the wrong model. So, I would
[53:08] say like this should just not happen.
[53:10] Um, let's see. Um, incremental content
[53:15] updates without re-mbedding.
[53:18] Okay. new content, introduce, updated
[53:20] terminology, policy changes,
[53:24] um, new product or domain concepts.
[53:27] But I don't I feel like that's not even
[53:29] an issue because I feel like if there's
[53:31] a new product or domain concepts, it
[53:34] whether you in whether you made an a
[53:36] vector for that content today versus a
[53:39] month ago, it would be the same vector.
[53:42] Right? Now, if you were doing like a
[53:44] like if you were fine-tuning your
[53:45] embedding model based off your original
[53:47] data, then I could see this being an
[53:49] issue, right? Because if you're doing a
[53:50] because some people do do that. They do
[53:51] fine tune embedding models in order to
[53:53] really improve retrieval if they have
[53:54] really domain specific specificity. Um,
[53:59] then of yeah, of course, like if your
[54:01] domain changes, then you need to
[54:02] fine-tune your model. Again,
[54:04] um
[54:06] uh I I just don't I don't understand how
[54:10] a re-mbedding would help in this case.
[54:12] Um, this I agree with. Okay, so if you
[54:14] do change your chunking over time, I
[54:16] agree. This is what I see as the biggest
[54:17] issue is you change your chunking over
[54:19] time and we always worry whenever we
[54:21] change the chunking algorithm on our rag
[54:23] reap like uh oh, people are going to be
[54:24] mad, right? Um, I agree on this one. So
[54:27] yeah, I think that if you do change your
[54:29] chunking strategy, you ideally are going
[54:32] to create a parallel index and re-chunk
[54:35] everything to be consistent there. Um,
[54:39] and yeah, I guess you could chunk. Yeah,
[54:41] you could store that as metadata um so
[54:43] that you knew what chunking strategy was
[54:46] used. So I do agree with that. I can I
[54:48] can see that being um you know
[54:52] an issue.
[54:55] Okay. Um
[54:58] yeah. So those are my thoughts on vector
[55:00] drift at least according to this blog
[55:01] post what I understand of it.
[55:05] Um all right
[55:08] cool. Okay. All right. We're at the end
[55:11] of the hour. Thank you for all the great
[55:13] questions
[55:14] and I know we need to I need to work on
[55:18] um having some more solid answers then.
[55:21] But that's part of why we're trying out
[55:22] this new technology so we can learn what
[55:24] the questions are and figure it out
[55:27] together. And uh so thank you everyone.
[55:29] This is like this is like the office
[55:31] hours is where I learn learn the most.
[55:33] So I always appreciate it. Okay. So I
[55:38] will see. Yeah, so many questions today.
[55:42] You're right, Pablo. Um, I will
[55:44] hopefully see you all tomorrow for
[55:46] evaluations and hopefully I'll have
[55:49] logged into Azure by then. Yay. Okay,
[55:52] bye everyone.

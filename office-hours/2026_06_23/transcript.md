[00:03] Okay, good. That is recording.
[00:07] Great.
[00:12] All right,
[00:13] welcome everyone to our weekly Python
[00:17] plus AI office hours. Uh this is where
[00:20] we get together to talk about what's
[00:23] happening in the Microsoft GitHub
[00:25] foundry side, what's happening in the
[00:28] industry, anything I've been working on.
[00:31] Uh so generally I start off with this
[00:34] weekly news roundup here and uh but also
[00:38] we just talk about your questions in the
[00:41] chat. Uh so if you do have questions,
[00:43] write them in the chat. Just type them
[00:46] out. Uh but since we are recording on
[00:48] StreamYard, uh the only audio is from
[00:51] me. So just write your questions in the
[00:54] chat. All right. So let's see what what
[00:58] kind of news do we have this week. Um a
[01:02] big thing that we've been talking about
[01:04] is that Copilot uh and pretty much
[01:08] everywhere VS Code CLI app supports
[01:11] bringing your own key. Uh so that's
[01:14] important for giving you lots of model
[01:16] choice. So if you find that you know the
[01:19] enthropic models are too expensive or if
[01:21] they're you know forbidden in your
[01:22] country or whatever might be happening
[01:24] any particular week you can bring your
[01:27] own um your own models. Um so uh you
[01:32] could be bringing models from open
[01:33] router. You could be bringing models
[01:35] that are running locally on your machine
[01:37] if you have a powerful enough machine to
[01:41] run open watt models like the Quen
[01:44] models are are very good. I've heard a
[01:46] lot this week about the GLM models.
[01:48] Everyone talking about GLM 5.2.
[01:51] Um Kimmy 2.6 is very good. I've been
[01:54] testing that this week. So, uh yeah. So,
[01:57] basically, wherever you're using
[01:58] Copilot, um you should be able to bring
[02:01] your own models. Here's the um this is
[02:05] the blog post
[02:07] from the VS Code team about the same
[02:09] thing. Uh bringing your own language
[02:12] model in VS Code. Um,
[02:16] and they go through some examples here.
[02:20] This one's using a mist.
[02:23] Uh, you could also be installing
[02:24] extensions that give you access.
[02:27] And, um, yeah, you can also change the
[02:32] defaults for the smaller models that are
[02:34] used for stuff like chat titles and
[02:37] commit messages.
[02:41] So, you know, hopefully that gives
[02:42] everyone more model choice and, you
[02:45] know, maybe allows you to be more
[02:46] costefficient as well.
[02:49] Um, related to model, a few more things
[02:52] related to models that you could use
[02:54] with co-pilot,
[02:56] Microsoft AI announced a bunch of models
[02:59] at Microsoft Build. One of them is a
[03:01] coding LLM which is MAI code1 flash and
[03:05] that should be now available across all
[03:08] the co-pilot surfaces here. You can see
[03:10] Jet Brains, Copilot CLI, Copilot app,
[03:12] Copilot chat on GitHub, right? Lots of
[03:14] places. Uh so I'm still on Opus. Um you
[03:19] know I'm not going to switch because
[03:21] it'll bust my cash for this session. Uh
[03:23] but we could, you know, do it in a new
[03:27] just a new quick chat here. Let's make
[03:30] sure. There we go. We can see MII code
[03:34] one flash.
[03:35] Uh, so I've heard it's basically similar
[03:37] to Haiku. Uh, so any task that you would
[03:41] do with HiQ, um, you know, tasks that
[03:44] you think are not too tricky could be a
[03:48] good one for MI code one flash.
[03:52] So check that model out. Let me know
[03:55] what you think of it. Uh I really
[03:57] haven't spent a lot of time with it yet.
[03:59] Um but I'm excited that we're starting
[04:01] to have our own models.
[04:04] Uh so that's on the co-pilot
[04:07] front. Um
[04:10] uh one more thing related to VS code is
[04:14] that in the latest release the there is
[04:17] support for
[04:19] um the what's called the enterprise
[04:22] managed authorization for MCP.
[04:25] Um that's a bit of a a mouthful. Let me
[04:29] find the a better link for it. Uh so
[04:32] here there we go. So this is a an
[04:36] article about it.
[04:38] It's it's a new part of the MCP Ospec.
[04:42] And here it makes it easier for um
[04:47] enterprises to have MCP servers that
[04:50] like you can have you could have one MC
[04:52] server connect and then that
[04:54] authorization would be shared across a
[04:56] bunch of MCP servers.
[04:58] uh and this way you know all the MCP
[05:02] servers can go through a common
[05:03] authorization
[05:05] flow and they can they can also audit
[05:08] that authorization right uh so
[05:13] yeah so here there's like this diagram
[05:15] here blah blah blah right um so instead
[05:19] of the user doing the off for every
[05:21] single server this time uh for this set
[05:24] of servers it's going to go through that
[05:27] identity provider in a consistent way
[05:29] across all the servers.
[05:32] Uh so uh that's supported by Microsoft
[05:36] VS Code. It's supported by claude
[05:39] uh a bunch of other places as well. Um
[05:44] so uh yeah so people are excited about
[05:46] that uh for people who are doing MCP uh
[05:49] at the enterprise level and want better
[05:52] security for the off.
[05:55] All right. Uh let's see more on the
[05:58] Python side.
[06:01] Um I thought this was cool for the
[06:03] Microsoft agent framework. Uh in the
[06:05] most recent release they added this
[06:08] agent loop middleware.
[06:12] So um in the middleware you can see this
[06:15] is you know because everybody was
[06:17] talking about loops for the last few
[06:19] weeks at least on social media on
[06:21] Twitter. Um, and the idea here is like
[06:23] rerunning an agent until some condition
[06:26] is met. Now, it's already the case that
[06:27] an agent runs until it gets to an
[06:30] answer, but that answer may not actually
[06:32] be the goal you want it to have.
[06:36] Exactly. Like, so you can like really
[06:38] force an agent to loop even harder using
[06:41] different techniques. Um, and uh there's
[06:46] three techniques in this agent loop
[06:49] middleware that are interesting. So the
[06:52] first one is the Ralph loop. Uh this was
[06:54] the first famous loop and um this is
[07:00] this was came about even a year ago and
[07:02] this is also what is the basis for
[07:05] codeex goal and claude code goal. I
[07:08] think they both call it goal. Um and so
[07:11] this just what does this do? It's no
[07:14] exit criteria bounded by an optional max
[07:16] iteration includes feedback tracking. So
[07:19] it accumulates progress log
[07:22] um restarts sees pass
[07:25] is complete.
[07:27] So I admit I don't even quite understand
[07:29] the RAL loop because it says it has no
[07:31] exit criteria but it has to
[07:34] I think it should it does see that it
[07:37] says it has an is is complete. So there
[07:40] there must be something that's signaling
[07:41] completion besides just a standard um
[07:44] agent loop. So, I think I'd actually
[07:45] have to try that out to see what happens
[07:48] when you use the Ralph loop versus just
[07:50] a standard agent run.
[07:53] Justin says you got to loop harder, loop
[07:55] more, and loop better. Yeah, just put it
[07:57] in your system prompt. That's all you
[07:58] have to do for loops. Let's just add
[08:00] that. Um, there's predicate. Uh, and
[08:04] this one makes sense. This is just a
[08:05] callback function, right? So, you have
[08:07] any sort of callback function and you
[08:09] know, so that in the examples here are
[08:12] like do you have remaining to-dos? Do
[08:13] you have background tests running? Um
[08:16] because those are built in with existing
[08:18] providers, right? So that makes sense.
[08:20] If there's any sort of predicate uh some
[08:23] like callback function that you can
[08:25] define to return true or false, then
[08:27] it'll just keep looping
[08:29] on um you know until that's false. And
[08:33] then judge, this one makes sense too. So
[08:35] you give it a judge and it's an LLM
[08:36] judge and that judge is deciding whether
[08:39] the original request was answered. Uh,
[08:41] and it's using a structured output judge
[08:44] verdict and it'll just keep looping if
[08:47] the judge says it's not done. That one
[08:48] makes sense to me, too. Yeah, the raw
[08:50] loop is the only one that I'm not
[08:52] entirely um understanding. So, I think
[08:55] I'd have to really try that out to see.
[08:58] Um,
[09:01] and
[09:04] okay. And then they added some changes
[09:05] to approval handling. um because you
[09:09] know of course if you're trying to loop
[09:10] then approval from humans is going to
[09:13] interrupt with your loop. So they kind
[09:15] of changed that a bit.
[09:17] So there you go. If you wanted loops you
[09:20] can um try that with Microsoft agent
[09:24] framework and add this middleware. Uh
[09:27] let's see if they had an example here.
[09:28] Sample. Yay samples. Okay so like the
[09:32] here's the judge
[09:35] the judge loop. Let's see what this loop
[09:37] is doing.
[09:40] Uh dot dot dot explain why the sky is
[09:44] blue and sunsets are red. Okay.
[09:48] Uh so that's the agent
[09:51] and there's the middleware which is the
[09:53] loop. There's the loop. You have a judge
[09:55] client criteria mentions the moon
[09:58] includes at least one good joke is
[10:00] written as a single piece of fluent
[10:01] pros. Max iterations four.
[10:04] Okay.
[10:07] And that
[10:09] uh makes sense. Okay. It's not the most
[10:12] exciting thing for the agent to work on,
[10:15] but it does make sense. Uh let's see.
[10:18] Refinement loop. Is this one going to be
[10:19] a Ralph loop here? Agent loop
[10:22] middleware.
[10:27] Oh, no. This one's with a should
[10:28] continue predicate. Okay. So this one is
[10:30] using should continue
[10:33] and should continue
[10:36] is tracking feedback.
[10:40] And what is this one doing? Suggest a
[10:42] name for a note-taking app. Okay. So I
[10:44] think this one's getting feedback from
[10:47] another model and deciding when it's
[10:49] done. All right. So there's various um
[10:55] you know examples in the repo that you
[10:57] could look at.
[11:00] to get an idea for how to use it.
[11:06] So, Pablo says, "I have seen several
[11:08] analyses where people say that using
[11:09] loops without proper specs would lead to
[11:12] high token consumption with a high
[11:14] probability of notes desired features."
[11:16] Yeah, I agree. Yeah.
[11:19] Yeah, I agree. Um, I mean some of these
[11:22] things like like clearly like they're
[11:24] going to loop a bunch because the
[11:25] original prompt didn't even adhere to
[11:29] what the loop was checking for, right?
[11:31] So, you know, like the with the judge
[11:34] loop, um, you know, this one says,
[11:36] explain why the sky is blue and sunsets
[11:37] are red. And then the judge is saying,
[11:39] "Oh, it has to include at least one
[11:40] joke." Well, that's going to loop for a
[11:42] long time because it never got asked for
[11:44] a joke. Um, so you know, your your your
[11:50] agent prompt should ideally have
[11:53] as much information as your judge
[11:55] prompt, right? Because and sometimes we
[11:57] build these like LLM as judges and they
[11:59] have all this good information in it
[12:00] because that's what they're checking.
[12:02] Um, but if you find that your output is
[12:05] actually consistently failing that LM is
[12:07] a judge, then probably like that
[12:09] criteria belongs in the system prompt as
[12:12] well, right? Um, the LLM as a judge is
[12:14] just a second check. So, you know, your
[12:17] LLM as a judge shouldn't like really
[12:20] know more than your system prompt.
[12:24] Um, unless it's that you're just really
[12:26] trying to like the reason that your
[12:28] system prompt might not have as much
[12:30] information is that if you're really
[12:31] trying to save on tokens in your system
[12:34] prompt and you you know you think you
[12:36] can at least you think with the current
[12:38] models that you're using that you can
[12:39] get away with skipping some details and
[12:43] that's why your judge LLM is checking
[12:45] for things that aren't in your system
[12:47] prompt. That would be the reason you
[12:50] know why. Um but that does mean that you
[12:54] know as you like move models then your
[12:57] assumptions about what works uh you know
[13:01] could break. So you know I think it's
[13:03] important like have all the criteria in
[13:04] your LM as a judge. Um but also consider
[13:08] like
[13:09] when you run that you know if you are
[13:12] failing then move that back into your
[13:15] original prompt as well. Um, and
[13:18] consider like caching, right? Like the
[13:22] length of the system prompt isn't
[13:24] necessarily as big of a deal. Like small
[13:26] little tokens like a few sentences here
[13:28] and there isn't that big of a deal if
[13:30] you are able to take advantage of prompt
[13:32] caching, right? If that system prompt is
[13:35] able to be reused and cached.
[13:40] Um, and Justin says, "If you have bad
[13:42] specs with coding agents, it's going to
[13:44] fail the larger your
[13:47] uh code base gets."
[13:49] Yeah. Uh, yeah, I agree. Um, specs, best
[13:54] practices, conventions,
[13:56] um, all of that stuff. Like there's I've
[13:59] been looking at a lot of LLM generated
[14:02] code and pros over the last few days and
[14:04] there is so many LLM code smells out
[14:07] there that you really have to counter
[14:10] the uh LLM's bad tendencies with you
[14:14] know with detailing what your best
[14:16] practices are, right? Like and um you
[14:19] know making sure it knows what you
[14:21] consider to be good.
[14:27] Are these loopes open to modify the
[14:29] middleware to add agents evaluation etc.
[14:34] Um well this is middleware. Let's see
[14:36] what kind of middleware this actually
[14:38] is. Um so this middleware is on what
[14:42] level is it on?
[14:46] Um okay so it is agent middleware. So
[14:50] agent middleware for agent framework
[14:54] means that let me get my
[14:58] um
[15:01] let's see where did we Python agents
[15:04] resources let me get my slides up for
[15:07] that uh building your first agent okay
[15:11] middleware middleware
[15:15] okay all right so with agent framework
[15:17] you have an agent and there's three
[15:19] different kinds kinds of middleware.
[15:20] There's agent middleware, chat
[15:21] middleware, and function middleware.
[15:23] Agent middleware is the highest level
[15:25] middleware. So, it intercepts the run
[15:27] call. So, when the you know when you say
[15:29] agent.run in agent framework, that's
[15:32] what it's going to intercept and it gets
[15:33] access to the messages, the actual agent
[15:36] object, the result uh and whether to
[15:38] terminate. Uh so that's it's it's at
[15:41] that layer because that's the layer it
[15:42] makes sense to do it at, right? So like
[15:44] you know um you know your most basic
[15:47] agent middleware it's going to receive
[15:49] the agent context going to do something
[15:51] call the next step in the agent and then
[15:53] maybe do something else. Uh so that's
[15:56] that's what this loop middleware is is
[15:59] an is an agent middleware. Here's the
[16:02] middleware slides if you're curious. Um
[16:07] so so yeah so you you know this is
[16:10] already you know this is sitting at that
[16:12] agent middleware level. Um so you could
[16:15] add a additional middleware. Um you
[16:19] could you could write your own I mean
[16:21] thing here's a great thing is that this
[16:22] is all open source code right so you
[16:26] know you can use this you know you can
[16:28] try using this but also if you find that
[16:31] this isn't working for you and you need
[16:34] more flexibility you can either file a
[16:36] feature request like oh add this option
[16:38] parameter to the middleware or you just
[16:41] copy this code and you modify it that's
[16:43] what I think is great about middleware
[16:45] like it's you know it's fantastic when
[16:47] the frameworks you know agent framework
[16:49] and lane chain have middleware built in
[16:51] that they think is really common. Um,
[16:53] but also when these are open source
[16:55] frameworks, you just take that
[16:58] middleware and make your own middleware
[17:00] based off of it, right? If it doesn't do
[17:03] what you need it to do, you shouldn't
[17:05] have to feel beholden
[17:07] um to, you know, to that. And middleware
[17:10] is generally pretty modifiable because
[17:12] middleware isn't using um is usually not
[17:16] you like it's not like it's it should
[17:18] should be using things in a safe way
[17:21] because middleware is generally designed
[17:23] so that you can build your own
[17:24] middleware right so I feel pretty
[17:26] comfortable taking a framework's
[17:29] middleware as a basis and then you know
[17:33] modifying it to be my own um variation
[17:36] on the middleware. So that is what I
[17:39] would suggest.
[17:47] Let me just read here. Sorry. Shouldn't
[17:50] have drink. Okay. So John says um oh uh
[17:56] okay let me also just see if there's any
[17:58] additional questions on this. Um we also
[18:01] got oh and they did a whole harness
[18:03] agent too. That's worth pointing out on
[18:05] the agent framework is that they have
[18:08] added this like harness agent. Uh this
[18:10] one's on.net.
[18:12] Oh no, no, there we go. The Python
[18:15] create harness agent. So if you want,
[18:17] this is actually similar to linkchain um
[18:20] deep agents.
[18:23] If you want a agent that has you know
[18:27] everything built in, um let me see if I
[18:30] can find the release where they
[18:31] announced it. Then you can use this
[18:33] harness harness agent. Um to approval
[18:39] uh trying to find let me find all the
[18:42] releases releases
[18:46] it was pretty recently that they
[18:49] added it. Um add background agent
[18:52] support uh add harness agent. Okay this
[18:56] was it. Um,
[18:58] so in 1.7, which was
[19:02] a couple weeks ago, they added the
[19:04] harness agent,
[19:07] which I I think of as being similar to
[19:09] the link chain
[19:12] deep agents.
[19:14] Um,
[19:16] and let's see if they have a good
[19:18] explanation of it. Harness agent
[19:20] feature, a preconfigured bundled agent
[19:23] batteries included. Right. So you get um
[19:26] call history persistence compaction and
[19:28] a rich set of default context writer
[19:30] to-do mode memory skills
[19:33] and you got this like system prompt
[19:35] here. Um
[19:39] so this also kind of would be more
[19:40] similar to using like the copod SDK
[19:43] which is has more of an opinionated um
[19:46] harness that has more stuff built in.
[19:48] Right? So you can see everything that it
[19:51] builds in here. it's, you know, it's got
[19:54] u it's got middleware, it's got skills,
[19:55] it's got tools, right? So, that's
[19:58] another thing to consider with agent
[20:00] framework as a um you know, a bigger
[20:04] feature that's interesting.
[20:07] Okay. All right. So, I saw there was a
[20:10] question from John. I'm trying to
[20:12] understand use cases for MCB and
[20:14] production servers. for production
[20:16] systems. For example, if a user wants to
[20:18] give access to multiple MCP servers, how
[20:20] can they do that? Before they use, do
[20:22] they have to authenticate the agent for
[20:23] all MCP servers? Um, you know, once the
[20:27] user authorizes the agents to use on
[20:29] their behalf,
[20:30] um, what use case you see in production
[20:32] system for general users, not
[20:34] developers. So when you say for general
[20:36] users then I assume we're talking about
[20:38] people using MCP with agents like coding
[20:43] agents or um you know with other agents
[20:46] that you know like claude desktop for
[20:48] example that supports MCP.
[20:51] Um so that's where you know what we were
[20:53] just talking about the enterprise manage
[20:55] off um is is actually use uh useful is
[21:00] that you want to
[21:03] um you know this is for the end user
[21:06] they'd be able to authenticate to the
[21:09] identity provider. Let me see the cloud
[21:11] announcement because that might be the
[21:13] one that makes it a little more um
[21:16] clear. Clad
[21:19] centrally. There we go. Okay. So, this
[21:21] was their
[21:23] announcement for it. So, admins can now
[21:25] provision MCP connectors for their whole
[21:27] organization through their identity
[21:28] provider starting with Octa.
[21:31] They don't mention Entra. Um, uh, users
[21:34] get connector access automatically on
[21:36] first login. Um
[21:40] and uh
[21:43] yeah and so they can actually
[21:46] the admins can enterprise can authorize
[21:49] the connector.
[21:51] So you're going to connect your
[21:52] identifier to claude and choose which
[21:54] connector. So I think on the VS code
[21:57] side it would be uh you know with Entra.
[22:00] Let's see what happens if we search
[22:02] manage authorization. Well, obviously VS
[22:05] Code also could be octa, you know, it's
[22:07] just what what matters is your identity
[22:08] provider. So, Claude, VS Code, they all
[22:10] support this. Now, the question is, does
[22:12] your identity provider
[22:16] um support it too?
[22:18] Um,
[22:22] let's see. There we go. There touch.
[22:25] Okay.
[22:26] Where is
[22:30] uh this is the one from MCP the MCP or
[22:37] so. So that's actually that would be the
[22:38] more official
[22:40] host. Um Octa is the first supported
[22:43] identity provider.
[22:46] Uh
[22:50] servers and there's also which servers
[22:52] support it.
[22:55] Um,
[22:58] I'm trying to see if we
[23:05] So, what I don't see is specifically
[23:09] whether Entra
[23:14] supports it. It's It claims It claims,
[23:18] you know, that AI answer claims it does.
[23:20] I'm going to ping
[23:22] um ping Harold uh from VS Code. Does
[23:27] Entra support EMA?
[23:35] All right. I'm guessing, you know, I'm
[23:37] guessing Entra doesn't. Um but if you
[23:40] were using VS Code or Claude and Octa
[23:43] was your identity is your identity
[23:45] provider for an org, then you know that
[23:47] does streamline the process there. Um
[23:49] but even if you don't have that like you
[23:52] know then they're going to be yes the
[23:55] user will individually authenticate the
[23:58] agent to each of the MCP servers and
[24:01] then the you know the that coding agent
[24:04] will you know it's it's an OOTH client.
[24:07] So an OOTH client is going to remember
[24:09] the OOTH connections. It's going to take
[24:12] care of refresh tokens like here. Um,
[24:15] you know, I there's these authentication
[24:18] providers and I can like clear the cache
[24:20] if I want to. Um, but um otherwise, you
[24:24] know, the O is stored for um for a bunch
[24:28] of servers. So, for example, here, let
[24:31] me show you. I've got a few servers,
[24:34] right? So, oh, I just have one right
[24:35] now. So, hugging face is a server that
[24:38] requires authentication.
[24:41] Um,
[24:43] uh, actually wait, let me show with with
[24:45] authentication. This is actually how we
[24:46] do authentication for this one. So, I'm
[24:48] going to say start. And here you can see
[24:51] it wants to authenticate to hugging
[24:53] face. So, I'm going to say allow.
[24:56] And then um you can see that VS code
[25:00] already knows that I have uh logged into
[25:03] this uh authorization server before. So
[25:06] it has actually remembered my username.
[25:08] I can change it if I want. Um but I'll
[25:10] go ahead and and use this. Right? So VS
[25:13] Code is, you know, is acting as an OOTH
[25:15] client. It's remembering what I've
[25:16] logged into an identity provider with
[25:18] before. And then actually and that was
[25:21] it. That was all I had to do. Now, if I
[25:22] had um so it must have already had a
[25:26] token and a refresh token for that one.
[25:28] And then I can choose to disconnect the
[25:30] account and all that stuff. Um let me
[25:33] try doing it from scratch so you can see
[25:35] like the actual OOTH flow. So I'm just
[25:38] going to say sign into another account.
[25:40] I'm going to say open.
[25:43] And um there we go. It's already logged
[25:47] in. Too easy. I wanted to show like the
[25:49] hugging face flow. Um, okay. So, my
[25:53] browser also has my hugging face login
[25:56] cache, right? So, this is all part of
[25:57] OOTH, right? Like OOTH does try to make
[25:59] this easier. So, yeah, if you've already
[26:01] logged into, you know, an OOTH provider,
[26:03] like it tends to remember your
[26:04] credentials, my browser's already logged
[26:06] in, so it did that login step really
[26:08] quickly. If I wasn't logged in anywhere
[26:10] and like didn't even have an account,
[26:12] then, you know, then I would do the
[26:13] entire OOTH login flow from the
[26:16] beginning.
[26:18] Um but um but yeah, so that's that's
[26:21] that's the point, right? If you're if
[26:23] you're using an an agent like Claude or
[26:28] um GitHub Copilot that has um support
[26:30] for MCP, then it should have support for
[26:33] doing the MCP off flow with OOTH and it
[26:36] should take care of refresh tokens and
[26:38] stuff like that. Um the advantage of the
[26:40] new feature announced this way with
[26:42] enterprise managed authorization is that
[26:44] it's better auditing and it is less
[26:47] login if all of the MCP servers are
[26:50] going through the same identity provider
[26:51] right or if many of the MCP servers are
[26:53] going through the same identity
[26:54] provider.
[26:57] Um so Pablo says is the authorization
[26:59] linked with the specific MSV tool
[27:01] permissions that the current user should
[27:03] have? Where would that be configured in
[27:06] the Microsoft platform?
[27:10] Um
[27:12] h
[27:14] yeah I don't I don't know where you
[27:15] would configure that in the Microsoft
[27:17] platform. Um I think maybe if you were
[27:20] doing your own um MCP registry. Let me
[27:24] see what MCP like registry enterprise
[27:27] controls because we might give people
[27:33] yeah let me see on these docs we may
[27:35] give some additional
[27:38] customization right so you can yeah so
[27:40] you can there is some
[27:44] um ability here that if you're using
[27:46] GitHub enterprise uh sorry copilot
[27:48] enterprise or copilot business then for
[27:51] the enterprise level First, you'd have
[27:54] to create an MCP registry. So, if you
[27:56] really wanted to lock stuff down, right,
[27:58] you'd create an MCP registry and then
[28:00] you have to create an allow list policy.
[28:04] Uh, so you'd say, okay, MCP servers.
[28:08] Uh, then you'd enter the name of your
[28:10] registry. So, this example is using
[28:12] Azure API center for the registry. Um
[28:16] and then uh you decided like are you
[28:19] going to allow all or only servers from
[28:22] the registry. So that that's just which
[28:24] servers you can use. Um and then
[28:29] and then oh and that's so that's per
[28:30] organization that's for an enterprise.
[28:32] Okay. All right. So then oh and then you
[28:36] can do let's see MCP allow list
[28:38] enforcements.
[28:42] Um MC allow list. All right. So
[28:44] enforcement is based off of survey name
[28:46] ID and policy resolution.
[28:50] It sounds like this is still like it's
[28:52] not getting as detailed on the tool
[28:54] level. I don't see any is that is that
[28:56] what we're looking for? Are we looking
[28:57] for the ability to restrict which tool
[28:59] you can use from an MCP server? Um
[29:03] because if that's the case,
[29:05] I think you'd have to build the MP
[29:09] server specifically to only allow those
[29:11] tools.
[29:13] Um, but if that's the question that I
[29:15] can
[29:17] ask, uh, if the MTB server is external
[29:20] to the company, then you wouldn't want
[29:22] to do
[29:23] um, you wouldn't want to, you know, only
[29:25] allow from the registry, right? Like
[29:27] this is like for companies that really
[29:29] want to lock down MP servers or if they
[29:32] like, you know, you can treat this two
[29:33] ways like you make it an MCP registry
[29:35] just to make it easy for people to
[29:37] discover MSP servers from, you know,
[29:39] from your internal org. uh but you still
[29:43] let them install like add MCB servers
[29:45] from elsewhere. Uh or two, you want to
[29:47] make sure they can only add those MCP
[29:49] servers if you really want to lock stuff
[29:51] down.
[29:55] Um
[29:59] so yeah, I don't see how you would
[30:02] enforce on the tool level, right? So if
[30:05] you if I think if the enterprise is
[30:07] uncomfortable with some of the tools
[30:09] like some of the right tools then I
[30:12] don't see a way that they would enforce
[30:13] that on the tool level as a user you
[30:15] know you can turn tools on and off and
[30:17] you can uh you know make agent.mmd files
[30:20] that only are allowed to access certain
[30:22] tools and that's how you can be a little
[30:24] stricter. Where's my blog post? MCP tool
[30:28] filtering.
[30:29] Uh filter the tools from MCP servers.
[30:33] Right. Um, so you know, we can check
[30:36] tools on and off. We can make custom
[30:38] modes which are now known as custom
[30:40] agents. Um, and then of course when
[30:43] we're building programmatic agents, we
[30:45] can filter the tools there too.
[30:52] Uh, but I don't see a way of doing that
[30:53] at the enterprise level. I can ask if
[30:55] that's the question though.
[31:00] Okay. So Pab Pablo says policies per MCP
[31:03] server assigning specific tools per user
[31:04] role or groups team then citing the
[31:06] users role in teams. So you can do that
[31:08] if you are building the server yourself.
[31:11] That was the talk I gave at Cosmos comp.
[31:14] Um you know if you're building the
[31:16] server yourself then you know then you
[31:19] can definitely do that. Um this was
[31:22] example here where I had a tool that
[31:27] required a certain group, right? So here
[31:29] I decorate it and say like okay we
[31:31] require the admin group here and then
[31:35] require admin group is doing this check
[31:38] to see okay um you know let's get a
[31:41] token from the graph API for this user
[31:45] and then we're going to check to see if
[31:46] the user's in that admin group. If so,
[31:49] we will let them use the tool. If not,
[31:51] then we won't.
[31:53] Uh, so that's the way that I know how to
[31:56] do that. I don't know if there's another
[31:59] way to do that with like Azure API
[32:01] management, then
[32:03] there could be. Um, but uh there'd have
[32:06] to be something that you put in front of
[32:10] the server.
[32:12] So yeah, I can research that more. If
[32:16] you're looking for something for servers
[32:17] that you don't control, I think you're
[32:20] basically going to have to do some sort
[32:21] of there has to be some sort of proxy
[32:23] interception middleware that's checking
[32:24] that. And the question is where you know
[32:26] what what you know where that middleware
[32:29] lives, right? Like can you do that with
[32:31] API management? Can you do that with
[32:32] some sort of like I know we have this
[32:34] new you know agent governance for
[32:36] Microsoft and I really haven't messed
[32:38] with that at all. Like is that something
[32:39] we could do with a agent government,
[32:41] right?
[32:42] um agent government. So maybe I haven't
[32:45] dug into that.
[32:48] Good questions. All right, I'll have
[32:50] some more homework. Um okay, so what
[32:55] else? Um this just on the industry side
[32:59] actually related to MCP. I'll share this
[33:01] is that last week we did have um a bunch
[33:04] of internal co-pilot day workshops. So
[33:07] my workshop for that is here if anyone
[33:10] is you know looking for
[33:14] um some sort of similar
[33:17] um material. There's a slides and
[33:21] exercise for a two-hour tutorial about
[33:23] using GitHub copilot from VS Code, the
[33:26] CLI and the app to MCB servers doing
[33:29] both public servers and authenticated
[33:31] servers using the GitHub MCB server. Uh
[33:33] so that could be useful
[33:36] uh for you for internal use.
[33:40] So Yadell said, "Isn't that what you do
[33:43] with toolbox in VS Code?"
[33:47] Which of the toolboxes are we talking
[33:49] about in VS Code? Are we talking about
[33:51] tool kit? Oh, or Oh, there's also
[33:54] Foundry Toolbox. Are we talking about
[33:55] Foundry Toolbox?
[33:57] So Foundry Toolbox might be a way of
[33:59] doing this if you wanted to. Yeah,
[34:01] Foundry Toolbox. Yeah, I mean because
[34:04] that's basically like bundling up um you
[34:07] know bundling up some tools and
[34:10] packaging them up for others to use. Uh
[34:13] and that becomes that becomes the proxy,
[34:15] right? So the question is is it going to
[34:18] have the tools that we need or not? Uh
[34:22] so let's see if we can make a little
[34:26] toolbox here. Uh Foundry Experiments
[34:30] project. That's a good one. Okay. Tools.
[34:32] We go to tools.
[34:34] Connect your first tool. Toolboxes.
[34:38] Create a toolbox.
[34:42] Um, okay. Test for
[34:47] for office hours.
[34:49] Testing if we can pick certain tools.
[34:56] All right. And what can we can add tools
[34:58] and skills?
[35:01] So the tools we have here is you know
[35:04] like code interpreters good one web
[35:07] search is good one. Oh add one at a
[35:09] time. Okay.
[35:12] All right we'll just do that one. Let's
[35:15] add another tool catalog.
[35:18] All right. And then there's like MCP
[35:19] servers. So here's the question is if we
[35:21] do the MP server like work IQ. So let's
[35:25] see if we can filter
[35:29] OOTH identity pass through OOTH provider
[35:33] managed.
[35:34] Okay, connect.
[35:37] I don't Let's see if it even lets me
[35:39] connect in my account here. Okay, but
[35:43] here's the issue is that I don't see a
[35:45] way to Oh, here we go. Yes. All right.
[35:48] Let me take a little screenshot here.
[35:50] Um,
[35:52] so when it's an MTP server, you can
[35:55] allow certain tools,
[35:58] right? Um, now we have to figure out
[36:00] what those tools are. Uh, because I
[36:02] think they just changed their tool name,
[36:04] so I don't even remember. Okay, it would
[36:06] help if I knew what the tool names were.
[36:08] Um,
[36:11] select list of tools. I don't see. It
[36:13] used to be uh ask
[36:22] It doesn't say the tools there. All
[36:24] right. That's a bug report. Note for my
[36:26] transcript. That is a bug report. Okay.
[36:29] Um,
[36:32] so you could auto approve specific
[36:33] tools, right? All right. So, if you knew
[36:36] what the list of tools were here
[36:39] and then you could configure it. Let's
[36:41] try another MCP server. Maybe there's
[36:43] one where I actually know the um, so
[36:47] type. Let's try remote MCP.
[36:50] Um, work IQ. Work IQ. Oh, there's like
[36:53] specific work IQ.
[36:56] Really? I didn't know we had specific
[36:58] ones, too.
[37:01] Um,
[37:02] boundary IQ. That one I know it only has
[37:05] a single tool. So, bright data browser
[37:09] base. Okay. I'm I'm just curious to try
[37:12] this calendar one to see.
[37:16] Okay. Work IQ calendar configure.
[37:22] Oh man. All right, that links. Let's try
[37:24] this one. Work IQ calendar. Okay.
[37:28] Server ID. SP calendar tools. Explaining
[37:31] available tools. There we go. Okay. So,
[37:34] these are the things. So, we could say
[37:36] that all you're allowed to do is,
[37:41] you know, that tool right there, right?
[37:46] Okay. So now we have that one. Oh, so
[37:49] this was work IQ teams. Oh, so they've
[37:51] gotten really specific. Okay. Going to
[37:53] remove that one.
[37:56] All right. So now we have this one. And
[37:58] it should be configured to only allow
[38:00] certain tools. So then we'll say
[38:02] publish.
[38:08] And then um this is an MCP
[38:14] server here.
[38:16] Um and there's the Microsoft agent
[38:20] framework code
[38:23] that connects to it. And this is sending
[38:26] in
[38:27] O. Uh let's see if it also gives
[38:32] Can we just add this to our
[38:35] Let's just try adding it to our VS code.
[38:42] Toolbox MCP
[38:45] server. Nope. This.
[38:50] Okay.
[38:54] Fingers crossed that we get the
[38:56] authorization does not. Do you want to
[38:57] proceed?
[38:59] H.
[39:02] All right. So, it doesn't
[39:05] doesn't um support. Well, it makes sense
[39:08] that it it doesn't work because it uses
[39:10] Microsoft Entra which doesn't support
[39:13] all of MP off. Um, so it looks like this
[39:18] isn't currently I I I will check with
[39:21] the engineering team, the product team
[39:23] on this. Um, but it it doesn't look like
[39:26] this is usable from
[39:29] VS Code. Um, let me
[39:35] uh let me find my chat about this with
[39:39] the right people.
[39:47] Um,
[39:50] who was the person?
[39:56] Who was that? Okay.
[40:11] All right. So, I'll find out who to ask
[40:13] about that. Um, so it uh, you know,
[40:16] doesn't work currently as just a direct
[40:18] MCP server that we connect there. Of
[40:20] course, we can just manually we could
[40:22] just generate um a token and put it in,
[40:26] you know, in in here like uh probably
[40:29] headers authorization
[40:32] bear,
[40:34] right? And we'd have to go and generate
[40:37] a token for it that would work based off
[40:40] this because you see what this is doing.
[40:42] It's getting a token for ai.asure.com
[40:44] azure.com
[40:46] and then um you know sending
[40:50] it should be sending that
[40:53] as the oh the off yeah so sending that
[40:57] as the off
[40:59] um so you wouldn't get an you can't get
[41:02] a nice off flow from it you may be able
[41:05] to do it with thing I don't think
[41:07] there's even keys available for it
[41:09] though so then you'd have to like update
[41:11] the token once an hour which wouldn't be
[41:13] a good flow. It's fine here because you
[41:16] can, you know, you can programmatically
[41:19] refresh the token. Uh so you can do it,
[41:21] you know, do it in your code.
[41:24] Um but uh yeah, not not so useful
[41:28] otherwise. Let me just share the code
[41:30] that they output so you can see. Foundry
[41:34] toolbox math code.
[41:42] Here we go.
[42:03] All right.
[42:05] So, so there's a few things to dig into
[42:08] there, but at least the the Foundry
[42:10] tobox MCP server looks like a good
[42:12] objects uh good option for agents,
[42:18] but not necessarily for users. So like
[42:21] programmatic agents for Python agents,
[42:23] you know, it does have some of the stuff
[42:24] for looking for in terms of allow
[42:26] listing certain tools. Uh but it doesn't
[42:29] seem very compatible with uh userfacing
[42:32] off due to just the way Entra O works
[42:35] right now.
[42:40] All right. Um what else? See that we
[42:44] have someone typing. Uh let me see if
[42:46] there's something related here. Um
[42:51] just like following up from a discussion
[42:53] we had last week about
[42:57] uh like tool you know delayed tools like
[43:00] there was all these concern like okay if
[43:02] you use MCP servers then you know you're
[43:05] loading all these tools into the context
[43:07] and we talked about deferred tool
[43:09] loading and how VS code implements that
[43:12] um and I did some digging into it and
[43:13] realized that both OpenAI and Enthropic
[43:16] both both actually have tools tool
[43:18] search as like a first class
[43:20] functionality of the model. So it's
[43:22] actually trained into the model the idea
[43:24] of searching for a tool when it you know
[43:28] when it doesn't have the tools that it
[43:30] needs. Um and there's also
[43:34] um similar docs
[43:37] on
[43:39] um the messages API. Where is it?
[43:43] Enthropic messages API. So they so
[43:45] they're just trained really um really
[43:48] similar here. So, so not only do the
[43:51] harnesses like the coding agents like
[43:52] co-pilot have, you know, have it built
[43:55] in the idea of deferred tools and tool
[43:56] searches, but also the models itself
[44:00] have actually, you know, been trained,
[44:02] at least these two, you know, models
[44:04] that are very popular, the OpenAI models
[44:06] and anthropic models, they have actually
[44:08] as part of their training learned um,
[44:11] you know, how to do tool search and that
[44:13] is a a first class functionality uh like
[44:16] built-in tool uh part of their server.
[44:19] So that's that's part of why um you know
[44:22] and this is specifically well not just
[44:24] with MCP in mind but it is with MCP in
[44:26] mind right you can see a reference to
[44:27] MCP in the opening docs itself it says
[44:30] like okay if you're using MCP servers
[44:32] you're going to set defer loading uh so
[44:35] that is a nice practice and I saw it
[44:38] with co the copot when you add a um a
[44:43] new MCP server it will even specifically
[44:45] ask do you want to always include the
[44:47] tools or you want to defer loading and
[44:49] the default is to defer loading.
[44:53] Okay. I see another question from John.
[44:55] Uh one more question about production
[44:57] systems. Most of the use cases are rag
[44:59] based system which read the data from
[45:00] your resources or database. Um have I
[45:04] seen any use cases for agents in
[45:06] production systems that are allowed to
[45:07] do write actions to production system?
[45:10] Yeah, that's a great question. Um if any
[45:12] of you are using agents with right
[45:14] access in production, please share your
[45:18] scenarios. Um I think uh thinking
[45:23] let's see
[45:26] uh I think the use cases I've seen is
[45:28] like well code changes like if people
[45:30] are doing like really large programmatic
[45:32] code changes you could use an agent to
[45:34] do that um behind the scenes and send
[45:37] PRs right and um and with the thing um
[45:41] of course it's probably easier just to
[45:43] use a co-pilot coding agent but some
[45:45] people are going through additional
[45:47] effort of doing um modernization, right?
[45:50] So code is a good one because you can
[45:53] send a PR and review the PR, right? Um
[45:56] so code modernization, like really wide
[45:58] code modernization.
[46:00] Um using, you know, using agents to
[46:04] automatically send emails and calendar
[46:07] events for for events. That's fairly
[46:09] common, right? is like, you know, we're
[46:11] just going to um send off a bunch of a
[46:15] bunch of things to all the attendees of
[46:17] something and the agent can do that.
[46:19] I've seen a lot of um well, I've seen a
[46:21] lot of LLMs used in production for data
[46:25] like classification purposes. They don't
[46:28] necessarily use a full agent to do that.
[46:30] Um they're, you know, they at least
[46:32] using an LLM call. They might also be
[46:35] using an agent um in order to be able to
[46:38] get access to certain tools.
[46:40] uh but their end result is doing some
[46:42] sort of classification. Also seen agents
[46:45] use for like generating reports, right?
[46:47] Because that way you can have right
[46:48] access to the systems but you're writing
[46:50] something new. It's not as big of a deal
[46:52] if you're writing something new and if
[46:53] it just sits somewhere there ready for
[46:55] human review, right? So pull request,
[46:57] it's something new and it sits there
[46:59] waiting for human review. Now it's
[47:01] really annoying if it's not on your repo
[47:03] and it's somebody else automating PRs on
[47:05] your repo. But if it's for internal use
[47:07] and you know you want those PRs then you
[47:10] know having an agent in the background
[47:13] create a bunch of PRs that you want and
[47:14] you want to look at then that's a good
[47:16] use. Um same thing with generating you
[47:18] know reports like the agent in the
[47:20] background can be generating weekly
[47:22] reports puts it in a certain SharePoint
[47:24] folder and you know you're able to
[47:26] review it. um the the where you really
[47:30] want to have the most pause if your
[47:32] agents are updating existing documents
[47:35] that are human created, right? Like you
[47:37] really don't want to step on human toes.
[47:39] Uh or if the agents are um deleting, of
[47:44] course, that's a really big deal to be
[47:46] deleting anything. You always have to be
[47:47] really careful about that. Uh but I
[47:49] still think there's good uses for that.
[47:51] Like I mean I'm thinking back to like
[47:52] freaking 2006 when I first started
[47:55] automating things with Python and I was
[47:59] using Google spreadsheets with the
[48:00] Google spreadsheets API
[48:02] and there I you know we were using
[48:04] spreadsheets to organize our um our uh
[48:08] the video game projects we were working
[48:09] on in our games class. And I, you know,
[48:13] used the spreadsheet to go through and
[48:15] audit all the rows and see like, hey,
[48:17] is, you know, does this row have all the
[48:19] correct information. And that data was
[48:21] pretty messy data, right? So I had to do
[48:23] a lot of like kind of fuzzy checking.
[48:26] And I imagine if I wrote that automation
[48:28] in modern times, I would use an LLM in
[48:31] order to, you know, reason better about
[48:34] the the more fuzzy data that was in
[48:37] those rows. and then you know and then
[48:39] the LM ultimately could you know update
[48:41] a row in the spreadsheet right so I
[48:44] think you can use agents for updating um
[48:47] you know existing documents
[48:49] but you do want to you know be really uh
[48:53] careful about that and do a lot of tests
[48:56] and you know don't let your agents go
[48:57] wild uh Justin gave some examples there
[49:01] customer service right phone agents
[49:03] writing booking events oh yeah the
[49:05] travel booking example the classic one
[49:07] And people are doing that in reality. We
[49:09] had a talk at Build from a huge airport
[49:12] uh or airplane like an organization that
[49:15] works across a bunch of airplane
[49:16] agencies in Asia and they use it for
[49:19] customer service that helps people with
[49:21] bookings, right? So, it's helping with
[49:23] refunds, it's helping with rebooking,
[49:24] right? And um it's been really helpful
[49:27] for them.
[49:29] So, there you go.
[49:32] uh you just want to be really, you know,
[49:33] responsible about it and set up um
[49:36] evaluations and tests and all that good
[49:38] stuff.
[49:39] All right, we're in our last minutes.
[49:41] Let's see if there's any um
[49:44] uh big things I wanted to share. Let me
[49:46] just put these um
[49:51] additional
[49:53] uh some additional fun things in the
[49:54] chat. This was a paper that I read last
[49:56] night which was interesting with a
[49:58] prompt engineering
[50:00] um skills bench. I might have mentioned
[50:02] this last week. This is a cool benchmark
[50:05] for skills. Uh UV audit new tool from
[50:08] the UV team for vulnerability scanning
[50:11] for Python. That's nice. Uh on my side I
[50:14] shared the workshop. Um remember that
[50:17] we're doing the Microsoft IQ deep dive
[50:20] series at the end of the July. So sign
[50:21] up for that one if you haven't yet. Uh
[50:24] this in the weights website is super fun
[50:26] to see if LLMs have memorized you in
[50:29] their weights. That was a fun little
[50:31] experiment. And then yeah, I'm busy
[50:34] preparing for the AI engineer worlds
[50:37] fair. So I'm working on a bunch of labs
[50:39] and workshops. Um particularly one where
[50:41] you try out lots of models. So you can
[50:44] see that in progress here. Um but
[50:46] there'll be a lot of changes for the
[50:48] world fair. So next week I'll be at the
[50:49] engineer world's fair. Uh, I think that
[50:52] means I'll have to cancel or postpone
[50:56] the office hours. Uh, let me go ahead
[50:59] and check the schedule. Let me show you
[51:00] the schedule because it is a really cool
[51:01] schedule. Uh, so if you go, let's see,
[51:05] schedule. Okay, schedule. And then you
[51:08] go to the detailed schedule. Let's open
[51:10] the the full page. Um, so here, this is
[51:13] fun. The schedule has a JSON, an MCP
[51:16] server, an iical vector embeddings
[51:18] lm.ext, text and a skill, a schedule
[51:22] design skill. So, everything you weave
[51:24] for hacking on the schedule. Um, and
[51:26] then of course this the it has semantic
[51:28] search. This is the nerdiest schedule
[51:30] I've ever seen. All right. So, I'll be
[51:32] really busy on Monday. On Tuesday,
[51:37] I do have a talk at 11:40. And then
[51:40] Wednesday, I also have a talk at 11:40.
[51:42] Gh. Okay. And Thursday,
[51:46] I do not have anything. Um, so yeah. So
[51:51] maybe I'll be able to delay office hours
[51:53] till Thursday or I might just have to
[51:55] cancel for next week because I might be
[51:58] boothing on that day. Uh, so there we
[52:01] go. All right. So, thank you everyone
[52:04] for coming today and I may not see you
[52:07] next week.
[52:10] Uh, but I'll see you at least the week
[52:12] after that.
[52:14] All right. Bye everyone.

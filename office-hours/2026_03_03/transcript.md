[00:00] Let's check out what questions we have.
[00:04] Uh so Nambdi asks, "How do you stop an
[00:08] agent from outputting an old value in
[00:11] its context rather than rerunning a
[00:14] function tool or an API call?" Well, I
[00:17] guess the question there um
[00:21] why what are the situations in which the
[00:23] agent is outputting the old value in its
[00:26] context? Is this where you have like a
[00:27] really long conversation history and
[00:29] it's deciding to use its cached um you
[00:33] know it's cached results instead of
[00:35] recalling a function. Is that the
[00:37] situation you're running into? Um
[00:41] I'm curious like what sort of failure
[00:43] situations you're seeing there. So it's
[00:45] exchange rate agent and you're are you
[00:48] saying that you know previously in the
[00:49] history like the exchange rates change
[00:52] over time? I mean so one thing you could
[00:53] do this could be a good use of
[00:55] middleware right is that you could you
[00:57] could invalidate previous um tool call
[01:00] returns like if if you know that um you
[01:04] know tool calls are return tools are
[01:07] returning values that get out of date
[01:09] then you could build some uh middleware
[01:13] that says okay like um you know we're
[01:16] going to look back at the tool call
[01:17] history and for this particular kind of
[01:19] tool call if the time stamp temp is, you
[01:23] know, um, you know, uh, you know, 10
[01:27] minutes, you know, too old, right? It's
[01:29] 10 minutes old or it's an hour old, 3
[01:30] days old, whatever it is, right? Then
[01:32] you could just remove that tool call
[01:35] from from the history, right? Um, and
[01:37] there's certainly like it's very common
[01:39] to mess with tool calls in um in in
[01:43] middleware. Uh, because a lot of people
[01:45] when they summarize, they might decide
[01:47] to like leave out tool calls, right? Uh,
[01:49] so remember we talked about that last
[01:52] week. We talked about middleware and all
[01:53] the different kinds of middleware you
[01:55] can do. So, um, yeah, I I I would do
[01:58] that. I mean, you can also, of course,
[02:00] put in the prompt like, oh, like inspect
[02:02] the value and see how old is, but I
[02:04] think that sounds like a really nice
[02:05] opportunity for using um using tool
[02:09] call. So, I think you would need to the
[02:10] problem is you can't do it on as
[02:13] function middleware. Um, you'd have to
[02:15] do it because the issue is it's not even
[02:17] calling the function at all.
[02:19] So you would want to have it be either
[02:22] agent level or chat level where you um
[02:26] you know look at you could basically
[02:28] base it off the summarization middleware
[02:30] that we showed. Uh let me bring up right
[02:33] we did summarization.
[02:38] So that's what I would try doing is
[02:41] seeing if you can kick out the the tool
[02:44] the old tool return values.
[02:50] Yeah, the agent didn't respect the
[02:51] prompt. I'm not surprised agents don't
[02:53] always respect prompts. Uh so yeah, I
[02:55] would I would think you'd want to um do
[02:59] some middleware that removes those old
[03:01] tool return values.
[03:05] Okay. Um, where do I post these Discord
[03:09] sessions? Everything gets posted to um
[03:13] to this, let me give the nice version of
[03:15] the links. This resources thread here.
[03:18] Uh, you'll find everything posted there.
[03:21] Um, and for the office hours in
[03:23] particular, I even post every question
[03:26] as a comment. Uh, so that's why we do
[03:29] the recordings is because then the I
[03:32] have an agent go through and make these
[03:35] into into nice writeups.
[03:39] All right.
[03:40] Now, we have a question from the only
[03:43] word. How do you prevent malicious
[03:45] prompts from proliferating your
[03:48] workflows?
[03:50] Uh well, it just depends what kind of
[03:52] malicious prompt we're talking about
[03:53] here. But um you know uh generally uh
[03:58] when it comes to safety, let me just get
[04:00] the safety deck. Safety. We did talk a
[04:04] bit about safety on Thursday, but we
[04:07] really didn't get to dive deep into it.
[04:12] Um let me come on PowerPoint. You can do
[04:15] this. Uh
[04:17] safety. Just trying to find Okay, that
[04:21] one should work. Yeah,
[04:24] give me a safety deck.
[04:28] This one.
[04:30] With PowerPoint, there's always like six
[04:32] different versions of the document. You
[04:34] don't know which one's which one's going
[04:36] to work. Okay.
[04:38] So, with safety, we like to think about
[04:41] the risk mitigation layers, right? So
[04:44] the system message and grounding can
[04:45] help but it's you know it also it has it
[04:49] a lot of limitations right. So you want
[04:53] um ideally you want a separate safety
[04:55] system that's uh checking for something
[04:57] like malicious prompts and also you want
[04:59] the model itself to be fairly safe,
[05:01] right? So I talked about this um you
[05:05] know that uh LLMs like they have this
[05:07] training process and so many of them go
[05:09] through this training called RHF that
[05:12] makes them safer. So you do want to use
[05:14] like a frontier level model that has
[05:17] been through really vigorous RHF and
[05:19] specifically for safety. So whenever
[05:21] you're like looking at a new model, you
[05:23] can look at its model card and you can
[05:25] see what safety uh red teaming they did
[05:28] on the model itself.
[05:31] Uh so I have some like examples of of
[05:34] model cards here. But uh general best
[05:37] practice is that when a new model comes
[05:39] out, the provider will come out with a
[05:40] model card. Now there are some providers
[05:43] like Grock that doesn't follow those
[05:47] best practices necessarily. So I have
[05:48] not seen their model cards. So I don't
[05:50] use those models personally. So I only
[05:52] use models that have model cards that
[05:55] show that they've explicitly been
[05:57] through um a safety RLHF. Right? So
[06:01] that's on the model layer. And then um
[06:04] on Azure we have this content safety
[06:06] system. And in the content safety
[06:07] system, let me like make this like way
[06:09] bigger. You can see that you can
[06:11] configure um the sorts of stuff it
[06:13] blocks and it also has configuration for
[06:15] jailbreak uh two different kinds of
[06:17] jailbreak also use of protected
[06:19] materials right so if you're using
[06:21] models hosted on uh foundry as it's now
[06:26] called uh then you will get the filters
[06:29] built in and it'll default to medium I
[06:32] actually got blocked for several of my
[06:34] messages yesterday um so you know medium
[06:36] will block you know a good number of
[06:38] things Um but you can make it you can
[06:41] make that threshold higher, you can make
[06:42] it lower, you can turn on jailbreak
[06:44] detection. So I would certainly
[06:46] recommend using um Azure deployed models
[06:49] because we do care a lot about safety
[06:51] because we are making you know
[06:52] production
[06:54] level applications. Um
[06:58] so so yeah that's what I would recommend
[07:00] is you know using um safety layers like
[07:03] you can you know put stuff in your
[07:05] prompt but the prompt can only go so
[07:08] far. So yeah, you can put stuff in your
[07:09] prompt, but you really, you know, you
[07:12] want it to be part of the model and you
[07:13] want it to be um ideally like a separate
[07:16] system.
[07:17] Uh so that those are, you know, some of
[07:21] some suggestions there.
[07:26] Um okay so let's see what Z doc says
[07:31] what would be your recommended pro
[07:32] approach of integrating the GitHub copi
[07:36] and SDK
[07:38] in a dev ops workflow right and so Gwen
[07:42] followed up like what kind of DevOps
[07:43] workflow what are you trying to build
[07:45] and accomplish um like are you trying to
[07:47] do something in CI or trying to do
[07:49] something locally um
[07:53] Uh I I haven't built many automations
[07:57] using the SDK yet. Like we did have an
[07:59] experiment. Um I did just do some
[08:01] experiments with it, but I haven't
[08:04] there's I don't have I haven't done any
[08:06] automation that I'm like using a lot of
[08:08] but let me just get my examples because
[08:10] we I did have a live stream where I just
[08:13] played with the SDK the whole time. Uh D
[08:17] and here is the experiments branch that
[08:23] I was using.
[08:25] Um
[08:27] so you know you can visualize your PRs.
[08:30] Um triagger this is the the main thing I
[08:32] care about is triaging issues. So um I
[08:36] was using it to to triage issue. So
[08:39] generally what I would say is that if
[08:41] you if you know if there's something
[08:42] that you know you're currently able to
[08:44] use any sort of coding agent for like
[08:47] GitHub copilot or cloud code or whatever
[08:50] and it's something you do a lot then you
[08:53] may be able to build automation for it
[08:55] right like uh like a script that'll just
[08:58] do it for you that's easier to run and
[09:00] you can even like you know be running
[09:02] these things in um you know in GitHub
[09:05] actions in CI. We recently came up with
[09:07] this GitHub agentic workflows and this
[09:10] is kind of a different thing um not
[09:13] using the copilot SK. Is this even is
[09:16] this correct? Let's see. February 13th.
[09:18] This should be correct. Okay.
[09:21] Um so these are workflows that use use
[09:25] LLMs. Um they don't I don't think they
[09:28] actually use the C-pilot CLI or SDK. Uh
[09:31] oh, they can. They can actually. Yeah.
[09:32] So they can use C-pilot CLI. Uh but the
[09:35] point about these workflows is that you
[09:38] write them just in plain text basically
[09:40] with some security YAML and then it'll
[09:43] generate the workflow for you. Um
[09:45] because basically like it's kind of hard
[09:47] to write workflows. I don't know if
[09:48] you've ever written a GitHub actions
[09:50] workflow. It's actually kind of hard to
[09:52] do it. So the idea here is that they're
[09:55] trying to make it really easy for you to
[09:57] write workflows that still have security
[10:00] boundaries but that can do like useful
[10:03] things, right? daily repo report. Um,
[10:06] you know, they have tons and tons of
[10:08] examples here of different workflows. So
[10:11] they have chat ops, data ops, issue ops,
[10:13] project ops, multi-reo ops, right? Um,
[10:17] so that might be that might be what
[10:19] you're looking for. So these will you
[10:21] know the idea here is that you're
[10:22] writing your your workflows in plain
[10:26] text and it is generating the workflow
[10:30] file for you. Right? So this is all you
[10:32] write is you have some front matter that
[10:34] says okay these are your permissions
[10:35] because this is the security part is
[10:37] what's really important right you say
[10:38] okay this is when you're going to run
[10:40] these are your permissions this is what
[10:42] you're allowed to output and these are
[10:44] the tools you're allowed to use like um
[10:46] you know this is like the GitHub MCP
[10:48] server and then the rest of your
[10:50] workflow is just markdown and so
[10:52] basically you compile this into a
[10:54] workflow file and it adheres to these
[10:57] security constraints but then you know
[11:00] enables all this to happen. So, this is
[11:03] a neat way of getting started with using
[11:05] LLMs in your GitHub actions uh without
[11:09] having to learn like how to build
[11:11] workflows because that's that's like too
[11:13] hard.
[11:15] So, the example was analyzing CVE's
[11:17] independencies and making corrective
[11:20] actions on the the PR. Um yeah, so there
[11:26] you'd have to. So that that would be
[11:27] something I would certainly um try using
[11:30] this was because you should be able to
[11:31] do that on like pull request, right? So
[11:33] on pull request you could read the
[11:35] contents of the PR and you could tell it
[11:37] to to to analyze those. Um and uh you
[11:41] know it and tell it like you know what
[11:43] tools it could use if you need to
[11:45] configure it. Um you can probably
[11:46] configure it with custom MCP servers as
[11:49] well if you want to do that. So uh I
[11:53] would try that. Um since you do want it
[11:55] to work uh as like you know in reaction
[12:00] to a PR um then I think this is going to
[12:02] be your easiest path path for doing
[12:05] that.
[12:06] Uh you can probably more if you if
[12:09] you're comfortable writing workflows and
[12:10] you want to do that uh you should
[12:13] probably be able to use the copi
[12:17] yourself from a workflow. Um,
[12:21] and but I don't have an example of that
[12:23] offh hand.
[12:26] Have I tried? Okay.
[12:29] So, have I tried building math
[12:31] applications using cloud code or codeex?
[12:36] Uh, I have not. I've only used codeex
[12:39] once just to try it out when it came out
[12:41] when the desktop app came out for Mac a
[12:43] few weeks ago and it was good. It was
[12:44] quite good and actually I don't even
[12:47] know if I've ever used cloud code. I've
[12:48] seen it quite a bit. I see it demoed a
[12:50] lot. So, um, so I have not I built, you
[12:54] know, I I built all these examples using
[12:56] GitHub Copilot. Uh, so if you, you know,
[12:59] it might be useful to see what my
[13:00] agents.mmd looks like for for this repo.
[13:04] Um, right. So, uh, I tell it, you know,
[13:08] we're using the Microsoft agent
[13:10] framework. The repo is here. Um, you
[13:13] know, we're using Python. Um, I told it
[13:16] that it's also known as math, which is
[13:18] helpful because then I can just write
[13:20] math in the chat. Um, you know, I told
[13:22] it that it's changing a lot. I pointed
[13:24] the change log. I pointed the framework.
[13:27] I told it what MCB server can use. So,
[13:30] this, you know, I would say this is just
[13:32] generally useful information for any
[13:34] coding agent that you're using. So, you
[13:36] may want to put that in your agents.mmd.
[13:38] And it's been pretty good. Um it will
[13:41] you know because we are using a very
[13:43] very latest version of here like you can
[13:45] see we're pinned to a hash uh oftent
[13:48] times it will actually just search
[13:50] through the entire agent framework
[13:51] codebase since it knows to do that and
[13:54] and figure things out based off the
[13:55] codebase itself. Uh I think the rest
[13:58] yeah are not as useful but this top part
[14:00] here should be generally useful for any
[14:03] coding agents.
[14:06] All right question from Bane. How likely
[14:09] is there to be a scenario where the
[14:10] conditional workflow keeps requesting a
[14:13] revision causing infin loop and is there
[14:15] a way and need to prevent that? Yeah,
[14:16] great question and this actually relates
[14:18] to one I saw in the chat. Um, yeah, that
[14:21] is very possible. I I don't remember
[14:23] which one it was that was having an
[14:24] issue, but there was one where I was
[14:26] having that issue and I had to make the
[14:29] reviewer less critical and it might have
[14:31] been this one. There was certainly one.
[14:33] Um, but I think there was one where I
[14:34] added, let me see, max,
[14:37] is it max turn? No, max iteration. Okay.
[14:42] Yeah. All right. So, here you can see
[14:44] that um, in this one.
[14:48] Oh, because I think Gwen, wasn't this
[14:50] one I had to change because you said
[14:52] this was too low?
[14:54] Um, oh, yeah, because this one. This
[14:56] one. Yeah. Oh, I didn't change it in
[14:58] Spanish. Sorry, Gwen. Okay. So, yeah,
[15:01] Gwen was saying when Gwen did this in
[15:04] maybe code spaces that it required way
[15:06] too many. It required more than eight
[15:09] iterations. Uh, so I bumped it to 20,
[15:12] right? Um, so,
[15:15] so yeah. So, yes, you can have
[15:17] situations where it will loop a lot and
[15:20] you have to decide like, you know,
[15:22] what's what's going to happen if it goes
[15:25] over those max iterations. Uh let me
[15:28] actually see what does happen
[15:31] for workflow convergence. Right? Default
[15:33] is 100. All right. What if we just
[15:36] change that to two?
[15:39] Um because the question is when is it
[15:40] going to when is it going to stop at
[15:43] what note is it going to stop and how
[15:44] are you going to handle that? Right? So
[15:46] probably what you want to do in reality
[15:48] there's probably some sort of good like
[15:51] error handling that we could do. Let me
[15:54] see. Let's just ask um what's best
[15:59] practice for handling a workflow
[16:03] getting in a
[16:06] a loop.
[16:11] What will it do? See, I just asked and
[16:16] uh you know,
[16:19] let it do some research here. Dig into
[16:21] the code. Uh so you can see quite a few
[16:23] of ours do have this max iteration set
[16:26] on it and you can like this is also
[16:28] something this was on the workflow level
[16:30] but I believe we can do it on
[16:34] we've done it on the edge level as well
[16:36] let's see source target condition no
[16:40] um oh I know we've done this also in the
[16:44] built-in orchestrations they have their
[16:45] own ways of doing it okay all right so
[16:51] Uh, so here I set the max iterations
[16:54] really low. Are we going to get an
[16:56] error? I feel like it would probably be
[16:58] an error. Um, but it's we're looking at
[17:01] the code now, right? Uh, so we can see
[17:04] we're looking at the code. What happens
[17:07] when we reach max iterations? Like do we
[17:09] get a particular error when that
[17:11] happens?
[17:14] Yeah. Well, I set this down. I'm running
[17:16] this right now with two.
[17:19] I'm trying to run into that that
[17:21] situation.
[17:23] Okay, great. Good. Got it. We get a
[17:26] particular exception. Runner did not
[17:28] converge. So, probably, you know, best
[17:31] practice for production would be um you
[17:34] know to you could wrap this whole thing
[17:36] in a um a try except um
[17:42] workflow convergence exception because
[17:45] you decide like what this is like
[17:46] dividing by zero, right? what should you
[17:48] do in that case right like what should
[17:50] happens right do you just mark this as
[17:53] you know needs a human like what do you
[17:55] do right you just put it in your log so
[17:57] you figure out why um you know what what
[18:00] stage was too critical that it didn't
[18:01] get passed um so that would that would
[18:04] be like the the bare bones thing I would
[18:06] do would be to to catch that exception
[18:09] because you don't want exceptions
[18:11] happening in production
[18:13] um but there might be there There might
[18:17] be other clever things to do as well.
[18:20] We'll see if uh if co-pilot learns
[18:22] anything from its experimentations here.
[18:26] Um
[18:29] and Nambdi says, "Oh, the LM's getting
[18:31] into an attractor state. Maybe you need
[18:32] to summarize and restart." Well, yeah,
[18:34] you could also um on the agent level
[18:37] remember we can add like you know if the
[18:39] agent is getting is having too many
[18:41] iterations like you could add in some
[18:43] middleware there to say um you know the
[18:47] the agent is going too long it's doing
[18:49] too many tool calls right so if it's on
[18:51] the agent level then I would address
[18:54] that with middleware um on the workflow
[18:57] level
[18:59] uh we don't really have a notion of
[19:01] middleware ware
[19:04] for workflows
[19:06] um because you would just add in
[19:08] executives at points. What about output
[19:11] exeutors? What is that? Uh no. Yes. So I
[19:15] don't really have a notion of middleware
[19:16] for workflows. Um
[19:19] but you could you could you know you can
[19:21] do exception handling and you could add
[19:23] additional executives in as as helpful.
[19:27] Um oh that's a good question. Does the
[19:28] executive contest include iteration
[19:30] count? Uh, it does. It does. I know that
[19:33] because
[19:35] of examples for Thursday that I was
[19:38] working on. Um, but um, yeah, it does.
[19:40] Let me see if I can bring up the
[19:42] workflow context. Uh, let's go to that
[19:45] definition. Um,
[19:51] actually, I can just show you. I have
[19:52] this
[19:55] I happen to have serialized um,
[19:58] workflows here. Okay. workflow. Oh, we
[20:01] did get this open. Okay, let me also
[20:02] just run this.
[20:05] Um, okay. So, here and let me just
[20:09] format this. Okay.
[20:12] Um, so yeah, you can see like this is um
[20:17] this is like the uh this is a serialized
[20:20] state of a workflow and you can see that
[20:22] it has an iteration count in here. Um,
[20:26] let me see if that's on workflow
[20:27] context. Is that where it is?
[20:33] Send message yield output.
[20:38] Do we have iteration
[20:42] iteration? No. Where is it actually?
[20:50] Agent executive response. What does this
[20:52] have in it? Executive ID.
[20:55] Okay.
[20:58] All right. So it says yeah track
[21:01] revision. Oh this is what interesting.
[21:03] Okay so h
[21:06] it's saying that we should use workflow
[21:08] state to break loops intentionally that
[21:10] you that you could certainly do if we
[21:13] can't actually I thought we would be
[21:14] able to get access to
[21:17] the iteration count in the in the
[21:20] context but now I'm not seeing it there.
[21:23] Um
[21:25] so if we can't access it just naturally
[21:28] then yeah we could we can we can add our
[21:30] own um state to break loops right with
[21:34] set state and get state
[21:36] um and then and then yeah catching the
[21:38] exception right
[21:41] design conditional edges to guarantee
[21:43] termination right having a default
[21:45] fallback that's what we talked about
[21:47] that in there and then you can also
[21:49] instruct the agent the system prompt
[21:52] uh so there's
[21:54] There's some there's some good ideas
[21:55] there. I think there's a good question
[21:57] as to whether we can directly access
[21:59] that iteration count without having to
[22:03] save it ourselves. But uh but if we
[22:05] can't then we could we could save it
[22:07] ourselves.
[22:11] Um Robba yeah it is we are recording
[22:14] this session so I will post it in the
[22:16] resources link afterwards.
[22:21] Uh yeah, Tea Leaf says, "When you run
[22:23] switch case UI, you get an unhandled
[22:25] exception. Is it something in your
[22:26] environment?" Uh I got that as well.
[22:29] That's why I didn't use DevUI for that
[22:31] one. Um I'll have to uh I'll let me
[22:35] write a note. Um it might be a bug with
[22:36] agent framework. Uh or
[22:39] it might be the way in which we're
[22:41] giving the the input. I didn't have
[22:43] enough time to debug it this morning
[22:44] when I ran into it, but I I ran into the
[22:47] same thing. So it's not it's not it's
[22:49] not just your environment. Um I ran into
[22:51] that as well. Uh let's see because it
[22:55] gets a what is the start input for
[22:57] classifier?
[22:59] What do we run this with? We run this
[23:02] with just a straight message.
[23:04] So I feel like here I'll show you we can
[23:07] just let's just do this live and get
[23:10] this filed. So I'll show you how I like
[23:12] file issues. Um, so we're going to run
[23:15] this with devi
[23:18] because it should be able to handle
[23:21] the free text input here because we're
[23:23] doing the same input and we're Yeah. All
[23:27] right. So, let's let's replicate that
[23:31] bug and report it like good responsible
[23:35] library users.
[23:42] starting it up. Yeah, I had a few weird
[23:45] things with um WI today with especially
[23:50] with my conditional workflows where it
[23:53] like wasn't continuing to the node. So,
[23:57] I don't know if it was like late like
[23:58] weird latency on my end or something. Um
[24:03] so, that's why I didn't use Debi for
[24:05] everything. All right, so we're going to
[24:06] try this out. But we're going to set the
[24:07] message and then um
[24:13] I think we'll get the error pretty
[24:14] quickly here.
[24:17] I think it's on is it non time has no
[24:22] category question. Yeah. And it says
[24:24] failed category question.
[24:29] Let me take a little screenshot here.
[24:35] Okay.
[24:40] All right. So then we got that error
[24:44] event type. Yeah. So it's coming through
[24:46] as a dictionary
[24:49] instead of coming through as the value
[24:51] itself.
[24:54] Um so let's see getting this bug
[25:00] only in WI but not when running via CLI.
[25:05] All right. So, we'll let we'll let
[25:07] co-pilot do a little investigation there
[25:10] and see um if it can
[25:14] uh figure that out.
[25:18] All right.
[25:19] Yeah. So, T Leaf says in a couple of the
[25:21] other switching ones, the workflow
[25:22] didn't complete under DevUI, but worked
[25:24] fine with command line. Okay. So, you
[25:26] saw the same thing I did. Um and it's
[25:28] really weird because I definitely I I
[25:31] don't know. It might be a a recent
[25:34] regression. So I'll also um report that
[25:40] uh they definitely worked when I first
[25:41] made them but you know we are
[25:44] continually uh pinning to the latest
[25:46] version of agent framework and you know
[25:48] there could have been some slight slight
[25:50] changes there
[25:53] and it might be something so it may be
[25:54] that there's some weirdness with
[25:55] structured outputs in particular that
[25:57] it's maybe handling them differently
[25:59] than before because all these examples
[26:02] are using structured outputs now. And I
[26:05] like to push structured outputs to their
[26:07] limit because I love structured outputs
[26:09] so much.
[26:20] And what is it not even? It didn't
[26:22] reply. All right. We're going to pick a
[26:24] different model.
[26:26] Okay. All right. And we'll just retry
[26:29] that. Okay.
[26:31] It's being everything's being a little
[26:33] slow. All right. So, while that's
[26:34] working, um what other
[26:37] questions
[26:40] um that people have?
[26:46] I'll just uh open the slides just as a
[26:52] reminder.
[26:54] Oh, I've got so many of these ones open.
[26:56] Okay. Close. Close.
[27:00] Okay.
[27:01] Oh, we open this one too. Okay.
[27:04] Am I taking part as in a Agents League
[27:07] judging? Uh, no, I'm not. My colleagues
[27:11] are doing Agents League. Um,
[27:14] this series is keeping me pretty busy.
[27:18] Uh, I do have a Friday talk as part of
[27:20] the Rag JavaScript part of the
[27:23] JavaScript series. I'll be talking about
[27:24] Rag. Um, so that I do have I am doing
[27:28] that on Friday.
[27:30] Um but uh yeah, this series is keeping
[27:34] me pretty busy this week.
[27:37] Okay, so this is so here's reminder
[27:42] of what we talked about the switch case,
[27:45] the state management, all that stuff.
[27:48] And then we showed that example at the
[27:49] end.
[27:52] I think just all my models are being
[27:54] slow this morning.
[28:02] What else can I show? Um, also a
[28:06] reminder like all of this is
[28:09] documented although sometimes the
[28:12] documentation could be slightly out of
[28:13] date with like very latest but I've been
[28:15] trying to file I file bugs whenever
[28:17] running stuff. So for workflows there's
[28:19] this whole section here.
[28:21] Uh so we have the workflows
[28:24] and you know basically by the end of
[28:26] this week we will have gone through
[28:29] almost everything in here. Um I tried to
[28:33] be pretty thorough. There's a couple
[28:34] orchestrations we're just like we're
[28:37] skipping one of the orchestrations but
[28:40] uh we're you know trying to be pretty
[28:42] thorough here. So it's like you don't
[28:45] even have to read the documentation. You
[28:47] can just come to the series. Oh there's
[28:49] a GitHub outage happening. Oh, good. All
[28:52] right. Well, I guess we won't use
[28:54] GitHub.
[28:58] Oh, that's why. Okay. All right. Uh, and
[29:01] what's the link to the JavaScript
[29:02] series? That's a good question. What is
[29:04] the link to the JavaScript series? Um,
[29:07] we'll just search Microsoft Reactor.
[29:11] And I'm sure we can find it on Reactor.
[29:16] Let's look for rag JavaScript.
[29:22] Oh, okay. Rag.
[29:24] I think it's called Buildathon. There we
[29:26] go. The JavaScript AI buildathon. Okay.
[29:30] And here we go.
[29:33] So, I need to remind myself how
[29:36] JavaScript works before then.
[29:40] I actually was a mostly a JavaScript
[29:42] developer for many years. I always used
[29:43] both JavaScript and Python. Um, but I
[29:47] only use JavaScript on the server uh for
[29:50] one company. Usually I use Python on the
[29:52] server.
[29:55] Uh, if you cannot hear, typically that's
[29:57] a Discord issue
[29:59] and um, you know, people usually
[30:02] recommend restarting Discord in that
[30:04] case.
[30:07] All right. Do we have any other
[30:10] questions?
[30:13] Any desires for what we do for our next
[30:15] series? Um, is there a certification
[30:18] about agents from Microsoft?
[30:21] That's a good question. Let's look at
[30:24] learn Microsoft certifications. I know
[30:27] there's often recommendations for our
[30:31] like for different AI ones we have.
[30:33] Isn't it like 900 or something that
[30:35] people there's one that people always
[30:38] are recommending? Um,
[30:42] oh, there's one for co-pilot now.
[30:45] Uh, let me find the AI is like AI
[30:48] engineer or something as your AI
[30:50] engineer associate. I feel like this one
[30:52] gets recommended a lot.

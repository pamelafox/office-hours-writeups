[00:00] Welcome everyone
[00:03] to our Python plus AI weekly office
[00:05] hours. So how we run this is that you
[00:10] know I've got some links here we can
[00:13] talk about for things that have been
[00:15] going on in the last week. Um but uh we
[00:18] can also talk about whatever is on your
[00:20] mind. um answer questions, try sometimes
[00:25] we do live coding um whatever is
[00:28] helpful.
[00:30] Um so what were some
[00:35] things in the last week that were
[00:37] interesting? Um
[00:41] uh on the Microsoft side um we've talked
[00:43] about Monty a few times here and the
[00:48] the um Monty is the the Python code
[00:52] sandbox that did get merged into agent
[00:55] framework as a possible way of
[01:00] implementing code act and codeact is
[01:02] basically the same thing as code mode
[01:03] which is supposed to be a more efficient
[01:05] way of doing tool calling. So, if you
[01:08] are using agent framework and you're
[01:10] curious to use Monty, that's an op
[01:12] option for you. Let's check to see. I
[01:14] actually don't know if they did the
[01:15] latest release yet because they did
[01:17] merge it into Maine, but I don't know if
[01:19] they did the actual release. So, let's
[01:21] see when our latest thing was. So, May
[01:24] 21st 1.6.0
[01:27] and it was merged
[01:31] um bump Microsoft agents
[01:36] last week. So, little hard to tell when
[01:39] like it it got part of it. 5 days ago. I
[01:42] think it might be in there. There we go.
[01:44] It is here. So, here we go. If you look
[01:46] at the Python 1.6.0 release
[01:59] then you can see it has it. Um,
[02:03] can you all hear me by the way? I don't
[02:05] know. No one ever actually said if you
[02:06] could if they could hear me. We always
[02:09] have to check in Discord if the audio
[02:10] works.
[02:15] Uh, okay.
[02:17] Okay, great. Okay. All right. So, yeah.
[02:20] So, there's some good stuff from the
[02:22] latest math math release there. Um,
[02:29] uh, let's see. Uh, I was excited that
[02:32] the GitHub MCP server added the um
[02:37] ability Oh, I have to do a fancy off for
[02:41] that. Okay, they added the ability to
[02:42] reply to inline PR comments. And that's
[02:45] something I needed for my um my skill to
[02:48] review PR comments. This is what I use
[02:50] when I want to collaboratively triage PR
[02:53] comments. And it uses the GitHub MCP
[02:56] server. And so now the g the MCP server
[02:59] has an like an actual dedicated tool
[03:02] called add reply to pull request comment
[03:05] that can add replies to inlines. So this
[03:07] is a it's a small thing but this is this
[03:09] is the skill that I use the most often
[03:12] every single day. And so u I was really
[03:16] excited when they when they added that.
[03:19] Um
[03:21] what else? Okay. So, I don't think they
[03:24] Oh, yeah. We did just get an email today
[03:26] that if you are using the assistance
[03:29] API, it is officially being retired.
[03:32] Uh, it'll be retired Oh, pretty soon
[03:35] actually. August 26, 2026. Wow. Um, so
[03:39] the recommendation here is that if you
[03:41] were using assistance API, you should
[03:42] now move to the Foundry agent server
[03:46] service. And they have a um migration
[03:49] guide here specifically about that.
[03:55] Uh I never I never used the assistance
[03:58] API myself, but I know a lot of people
[04:01] did because it they like like the manage
[04:03] threads and stuff. So now you get the
[04:05] same thing from the agent service.
[04:09] Yeah. So Adam says, "How's the GitHub
[04:11] copilot app so far?" Yeah. So for me
[04:14] like um
[04:17] now that there's the GitHub desktop app,
[04:19] there's no reason for me to use the CLI.
[04:21] Like I was trying to use the CLI earlier
[04:23] today. You can see I was actually using
[04:24] it and then I was like wait a second we
[04:27] have a desktop app now. Why am I like
[04:29] struggling to you know edit like because
[04:33] I always want to give feed I'm still at
[04:34] the point I give a lot of feedback
[04:36] right? I'm I'm very critical person. So,
[04:38] um, for me, like I want it to be really
[04:40] easy to see what's going on, to give
[04:42] feedback, to to view code differences.
[04:44] So, um, definitely for these sort of
[04:48] things, uh, uh, I I I don't see any
[04:51] reason why I would personally ever use
[04:53] the co-pilot CLI given that the GitHub
[04:55] Copilot desktop app is a wrapper for the
[04:58] CLI. So, all of my same MCP servers and
[05:02] skilled are all supported. Plus, we've
[05:04] got extra features like workflows and
[05:07] inbox, all that stuff. So, I don't I
[05:09] don't see any reason why I personally
[05:12] would use the copilot CLI because I'm
[05:13] not actually that big of a fan of a CLI.
[05:16] Um, you know, so and this is this is
[05:18] really nice for me just for doing these
[05:20] like, you know, little things like um
[05:23] this is where I was generating the
[05:24] PowerPoint deck that, you know, that I'm
[05:27] using right now. So, I did that just
[05:29] before. Um, and it's really, you know,
[05:31] it's just really makes it super easy to
[05:34] check all the tools it's using. So, it
[05:35] was doing work IQ and Twitter and Gmail
[05:38] and GitHub and web search and blah blah
[05:40] blah blah. And really easy to expand all
[05:42] the tools, really easy to see the diffs,
[05:44] right? Like I just like how easy it is
[05:46] to see all the all the changes.
[05:50] Uh, so yeah, for me, GitHub desktop app
[05:53] definitely. Um, so Adam says, you know,
[05:57] uh, you wonder whether the industry has
[05:58] mostly settled on the desktop UI. They
[06:01] all seem to be quite similar. Uh, yeah.
[06:03] So I I was reading about anti-gravity,
[06:06] uh, the new anti-gravity changes that
[06:09] they announced last week from Google.
[06:11] And it sounds like it's I think it's
[06:12] funny. Basically, everybody is coming up
[06:14] with the same things. Like we Let's do a
[06:17] little like diagram of this. Um
[06:21] so we have for you know for like GitHub
[06:25] we have our offerings are like a VS code
[06:28] plus GitHub copilot chat. So that's if
[06:32] you're like, you know, really very very
[06:35] codeheavy, right? Like very very code
[06:37] first, I would say. And then you have
[06:40] the VS Code agents um agents tab, I
[06:44] think they call it like basically I
[06:46] actually haven't even tried it yet. Um
[06:48] but if you do new window, you'll see try
[06:52] out the new agents window. So that's
[06:53] what they're calling it. So the agents
[06:55] window is like an agent centric u
[06:58] version of copilot chat right uh so
[07:02] that's agents window
[07:04] and then we have the github co-pilot
[07:07] desktop app
[07:10] and then we have the github copilot cli
[07:13] and then of course there's also the
[07:15] copilot coding agent. So there's all
[07:17] these different manifestations of aentic
[07:21] coding and these ones to me are like
[07:23] actually like a spectrum where it's like
[07:25] how much how much um control you you
[07:30] know you want uh over
[07:33] over the code versus like how much you
[07:35] trust the agent like and so for me it's
[07:37] like how trivial of a task I'm doing
[07:39] because I definitely will use the some
[07:41] of these options right so like you know
[07:44] this is like you know hi high code
[07:47] control, right? And then and then we go
[07:51] like here it's going like high agent
[07:55] agency like agent low I guess low code
[07:59] control, right? Um which means lots of
[08:03] agency for the agent. I'm trying to
[08:05] think how to word word it. Um and I
[08:09] think we're seeing the same things like
[08:11] you can do this you can make the same
[08:13] list for for the other ones, right? So,
[08:14] if you go to Google, uh, let's see,
[08:17] Google. So, Google, they just came out
[08:19] with a new one. And so, they apparently
[08:21] have an anti-gravity
[08:25] anti-gravity IDE agent manager. That's
[08:28] what I was reading. That's what they
[08:29] called it. They just launched it as like
[08:31] an experiment. And then they have the
[08:33] anti-gravity IDE. And then it sounds
[08:35] like basically anti-gravity 2.0 is the
[08:38] equivalent of the desktop app. Um, and I
[08:41] don't know if they have equivalents of
[08:42] of these two, right? And then we have
[08:46] Claude code.
[08:48] Um, and they have
[08:51] and these are all codingcentric ones,
[08:53] right? Obviously, there's also things
[08:54] like that are not coding centric, but
[08:57] for claude, we have what do they have?
[08:59] They don't really
[09:02] I guess here it' be like the claude
[09:04] extension, right?
[09:09] Sorry, I got sick last week. Um, I might
[09:13] still be sick. Who knows? Uh, I don't
[09:15] think they have really an equivalent of
[09:16] this, but then the desktop app, they
[09:18] have like the cloud code desktop app,
[09:21] right? That's what they call it. And
[09:23] then obviously their CLI is the CLI. And
[09:26] then I don't know about their like um
[09:30] they have claude agents. I guess the
[09:33] clawed agents. I'm not sure like whether
[09:35] they have a repo specific agents.
[09:38] Uh oh, is there an anti-gravity CLI?
[09:40] Okay. I didn't know there's an
[09:41] anti-gravity CLI. All right.
[09:46] And then of course, um I kind of want to
[09:50] like make this table in conjunction with
[09:52] all of you. So, humor me here. Um
[09:54] because then we also of course have
[09:56] OpenAI, right? Uh so openAI has some
[10:01] overlap with all these as well.
[10:05] Let's see. Uh
[10:08] Open EI. So OpenI has
[10:13] what do we got for OpenAI?
[10:17] Uh so they have the desktop app is
[10:20] definitely OpenAI and so it's Kodak's
[10:23] desktop, right?
[10:26] And then the CLI is the codec.
[10:29] And then I don't know that they have any
[10:33] I don't think they have something
[10:36] that's like just VS code,
[10:40] right? Unless they acquired one of the
[10:42] Did they acquire I don't think they
[10:43] acquired Cursor Windserve. Did they?
[10:47] It's hard to keep track of who gets
[10:48] acquired.
[10:51] Um,
[10:53] okay. So that's that that is how I think
[10:56] of it now and right now I think we need
[10:59] all these options because
[11:02] um you know because some you have some
[11:04] tasks that are very code centric uh
[11:06] where some tasks that are kind of like
[11:08] routine trivial and also like don't
[11:11] require a lot of like code editing. So
[11:13] you know I I use at this point like well
[11:16] this the CLI and the desktop app they're
[11:18] basically the same thing right it's just
[11:19] a different interface. Um, so I
[11:22] basically will either use co, you know,
[11:24] VS Code Copilot chat for full control or
[11:27] I'll use desktop app for less control or
[11:29] the coding agent if it's just like
[11:31] really really totally doable in the
[11:34] cloud and I can't be bothered. Um,
[11:38] maybe we'll call this the cloud agent.
[11:40] All right, so let's see. Oh, open code.
[11:43] Okay, I've run out of room on here
[11:44] though.
[11:47] Um, yeah, so open code. But open code
[11:50] are they are they both a CLI and a
[11:52] desktop?
[11:53] Um yes. So by the coding agent I mean
[11:56] when you go like the other day I was um
[12:02] uh I signed an issue because I was
[12:04] running the workshop and somebody said
[12:05] oh there's no license right and so I
[12:08] just went here and it said oh add a
[12:09] license and I signed it to co-pilot.
[12:11] Right? And so then co-pilot co-pilot did
[12:14] it. Um so that's what I meant by the
[12:16] coding agent. Right? So, this is
[12:17] something where I'm like just walking
[12:18] around on my phone and someone reports a
[12:20] bug, I'm like, "Okay, boom." You know,
[12:22] you do it. Uh, so, um, you know, very,
[12:29] uh, very handsoff with the the cloud
[12:31] agent. Okay. Um, and the cloud agent
[12:34] works pretty well in conjunction with
[12:36] issues because if someone has opens the
[12:37] issue, you're like, "Oh, okay. Well,
[12:40] uh, let me just assign it." So, if you
[12:42] get an open issue, which seems trivial,
[12:44] then you know, then you can do it. All
[12:46] right. So, we're just saying they have a
[12:48] I guess it's all called open code. I
[12:50] don't know.
[12:53] Uh Cloud has coding agents, too. Um
[12:58] you mean does like something equivalent
[12:59] to this? I guess here's So, if you were
[13:02] if you had an issue in a GitHub repo,
[13:04] can you easily assign that to Claude?
[13:06] How what is that called when you do
[13:08] that? I imagine that does exist. I just
[13:10] haven't used it and don't know what they
[13:12] call it.
[13:15] Um, and Pablo asked, "Can you create sub
[13:17] aents with the GitHub copilot desktop
[13:19] app?" Um,
[13:21] I don't know that you like I don't know
[13:23] if they have an explicit
[13:26] thing for making sub agents.
[13:30] Um,
[13:32] I guess if wait if we did like this sub
[13:35] agent, is that going to be a thing? No.
[13:40] Yeah. I don't know if they have a if
[13:41] they have a UI based way of making sub
[13:43] agents. I think they can use sub agents.
[13:46] They should be able to use anything that
[13:47] the CLI can use, but I don't see like a
[13:50] particular
[13:53] um
[13:54] Oh, we can also check the docs agent
[13:57] management
[13:59] sub agent.
[14:05] There we go.
[14:07] Uh defining well this is with the SDK.
[14:14] Nope.
[14:16] Uh
[14:20] oh. I'd have to I'll have to ask the
[14:22] team about that. All right. So let's
[14:24] see. Um so you can add Claude is the
[14:28] Claude GitHub app. Okay. Great. So there
[14:30] is a way of doing it. The Claude
[14:33] Claude GitHub app. Okay. All right. So,
[14:37] Claude
[14:38] GitHub app.
[14:44] Um, and then
[14:48] so Pablo says, "Another argument to use
[14:50] CLI versions is possibility to modify
[14:52] the harnesses using open-source
[14:56] plugins."
[14:57] Um,
[15:01] yeah. Oh, you're saying that I see
[15:03] you're saying it's easier to
[15:06] it's easier to modify a CLI experience
[15:10] versus a desktop app experience just
[15:12] because CLIs are like easier to
[15:14] intercept.
[15:16] Is that because it's just all standard
[15:18] input output that I could see that
[15:20] there's um that there there might be
[15:24] some way I haven't tried that because
[15:25] like it seems like it would be a bit
[15:27] messy. Um, but I could see that a CLI
[15:31] might be more naturally extensible than
[15:34] a uh than a desktop app.
[15:39] Um, oh, and then Jet Brains. Yeah, I
[15:41] don't have Jet Brains here. Well, we've
[15:43] run out of space. These are the only
[15:45] ones you can use because this is all the
[15:46] only ones that fit on the slide. Um,
[15:52] yeah. Well, so I think that here's the
[15:54] thing is that I I feel like if the CLI,
[15:58] right, um if I think if the GitHub
[16:00] copilot CLI supports something, then the
[16:04] desktop app should also support it. Um,
[16:06] so I guess give me your give me the list
[16:08] of things that you're wondering whether
[16:10] they work in the desktop app and I can
[16:13] just, you know, um, ping that to the the
[16:18] desktop team and see can we do this this
[16:22] this is this um
[16:26] because my hope is that I could use it
[16:28] for everything.
[16:30] Uh, because I use it all the skills,
[16:31] right? It has very good support for
[16:33] skills. Like pretty much everything I'm
[16:34] doing here is using skills and skills
[16:37] can use sub agents.
[16:41] All right. GST. What is GSD? No, no, no.
[16:45] Okay.
[16:50] Oh, but you're saying Okay. Yeah, we
[16:52] don't know if there's hooks. Maybe the
[16:54] hooks system is different. General
[16:57] themes.
[17:04] experimental canvas
[17:07] sessions. Use agency.
[17:11] Oh, there's a lot of stuff that's just
[17:12] for me.
[17:15] Um, well, probably I'm not supposed to
[17:18] show you this then. Okay.
[17:22] All right.
[17:23] Um, can I get access the hooks of the
[17:25] GitHub Copilot desktop app? Yeah, that's
[17:27] a good question. All right. Because I
[17:28] didn't see anything. All right. Well,
[17:30] let's check the experimental thing.
[17:32] That's Is there anything for hooks here?
[17:37] Um,
[17:45] I didn't see anything about hooks there.
[17:47] GitHub
[17:48] hooks supports agents hooks. Okay. Uh,
[17:56] let me see.
[18:09] Let me find it.
[18:17] All right, I'll find out best person to
[18:19] ask
[18:21] for all of our desktop questions.
[18:25] So, we want about hooks and sub aents.
[18:27] All right. Um,
[18:31] yeah, I think the interesting thing is a
[18:32] year from now, like, you know, we we'll
[18:34] probably use move increasingly toward
[18:37] these ones as the, you know, things get
[18:39] more and more powerful, but I think it's
[18:42] always nice. Right now, I feel like I do
[18:45] all like I like having this option with
[18:48] high code control, but who knows? Who
[18:50] knows? Like I I can't predict the future
[18:52] right now.
[18:53] Um, let's see what else. Uh, I think we
[18:58] talked about the MI models last week
[19:01] with the image 2e being really fun. Um,
[19:06] oh this like some exciting stuff on the
[19:08] industry
[19:09] industry side is that there is a new
[19:12] release candidate for MCP
[19:16] and uh the new one
[19:19] as uh let's see where did they put the
[19:23] release candidate?
[19:26] Um,
[19:28] it was on Let's find
[19:32] Let's find the tweet. MCPRC.
[19:38] There we go. All right. Uh,
[19:42] here's the release candidate. All right.
[19:44] So, it has quite a lot of potential
[19:47] changes in there. So, a stateless core.
[19:51] Um they are building MCP apps into MCP
[19:56] itself.
[19:58] Um they are changing things about
[20:00] authorization
[20:02] uh off hardening and then a deprecation
[20:06] policy. So I guess they're getting ready
[20:08] to deprecate stuff. So a lot if you're
[20:11] doing MCP there's a lot of potential
[20:13] changes. This is a release candidate so
[20:15] it's not it could still change. Um but
[20:18] there's a lot of interest in it.
[20:21] related MCP work OS came up with this
[20:24] like new off protocol for agents.
[20:28] I don't know if this is going to take
[20:30] off or not, but I read through it just
[20:33] in case it does.
[20:35] So that's OMD and it builds on top of
[20:39] OOTH, but it basically gives agents
[20:41] their own endpoints
[20:44] for authorizing.
[20:46] Um,
[20:48] I don't 100% understand it because it's
[20:50] it's building on a lot of OAS stuff and
[20:53] I haven't dug into all of it. Uh, but
[20:56] that's maybe another interesting thing
[20:58] to watch in case in case that becomes a
[21:02] thing. Um,
[21:05] what else?
[21:07] Uh, let's see. We Yeah, I mostly been
[21:10] prepping for build. I pretty much spend
[21:13] all day prepping all all day all week
[21:15] prepping for build. Build is coming up.
[21:17] There is a virtual option for build. So
[21:19] if you're not able to come in person uh
[21:21] maybe you can watch virtually and you
[21:23] know of course we always like to put all
[21:26] of our slides and stuff online
[21:28] afterwards. Uh we'll be doing a workshop
[21:30] on the three IQs, Foundry IQ, Work IQ,
[21:35] and Fabric IQ. Uh, so I've been
[21:40] uh testing those ones out more.
[21:43] And uh yeah, what else? Uh we've been
[21:48] doing more with the clawed models and
[21:50] trying to get that um the claw on
[21:54] boundary experience
[21:56] better. Um and I recorded a video using
[22:00] that.
[22:02] Uh let's see if any of you use Gmail.
[22:04] actually not a Microsoft thing, but I
[22:07] did hook it up to my desktop app. So,
[22:09] this is if you want an MCP server that
[22:13] connects to your Gmail, then my
[22:16] colleague made this repo here. And I I
[22:18] set it up this morning so that I could
[22:20] use it to to help find news for today.
[22:25] So, you can see here
[22:28] um Gmail, right? So, it searches for
[22:30] threads, right? So, it was looking for
[22:32] like the OpenAI threads.
[22:34] Um, so yeah, now I've got access to I'm
[22:38] pretty excited because a lot of my email
[22:40] comes in through Gmail because I I've
[22:42] had a Gmail address for many, many, many
[22:44] years. That's my personal address. So,
[22:47] now I've got, you know, I've got so many
[22:50] MCPS hook up. Now, I do have to be
[22:51] careful because a lot of these have read
[22:53] and write access, right? So, I've got
[22:55] Twitter, I've got Crossost, which is
[22:57] Twitter and Blue Sky and Maston. I've
[22:59] got Gmail,
[23:01] um, V IQ. So,
[23:04] I I have to be careful what I ask my
[23:06] agents for because they can do a lot.
[23:10] Um,
[23:12] what else?
[23:14] Let's see.
[23:17] Um,
[23:20] I think I already talked about Pyon last
[23:22] week.
[23:24] Am I working on any new samples?
[23:26] Um the No, I think uh really I'm just
[23:31] working on that lab. Um um the uh I mean
[23:35] I guess the the like the lab will maybe
[23:38] be interesting like I'll I'm happy to
[23:41] um let's see because in the lab we're
[23:44] going to have
[23:46] we're going to have Foundry IQ. We're
[23:48] going to have fabric IQ.
[23:50] Um, so that'll be that'll be useful
[23:52] because this will be public, right? So
[23:54] you'll be able to see how you can
[23:56] connect a connect to a fabric ontology
[24:01] uh and do do have it do queries to the
[24:04] ontology
[24:06] and then similarly with work IQ.
[24:09] Uh so mostly working on that right now.
[24:12] I think the other thing I want to do is
[24:14] take the because right now basically
[24:18] everything has to be an agent right so I
[24:20] want to take you know our rag repo and
[24:25] port it to agent framework so that it's
[24:28] an agentic application
[24:31] because I think at this point basically
[24:32] for anything to be relevant it has to it
[24:34] has to be an agent because people right
[24:37] now are so I think people right now
[24:39] expect to be able to hook up multiple
[24:41] tools right like if you're using an LLM
[24:44] in some sort of application, you expect
[24:46] to be able to easily bring tools into
[24:48] that application. So I think that I have
[24:51] to make this rag chat more relevant by
[24:55] making it a proper agent. And now agent
[24:58] framework is GA so I can go port it to
[25:00] agent framework.
[25:02] Uh after build
[25:07] will I incorporate MCP somehow here? Um
[25:10] well our lab is entirely MCP. So every
[25:12] time after you um you know you like you
[25:16] do set this all up via the SDK but then
[25:19] uh there's an MC endpoint for every
[25:22] Foundry IQ knowledge base. So then that
[25:25] endpoint you can hook up your you know
[25:29] your copilot CLI to that endpoint. Um so
[25:33] we can consume the Foundry IQ knowledge
[25:36] base as an MP server. Um we also do have
[25:40] uh you know one of the examples here is
[25:42] actually connecting to a new service
[25:45] that is only available over MCP. So yeah
[25:49] in this lab
[25:51] we have those options. Now for this one
[25:53] the rag repo it would be super fun to
[25:56] expose this over MCP but the big issue
[26:00] is that we support entra authorization.
[26:04] So, I think if I did it in order to do
[26:06] it the proper way security-wise, it
[26:08] would be an MCP server using that only
[26:13] uh worked in VS Code. Um because right
[26:15] now Entra doesn't support everything you
[26:17] need for the full Oflow. Uh but I could
[26:20] get it working in VS Code which would be
[26:21] fun. Uh so I think that would be really
[26:24] fun. The other interesting thing is and
[26:26] I have to think through this is um how
[26:29] would I add that in because right now
[26:30] this is built on the court framework.
[26:34] and fastm is b built on the starlet
[26:37] framework, right? So those are two
[26:38] different asgi frameworks. So I have to
[26:41] reason about what would be the the right
[26:45] way to have an application that both
[26:48] uses quart and fast mcp. Um
[26:53] so I haven't I haven't decided on that
[26:55] yet. It's much easier if you're mixing
[26:57] and matching things like it's much
[26:59] easier like if you have a fast API
[27:01] server it should be a lot easier to add
[27:02] in fast MCP since they are both built on
[27:05] top of Starlet right uh but I think it's
[27:08] going to be harder for me to just merge
[27:11] the MCP routes into this server since I
[27:14] don't have an underlying framework.
[27:17] Yeah, they could be separate services
[27:19] like it could have separate Docker
[27:21] files. Um, you know, because right now
[27:22] we have right now we just stuff
[27:24] everything into the same container. Um,
[27:28] but it it could be an entirely uh
[27:30] separate Docker service or within the
[27:34] Docker. I guess the Docker file could
[27:36] also launch
[27:38] um, you know, launch two
[27:41] services at once. Um,
[27:44] yeah. So that that's that and I I think
[27:48] that would be really interesting too to
[27:49] figure out the right way to do that.
[27:53] Uh, I need to actually because that was
[27:56] a lot of the questions I got on the
[27:58] workshop at Pyon were like, "Okay, I've
[28:00] got an existing app. How can I add fast
[28:03] speed into it?" And
[28:06] let me see if like
[28:10] fast I love. Okay. So, yeah, if you if
[28:14] you already have they make it super easy
[28:17] for fast API and then okay, open API
[28:20] from any OpenAI specification.
[28:26] Yeah. Yeah. I think I'd have to figure
[28:28] out what is the right way
[28:31] to add fast MCP onto a court app or I
[28:35] just say screw it and I port this to
[28:37] Fast API.
[28:40] I don't know which one would be easier.
[28:42] Um, so Pablo says, "Do um all the
[28:47] official mo models used through GitHub
[28:49] Copilot, are they being protected
[28:50] against prompt injection?"
[28:53] Um,
[28:55] it's a good question as to where GitHub
[28:58] copilot models
[29:00] because I don't know if they're all
[29:02] going behind are the question basically
[29:04] is are they all going behind our content
[29:06] safety filters?
[29:10] Oh, here we go. Learn how different AI
[29:12] models are. This is usually the one
[29:14] that's useful. Um,
[29:17] so like you can see for each of them,
[29:19] right? These are hosted by Azure's
[29:22] infrastructure. They go through, oh,
[29:25] there's a typo here. Um, they continue
[29:27] to pass through GitHub Copilot's content
[29:29] filtering system. So, that one goes
[29:31] through,
[29:32] um, looks like we have some fine-tuned
[29:35] models.
[29:37] uh and that would go through it as well.
[29:39] Enthropic models. So these ones are
[29:41] hosted on AWS.
[29:44] Um
[29:47] and they use prompt caching. Oh, it does
[29:50] say they they continue to run through
[29:51] GitHub copies content filter for public
[29:54] code matching along with those for
[29:55] harmful or offensive content. Okay. It
[29:58] doesn't explicitly say whether they're
[29:59] going through for the prompt injection.
[30:01] I want what kind of prompt injection
[30:03] attacks are you worried about for
[30:04] copilot? like something like delete like
[30:06] in skills like delete my things. Yeah, I
[30:09] don't know if they're going through that
[30:10] um for along with those for harmful. So,
[30:13] none of these explicitly mention prompt
[30:15] injunction as a thing they check for.
[30:17] So, that would be
[30:20] a good um
[30:23] that's a good question. Um but it does
[30:25] seem like all of them are going through
[30:28] our content safety filters. So they very
[30:30] well like when you set up the content
[30:32] safety filters you can toggle on whether
[30:35] you know what kinds of um protection you
[30:38] want and one of those is the you know uh
[30:41] the jailbreak uh or as they say direct
[30:44] attack or indirect attack. Uh so they
[30:47] they might they might have that enabled
[30:50] but they might not. Um because the like
[30:53] the risk whenever you enable these
[30:55] safety filters is that you get these
[30:56] false positives all the time and then
[30:58] you're like h
[31:00] right you get frustrated. So they have
[31:02] to be really they have to do a really
[31:05] good job with safety filters um because
[31:08] it can be such a bad experience if it if
[31:10] they haven't done a good job.
[31:13] Um so yeah so certainly like it and I
[31:17] think as you're for foundry you can find
[31:20] a a similar listing like foundry if you
[31:22] host enthropic on foundry it's the same
[31:24] deal where currently they are not hosted
[31:26] by us directly right they but um but I
[31:29] think they
[31:32] probably go through the safety filter
[31:34] too
[31:37] um
[31:38] okay yeah so Pablo says started to worry
[31:40] about the requests you make that get
[31:41] information. Anyway, yeah. So, that's
[31:43] the good old lethal trifecta. Yeah. And
[31:47] I I want to make a slide about this for
[31:48] our our lab workshop. Um,
[31:53] access to private data, ability to
[31:55] communicate, and exposure to untrusted
[31:57] content.
[31:59] So, yeah, it's definitely a risk, right?
[32:01] Like I do have a lot of NC servers
[32:03] enabled here for my desktop app and um,
[32:07] you know, it's it's it's worrisome,
[32:09] right? because it could in theory like
[32:11] delete all my Gmails. Uh which might be
[32:14] good for my my state of mind but
[32:17] probably bad for other people. Uh yeah.
[32:20] So um I would be more nervous if I had
[32:23] all these enabled in VS Code where I do
[32:25] a lot more of my work. So uh it is a
[32:29] yeah there's it's good to be concerned.
[32:33] Um
[32:36] so yeah it's a good question. uh see if
[32:39] we have any any additional
[32:43] documentation about in prompt injection
[32:45] itself.
[32:50] Uh
[32:52] okay. And then Sylvest shared from the
[32:55] NSA
[32:58] concerns in MCP design implementation.
[33:02] The NSA is getting into MCP.
[33:05] What? That's crazy. That's cool.
[33:11] Nice.
[33:14] Yeah, that actually reminds me that my
[33:16] colleague is at
[33:19] um conference this week that looks like
[33:22] it's got some good stuff. Maybe there'll
[33:24] be some good papers out of it. So, it's
[33:25] the ACM CIS. It's happening in
[33:30] uh
[33:32] in San Jose this week. Um, I don't think
[33:36] I'll make it because I'm still working
[33:38] on the lab, but uh, but I think there'll
[33:42] be like maybe interesting papers that
[33:44] that come out of it. Uh,
[33:47] where's the program topics? Okay, I'm
[33:49] trying to get All right, let me ACM CIS
[33:53] 2026.
[33:57] Here we go.
[34:01] Ah.
[34:12] Uh, I see there's a question about the
[34:14] US government. I have no idea what the
[34:16] US government will do um,
[34:19] in terms of limiting access to Chinese
[34:21] open source models. I think generally
[34:23] it's good to be able to
[34:27] know how to use different models. Um
[34:31] so to have the the flexibility to be
[34:35] able to switch from one to the other and
[34:37] not be completely dependent on
[34:40] uh anyone model like whether that's a
[34:42] Chinese model, anthropic model, openAI
[34:44] model
[34:46] um I think we ideally
[34:49] want to have the flexibility to switch
[34:50] between them
[34:53] but I I don't know what our government
[34:55] will do. We have a very unpredictable
[34:56] government.
[34:59] Uh so Pablo says starting to think that
[35:01] open shell makes more and more sense.
[35:02] Okay, I don't know open shell. I know my
[35:04] colleague said like right now at the
[35:05] conference he just saw a presentation
[35:07] about open hands. So that's the first
[35:09] time actually I'm hearing this way but
[35:11] this is like an open looks like an open-
[35:14] source coding agent. What is open shell?
[35:24] Oh, so this is so like maybe open shell
[35:27] is so that is this what open shell is um
[35:30] is open shell just you're taking in
[35:32] terms of security
[35:35] um
[35:38] oh from Nvidia Nvidia okay Nvidia
[35:44] okay so let's see what openshell is
[35:52] safe private runtime ah Okay. So this is
[35:54] about the security. Yeah.
[35:57] Declarative YAML files.
[36:03] Okay.
[36:05] Create a sandbox. Okay. Open shell
[36:07] sandbox create. Docker has something
[36:08] very similar now too. Docker sandbox
[36:10] create. Oh, but this one has a d-cloud.
[36:13] Oo dash copilot.
[36:17] Fancy.
[36:19] Every stand signbox. Okay. So VS code is
[36:22] experimented with this now too. Like I
[36:23] actually ended up changing my setting
[36:25] because I was getting annoyed by it. Um
[36:28] but if you go to your settings now uh
[36:31] maybe search for sandbox. Yeah. So we
[36:34] have
[36:36] um the sandbox. So right now I turned it
[36:40] off entirely.
[36:42] Um but what you can do you can have it
[36:44] on which does like a you know very very
[36:48] limited um abilities in the sandbox or
[36:51] you can have it on but allowing network
[36:54] calls right. Um
[36:58] so uh so this is if you want a higher
[37:01] degree of security inside VS Code then
[37:04] you know then you want to go for this.
[37:07] This may be insiders only. I don't know
[37:08] if it made it out to stable yet. Um, I
[37:11] think that like in allow network, I
[37:13] might go back to allow network. I guess
[37:15] I think I was doing some cross repo
[37:17] stuff and that's why I ended up changing
[37:18] it. Um, but there's a bunch of options
[37:22] there. So, yeah, definitely check that
[37:24] out for um
[37:28] for VS Code specifically.
[37:30] Uh, and this sounds like this could do
[37:32] something similar
[37:34] at the for for Copilot or or other
[37:38] coding agents, right? to like block the
[37:41] network request. I gotta say like when
[37:43] your network requests are blocked you're
[37:45] it's really hard to get anything done
[37:48] because you know constantly like being
[37:50] like hey look at these docs look at
[37:51] these docs look at these docs right so
[37:53] if you're going to you know it's
[37:56] definitely like good from a security
[37:58] perspective but um you have to have a
[38:01] lot of patience to
[38:04] allow
[38:05] all those domains specifically that you
[38:07] might be reaching out to because I I I
[38:09] do a lot of referencing of documentation
[38:12] and this and that. Like I'm always
[38:14] bringing context in from the web into my
[38:17] conversations.
[38:19] Um so I I was finding it limiting to
[38:22] have the network be blocked. Um but um
[38:25] but yeah, if you have the patience for
[38:27] it and you might not be like I and I
[38:30] also work on lots and lots of different
[38:32] tasks. I think if I was working on a
[38:34] more like, you know, if I was working
[38:36] more consistently on the same kind of
[38:37] task day in day out, it would be easier
[38:40] for me to say like, oh yeah, this is
[38:42] exactly the sandbox rules that are going
[38:44] to work. Um, but I think that because I
[38:46] work on like, you know, 20 different
[38:47] projects at once that are all different
[38:48] kinds of things. Like it's it's uh hard
[38:51] for me to set up a sandbox policy that's
[38:53] going to work across all these different
[38:55] types of projects.
[38:58] Um but that looks good. DP protection
[39:04] layers. So file system. Yeah. So
[39:06] prevents read rights network process. So
[39:10] I think the VS code sandbox must work
[39:12] pretty similar to this. Um right. And
[39:15] it's just that you have the controls
[39:19] um for whether what sort of network
[39:21] stuff you're going to allow.
[39:23] And then we have GitHub copilot CLI.
[39:26] Very nice.
[39:28] Open claw.
[39:30] Oh, right. Open claw with Nemo claw.
[39:33] That sounds fun.
[39:37] All right. Um, hi Ahmed. In these calls,
[39:41] we just talk about stuff happening in
[39:43] the Python AI world and
[39:46] um, yeah, you just just people ask
[39:51] questions or share share interesting
[39:53] things.
[40:02] Um yeah I so as Nomi says like well like
[40:05] if you block off access to all your
[40:07] stuff then it takes out a lot of the
[40:08] traction certainly something like
[40:10] openclaw right like I think that's why
[40:11] people are excited about openclaw is it
[40:13] came up with it came out the gate with
[40:15] all this access
[40:18] um but but with a coding agent like if
[40:21] you're you know if you're really just
[40:23] writing some code like you know you
[40:26] don't you don't need access to to you
[40:29] know to that many things right like
[40:31] maybe to your issue tracker
[40:34] uh and to documentation right so um you
[40:37] know if you're able to allow the network
[40:40] calls for
[40:42] you know for your your issue tracker and
[40:44] your documentation
[40:46] then I think you can actually like I
[40:48] feel like for most coding tasks actually
[40:50] it would be fine to work inside inside
[40:54] the sandbox. Um it's the m like I find
[40:58] like you know it's these kind of more
[41:00] like productivity things like oh you
[41:02] know make me my you know weekly
[41:04] PowerPoint for the office hours right
[41:06] that's the kind of thing where it really
[41:07] helps to bring stuff like so things that
[41:09] are more not just coding that you're
[41:13] you're you're that you need to gather
[41:16] this information right like more
[41:18] productivity planning
[41:21] presentations
[41:23] uh that sort of
[41:29] Um,
[41:37] yeah. And there was also I saw a
[41:38] presentation about Docker sandbox
[41:40] create.
[41:42] I haven't tried them, but I did watch
[41:43] the talk about it. That would be another
[41:45] one.
[41:47] Uh, oh, SPX. Here we go. Sorry. SPX. I
[41:50] forgot they did. Okay. Docker sandboxes.
[41:56] So AI run AI code agents in isolated
[41:59] microVM sandboxes.
[42:03] Um so you install it and then you can
[42:05] launch an agent right so here we do once
[42:09] again have copilot as one of the
[42:11] supported agents. So you' be download S
[42:14] spx and SPN run copilot right and then
[42:18] um you can use stored secrets right
[42:21] because that's already something that uh
[42:24] docker knows how to do is to manage
[42:27] secrets.
[42:29] So I don't know how this compares to
[42:31] let's see open shell versus spx. I don't
[42:34] know if anyone's done a comparison of
[42:35] them.
[42:37] Well yeah thanks co-pilot. Um,
[42:43] okay. I don't I don't see a comparison.
[42:47] Uh,
[42:51] yeah.
[42:55] Okay. So, security model, right?
[42:57] Container level kernel level sandboxing
[43:00] policy control
[43:04] um deployment
[43:10] Okay. All right. So, I think that
[43:13] generally, you know, they're they're
[43:17] fairly similar. Um, so if you're already
[43:19] using Docker, then SPX might be
[43:23] might be a good one to try as well.
[43:26] Um,
[43:28] I do I mean, yeah, I started using I
[43:30] didn't I wasn't using Docker on my last
[43:32] machine because I ran out of RAM and
[43:34] hard drive space. But on my new machine,
[43:36] I should be able to use Docker. Easy,
[43:38] easy peasy.
[43:44] All right. Um,
[43:51] what what else? Anything else?
[44:01] And next week I will be at Build. So we
[44:04] won't have office hours next week. Um
[44:07] but we there'll be lots of stuff coming
[44:09] from Build. So you'll be busy watching
[44:13] build build talks or seeing the posts
[44:16] that come from there.
[44:20] All right.
[44:22] I think we'll have a Oh, we had a
[44:26] suggestion. Docker agent. Whoa.
[44:32] Oh, so this is trying to make it easy to
[44:34] deploy
[44:36] agents. So I get think this would be the
[44:38] most similar to
[44:41] a cloud agent or a you know foundry
[44:44] foundry hosted agent right to find an
[44:47] agent.
[44:49] Yeah. And do they go over A2A what you
[44:51] get? Yeah. So I was just getting a
[44:52] question about A2A
[44:54] um to TUI CLI.
[44:57] So this is Yeah. This is very much like
[44:59] Foundry hosted agents. Uh, so you build,
[45:02] run, you describe what your agent does.
[45:04] Oh, a YAML file. Okay, that would be
[45:06] more like a claude agent. I think claude
[45:08] agents use YAML files. At least I saw
[45:10] they use YAML files for some parts of
[45:12] it.
[45:14] Um, so this is like very I I really
[45:17] don't like putting agents in a YAML file
[45:19] like because it's like how good could
[45:22] your agent actually be if you could
[45:24] describe in Yam? I don't know. Maybe it
[45:25] could be. Maybe if it was like
[45:29] basically if it's like a skill like if
[45:31] your agent is doing the same thing a
[45:32] skill can do then you know you could do
[45:35] it right. So you you've got instructions
[45:37] and you've got tools. So maybe you can
[45:40] do useful things there. I just think it
[45:42] eventually you would run into the limits
[45:44] of it.
[45:46] Uh then you can
[45:50] run
[45:52] uh run it. Okay. Okay. Blah blah. Uh,
[45:56] reusable YAML bone tools.
[46:00] Um, I don't know if it integrates with
[46:02] Foundry, right? Because it says like
[46:03] enthropic. So, here you say like which
[46:05] model you want to use. I don't know
[46:07] which whether it's going to support
[46:09] Foundry models too.
[46:11] Um, built-in tools
[46:19] and then model tools sub stream. All
[46:22] right. And then they're going to
[46:27] are they going to expose it as an MCP
[46:29] and A2A? Let's see.
[46:34] Okay, let's see. A2A
[46:37] features.
[46:40] These docs are a bit funny. Um,
[46:45] doctor agent run and then
[46:50] nope. A2A. A2A. I want to see A2A
[46:53] features terminal UI. Okay, so we have
[46:57] MCP mode. So you can expose them as MCP
[47:00] mode. You can expose them as A2A.
[47:03] You can expose them as ACP
[47:08] uh API server. Well, they can I do like
[47:10] how you can expose them as like a lot of
[47:12] things. That's kind of sweet, right? an
[47:14] API server
[47:16] um with SSE and
[47:19] a chat server using the chat completions
[47:22] API. Interesting. Not the responses API.
[47:24] I wonder if they're going to add that
[47:26] later.
[47:27] Um
[47:30] you can do eval
[47:33] supports skills as well. Okay. But
[47:35] what's interesting is that you get a
[47:37] TUI,
[47:39] CLI, an MCP, an A2A, an ACP, an API chat
[47:43] server. So, if you're wondering all the
[47:44] possible ways that you might want to be
[47:47] exposing your agent, here you go, right?
[47:49] Because we've moved beyond, you know,
[47:51] just having full stack uh, you know,
[47:54] chat apps. Now, now you want all these
[47:56] integration ports. Um, so like Foundry
[47:59] Hosted agents does support some of these
[48:02] and I think they're going to support
[48:04] more of them very soon. Uh it's just but
[48:08] it is really interesting to see because
[48:09] I just got a question today from someone
[48:11] who was like trying to figure out
[48:12] they're building multiple agents and
[48:14] what protocol should they use for those
[48:16] agents to talk to them and I don't think
[48:18] we really know at this point what's the
[48:20] most compatible because it really
[48:21] depends how you're going to use them but
[48:22] it's interesting to see all the
[48:24] different possibilities.
[48:27] Um
[48:31] yeah. Oh, so for Docker agents, what I
[48:33] was wondering was the models, not the
[48:35] hosted agents, right? Because I think
[48:36] Docker agents basically are competitive
[48:39] with Foundry hosted agents, but in terms
[48:41] of these models here, what are the
[48:45] allowed
[48:47] um so these are coming models use
[48:50] provider. Okay, they these docs are kind
[48:53] of messed up. Um model config model
[48:57] configuration. All right, one of
[49:00] Azure, right? So you can see here's
[49:02] Azure.
[49:03] Um,
[49:07] okay. So here, so the I think the thing
[49:10] I'm not sure of I think it probably
[49:11] requires Oh, it must require of course
[49:13] it requires a key because it's hosting
[49:14] on Docker. So you would set up an Azure
[49:17] deployment. Um, it looks like it at
[49:20] least works as Azure OpenAI. I don't
[49:21] know whether it would work with the
[49:23] other ones. Um, there's probably some
[49:25] way to get it to work, but it would need
[49:27] to be with a key, not with keyless.
[49:31] Cool. All right. Yeah. So, that's a
[49:34] another um potential way of running
[49:37] agents
[49:38] uh in comparable to the foundry agents
[49:42] perhaps.
[49:44] All right.
[49:45] Well, we are now at time. Uh thank you
[49:49] everyone for coming. As always, I
[49:52] learned a lot from you and I will, you
[49:56] know, post up the recording and uh the
[50:00] transcript and if there are any
[50:01] follow-up questions, like I I just got a
[50:03] good lead for who to ask about the
[50:06] GitHub app stuff. So, if there's
[50:08] follow-up questions, I'll I will be
[50:10] asking the product teams.
[50:13] Okay? And then I will see you in two
[50:16] weeks.
[50:18] Bye, everyone.

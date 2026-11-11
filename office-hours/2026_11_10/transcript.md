[00:00] Welcome everyone to our weekly Python
[00:02] and AI office hours. As usual, I have a
[00:06] roundup of the weekly news. So we can
[00:10] talk over some of these things. We can
[00:12] do some live coding, some demos, answer
[00:16] questions from the chat, whatever it is,
[00:19] um however you all want to take this
[00:21] today.
[00:23] Um so as I was just saying, yes, I
[00:25] next week is Ignite. So that is what
[00:28] we've been spending all our time on for
[00:30] the last month or months or whatever
[00:33] since Build uh prepping for Ignite
[00:36] because it's also when we uh when we
[00:38] launch a lot of the stuff.
[00:40] Um so I've got
[00:42] uh quite a few sessions. A lot of these
[00:44] are a lab, um but the lab will also be
[00:48] uh going into new stuff.
[00:50] Uh so um so yeah, there's going to be a
[00:54] lot of a lot of new things happening
[00:57] there.
[00:58] All right. So what else is going on this
[01:01] week? So the one of the big things I
[01:03] wanted to talk about was skills over
[01:05] MCP. This is something we've talked
[01:07] about here
[01:08] in the past, and there is support for it
[01:12] in the Copilot Rest harness, which means
[01:16] the Copilot CLI. It means all of the
[01:18] like everything that uses the Copilot
[01:21] harness can easily add support for it,
[01:23] but they do need to, you know, um you
[01:25] know, add some kind of mechanism to
[01:26] enable it. So the Copilot CLI has an
[01:28] environment variable, and then VS Code
[01:31] Insider in the most recent version,
[01:34] November 4th, they added um they added
[01:37] support for it in this version,
[01:41] Um so they do have experimental support
[01:44] for it
[01:45] uh here, right? So add
[01:48] uh add support for agent skills. Here we
[01:50] go.
[01:52] Uh so I've actually got that working
[01:55] over
[01:57] um
[01:58] over here. Okay.
[02:00] So what I did to get this working
[02:04] is that I went to my user settings
[02:09] uh and then you just type you just type
[02:11] MSP skills
[02:13] and you'll see this chat agent host MSP
[02:15] skills enabled. So, I checked that on,
[02:17] right? By default, it's off right now
[02:20] um cuz you know we want to do some
[02:22] testing, make sure it's all working.
[02:24] Um but the goal is actually to have it
[02:26] default on next week uh which is pretty
[02:29] cool.
[02:30] Uh and that would even be in VS Code
[02:32] stable. Uh so right now it's insiders
[02:34] and it's something you toggle on, but it
[02:37] should be default on very soon.
[02:39] So, once we have that on, then um
[02:42] there's you know a couple ways we can
[02:44] trigger it, right? So, I added this D
[02:46] Scope server. D Scope
[02:48] they are like um MSP auth um
[02:53] provider and so I signed up for them and
[02:56] I authenticated to my D Scope account.
[02:59] See I'm like
[03:00] logged in over here.
[03:03] Um and then I can say like oh what D
[03:05] Scope skills are there?
[03:11] And uh it should see that the D Scope
[03:14] server exposes a skill.
[03:18] Oh yeah.
[03:20] Okay, turn Okay, let's also do
[03:24] um
[03:24] turn off
[03:27] find my VS Code agent hook that plays a
[03:31] sound
[03:33] when agent stops and comments out the
[03:37] sound at line
[03:41] Okay.
[03:42] So, as you can see there's one D Scope
[03:44] skill provided by the D Scope
[03:46] MSP server and uh this is how it comes
[03:50] down
[03:51] um and saying oh they also provide
[03:53] skills, right? So, this is a skill
[03:56] coming from an authenticated MSP server
[04:00] that is remote, right? So, that would be
[04:02] you know one example of skills. But then
[04:03] I also went ahead and quickly made a
[04:07] fast MSP server that has skills. So here
[04:11] and it only has skills actually, that's
[04:12] all it has. So I said, okay, we're using
[04:14] fast MCP. We're adding the skill
[04:17] provider and this one is just loading
[04:18] skills
[04:20] just from this local folder here. So I
[04:22] just everything in here. And right now
[04:24] this only has one skill.
[04:26] You know, it's
[04:27] it's not a very exciting one. It just
[04:28] says release notes, write release notes
[04:30] from merge pull request, right?
[04:34] And that's it, right?
[04:37] Oh, and it has a template. So that's
[04:39] nice.
[04:40] You know, this is very minimal here.
[04:43] Oh good. All right. It it did
[04:45] you won't have to listen to the constant
[04:47] giggling because
[04:50] we've now calmed it down.
[04:52] All right. So we can use the right? So
[04:55] let's say you know, I have that server
[04:57] running here that local MSP server that
[05:00] has the skills in it. So I told Copilot
[05:02] like, hey, draft release notes for this
[05:05] you know, for this repo. And what you
[05:07] can see is that it pops up this allow
[05:10] skills from local skills.
[05:12] And it says MSP server local skills
[05:14] provide skills that want to load
[05:16] instructions into the session.
[05:18] So that
[05:20] that is presumably the experience of VS
[05:23] Code the first time you are loading
[05:25] skills from an MSP server. I need to
[05:27] check with the team to see like, oh, is
[05:29] that you know, kind of what it would
[05:30] always
[05:31] be like. And then you can see it read
[05:33] the skill, right? So
[05:35] that was interesting actually read skill
[05:37] skill. Okay. And then it read the actual
[05:40] so read skill. So it says, oh, it wants
[05:42] this skill.
[05:43] And then here's the input. All right. So
[05:46] the skill has this crazy resource ID. I
[05:48] guess this must be the resource ID on
[05:50] the MSP server.
[05:54] And
[05:56] yeah, and then it's no resource template
[06:00] no resource reader
[06:01] Okay. So let's see
[06:04] Oh, the release notes skills. Oh,
[06:06] interesting. It says the release notes
[06:07] skill point to a template .md, but I
[06:09] couldn't open because no tool to read
[06:11] that file was available.
[06:14] Huh, so maybe um
[06:18] skills struggle with having cuz this was
[06:21] example of a skill that had a
[06:25] template .md
[06:28] like locally, right? But I'm thinking
[06:30] that when skills are exposed over MCP
[06:32] like you know, it doesn't
[06:34] it doesn't work to do that. So, that
[06:37] would be
[06:39] that would be a good thing to to keep in
[06:40] mind is that if you're going to have a
[06:42] skill that references an asset like
[06:45] this, then
[06:47] you know, then you probably need to
[06:49] serve up that asset using
[06:52] an MCP resource. So, let's try making
[06:54] that change.
[06:57] So, let's say
[06:59] okay. Let's go here and say
[07:03] when I try to
[07:05] use this skill over
[07:08] to key from server .py
[07:12] my agent couldn't read template .md.
[07:17] Should we serve that as an MCP
[07:21] resource instead?
[07:23] So, this is a good question for people
[07:25] working on this. Yeah, exactly. So, as
[07:27] Bernard says
[07:29] yeah, we are doing I am trying out
[07:31] skills over MCP cuz it is now in the
[07:33] Copilot
[07:34] harness
[07:36] and VS Code 1.146.
[07:39] So, just want to see if there's any
[07:41] issues with it. I've already run into an
[07:43] issue, which is good.
[07:47] So, it should be discovering and
[07:49] retrieving skills via skills listen
[07:50] skills get loading skills through
[07:51] resources read verifying resources
[07:53] manner while preserving server origin.
[07:57] Sharing media okay.
[08:01] Publish skills
[08:07] okay.
[08:08] So, I the question is why how do we make
[08:12] it so that
[08:14] it's it claims that it's already
[08:19] served as a template. It says that the
[08:21] agent had no tool for
[08:24] reading MCP resources.
[08:33] Let's see how it's supposed to work.
[08:36] Okay.
[08:37] All right. So um
[08:40] let's see.
[08:42] This is this is the same
[08:46] Yeah, this is the same issue I was just
[08:47] pointing at. Yep, that's correct. Mhm.
[08:51] Uh so Adam says currently Codex cursor
[08:56] etc. had agent skills bundled with MCPs.
[08:59] That's agent plugins. Yeah. Yeah, so the
[09:01] the
[09:03] that's agent plugins um and yeah,
[09:06] cursor, ChatGPT, open Claude, Plexi,
[09:08] Open Hands, Kiro, Graph Bot, GitHub,
[09:10] Nano Claude, VS Code, Hermes.
[09:13] Um those are all ones that like formally
[09:15] support the agent plugin spec, but
[09:17] others might
[09:18] not so formally support it or they just
[09:20] have another way of bundling.
[09:22] So
[09:23] um so yeah, you can do that and that's
[09:26] probably what we're doing it. The
[09:27] advantage of doing skills over MCP is
[09:29] that then um you can actually
[09:32] personalize the skills in theory, like
[09:33] if you have an authenticated server,
[09:35] right? D Scope, I actually logged into
[09:37] my D Scope server. So uh in theory,
[09:41] depending on like which plan I have with
[09:43] D Scope, you know, what data I have in D
[09:45] Scope, D Scope could serve me
[09:48] different skills, right?
[09:51] Um
[09:53] Okay, so da da da.
[09:57] All right, so I think
[09:59] Okay, so it says we should file a VS
[10:01] Code issue.
[10:03] Okay, can you file that issue and say
[10:08] that co-pilot threw it.
[10:13] on my behalf.
[10:14] Yeah, so skills over in speech should be
[10:17] more flexible, more customizable, right?
[10:19] Because it's not necessarily just a
[10:20] static. Like in this case, you know,
[10:22] just the way it quickly
[10:24] uh you know, wrote this MTP server, you
[10:26] know, it was just filling
[10:27] you know, just just outputting some
[10:29] local files, but um you know, you could
[10:32] be dynamically generating these
[10:34] skill.mds, you know, using templating
[10:36] languages, Jinja, that sort of thing. So
[10:39] I think there is potentially a lot of
[10:40] really interesting things you could do
[10:42] with skills over MCP
[10:44] um
[10:47] uh
[10:47] once we you know, work this all out. All
[10:49] right, so let's see
[10:52] uh oh I am in VS Code
[10:57] in my
[11:01] Um
[11:02] yes
[11:05] on
[11:09] MTP
[11:12] Okay.
[11:14] Uh
[11:14] cool. Okay, so
[11:18] so it's generally skills over MTP
[11:21] you know, works except you know, what
[11:23] we're seeing is maybe the attached
[11:25] resources that that can be an issue. Of
[11:27] course, lots of agent skills not don't
[11:28] necessarily have attached resources,
[11:31] um but many of them do. So I think we do
[11:33] need to
[11:34] um
[11:36] figure that out. Let's see if we can try
[11:37] using the like what happens if we
[11:40] actually use
[11:42] can we use the
[11:45] let's see, can we use the
[11:49] can we use the d skill f p g a skill
[11:58] MTP Jam Inspector has support. Very
[12:01] nice.
[12:05] Oh, cool. So you found a
[12:08] a page that has a little support, right?
[12:09] So and then let's see did they add it to
[12:12] can I use dot dev skills? Okay.
[12:14] So they did add it to skills the
[12:17] mcp.devs. Let's try adding on all the
[12:19] things. I'm sure it's going to say not
[12:21] supported for
[12:24] everything, so I just need to let them
[12:25] know. I mean it's still kind of true.
[12:26] It's not supporting VS Code because
[12:30] um you know it's behind a
[12:33] a flag right now, but in a couple weeks.
[12:35] So yeah, right now it's a whole lot of
[12:37] not supported.
[12:39] Um
[12:40] but here you can see that there's a lot
[12:42] of progress being made.
[12:44] Um
[12:47] you know Fast MCP.
[12:50] We just used that.
[12:53] And then the servers.
[13:00] Nice.
[13:08] All right, so let's see. So here I said
[13:10] can we use the dsco fpga skill? And once
[13:13] again we get this pop-up and it says you
[13:17] know do we want to allow it to use those
[13:19] skills?
[13:21] I'm going to say allow once and then
[13:22] it's reading the skill. So you can see
[13:26] um it read it all in.
[13:28] And you know it's kind of looks like in
[13:32] this case it's basically dynamically
[13:33] pulling down some
[13:37] documentation.
[13:39] Uh so your project has no FPGA schema.
[13:44] You can make it up. This is
[13:47] my demo.
[13:52] Okay.
[13:53] So I think that this skill didn't
[13:55] necessarily have Let me see if it kind
[13:57] of has any links in it.
[14:02] Yeah, so this skill does not have any
[14:03] associated resources, which is why we
[14:05] didn't have many issues with it. This
[14:07] was just only the skill.md.
[14:11] So it was able to work successfully.
[14:15] All right, so that is skills over MCP.
[14:19] Um
[14:20] let's go find the
[14:23] issue that it filed
[14:25] um about it
[14:27] so we can follow that and see that's
[14:31] here.
[14:34] Okay. Agent can't read over recent agent
[14:36] load it can't open following
[14:45] Recesses when a client and recent
[14:47] returns the template.
[14:52] Okay.
[14:54] All right. So here's here's issue filed
[14:56] there and I'll ping this
[14:58] to the
[15:00] VS Code team.
[15:14] Okay. All right. Cool. So then let's go
[15:18] back and see what else is happening
[15:22] this week. I did post that now our Azure
[15:26] OpenAI starter kit does have all the
[15:27] decision API samples in it. So that
[15:30] means
[15:31] you've got samples in Python,
[15:33] TypeScript, Go, .NET, Java, Ruby that
[15:36] show you how to use either responses API
[15:38] or the decisions API.
[15:40] So you can go you can go either way.
[15:43] Lots of people like Amazon just posted
[15:45] that they ported a big internal usage of
[15:49] LLMs to decisions and that they're you
[15:52] know getting massive savings from it.
[15:56] So you definitely want to think about
[15:58] whether there's places
[16:00] where you can save money as well by
[16:03] porting to decisions. So we
[16:06] saw this before, right? So you can do
[16:10] in this case we're doing an image so we
[16:12] pass in
[16:13] an image and then we ask some questions
[16:17] and we'll get back.
[16:20] We'll get back the answers and can use
[16:23] the answers and the probability or
[16:26] confidence in order to decide what to do
[16:28] next.
[16:31] Um and then, you know, you can also just
[16:33] do it with text as well and that's a lot
[16:35] simpler.
[16:37] Uh
[16:39] and this has the infra to deploy the
[16:40] models as well. It's just a GPT-6 Luna,
[16:43] so anywhere where you can deploy GPT-6
[16:45] Luna, you should be able to use the
[16:48] Decisions API.
[16:50] Except I heard maybe like one of the
[16:52] East US ones, I think.
[16:55] Patrick says you ran experiment with
[16:56] some sparks from NVIDIA to use local
[16:58] models to save costs. Oh there yeah,
[16:59] local models without to be an approach
[17:01] if you've got the, you know, hardware to
[17:04] run them.
[17:06] All right, what else is happening here?
[17:09] Um
[17:12] in the industry side, Claude added
[17:14] message threads. I find that very
[17:16] interesting because that's basically
[17:17] what Responses API has always supported
[17:20] is that Responses API can either be
[17:22] stateless or stateful.
[17:24] Um the Message API has always been
[17:26] stateless, uh but now with Message
[17:28] threads, then it looks basically like
[17:30] the same
[17:32] thing as Responses API from what I can
[17:35] tell, right? Which is that you make the
[17:37] thread, you get back the ID, and then
[17:38] going forward, you're just passing the
[17:39] ID.
[17:40] Uh so it's very interesting to see them
[17:42] basically follow suit from the Responses
[17:44] API there. Um I've asked whether this is
[17:47] something we're adding support to on um
[17:50] our Message API because we of course
[17:52] serve the Anthropic models as well.
[17:55] And let me see if I heard back about
[17:57] that yet. Uh
[18:00] no, I haven't heard back yet.
[18:02] Um so yeah, just something to keep in
[18:04] mind if you are working with Message API
[18:07] and Claude models.
[18:09] Uh
[18:10] let's see. Claude added finance. Uh I
[18:12] haven't tried it, but sounds like a good
[18:14] idea. I'm pretty bad at money.
[18:17] And a lot of times I do use LLMs because
[18:19] they
[18:21] know a lot more about money than I do.
[18:22] Uh so they do this via Plaid, which is a
[18:24] common connector for financial accounts.
[18:27] Um
[18:31] Let's see. Uh OpenAI just launched a new
[18:35] model, GPT-6 Cyber. So they launched
[18:38] this
[18:39] five days ago.
[18:41] And this one is specifically tuned for
[18:46] finding vulnerabilities. Uh so I think
[18:49] you know maybe your here would be to
[18:52] encourage people to use this model, run
[18:55] this model, particularly
[18:57] to find vulnerabilities, kind of
[18:59] fighting fire with fire here.
[19:01] Um but you know lots of
[19:03] lots of software is getting hacked by
[19:06] LLMs um being good at finding finding
[19:10] those things. So the goal here would be
[19:11] that GPT-6 Cyber is ahead of
[19:15] you know the frontier ones
[19:17] on cybersecurity tasks uh and also
[19:20] presumably has different uh guard rails
[19:23] in place.
[19:24] Um the thing I don't know is how do you
[19:26] get access to it? Uh see
[19:34] So how do you get detecting misuse,
[19:37] blocking high risk, blah blah blah?
[19:40] Okay. So GPT-6 Cyber is initially
[19:42] available through the API and codex to a
[19:43] select group of approved Daybreak Red
[19:45] customers.
[19:47] All right. So yeah so as I would imagine
[19:49] that not you can't just give this access
[19:53] to anyone.
[19:54] Um but it looks like you can apply for
[19:57] Daybreak.
[19:59] And um
[20:02] get access to it. So Daybreak
[20:04] Blue defensive work, Daybreak Red
[20:06] advanced red teaming. All right. So
[20:07] that's probably has more of the guard
[20:09] rails turned off so you can do more
[20:11] stuff.
[20:14] All right. That's cool. What I'm curious
[20:17] if any of you are working with those
[20:18] with Daybreak Red, if you've got a loud
[20:21] for that.
[20:23] Let's see. There was lots of
[20:24] acquisitions last week. So, uh some
[20:27] folks uh like I know the folks at
[20:29] Pierre, they basically are the same
[20:31] people who created Twitter Bootstrap.
[20:33] Any of you have ever made a front-end
[20:34] website using Twitter Bootstrap, they
[20:36] went on to create the Pierre computer
[20:38] company.
[20:39] And they they were doing a lot around
[20:41] like code review, code storage, kind of
[20:44] diffs and stuff like that. And so OpenAI
[20:47] has acquired Pierre for integration into
[20:50] Codex.
[20:51] Um so that's good. It's a I mean it's
[20:55] they are fantastic developers, you know,
[20:57] some of the best developers at that are
[20:59] at that company. So,
[21:01] they're now at OpenAI. Um
[21:04] Meta acquired conductor. So, conductor
[21:07] is like for parallel agents. Uh so Meta
[21:10] just acquired conductor. So, that's
[21:12] presumably going to help
[21:14] Meta with their
[21:17] they have a coding agent now, I guess.
[21:18] They must have a coding agent.
[21:21] Um
[21:23] presumably.
[21:25] Meta Meta coding agent. Is it like Muse
[21:28] Code or something?
[21:30] Um yeah, Muse Code. That's correct.
[21:32] Okay.
[21:34] So, you know, maybe Meta is going more
[21:36] into the space of uh of coding agents.
[21:40] Oh yeah, there you go. 200 bucks a
[21:43] month.
[21:44] All right. So, that's going to help them
[21:46] out.
[21:48] Uh and then Human Layer joins Factory.
[21:50] That's their someone working on Software
[21:52] Factories, right? And Software Factories
[21:54] are like
[21:56] the big thing now. Um
[21:58] so there you go. A bunch of
[22:00] acquisitions.
[22:02] Bernard says, I hope the Daybreak Red
[22:04] customers don't raid the supermarket
[22:05] freezers again like they did last week.
[22:07] I heard about that.
[22:09] Uh supermarket freezer yeah, fridge
[22:12] hack.
[22:14] Uh
[22:16] so it was like all these supermarkets,
[22:19] all the here we go. Okay.
[22:24] Set That's horrible. So, they set the
[22:26] fridges to
[22:27] they hacked into the fridges, right?
[22:29] They found some really easy in.
[22:32] And they set them to defrost mode.
[22:36] And they lost tens of millions of euros
[22:38] of food. That's just that's just so
[22:41] horrible. Okay, it's because the login
[22:43] credentials were admin.
[22:44] And the current date was the password.
[22:46] Yeah, okay.
[22:51] But that's just that's just cruel. Like
[22:53] just
[22:56] It's just a waste. Like
[22:58] absolutely no respect for the
[23:00] environment there.
[23:01] And blood supplies in hospitals, jeez.
[23:05] Yeah, right now I'm reading this book,
[23:06] The Infinity Machine, which is about the
[23:10] creation of DeepMind.
[23:12] And one thing that DeepMind did at one
[23:14] point was try to work with the NHS in
[23:17] Britain
[23:18] in order to, you know, improve
[23:21] healthcare. And they had like this app
[23:24] that everybody was using
[23:26] or not everybody, but a lot of people
[23:27] were using in the hospitals and try to
[23:28] streamline things and they wanted to,
[23:30] you know, try and help, but then it all
[23:33] it all fell apart and there was this big
[23:35] backlash against having
[23:37] you know, big tech inside
[23:40] you know, inside the healthcare system.
[23:42] And it's an interesting debate like
[23:45] because in some ways obviously
[23:46] technology could streamline health by a
[23:48] lot, right? Like doctors don't want to
[23:50] spend all their time, you know, faxing
[23:52] things around, like using these
[23:54] antiquated technology to take
[23:56] track of things, but also obviously
[23:58] there's a lot of, you know, patient
[24:00] privacy to keep in mind as well.
[24:03] So you know, that's the thing with
[24:05] technology when deployed when deployed
[24:07] well, it can
[24:10] you know, help people,
[24:12] but it has to be, you know, have to
[24:13] really think a lot about security and
[24:15] privacy.
[24:18] Oh, they want to rename this.
[24:22] Let's see what else.
[24:26] I gave a talk last week about the impact
[24:29] of AI on CS curriculum. Um, I don't know
[24:31] if any of you are teaching
[24:34] at the K-12 or college level, but
[24:37] there's some slides about that there.
[24:40] Um, just trying to explain to teachers
[24:42] the, you know, the current state
[24:44] of software engineering
[24:46] and how it's been taken over by AI.
[24:48] Like, you know, we have these numbers
[24:50] here, right? Like, 70% of new code at
[24:52] Google is written by AI, 40% of code
[24:55] changes are started by agents,
[24:57] more than half of engineers are, you
[24:59] know, doing most of their work with AI.
[25:01] So, you know, the obviously AI is now
[25:04] the norm for coding.
[25:07] Um, so, you know, given that,
[25:10] uh, you know, what is the next step for
[25:13] software engineering, right? Because
[25:14] we're not we're no longer the writing
[25:16] code. We're increasingly, you know, not
[25:18] necessarily reading the code.
[25:20] Um,
[25:22] but there's still a lot of
[25:24] you know, a lot of aspects of software
[25:26] engineering life cycle
[25:28] where humans are very helpful, um, and
[25:32] where agents, you know, can't fully take
[25:34] over yet, right? So,
[25:36] here, like this is my thesis is that
[25:39] this is where we're currently at, where
[25:40] agents are mostly, you know, writing the
[25:42] code and writing the tests,
[25:44] um, but both both humans and agents are
[25:46] reviewing the work,
[25:47] shipping it, scaling it, um,
[25:50] and then humans are, you know, doing the
[25:52] problem design and the spec and and
[25:54] managing the agents, right?
[25:57] Um, the thing we don't know is what this
[25:59] is going to look like a year from now, 5
[26:01] years from now, right? We're in a very
[26:04] rapid very rapid pace right now. Um, and
[26:08] of course the teachers are trying to
[26:10] figure out what should they be teaching
[26:12] kids, you know, that are going to be in
[26:13] the industry like
[26:15] 8 year 10 years from now, right?
[26:18] And it's so hard to say because this is
[26:21] the fastest anything has ever moved,
[26:23] right?
[26:24] What do I think about learning coding?
[26:26] Do you try to learn Python still? I
[26:28] still say that you should learn one
[26:31] language right now.
[26:33] Uh before we had a big emphasis on, you
[26:34] know, learning lots of languages, but I
[26:36] think right now if you learn one
[26:37] language and learn it well enough to get
[26:41] the idea of, you know,
[26:43] what is a programming language, what
[26:45] kind of paradigms it has.
[26:47] Um
[26:49] uh I wouldn't like that that's the thing
[26:51] I would like, you know, cuz cuz then I
[26:52] propose like, you know,
[26:54] um yeah, and actually this is what I
[26:56] think is more important is understanding
[26:58] testing cuz a lot of times people kind
[27:00] of skip over
[27:02] you know, they skip over testing and
[27:03] they don't put as much emphasis on it,
[27:05] but now that's the most important thing
[27:07] because if you understand how to verify
[27:09] software,
[27:11] uh then, you know, then you can let
[27:13] agents loose on it, right? So
[27:16] uh in some ways I think this is uh more
[27:18] important is understanding the different
[27:19] kinds of testing, right? So this is
[27:21] what's called the testing trophy. And
[27:23] the testing trophy, you've got these,
[27:25] you know, end-to-end tests um that
[27:27] really check the whole user flow and to
[27:29] me those are actually the most important
[27:30] now because everything else could
[27:32] change, right? You might change your
[27:33] entire like you might say, oh, we're
[27:35] going to port from Python to Rust or
[27:36] something, right? And in that case like
[27:38] all of this code changes,
[27:40] uh but your end-to-end test should still
[27:42] be the same, right? We can still verify
[27:44] the user can start here, end here, and
[27:45] it still works.
[27:47] Um but then there's other kinds of tests
[27:49] like property-based testing, fuzz
[27:51] testing, those are very similar and and
[27:53] those are really important now, uh
[27:54] especially for like APIs should always
[27:56] have this, uh security tests,
[27:58] performance tests, very important. And
[28:01] then uh I just saw today more people are
[28:03] experimenting with formal proofs, right?
[28:05] So they just said they're using
[28:07] formal proofs on the MCP SDKs in order
[28:11] to look for bugs and they're finding
[28:12] bugs that way. Um and traditionally
[28:15] formal proofs were like something almost
[28:17] nobody did because it was this kind of
[28:19] obscure skill. Like I happened to learn
[28:21] it once at summer camp in eighth grade.
[28:24] And I will say it wasn't the most
[28:25] exciting summer camp
[28:27] cuz we spent all summer writing proofs.
[28:29] Um
[28:31] uh uh but um you know, I think most
[28:33] people necessarily learned how to write
[28:35] proofs and you ask me to write one right
[28:37] now I wouldn't be able to do it. So
[28:39] um but if you want to guarantee
[28:40] correctness that's like the only way,
[28:41] right?
[28:43] Um so I I think this is actually the
[28:45] more important part. I'd say like okay
[28:46] for this particular application
[28:48] you know do what is your verification
[28:51] look like, right? Cuz if you feel like
[28:53] you've got everything fully verified
[28:55] then you know coding agents can
[28:59] go wild with it. Um but if not then you
[29:01] know you're going to have to
[29:02] increasingly be involved and have much
[29:04] more manual QA which can just get really
[29:06] frustrating and boring.
[29:10] Um
[29:11] so yeah and I think what's increasingly
[29:13] important is you do need to understand
[29:15] how things work behind the scenes both
[29:16] like the basics of computers but also
[29:18] now with AI and LLM models
[29:21] um product judgment that's more
[29:24] subjective working with people still
[29:25] good.
[29:26] Um but for learning coding
[29:30] um you know I don't necessarily think
[29:32] that's the most important thing, right?
[29:34] I think it's more important for
[29:37] uh people you know to focus on the
[29:38] verification, the usability testing, um
[29:43] you know all of that stuff. Uh so
[29:47] yeah I think if you're deciding right
[29:48] now like it's still useful to be
[29:51] learning at least one language um
[29:54] because I think it helps you understand
[29:56] how computers work um
[29:59] but you you know you don't need to be
[30:00] memorizing syntax anymore. You should be
[30:02] able to read the code, right? Like even
[30:05] my most recent interview for this job I
[30:07] didn't write
[30:08] I I wrote like one bit of code but I
[30:10] mostly was reading code and explaining
[30:11] what it did, right? So if you can read
[30:14] code and explain what it did that is the
[30:17] main
[30:18] um you know thing right now
[30:21] and being able to write it and certainly
[30:23] memorize syntax is just not not that
[30:26] important anymore
[30:29] sadly.
[30:32] Um
[30:35] yeah uh let's see what else. Okay.
[30:39] All right. So yeah, you can look through
[30:41] that if you're curious what else I did.
[30:44] Um,
[30:47] what else is going on? Uh, I thought
[30:49] this was good is that secret scanning
[30:50] detect secrets and GitHub actions
[30:52] workflow logs. I feel like that's where
[30:53] a lot of people have found secrets. So
[30:56] um, you know, make sure you are enabling
[30:59] all the different options. Uh, so here
[31:02] you can say you can enable it by
[31:03] selecting policies,
[31:05] advanced security. That's underneath
[31:07] there. So that's good.
[31:10] You got to be really secure these days.
[31:13] Um,
[31:14] let's see there's some APIs for Copilot
[31:16] code reviews so you can
[31:18] you can control that a lot more.
[31:21] Uh, GBD 4.0 is for real retired. I feel
[31:24] like it was already retired, but let's
[31:25] see.
[31:26] Um,
[31:28] uh, we always call it GBD 4 no cuz we
[31:31] really you know don't want people to be
[31:33] uh, using it anymore.
[31:35] Um,
[31:37] so uh,
[31:39] yeah, I think it's for real retired now.
[31:42] Uh, so you should be long moving on from
[31:44] that. That was years ago.
[31:49] Uh,
[31:51] GitHub and Slack and Teams is generally
[31:53] available.
[31:54] Um, this is definitely something you
[31:56] should try out for you know basically
[31:58] having a GitHub agent
[32:01] uh, you know just in your in your Teams
[32:04] channel or in your Slack channel.
[32:07] Um, it it should we first tried it out
[32:10] here a couple months ago when it was
[32:11] kind of an alpha. Now it should be uh, a
[32:15] lot more slick, right? So you can
[32:17] basically let me see if I can still find
[32:19] my
[32:21] my uh, channel for it.
[32:25] Go.
[32:27] Okay, so this is one
[32:29] right where I like made a channel
[32:33] and you know made the channel said hi to
[32:36] GitHub
[32:37] and then you know you set the channel
[32:39] default repository
[32:42] and basically associate and say, okay,
[32:44] this channel is with this repo.
[32:47] And then you can add GitHub.
[32:49] And this was early days where I was kind
[32:51] of struggling a little bit cuz this is
[32:53] what like back in September looks like.
[32:59] So I encourage you to try it now cuz it
[33:02] should be even slicker now.
[33:06] And you can do the same thing in Slack.
[33:13] All right, what else?
[33:17] On the industry side, let's see. Okay,
[33:19] Python Okay, you should all be dropping
[33:21] Python 3.10.
[33:23] If you go to python.org,
[33:27] you can look at and see
[33:30] that if you look at this, you can see
[33:31] that Python 3.10 is now considered end
[33:34] of life.
[33:35] So if you haven't yet dropped it, it's
[33:38] time to drop it cuz it's not receiving
[33:40] security updates anymore.
[33:42] Python 3.11 we will have, you know,
[33:44] until next October.
[33:46] So
[33:48] yeah, all of your stuff should be at
[33:49] Python 3.11. Now, unfortunately, I have
[33:51] like a lot of ones that are not that are
[33:54] all like at Python 3.10.
[33:57] And so
[33:59] I had it go and open up,
[34:02] you know, open up PRs on
[34:05] on a bunch of repos here. So that's
[34:07] another use of like projects. If you
[34:10] haven't tried projects in the
[34:12] I made like a project around upgrading
[34:14] and so then
[34:16] when I have time, I can go through and
[34:18] see like, oh okay, what did it do?
[34:20] Right, you know, set the the minimum
[34:22] versions here. Oh, this was on 3.9.
[34:23] That's rough.
[34:26] We got some improvements on the typing
[34:28] side, right? And it changes the
[34:30] pyproject.toml.
[34:31] So this is the kind of updates you would
[34:33] expect to do if you're changing from
[34:35] Python 3.10 to Python 3.11
[34:39] is changing your pyproject, changing
[34:41] your CI matrix, and you might get some
[34:44] typing upgrades.
[34:47] Uh, but you know, you can just ask your
[34:48] friendly coding agent
[34:50] to do that for you.
[34:54] And then I guess I should just merge it.
[34:55] It looks pretty good actually.
[34:57] Okay, merge.
[35:05] All right, what else? Uh,
[35:10] OpenAI images got better. I don't use
[35:12] OpenAI images cuz I use MAI images,
[35:14] which confusingly is the same version
[35:16] number. So, there's OpenAI images 2.6
[35:19] and then there's MAI
[35:21] image 2.6 and as far as I know, they are
[35:24] two different models. They just happen
[35:26] to currently be at the same number. Um,
[35:29] they both seem pretty good.
[35:31] Uh, Gemini makes videos. I haven't used
[35:33] any of the video editing stuff yet. Um,
[35:35] I just use Opus and have it do graphic
[35:37] design and it's great at it.
[35:39] Uh, let's see. There was some research
[35:41] into uh hallucination of MCP servers.
[35:44] That was interesting. And then some
[35:46] other research that showed that, you
[35:48] know, agents like half their tokens were
[35:50] just not useful.
[35:53] And that is what I have for this week.
[35:55] Does anyone have any other questions or
[35:58] news that they want to share?
[36:08] Otherwise, maybe it's a quiet week this
[36:11] week. Um, there'll be certainly uh well,
[36:14] I won't have office hours next week.
[36:16] Okay, you have a Yeah, question?
[36:18] Um, there won't be offices next office
[36:20] hours next week since it'll be Ignite
[36:22] and uh that'll probably be I think
[36:24] during the Ignite keynotes actually. So,
[36:26] hopefully you'll be watching the Ignite
[36:27] keynotes.
[36:29] Um,
[36:31] and let's see. We won't have office
[36:32] hours the week after that cuz that's
[36:33] Thanksgiving week.
[36:36] We should have it the week after that.
[36:38] So, there'll be lots of really cool
[36:40] stuff coming out
[36:42] uh Ignite.
[36:46] Pablo says I have. Pablo, did you have a
[36:48] question? Maybe you're typing.
[36:51] Let's see.
[36:53] Let's see.
[36:55] Oh, okay, good, Pablo. All right.
[36:58] Um
[37:00] so Pablo's question is about Microsoft
[37:02] IQ. The more clean information an agent
[37:05] has, the better connect the dots.
[37:06] Connecting the dots is what makes
[37:07] intelligent.
[37:09] If the agent answered to users according
[37:11] to the rights user have, the agent has
[37:12] the same scope.
[37:14] Um
[37:16] how can Microsoft
[37:17] if the
[37:19] how can Microsoft IQ answer as well if
[37:22] the data the agent has access to depends
[37:25] on the user asking the question?
[37:28] My impression is that the company-wide
[37:29] knowledge graph and the agent-limited
[37:30] user information are not designed to
[37:32] work together.
[37:34] Um okay, so you said the agent So you
[37:37] could give the agent more access than
[37:39] the user. Um it depends on how you're
[37:41] you're setting up the agent. Um I think
[37:43] we call it agent with identity
[37:49] A365. I think that's the current term
[37:52] for it now.
[37:54] Um
[37:57] is this it? Yeah, I think this is it. So
[38:00] depending when you talk about agent,
[38:02] right? So an agent can either literally
[38:04] like you know, the user can log in to
[38:07] the agent and the user is just the agent
[38:09] is really just using the user's token to
[38:11] do stuff, in which case it's only going
[38:12] to have access to
[38:14] what the user has access to. So if it
[38:16] was like work IQ, then it would you
[38:18] know, the agent you know, work IQ is
[38:20] basically doing a bunch of Microsoft 365
[38:22] calls behind the scenes. So the agent be
[38:24] able to do all those Microsoft 365
[38:26] calls. Um the benefit of the agent is
[38:29] that you know, it can do like a lot more
[38:31] calls than a person would reasonably do.
[38:33] Like it's very good at you know,
[38:34] searching because it's you know, it's
[38:37] it's got kind of infinite patience where
[38:38] it's like, sure, I'll I'll do you know,
[38:41] a bunch of bunch of searches in order to
[38:43] find this answer.
[38:45] Um but yeah, ultimately
[38:47] if an agent is, you know, being
[38:51] authenticated using the user's token,
[38:53] then that agent is only going to be able
[38:55] to use that user token
[38:57] for, you know, on on behalf of for the
[38:59] on behalf of flows. However, you can
[39:01] also make an agent with an identity. And
[39:03] if you give it an identity,
[39:05] then, you know, you're you can give that
[39:09] agent different permissions, right? Um
[39:11] and you can decide
[39:13] uh you know, what what has access to,
[39:16] right? Oh, so here you have kind of
[39:17] example, right? So there's service to
[39:19] service. Okay, this is the one we've
[39:21] been showing more of, right? So on
[39:23] behalf of means, yeah, you're only going
[39:24] to be able to
[39:26] um access as much as that user has, and
[39:29] that's on behalf of.
[39:30] Um but the one that people are excited
[39:32] about is this one where the agent runs
[39:34] with its own Mark soft Ontra user
[39:35] account
[39:36] um and there the agent gets its own um
[39:39] you know, its own mailbox. So there what
[39:42] you would do is you'd put agent like
[39:44] you'd put the agent in the same Ontra
[39:45] group, right? Like you basically think
[39:48] like, okay, this agent is its own
[39:50] person. If I wanted this agent to have
[39:52] access to things
[39:54] um
[39:56] you know, what what sort of permissions
[39:57] would I need to give it?
[40:00] Um
[40:02] so that would, you know, that enhances
[40:04] the amount that it can do because it can
[40:07] see more.
[40:08] Uh but then of course, you know, you you
[40:10] want to be careful about giving it
[40:12] access to too much. Like you need to be
[40:13] comfortable.
[40:15] Uh but that's also why you have the
[40:16] governance here where you would, you
[40:18] know, you would
[40:19] be able to monitor
[40:21] uh what permissions they have, right? Uh
[40:24] so you have you can do you make this
[40:26] like agent blueprint
[40:28] which has their permissions and then
[40:29] people can like add that agent
[40:33] um
[40:33] like a new instance of that agent.
[40:37] Uh
[40:38] so
[40:40] so yeah, I would consider that that you
[40:41] may want to use this. Uh that's
[40:43] increasingly what a lot of my
[40:46] colleagues are doing
[40:47] in order to make more powerful agents.
[40:51] Pablo says that agent cannot be used by
[40:52] anyone. You should be able to
[40:55] you publish your agent and put it in the
[40:57] admin center and then people can
[41:00] This requires some degree of um you know
[41:03] administration.
[41:04] Um but then other people can actually
[41:07] uh
[41:08] create instances of it. Configure agent.
[41:11] Test agent team
[41:14] search for a new agent user.
[41:18] Cuz my colleague just made an agent last
[41:20] week and he was like, oh, I got this
[41:21] approved. So you're all going to be able
[41:23] to add this agent like an instance of
[41:25] that agents as well.
[41:28] So as I understand it,
[41:32] once you do this process, other folks it
[41:35] you know, depending on whether it's been
[41:36] approved, other folks should be able to
[41:37] add it as well.
[41:46] Um
[41:48] do do do. So let's see.
[41:51] The holiday
[41:53] If a company has a known out this agent
[41:55] can access then what do the rest people
[41:57] get? Yeah, so in this case the the idea
[41:59] is that other people should be able to
[42:02] also use the agent once it's set up.
[42:07] Do do do do.
[42:11] I don't know if you've uh messed around
[42:13] with this yet.
[42:19] Yeah, you create register an agent
[42:21] create agent identities from it.
[42:25] Uh
[42:27] so if Pablo says only a few months ago
[42:29] both Microsoft and Google talk Microsoft
[42:31] and Google talk anything at all about
[42:32] graphs, nouns, the main argument to have
[42:33] intelligence custody.
[42:35] Uh next year both companies will talk
[42:37] about the known all expert agent. Well,
[42:39] we are talking more about this now
[42:41] because the advantage of an agentic user
[42:44] is that it's more able to you know, it's
[42:47] it's got more capabilities, right? It's
[42:49] And also it's like better attribution,
[42:51] right? When you you know, it's very
[42:52] clear when the agent has its own
[42:54] identity that oh the email came from
[42:56] that agent, right? When we do this thing
[42:58] where agents are acting on our behalf
[43:00] and then they like post, you know, like
[43:02] when I posted the VS code issue, really
[43:04] it was co-pilot posting that and I told
[43:06] it like well make it clear that it's
[43:08] you, right? So
[43:10] it kind of leads to less trust because
[43:13] we don't know which of the things that
[43:14] we see coming out of our, you know,
[43:16] colleagues are actually from them or
[43:18] from agents that are acting on their
[43:19] behalf. So I also think just the agentic
[43:22] user is better in terms of
[43:24] um you know, building building a better
[43:27] trust model for saying like okay yeah
[43:30] this you know, this this came from this
[43:33] agent, right? It didn't come from a
[43:36] human it came from the agent and also it
[43:37] just enables the agent to do much more
[43:39] background work, right? So if the agent
[43:41] has its own identity it is not waiting
[43:43] for like token refresh and consent flows
[43:46] and that sort of thing. It's you know,
[43:48] it's got its own identity and it's able
[43:51] to act regardless of whether the user is
[43:53] there um
[43:56] uh so you know, so it's just more
[43:58] capable. So I think that is why you're
[43:59] seeing more of the demos that are using
[44:03] this agentic user approach instead.
[44:08] Um yeah okay and now we're getting the
[44:10] graph questions of course. Um
[44:13] so we talk a lot about vector databases
[44:15] right but tech giants are heavily
[44:16] pushing knowledge graphs now in
[44:17] production is graph fragmenting
[44:19] completely replace vector databases or
[44:21] are they implemented as a hybrid system?
[44:24] Um yeah that's a good question and
[44:26] that's one of the
[44:28] tricky things is that um you know,
[44:30] graphs can
[44:33] a a knowledge graph, right? There's
[44:34] different kinds of knowledge graphs so
[44:36] um
[44:37] like even within graph rag there's
[44:39] there's multiple kinds of knowledge
[44:40] graphs.
[44:41] Uh so but you know, in the knowledge
[44:43] graphs like for example you can have
[44:45] like
[44:46] a knowledge graph which is like entity
[44:47] and relationship, right? And you're like
[44:49] you know, you extract from all your data
[44:50] like this person did this thing in this
[44:52] location, right? You this
[44:54] subject, predicate object.
[44:57] Um, and so you can develop that graph
[44:59] and that graph can help answer questions
[45:01] better about connectivity between things
[45:04] in your data set, right?
[45:06] Um,
[45:08] so it it can it's really good for for
[45:10] those questions. And then there's other
[45:12] kind of graphs which are like more like
[45:14] kind of clustering clustering the
[45:16] information in a in a knowledge base to
[45:19] say like, oh, okay, we've got this graph
[45:21] of all the topics covered by this
[45:24] database and we can kind of zoom in and
[45:26] zoom out on this graph and and, you
[45:28] know, look at the different clusters of
[45:30] information and that helps you answer a
[45:32] completely different kind of question
[45:33] like a like a more zoomed out question
[45:35] like, oh, you know, generally like what
[45:37] are the, you know, kinds of um issues
[45:40] that we're seeing uh across the whole
[45:42] knowledge base, right? Um,
[45:45] so both of those help you to answer
[45:48] different kinds of questions.
[45:50] Then your question is do you can you
[45:53] completely get rid of um vector
[45:55] databases? And I would say no. I think
[45:58] both of those searches you actually want
[45:59] to do um in conjunction with a with a
[46:02] vector search there just to just to get
[46:04] your best results. And and that there's
[46:08] definitely a rely reliance on some
[46:09] vector uh math there. Um, but also I
[46:12] think there's still some questions that
[46:15] you don't necessarily want to answer
[46:16] using the entity graph or, you know,
[46:19] like a topic cluster graph. Um, so then
[46:22] you have the question of, you know, when
[46:23] do you do you, you know, do you try it
[46:25] with all all three different approaches
[46:27] at once? Do you use a router that routes
[46:29] between the different approaches?
[46:31] Um, and, you know, those are all
[46:33] different options. So
[46:36] you should come to Ignite or you should
[46:38] watch Ignite talks because we will um we
[46:41] will be talking about graph
[46:43] um at Ignite. Um, if you look at uh
[46:47] let me see. I don't see I was checking
[46:48] to see if they updated my
[46:51] No, they didn't update it yet. All
[46:52] right.
[46:53] The lab is going to get updated soon to
[46:55] mention the word graph. And then there
[46:57] is another one that already mentions the
[46:59] word graph. Um, here we go. There we go,
[47:03] this one.
[47:04] So, um, Pablo, I think you'll be
[47:07] very interested in this one.
[47:11] Uh, du du du.
[47:15] Knowledge graphs for better enterprise
[47:16] context. So that's that session will go
[47:20] a bit into it.
[47:25] Uh,
[47:26] oh, SharePoint agents and knowledge bot.
[47:29] Um,
[47:30] yeah, for SharePoint, um, I'm actually
[47:32] working on SharePoint today. Um, you
[47:35] have two options basically. One is to
[47:37] use Work IQ. Uh, you kind of have three
[47:39] options, right? You've got Work IQ,
[47:41] which would be on behalf of
[47:43] and, you know, it can access it should
[47:45] be able to access SharePoint docs.
[47:47] Um,
[47:49] but then you need the on behalf of flow.
[47:51] You've got the uh, let's call it Copilot
[47:53] Semantic Retrieval
[47:57] API
[47:59] Index.
[48:00] I think that Okay, this is it. The
[48:02] Microsoft 365 Copilot Retrieval API.
[48:06] That is
[48:09] another current option for SharePoint
[48:12] as well.
[48:14] Um,
[48:15] that you can try out.
[48:18] And your third option would be
[48:24] the um, SharePoint Indexer
[48:30] for
[48:33] du du du
[48:36] for Azure AI Search. Um, it says preview
[48:39] right now, but it's going to be GA
[48:41] very very soon.
[48:47] So that's what I would look into is Work
[48:49] IQ, Copilot Retrieval API,
[48:52] and SharePoint Indexer. Uh, just depends
[48:54] like kind of
[48:56] freshness and stuff like that and user
[48:59] and like of which SharePoint features
[49:00] you're using.
[49:08] I see.
[49:13] Are there also the types of AI agents?
[49:18] From a Neo for J printer combined hybrid
[49:19] and non-d is covers cases where
[49:23] semantic search meaning keyword search
[49:25] needed to get specific legal
[49:26] information.
[49:28] Yeah, Neo for J has quite a lot of
[49:30] talks about about this as well.
[49:36] Uh I I think our current experience is
[49:39] that you need a mix of the different
[49:41] kinds of searches and so you have to
[49:43] either run them in parallel
[49:45] or and or use a router.
[49:49] How does a chatbot go through this graph
[49:51] related work? How do they perform a rag
[49:52] systems? I mean, it just depends on the
[49:54] chatbot, but you know, many people in
[49:57] order to connect a chatbot to knowledge,
[49:59] they make an MSP endpoint that has the
[50:02] knowledge, right? So if you're using
[50:04] Azure AI search founder IQ, then it
[50:06] already has an MSP endpoint.
[50:08] Um
[50:09] otherwise, you know, you can make an MSP
[50:12] server or expose those tools.
[50:25] All right.
[50:28] Oh yeah, and I I guess related to that.
[50:29] I think I already shared this one
[50:31] before, but this was the
[50:34] yeah, how how we used founder IQ to
[50:36] build a knowledge base for GitHub
[50:38] Copilot, right? So if GitHub Copilot is
[50:40] your chatbot,
[50:41] you know, then that would be
[50:44] um the way to connect it.
[50:48] Send that right MCP
[50:51] and then
[50:57] right? So you like here we saying okay,
[51:00] agent, you can go send queries to this
[51:02] this knowledge base, you get back
[51:04] results,
[51:05] and then
[51:07] you know, and the agent can answer it
[51:08] access it, right?
[51:13] How do they perform swig tasks if I
[51:15] wanted to?
[51:16] Um, I think you you might need
[51:18] you might want to do some um
[51:23] some uh uh you know, basically AI agents
[51:26] are using tool calling
[51:29] um in order to call tools. There's
[51:32] some videos here about uh how AI models
[51:35] work and there's stuff at the end about
[51:37] agents and speed and tool calls and all
[51:39] that stuff.
[51:41] All right.
[51:43] Okay, now we are at time. Uh thank you
[51:46] everyone for coming by and for the great
[51:48] questions.
[51:50] Uh as usual, I'll post the recording in
[51:54] the thread with all of the um all the
[51:58] Q&A
[52:00] here.
[52:03] And I will see you in a couple weeks.
[52:05] Make sure you watch the Ignite talks.
[52:08] They should be pretty good.
[52:11] Yeah, the recording will be posted in
[52:12] the link I just put.
[52:14] So you just reload that tomorrow and
[52:16] it's usually there by tomorrow.
[52:20] All right.
[52:22] Bye everyone. Have a good day.

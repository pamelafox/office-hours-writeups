[00:03] Hello. Hello everyone. I am going to try
[00:07] out spec kit today. Spec kit is a way of
[00:11] doing specd driven development std an
[00:15] acronym that I learned today.
[00:19] Uh but I have been asked about spec kit
[00:21] quite a lot. And you know once I get
[00:23] asked about something enough times I
[00:25] realize it is time to just dive in and
[00:28] try it myself.
[00:30] So that is the goal for today
[00:34] and here we go. Let's take a look and
[00:38] see what this spec kit is. All right. So
[00:40] spec driven development. We're going to
[00:42] start with a spec which becomes
[00:45] executable somehow.
[00:47] All right. Now, first we have to install
[00:50] the specify CLI.
[00:53] Okay, so it recommends doing that with
[00:55] UV using UV tool install.
[00:58] I'm not sure if I've actually even used
[00:59] that before. So, let's give that a go.
[01:04] Let's see.
[01:07] All right,
[01:09] let's try this UV tool install. Okay, so
[01:12] I've got UV in my global path and it
[01:16] looks like it did uh it did install it.
[01:19] Okay, so now we've got this specify
[01:20] executable and then we can
[01:26] uh we can start using it. So okay, it
[01:28] says create a new project. Okay.
[01:32] All right. Now the question is what is
[01:36] the project going to be? We'll just call
[01:39] it spec kit project for now. So we
[01:43] figure out what it is. And then it says
[01:45] to choose your AI assistant. Okay. Well,
[01:48] typically I use copilot. So we'll go
[01:50] with that. And script type is shell. All
[01:54] right. So it just did a bunch of things.
[01:57] It said initialize check required tool.
[02:01] Okay. So it was just setting up. says
[02:04] project ready and it says consider
[02:08] adding agitub to get ignore or uh to get
[02:11] ignored from accidental credentials.
[02:13] Normally I would not put GitHub in get
[02:16] ignore. Normally I would put like and
[02:18] get ignore. So that's a bit interesting.
[02:20] Uh then it says to go into product
[02:22] folder and then start using slash
[02:24] commands. So I assume this is the order.
[02:27] First we make a constitution.
[02:30] uh then we specify then we implement
[02:34] and or no then we plan we okay create
[02:37] the implication plan then we create the
[02:39] task and then finally we implement okay
[02:43] so I have used a process like this
[02:45] before just not with spec kit itself uh
[02:48] we can do spec kitclarify
[02:51] which we do before plan specitanalyze
[02:54] and spec kitchecklist okay all right so
[02:58] we're going to go into the
[03:01] and then say
[03:04] uh and then we do we just
[03:09] it says do slash. I don't think we would
[03:11] do slash, right? Um maybe it means we
[03:15] would [laughter]
[03:17] we would do
[03:20] we can't just do or maybe we do the
[03:22] project. All right, I'm sorry. I'm
[03:24] already confused. Okay, where would we
[03:27] run slash from? Maybe they mean we run
[03:29] the the slash from VS Code because it
[03:32] knows we're in VS Code. Is that perhaps
[03:34] that's what it means? Let's see if we
[03:36] get okay. Launch your AI assistant. The
[03:39] spec commands are available in the
[03:40] assistant. Okay. All right. I was
[03:43] missing that pit of information. So that
[03:45] means we are going to open this using uh
[03:47] VS Code. So let's go and open it using
[03:49] VS Code Insiders
[03:53] and open up this new project.
[03:56] Here we go. Okay,
[04:00] so now inside this project we have a
[04:03] bunch of agents. Okay, so these are all
[04:05] implemented as agents. So that makes
[04:07] sense. And we can actually look at each
[04:09] of them and see what they do. We can see
[04:13] some of them do have handoffs, which is
[04:15] interesting. That means they hand off to
[04:18] a sub agent. Uh so constitution is the
[04:21] first one and that one has a handoff to
[04:24] specify.
[04:26] All right.
[04:29] So, let's just see what happens.
[04:31] Specit.constitution.
[04:35] Well, this is an agent actually. So, we
[04:36] wouldn't usually do a slash. We would do
[04:39] here. So, in the agent menu,
[04:42] uh, so here in the agent menu,
[04:45] we can see all these. So, what if I just
[04:47] select constitution? Okay.
[04:51] And then
[04:54] what do I do? Okay. All right. Launch
[04:56] your AI assistant. Use the spec
[04:58] constitution to commit your project
[04:59] governing principles. This all sounds
[05:01] really formal but okay your project
[05:03] governing principles and development
[05:04] guidelines that was create guide all
[05:08] subsequent development. So it says
[05:09] create principles focus on code quality
[05:11] test and standings. Okay.
[05:15] Um I'm not sure I Okay. I was going to
[05:18] do I wanted to make something kind of
[05:19] fun. So, I'm not sure if I really need a
[05:22] constitution, but uh let's just see what
[05:25] happens if we just straight up. We don't
[05:28] even have to do the slash. We're just
[05:29] going to say this. It feels like these
[05:31] principles would be similar across
[05:35] products projects and I would just be
[05:37] copying them in. Like usually I have
[05:38] like my bicep best practices, Python
[05:41] best practices, etc.
[05:43] So, I don't necessarily want an LM to be
[05:48] writing those from scratch for every
[05:49] project.
[05:51] Uh, but, you know, let's see what it
[05:53] does. And there's the prompts.
[05:56] Uh, oh, I see. So, each of these, okay,
[05:59] each of these prompts, all it does is
[06:01] just trigger you into using an agent.
[06:03] Okay. So that's how they've been able to
[06:05] support slash in VS code is that each
[06:08] prompt is literally just saying this
[06:11] prompt uses that agent. That is very
[06:13] interesting. I haven't seen that before.
[06:16] All right. Then under dodge specify we
[06:17] have some memory. Ah so look here's a
[06:21] just like it looks like a raw uh just an
[06:24] example constitution.
[06:27] Uh we've got scripts. I think the these
[06:30] must have all been copied from
[06:33] uh you know brought down when we did the
[06:35] specify init.
[06:38] So we can see development guidelines
[06:40] that looks like an agents.mmd. We've got
[06:43] checklist template if we do a checklist
[06:45] the plan
[06:47] the spec user scenarios. Okay so the
[06:50] spec is user stories like similar to
[06:53] behavioral testing and then the tasks
[06:57] and then what's under VS code we just
[06:59] have some auto approve. Okay we're
[07:01] approving all bash. Oh, okay. Living on
[07:04] the wild side there. And then some
[07:07] prompt file recommendations in the chat.
[07:10] Welcome you. Interesting. Okay. So, it
[07:12] says constitution has been created at
[07:15] constitution.md.
[07:17] So, what are his core principles type?
[07:21] Okay. All right. Sure.
[07:24] I mean, this is all good. It's
[07:28] reasonable, but um you know
[07:29] [clears throat] saying I have my own
[07:31] best practices for my things that I' I
[07:33] would probably tell it to make the
[07:34] constitution based off of uh my my best
[07:39] practices. Uh but that's fine. Uh so you
[07:42] could if while you're doing it, you
[07:44] could point out any existing best
[07:45] practices or or just copy it in. Okay,
[07:49] so
[07:51] that's fine. Suggested ratify
[07:53] constitution. Why is it using such
[07:55] formal language? I guess also I'm not
[07:58] sure how great our constitution is
[08:00] working out right now in America so I'm
[08:02] a little burnt but uh yeah I mean in
[08:04] theory constitution is a good thing. Um
[08:06] I just don't know about this lang this
[08:07] this verbiage.
[08:09] Okay so we made a constitution uh which
[08:13] was pretty generic right now. Um now the
[08:15] important part is this specify. So build
[08:18] an application. Okay so this one's like
[08:19] a photo album. Okay great. This is the
[08:21] fun stuff. So I want to do actually
[08:23] something somewhat fun because
[08:26] um even though I don't think that this
[08:27] is necessary the best use for spec kit
[08:29] but I have been told you can use spec
[08:30] kit for fun and I have been told I need
[08:33] to do more vibe coding for fun. So we
[08:35] are going to do something fun. Uh so I
[08:39] want to build make an a static app that
[08:44] generates
[08:45] a charade de printable charades. The
[08:49] thing is, I want to play charades with
[08:50] my three-year-old and my six-year-old,
[08:52] and I need better charade cards so that
[08:54] they can follow the cards. So, I need
[08:57] words and I need images. I want to make
[08:59] that generates printable charade cards
[09:01] across different themes.
[09:04] Each like printable should be easy to
[09:08] cut into squares.
[09:11] Each card needs a word and a picture. I
[09:17] want the pictures to all be either
[09:21] emojis or public domain images from
[09:26] Wikipedia.
[09:28] Okay.
[09:30] All right. Let's see how it works.
[09:34] Hello. Hi everyone in the chat.
[09:37] Has anyone used spec kit before?
[09:40] All right. So it is
[09:43] checking our git status right now it
[09:46] looks like
[09:49] um
[09:51] and it's specifying it's following this
[09:53] prompt which is actually using this
[09:54] agent right so you can see this one has
[09:57] handoffs to creating a plan and
[10:00] clarifying spec requirements. Uh so
[10:02] these are like potential handoffs it can
[10:04] do which is when one agent hands off to
[10:06] another agent. Uh, so we have the user
[10:09] input.
[10:11] I don't it has this userment arguments.
[10:13] I don't know if VS Code actually like
[10:14] puts this in here or if this is just for
[10:18] show. Um, but basically
[10:22] it's okay. It's making a branch. Oh,
[10:23] that's why it was going through all that
[10:25] effort to understand. So, it really
[10:27] likes using git. That makes sense. Is
[10:29] from GitHub. So, I actually hadn't run I
[10:31] don't think did I run git in it? I don't
[10:33] know. But it made a branch uh or I think
[10:35] it's making a branch right now.
[10:38] and
[10:40] uh checking for existing branches. Oh,
[10:42] that's why it did all this. So, fetch
[10:44] all remote branches. Find the highest
[10:46] feature number. Okay. Determine the next
[10:49] available number. So, this is following
[10:51] a very structured branch name system
[10:56] where it's going to do like each feature
[10:58] one, two, three, four, five. Um,
[11:03] so that's interesting. So, it's going to
[11:05] make branches ordered with feature
[11:08] names. Uh, then it's going to
[11:14] uh do this template. Look at the spec
[11:16] template. Uh, and in the spec template,
[11:19] it's this shows all these like user
[11:22] scenarios. So, it's it's really it's
[11:25] doing everything with like user stories.
[11:27] So, this could work as user stories. And
[11:30] now this one is making Okay. And now
[11:32] it's making checklists. So maybe it it
[11:34] moved on already to okay spec written.
[11:38] So it made the spec. It did quite a bit
[11:41] here. Okay. So it made the fe future
[11:43] branch. So I think if we will go to our
[11:46] terminal and check the branch. I assume
[11:50] we're in a branch now. Let's see. Get
[11:52] status.
[11:55] And yeah 001 charade cards. So it
[11:59] numbered the branch at one. And there we
[12:02] go. So it created the branch. Now it
[12:04] write wrote a spec
[12:07] and
[12:08] made a bunch of user stories. Selects a
[12:10] theme generates a printable page
[12:13] acceptance and when they select okay
[12:15] yeah this I don't know if any of you
[12:16] have ever done this style of um user
[12:19] testing. I think I did it with copy bar
[12:21] with Rails apps I believe. So you start
[12:23] with given when and then given when then
[12:28] and you write out all your user stories
[12:30] with um given when and then. So we did
[12:34] the spec.mmd
[12:36] and then the next thing it wanted to do
[12:40] uh let's see because right now we are on
[12:43] specify so if we look back at the actual
[12:46] the actual agent
[12:48] uh it created the spec and now it's
[12:50] doing the specification quality
[12:52] validation. So generates a checklist
[12:54] file
[12:56] h using the checklist template structure
[12:59] and for each feature
[13:02] it has a checklist for whether it's
[13:05] ready
[13:07] and then review the spec against each
[13:10] checklist for each item per pass or
[13:12] fails. Okay.
[13:14] Okay.
[13:17] Interesting. All right.
[13:19] So it's like writing tests against your
[13:21] spec, but you don't have no code yet.
[13:24] Very interesting. All right. Making for
[13:28] AI. Okay. All right. So, uh let's see.
[13:31] It made the spec. Now it wants to create
[13:32] the checklist directory. So we'll just
[13:34] allow it to make that directory.
[13:37] Um so that's under specs.
[13:41] So we have the specs checklist.
[13:45] Interesting. And so it even made a
[13:47] bolder name based off the branch. So I
[13:50] guess we're going to keep our progress
[13:54] as we go. Uh so here's our requirements
[13:57] MD. Uh so no content quality. I don't
[14:02] quite understand what this is. Purpose
[14:03] validate specification completements.
[14:07] I I guess this is just a way of forcing
[14:09] the LM to go through each of these boxes
[14:12] and say okay there's no invitation. It's
[14:14] focused on user value. Everything's
[14:17] measurable. Feature readiness. Okay. So,
[14:20] this is just a way of getting the LM to
[14:23] confirm that the spec meets all the
[14:27] requirements it put here.
[14:30] Notes.
[14:34] Okay. All right.
[14:37] Great. Oh, and look at this. This is
[14:38] cute. Um when you if you notice this
[14:41] right here proceed from spec kit.sp
[14:44] specify to either build technical plan
[14:47] or clarify spec requirements. So it
[14:50] knows I think that's because of the
[14:51] handoffs that it has in here that it
[14:54] knows those are the next possible Oh
[14:56] yeah. So that's the oh that's how hand
[14:58] I've never used handoffs before. So when
[15:00] you do an agent with handoffs it
[15:02] actually explicitly shows you what those
[15:04] next handoffs can be. Okay. So, let's
[15:07] look back at the readme and see what it
[15:09] says. So, it says the next thing you
[15:10] want to do is a plan.
[15:14] I'd also kind of thought we'd want to
[15:15] like look at our spec and see we agreed
[15:17] with it, but I don't know. It doesn't
[15:21] What is What is clarify? Right.
[15:23] Normally, when I'm doing this sort of
[15:25] PRD, I would
[15:27] um
[15:30] I would I would read it first and in,
[15:32] you know, ensure that I I like it. All
[15:34] right, let me just keep everything
[15:35] first. So we don't have the things
[15:38] system must generate a current must
[15:40] display one word one must support emoji
[15:43] must printable output must function as
[15:50] okay well looks good looks good all
[15:54] right now we're going to do plan so this
[15:56] time we're going to do text start okay
[15:58] uh text stack details okay so now since
[16:02] I want this to be a static app that can
[16:04] just run on GitHub pages because I don't
[16:05] want to maintain anything. Uh so let's
[16:08] see I can go and I can say build
[16:10] technical plan
[16:12] and create I am create a plan for the
[16:14] spec. Oh that's cute. So that came from
[16:17] I see. So when you do this then you can
[16:19] prompt it. Okay that's cool. uh create a
[16:22] plan for I am I am building with v uh
[16:26] vanilla HTML and uh web ele components
[16:33] templates when needed.
[16:37] I am not using react or any
[16:42] build system.
[16:45] Um
[16:47] there is no backend.
[16:50] though all cards must be premputed
[16:55] and stored in JSON.
[17:00] Um
[17:01] I I will deploy onto
[17:06] GitHub
[17:08] pages. All right.
[17:11] Uh use Bootstrap or CSS when
[17:17] needed.
[17:20] All right, let's see if it can obey my
[17:22] plan to only use vanilla HTML because I
[17:25] know that LLMs really like to use React
[17:28] and we're going to try
[17:31] not to use that. Um, I mean, when you're
[17:34] doing a static app, there's lots of you
[17:35] could use like a static app framework,
[17:38] static site generator. uh my personal
[17:40] website is actually built with Flask and
[17:43] then frozen flask in order to turn the
[17:45] the the flask into just HTML that I
[17:48] upload to GitHub pages.
[17:50] So there's many ways that you can
[17:53] ultimately generate a static site
[17:55] because you know it's all about your
[17:56] your how you build it. But here I don't
[17:59] even necessarily want there to be much
[18:00] of a build step at all. I just want I
[18:03] just want it to be easy peasy. Uh but
[18:07] you know, we'll see my dream.
[18:10] Uh so now it's coming up with plan MD
[18:14] and let's see. So the user wants me to
[18:16] create and so here let's take a look at
[18:19] this one. This is plan and it can go off
[18:22] to tasks and checklist. Uh so user input
[18:26] setup. Uh there is a script
[18:30] um which does some setup stuff. It loads
[18:34] the constitution.
[18:37] It
[18:40] generates research.m MD. Did it do that?
[18:43] Research.m MD.
[18:45] Oh, there we go. Phase zero. Generate
[18:47] research.m MD.
[18:50] Generate data modeld. Contracts and
[18:52] quick start.md.
[18:55] And then command ends after phase 2
[18:57] planning.
[18:59] So phase zero research research agents.
[19:05] Okay. And then consolidate findings in
[19:07] research.md.
[19:09] And then then you do data model
[19:12] um standard RS GraphQL patterns.
[19:15] [laughter]
[19:16] Okay. Well, wasn't going to use REST or
[19:18] GraphQL, but presum ignore that. I'm
[19:21] just going to use JSON.
[19:23] And uh then it's it has a script that it
[19:27] updates. Okay. And then so the ultimate
[19:31] outputs are going to be data model,
[19:32] contracts, quick start, and an agent
[19:34] specific file. Okay.
[19:37] All right. So it is doing
[19:41] a bunch of research
[19:43] here. Oh, and it's trying to figure out
[19:45] how to test it. That'll be really
[19:46] interesting to see how it decides to
[19:48] test it without using a build system.
[19:51] That'll be fun. Um,
[19:54] all right. We'll uh it's going to make a
[19:56] contracts directory. So, if it's already
[19:58] done contracts, that must mean
[19:59] research.md is complete.
[20:02] So, it says use a native web elements,
[20:05] use template elements. Uh, lit is
[20:08] actually the one that I use the most aft
[20:10] often. So, it's it's good um that I
[20:13] considered that uh implementation
[20:15] pattern. Great. This is what I wanted.
[20:18] Um,
[20:19] so I wonder how it will do with that.
[20:21] So, you can create like custom HTML
[20:23] elements.
[20:24] Then it's doing print CSS, which is
[20:26] good. Um, using CSS grid. I think that
[20:30] makes sense because we're literally
[20:31] making a grid. That's nice. Uh,
[20:35] Wikipedia common. So, it has an idea for
[20:37] how
[20:39] to
[20:41] uh how to gen get the images. That's
[20:44] good. That's a I guess it's a PHP API.
[20:48] We'll see if that's right. Uh, let's
[20:50] see. Bootstrap
[20:52] consider Tailwind. No, do not want that.
[20:56] Um, custom CSS more work. Bootstrap npm
[21:00] requires. Okay, so yeah, I figured out
[21:01] Bootstrap testing without build system
[21:04] use by test and play rate for end to end
[21:06] test. That's good. Um, I have used
[21:10] before. I have used mocha and I've used
[21:12] Cyprus.
[21:14] Good, very well thought out. This is how
[21:16] it'll look like. Um,
[21:20] and then we have ED testing. Now, you'll
[21:23] notice there's no Python in this. And
[21:24] normally, if you watch me, you know I do
[21:26] a lot of Python, but as it turns out, I
[21:28] actually do like JavaScript and used to
[21:30] do quite a lot of JavaScript. So, I'm
[21:32] okay with this being
[21:34] JavaScript heavy.
[21:37] And then, uh, let's see.
[21:41] It says we're going to use a service
[21:43] worker for offline caching.
[21:46] Uh, I don't know that we need that.
[21:49] We I really don't think we need cashing
[21:51] for a charades website. I'm only going
[21:54] to go to like once a month. Uh why do we
[21:58] need cashing? We don't need cashing.
[22:01] Okay. All right. So, how do I get
[22:03] feedback and saym don't do that. All
[22:06] right. Let's see. Um
[22:10] okay. Uh I the problem is I don't know
[22:13] what else followed from this research.m
[22:16] MD because I don't want it to do caching
[22:19] but I don't see whether I'm just
[22:21] supposed to edit it or
[22:25] um or what. Okay, then we have data
[22:26] models. All right, that's fine, I guess.
[22:32] Um we have an index schema. Okay, it
[22:36] generated a JSON schema for the JSON.
[22:40] Okay. So, that's all under the
[22:42] contracts.
[22:44] All right. So, I just want to make sure.
[22:48] Okay. I do not think we need service
[22:51] working. Oh, okay. Yeah, we can try type
[22:54] uh specit.clarify.
[22:58] Speck kit.clarify.
[23:00] All right. And what is clarify? Uh
[23:03] identify under
[23:05] specified. I just Let's just see if
[23:06] there's an example of it here. spec kit
[23:09] like just how they might clarify clarify
[23:12] uh it says recommended before spec
[23:14] kit.plan plan. So, I'm not sure that
[23:17] we'd want to use it at this point.
[23:20] Um, I think that would have been in
[23:25] Yeah, because I don't Yeah. So, I'm not
[23:29] sure where I think we just have to say
[23:31] like uh I don't want to implement
[23:34] service workering caching.
[23:37] That seems like overkill.
[23:42] So
[23:44] I I mean it's all in the conver in its
[23:46] history. So, um let's see if it so
[23:49] research.md
[23:52] maybe it was in plan.mmd
[23:54] that it really it decided it wanted uh
[23:58] constraints github pages hosting
[24:01] no built in okay caching browser oh okay
[24:05] it w it was in plan.mmd so if I had done
[24:08] I hadn't noticed it in plan.mmd because
[24:10] honestly there was a lot in plan.md
[24:13] um so I could have modified it at that
[24:15] point okay So
[24:18] great.
[24:21] All right. So now we've done that. So
[24:22] proceed from plan. So do we want to do
[24:25] do we want to do tasks or
[24:28] do we want to do
[24:31] checklist?
[24:32] Which one should we do? Let's see.
[24:36] Great. A technoation plan. Break it down
[24:38] into tasks. All right. Well, it seems to
[24:41] indicate we should do tasks next in this
[24:43] one. So we can take a look and see what
[24:47] checklist was. Checklist created agenda.
[24:50] Okay. Our unit test for requirements
[24:52] writing not for verication testing.
[24:54] Okay. All right. We'll just do spec. Uh
[24:57] oh no. We're going to do task. All
[24:58] right. We're just going to say create
[24:59] task. Okay. That's it. I just clicked it
[25:02] and it was good to go. So that was from
[25:08] that was from plan.
[25:11] All right.
[25:13] So now it is making tasks.
[25:17] [laughter]
[25:18] Um
[25:23] yeah, I think what you'd have to do is
[25:25] you know you really like with any sort
[25:26] of structure like this where you're
[25:29] doing spec driven, PRD driven, whatever
[25:33] you want to call it driven. Um you want
[25:35] to check you want to like read through
[25:37] things each step of the way and go
[25:39] through them. But one of the things that
[25:41] like LLMs can write a lot and sometimes
[25:44] they write more than you necessarily
[25:45] want to read and so it can be, you know,
[25:50] a little overwhelming to actually go
[25:52] through and read read every little thing
[25:54] in there. Uh but uh yeah, ideally that
[25:58] is what you do to check if there's
[26:01] anything that you're like, "Oh, I don't
[26:03] want that." Right?
[26:04] Uh, I really glazed over this also
[26:06] because I'm live streaming, but this
[26:09] looks reasonable. Data, themes, themes,
[26:11] tests.
[26:13] Okay. Yeah, that looks pretty good. All
[26:15] right. Task generated task.md total task
[26:18] 55 parallel opportunities 16 phases six.
[26:24] All right. Complete through phase three
[26:26] for a working app with the animals
[26:27] theme. Okay.
[26:30] All right. It is going to make lots and
[26:34] lots of things. All right, so I could
[26:36] look through this.
[26:38] Um, P can run in parallel. How is it
[26:40] going to run in parallel? Is the agent
[26:43] going to run it in parallel? I'm not
[26:44] sure that the agent's really going to
[26:45] run in parallel. Oh, why is it making a
[26:48] pack I guess it's making a package.json?
[26:50] I think that's just for local
[26:51] development. Let me just ask. Is the
[26:53] package.json just for local dev stuff?
[26:59] Uh,
[27:01] foundational
[27:03] data themes.
[27:12] All right. So the question is do we then
[27:14] go analyze? Oh proceed. Okay. All right.
[27:17] So chat package.json is just dev stuff.
[27:20] F test playright eslint and prettier. No
[27:22] mpm
[27:24] dependencies. Oh no. John
[27:27] [clears throat] says it says three days.
[27:29] Where did it say 3 days? Oh no.
[27:33] Where is it going to say three days? Um
[27:37] where? Wait, where does it say it'll
[27:39] take three day? Let me see.
[27:43] I don't see it, but just tell me where.
[27:46] Um uh complete through phase. All right.
[27:51] Okay. So let's do
[27:55] let's can can we complete with just
[27:59] emojis for now and not the Wikipedia
[28:05] and add that after
[28:11] after you're in task. Okay. Uh so let's
[28:14] see we have two follow-ups here is
[28:16] analyze for consistency.
[28:20] Uh that's using specit analyze and then
[28:23] implement project. So we could probably
[28:25] do analyze first and then implement. So
[28:28] maybe we do analyze first just to see.
[28:31] All right. It is editing task.md polish
[28:34] and cross cutting concern paper size
[28:37] selector. Okay. Keyboard navigation
[28:40] support. Add Arya levels. I mean I'm
[28:42] glad it's making it accessible.
[28:44] Lighthouse CI step. What is Lighthouse
[28:46] CI? Why? Wait, what is Lighthouse CI?
[28:51] Shouldn't we add a GitHub action?
[28:56] Handle very long words. I feel like
[28:59] phase five is too much polish.
[29:04] Lighthouse CI. Oh, okay. Google
[29:06] Lighthouse. I see. Um, I guess that's
[29:10] fun.
[29:12] All right, but we should do current
[29:15] scope 46 tasks. I see it got moved to a
[29:18] future section. Okay, that's nice. So,
[29:20] it still has the Wikipedia stuff, but
[29:22] that's in a future section. So, it says
[29:24] to do
[29:26] complete through phase three. All right,
[29:28] let's first let's try this analyze for
[29:30] consistency just to see what it does and
[29:34] see if we get some inconsistency here.
[29:40] Uh, so it is just looking to see
[29:43] everything exists. So it's like running
[29:45] a bash script here from the from this
[29:49] this thing here. Okay. So it just checks
[29:52] to see that everything exists.
[29:56] Um it is
[29:59] looking for issues. Looks like it found
[30:02] some issues. Okay.
[30:09] Okay.
[30:11] coverage summary tables, black and white
[30:14] legibility,
[30:15] testing standards, code quality,
[30:18] critical issues. Oh my,
[30:21] testing gap either we need to add test
[30:24] tasks.
[30:26] Um,
[30:28] couldn't testing be a phase in the
[30:33] tasks?
[30:37] And
[30:39] maybe what is style lint?
[30:44] I've only used prettier
[30:47] eslint
[30:49] remove visual regression testing
[30:54] plan.
[30:57] Um John asks when will we get compact in
[30:59] VS code copilot chat. Oh we did get
[31:02] compact did we not compact? Nope.
[31:06] H.
[31:08] Oh, we got compact in the CLI, right?
[31:11] That's why I was thinking of it. CLI.
[31:13] Where's our CLI at? Other CLI.
[31:17] Compact. I see. Yeah, we do have that in
[31:20] the CLI. I don't know. Let me I'll just
[31:22] ping Pierce.
[31:26] Uh,
[31:33] when will we get compact in VS Code
[31:36] Copilot chat?
[31:39] All right, I just asked.
[31:42] Yeah, I really only use the chat, too.
[31:45] Okay, so stylant is a CSS llinter. It
[31:48] catches errors since using prettier.
[31:50] It's unnecessary. Remove from plan. All
[31:51] right. Added fade five testing. Remove
[31:54] silent. Remove visual aggression. All
[31:56] right. Um, good. So, this is setup
[31:59] foundational US1 US2.
[32:02] All right. So, great. Uh, looks good.
[32:06] So, then we're going to do
[32:08] specitimplement
[32:11] the phases. So, let's take a look at
[32:13] these phases again. Foundational phase
[32:16] three printable cards.
[32:19] That looks uh like we do want
[32:23] do we want phase phase three? Okay.
[32:26] Implement FA FA implement phases
[32:31] 0 through three. I don't even know if
[32:33] there's a zero, but we're doing zero
[32:34] through three. [laughter]
[32:39] Uh let's see.
[32:43] And now it's compacting. We were just
[32:46] talking about compacting. Now it is
[32:49] compacting. Um,
[32:53] so you know VS Code compacts when it
[32:56] thinks you're getting close to the
[32:57] context window. I think there is like
[32:59] isn't there a better way of seeing?
[33:01] Let's see here. You can see
[33:04] uh where do we see the context context?
[33:07] Nope.
[33:09] Um, I thought they just added something.
[33:11] Context
[33:14] window.
[33:20] There's so many buttons here. Custom
[33:22] tool sets, chat settings, com files.
[33:26] Uh, oh, this one. There we go. I found
[33:28] it.
[33:31] Um,
[33:32] okay. So, context window. All right.
[33:35] Right. So, if we click on this, we can
[33:36] see context window is at 72%.
[33:39] Um, presumably that's after it just did
[33:41] the summarization. And we can see system
[33:44] instructions taking up 5.8%, tool
[33:46] definitions 12%, user context is 31%,
[33:50] tool results is 18%. And then files,
[33:53] it's interesting. So, what's taking up
[33:54] the most is the messages. And that makes
[33:58] sense.
[34:00] Um
[34:02] yeah, I don't know if there's a secret
[34:04] ray to
[34:06] trigger it. I have asked
[34:10] case.
[34:14] All right. All checklist complete.
[34:24] Proceed to load implementation. All
[34:25] right. So it is
[34:28] going into
[34:33] uh it's going into
[34:36] implementation time.
[34:39] I'm just going to allow it to make dur
[34:41] all the time
[34:44] because that takes too much time. So So
[34:47] we're going to have it implement and see
[34:49] how it does. I see like there's um CSS
[34:52] data JS you know so it's making stuff
[34:55] here now the test would be after
[34:59] after it does all this
[35:02] I should try the same thing just using
[35:04] plan mode because now you know because
[35:07] spec kit was made back when our models
[35:10] weren't as good and they needed like a
[35:12] lot more handholding to stay on track
[35:14] and and all that stuff now our models
[35:16] are quite good so interesting thing is
[35:19] you How, you know, could we just do the
[35:21] same thing? Um, I'm going to allow in
[35:23] this session to edit package.json.
[35:27] Um, you know, c can we would we be able
[35:29] to accomplish the same thing
[35:32] if we simply used plan mode? All right.
[35:36] So, we have a charade card generator, an
[35:39] index,
[35:41] and
[35:44] app.css CSS
[35:46] data JS components. All right. It's
[35:49] still building
[35:51] it's still building a bunch of the the
[35:54] files here.
[35:57] Um
[35:59] so
[36:01] to take a look at stuff as it's
[36:02] building. All right. I think we just got
[36:04] some more stuff came. Themes.json. Okay.
[36:07] And then themes.
[36:09] So, I wanted to pre-generate the the
[36:13] theme. So, that'll be kind of fun to see
[36:16] uh what it does. So, it's moving on to
[36:18] phase three. So, it says that it is
[36:20] done. Oh, and it edited it. Okay. So, as
[36:22] it goes along, it's basically using this
[36:24] as to-dos, right? So, it is editing them
[36:27] and saying that it's done with this.
[36:28] It's done with this. It's done with
[36:30] this. And then it is moving on. And now
[36:33] we have animals.json. Here we go. Oh,
[36:36] I'm excited to play this tonight.
[36:38] [laughter]
[36:40] Peacock, flamingo, crocodile. Good. Now,
[36:43] I don't see a seahorse.
[36:47] But of course, we don't have seahorse
[36:48] emojis, do we? All right.
[36:50] [clears throat] So, it is adding animals
[36:51] that Jason. Be nice to add couple other
[36:54] themes, too, after.
[36:57] Um, so it's still editing so we can see
[36:59] as it goes along. Um it's implementing
[37:03] the JavaScript
[37:06] and now working on printability.
[37:11] Okay. So that's in JavaScript. So we
[37:14] have charade card.js. You can see this
[37:16] extends HTML elements. So this is
[37:17] vanilla.js using modern web standards
[37:20] where you can define your own custom
[37:22] HTML elements. And uh looks like looks
[37:28] roughly correct. Um then we have card
[37:32] grid which is another custom element
[37:33] here
[37:35] which is looks
[37:38] looks correct I guess. Um
[37:43] card service
[37:45] is loading the themes. All right doing a
[37:48] little fetch shuffling the array
[37:50] generating the cards. Print service. So,
[37:53] it is I see it is adding I'm not It's
[37:57] interesting that it feels the need to
[37:58] add the print classes because usually I
[38:00] would just use at media print, but I
[38:02] guess it's trying to really customize it
[38:04] for different [snorts]
[38:06] different printers. I think that's
[38:07] probably overkill. I'd probably just
[38:10] make it be printable. Uh app.js. Okay,
[38:14] this is just handling everything and
[38:18] that's just vanilla JavaScript.
[38:21] Um,
[38:24] and hopefully it's written in a way that
[38:25] it works in the browser and doesn't
[38:28] require building. That's something that
[38:30] the uh models might struggle with here.
[38:36] Um, all right. So, let's see. So, now
[38:38] the project structure looks good. Okay.
[38:40] Phases one through three implementation
[38:43] complete.
[38:44] 25 tasks done to install the to test the
[38:47] MVMP. Okay. So, we're just going to run
[38:49] a a uh local
[38:53] a local server here
[38:56] and see what it looks like. I think I
[39:00] already have a local server on 8,000,
[39:01] but we'll find out. Oh, cool. Look at
[39:05] that. All right.
[39:07] Animals.
[39:09] Okay. I guess that's selecting generate
[39:11] cards.
[39:13] All right. And then print cards.
[39:19] Okay. Well,
[39:21] the thing is I think we need more cards
[39:24] than that. [laughter]
[39:27] Um because they're not filling the
[39:29] space. Uh add more cards
[39:33] to animals theme so that it fills a full
[39:37] letter. See, at this point, I'm just
[39:39] going to like go off script, right?
[39:40] Fills a full letter page. Also remove
[39:43] all the fancy page sized selection
[39:47] stuff.
[39:49] Just
[39:51] the media print query should be fine,
[39:54] right?
[39:57] All right. Well, you know, pro tip, use
[39:59] Chrome. Hm. I'm in Edge. Close enough.
[40:02] Uh, cards include cut guides.
[40:06] And we definitely need like a lot more
[40:09] themes.
[40:11] All right. So, if I print them. Yeah, I
[40:13] want it to fill the page more. I don't
[40:14] see any animals theme. Oh, oops. I'm in
[40:16] the wrong repo. Sorry. This is in the
[40:19] rag repo. It's so confused. It's like,
[40:21] what are you talking about? Okay,
[40:28] it wants to access data from other apps.
[40:30] [laughter]
[40:32] Okay. Um, so
[40:36] it is doing a little doing a little
[40:40] thinking here.
[40:45] It thinks that there's not Okay, it
[40:47] doesn't quite understand how many are
[40:48] printed on the page. I guess it what we
[40:50] should add is the end to end. If we
[40:51] added the end to end testing, then I
[40:53] think it would be able to tell because
[40:54] you can with Playright, you can like do
[40:56] print uh you can like do save as PDF and
[40:59] stuff like that. So, I think you'd be
[41:00] able to tell whether it looked like a
[41:02] good PDF. That would also be a nice
[41:04] thing to do is just uh like just have
[41:06] the PDF just already available. Okay.
[41:09] And then
[41:12] now we should have a few more.
[41:19] Okay. All right. Let's try this out.
[41:25] Select the theme. Generate cards. and
[41:28] then print cards.
[41:32] Okay. Well, not exactly filling the page
[41:34] here, but um looks like we got a couple
[41:37] more there.
[41:39] I think we need to add some testing.
[41:41] Huh. All right. So, let's go. Let's go
[41:43] to the right repo. Let me I got to close
[41:45] this. I stop opening it. All right. Um
[41:50] it says it now has 32.
[41:54] All right. move on to phase four
[41:59] or what is phase four
[42:14] user store theme selection. All right,
[42:17] implement
[42:18] phase 4.
[42:21] We need it to be a little bit fancier
[42:24] than this.
[42:27] So now it's going to go back to
[42:30] its um task.md. Right?
[42:34] So this is kind of a nice idea is just
[42:36] having the the the phases, right? So you
[42:39] can remember what you eventually want to
[42:40] do, but you can also kind of split it up
[42:42] into what you want to do now and then
[42:45] give some feedback and then what you
[42:46] want to do later. uh and then just have
[42:49] it, you know, put X's when it's when
[42:52] it's implementing. So, presumably, if we
[42:54] looked at the
[42:56] uh where's the implement agent, right?
[42:57] So, the implement agent, you can see it
[42:59] checks the checklist status. See? So, it
[43:02] it has instructions for how to count.
[43:04] And you know, LM are very good at
[43:05] counting.
[43:07] Um and uh and here so it'll say like
[43:11] it'll look at the checklist
[43:14] and
[43:15] um oh and it even has common patterns
[43:18] for technology. Wow. So it has a lot of
[43:22] like things it already knows about
[43:24] development.
[43:27] And then as it goes through for
[43:29] completed task make sure to mark the
[43:31] task off of X in the task file. So if
[43:32] you wanted to do something similar to
[43:34] this but more lightweight, you could
[43:36] have something like this, which is like
[43:37] a plan file that has checklist, and then
[43:39] you just tell it to mark off the X.
[43:44] The interesting thing is that I also
[43:45] have the VS Code to-do tool implemented
[43:50] right now. I think if we go here, we can
[43:52] see um the tool selector. It has to-do
[43:56] enabled. So, it's trying to both use
[43:58] task.md and it's also using tool to-dos
[44:01] within the session. So, I feel like that
[44:04] might be a little confusing, but it
[44:06] seems to be working. Okay.
[44:11] Oh, so John says follow the demo example
[44:14] without changing project and you got an
[44:17] error. So, you got an error with a SQL
[44:20] Wom. Um,
[44:23] I've used SQL Wasson before on Khan
[44:25] Academy when we taught SQL. Uh, I don't
[44:27] know what it's using SQL WSOM for, but
[44:29] maybe it's importing it using the wrong
[44:32] um
[44:33] wrong sort of uh module type like for
[44:38] ECMAScript modules
[44:40] maybe. Uh, all right. So, we got food
[44:44] actions.
[44:45] I want to see my children act out sushi.
[44:48] Okay.
[44:50] actions. The action I think makes more
[44:52] sense. Holidays.
[44:55] Okay. Occupations.
[44:59] We could try that. All right. Now, now,
[45:01] okay. So, let's see. Is Is this auto
[45:03] reloading? We'll find out.
[45:06] Okay. Great. So, now we can see
[45:08] occupations. Generate cards.
[45:11] It's certainly fun to see what my kids
[45:13] think these words, these emojis mean.
[45:16] [laughter]
[45:17] They're just going to act out a giant
[45:18] tooth.
[45:20] >> [gasps]
[45:22] >> Okay. Um and then All right. So it did
[45:25] that. All right. So now
[45:27] great implement
[45:31] uh now implement
[45:34] phase five
[45:37] of wait what is phase five?
[45:41] Let's see. Testing. Yeah it's testing.
[45:43] All right. So let's see how it does with
[45:46] testing.
[45:48] Implement phase five.
[46:02] I mean, it's pretty cool how quickly you
[46:04] can make things these days.
[46:08] I need to make more things that will
[46:09] entertain my children at night. During
[46:12] the day, I make I'll make apps that will
[46:14] entertain them at night. But this is the
[46:16] best because it I can print it out and
[46:17] so they don't have it's like not
[46:19] additional screen time, right? All
[46:21] right. Let's keep all the changes that
[46:23] we had before. All right. So, it is
[46:25] setting up tests. Right now, we've got a
[46:27] test folder with unit and end to end.
[46:31] And here we have the unit test using by
[46:34] test vid test. I don't know how to
[46:36] pronounce it. We'll go with by test. And
[46:39] this one is
[46:42] just doing some unit tests. Okay, not
[46:47] very exciting. The end like here's the
[46:49] thing. Kent Dods, you know, he's a
[46:51] well-known front-end developer and he
[46:52] argues we should start with endtoend
[46:54] tests as you're going to learn more from
[46:56] them. And I would definitely agree
[46:57] especially for front-end apps that end
[47:00] to end tests are going to be more useful
[47:02] because there's just so much mocked out
[47:04] in the uh in the unit test and we really
[47:08] what we really care about is the what
[47:10] the endto-end experience is.
[47:19] So I've asked my colleagues what they
[47:21] think about spec kit. um they say it's
[47:24] overkill for small products. Uh you have
[47:28] to iterate over and over especially in
[47:29] the task phase but been they've been
[47:32] getting very successful getting good
[47:33] results when using strong PRDS combined
[47:36] with a few skills.m MD files. So there's
[47:40] many different approaches that you can
[47:41] use. All right. So now it's going to
[47:43] install uh that's just install the
[47:45] chromium browser so that it can run to
[47:48] end test. So that should mean it okay
[47:49] good. So it should have the end to end
[47:52] test. Is it going to verify cards or
[47:55] enables print button displays cards in
[47:58] print med? Okay, this is fun. Emulate
[47:59] media print. So it's going to make sure
[48:02] that the
[48:06] um [clears throat] that one works. All
[48:08] right, let's try.
[48:13] All right, so question from
[48:16] Aeshwar. I think it is really great to
[48:18] start a new project with this. But will
[48:20] this approach work for a project which
[48:22] we already started? Um
[48:26] I think you could potentially use it for
[48:29] a uh for a big new feature. Now the
[48:32] annoying thing is though that you would
[48:33] need to bring in all these files here
[48:36] because um you know it relies on this
[48:39] specify directory. So you'd want to
[48:41] bring in the specify directory and the
[48:44] agents directory. So you can kind of do
[48:46] like specify a nit for your feature in a
[48:49] new folder and then just copy and paste
[48:51] everything into your repo. I don't know
[48:54] if there's another way that they have to
[48:56] like add it to an existing thing, but um
[48:58] but the important thing is that you know
[48:59] the agent definitions
[49:01] are there and they do rely on templates
[49:03] that are here and scripts that are here.
[49:05] So I think you certainly could bring
[49:08] these into an existing project and use
[49:10] them to do new features. Um
[49:13] and or you could just adopt a similar
[49:16] approach, right? Like uh and saying you
[49:18] can, you know, um just have an agent
[49:21] that's writes out a product plan and
[49:24] then you have another agent that turns
[49:25] that into implementation plan. Like
[49:27] that's the basic idea and I' I've shared
[49:29] this quite a bit in the past but um you
[49:32] know this uh from
[49:36] uh from Nicholas Zakis like he has a
[49:37] really similar approach here and it's a
[49:40] little more it's a bit more lightweight
[49:43] and um you know but it has a similar
[49:45] idea. Okay. All right. Okay, it is going
[49:47] to run the test.
[49:50] And of course, being npm, we have
[49:52] packages that are out of date because
[49:54] you always have packages out of date
[49:56] because that is my life is having
[49:59] packages out of date. Uh, but it is
[50:02] running the tests
[50:04] running the test right now. You can pop
[50:07] this out and see. So, we can see as it
[50:10] goes through and runs each of the tests.
[50:16] Uh,
[50:18] it looks like it might be timing out.
[50:20] So, with Playright, uh, so this one,
[50:21] let's see, it's doing theme selection.
[50:23] Okay. Oh, look at that. Okay, cool. I've
[50:27] actually never seen this from Playright.
[50:28] I normally write my playright test in
[50:30] Python. So, here we got a test timeout
[50:33] in this one. Um, but the other ones, it
[50:36] look like they all
[50:38] uh that they all passed. Um, one failed.
[50:44] So now it's going to be it should get
[50:48] that information that this is where it
[50:50] failed. So for some reason it never saw
[50:52] that generate button. So it didn't have
[50:54] anything to click.
[50:57] Uh so it may be that it is
[51:02] thinking about it now. Let's see what
[51:04] it's doing. Serving HTML report. That's
[51:08] cool. Okay. Is it going to What is this
[51:13] play button? continue in background. I
[51:16] wonder if I need to just quit it. Okay,
[51:18] I'm going to quit it so that it can keep
[51:20] going. Interesting. All right, so I had
[51:23] to quit it there because it was just
[51:24] kind of just serving it forever and
[51:26] waiting for me to to quit out of it. So
[51:28] now it sees that one test fails and
[51:32] it is doing some updates there. All
[51:34] right, so let's just check and see how
[51:36] this is doing. Anyway, cards 1 2 3 4 5 6
[51:40] 7 8 9 10 11 12. I'm confused because it
[51:42] claims 24 words, but I only see
[51:45] that's only 12 cards.
[51:49] So, where did the other uh ones go? I
[51:54] don't know. Um,
[51:57] all right. It's still working on fixing
[51:59] up the test. Animals.json.
[52:02] That does look like
[52:04] Oh, you know what it probably is? It's
[52:06] probably just cached. Let's try
[52:10] one, two, three. That still looks like
[52:11] 12 words. What about food and drink?
[52:14] And also, we don't really need this
[52:15] generate button. We're not really Oh, I
[52:17] guess it's randomizing it. Oh, is it
[52:19] randomizing? Oh, now it got even worse.
[52:21] Look at that.
[52:24] And probably have to control C again.
[52:26] Control C. Okay. [laughter]
[52:29] Um.
[52:33] All right.
[52:34] It it looks like it is uh basically it
[52:37] looks like it is generate cards. Oh, so
[52:41] I think it's generating 12 at a time and
[52:42] it's generating 12 random ones. The the
[52:45] truth is like you don't really I don't
[52:46] really need generation. I was just
[52:48] trying to make it fancier. Like it's
[52:50] just a static. It's just static cards,
[52:52] right? Um I just wanted to just altering
[52:55] between them. And then you shouldn't
[52:57] even need a print button. You should
[52:58] just be able to like I mean you can have
[53:00] a print button. Lots of websites have
[53:02] print buttons, but if you've done your
[53:04] CSS correctly,
[53:07] um, generate cards. Okay, if you've done
[53:09] your CSS correctly, when you click
[53:11] print,
[53:12] this is exactly right. Right. So, I
[53:14] shouldn't even need a print button. I
[53:15] mean, the print button is fine as a
[53:17] bonus, but in theory, when you're when
[53:19] you make a website, you shouldn't need a
[53:20] print button because you're just using
[53:22] the print CSS to get it to show the
[53:24] right thing.
[53:27] Uh, so let's see. Now it looks like it
[53:31] is okay. Unit test. All right. Nine
[53:34] passed. All right. So I think that it is
[53:38] making good
[53:41] progress here
[53:43] and I think we got everything passing.
[53:46] Okay. All right. So now we can be like,
[53:48] okay, um, remove,
[53:53] remove. We don't need the generate cards
[53:57] button since it's all static. Just show
[54:02] every single card when the user selects
[54:07] the theme.
[54:09] And
[54:11] um, okay.
[54:18] That should simplify things quite a bit.
[54:24] Also, I haven't done any git commits
[54:26] during this whole process. [laughter]
[54:29] And I think generally you would want to
[54:30] do some commits along the way,
[54:31] especially if you're changing you're
[54:33] changing as you go along.
[54:38] Now, how do I make this
[54:41] prettier? I was told I need to make
[54:42] something that's like visually
[54:44] interesting.
[54:45] Um, but we'll wait for it to to change
[54:48] that. Also, you know what I wanted to do
[54:50] is add translations, right? Because my
[54:53] kids uh well, at least the younger one
[54:56] is like kind of 50% Spanish, maybe like
[54:58] 30% Spanish realistically since we don't
[55:00] really speak it at home. But I figured
[55:03] we should maybe so maybe what we should
[55:06] have at the top is like options, right?
[55:07] and say uh like okay maybe you have the
[55:10] options for what languages to include on
[55:12] the cards and then you could include
[55:13] multiple because lots of people have
[55:15] multilingual families right so you could
[55:16] have like English and Arabic English and
[55:19] Chinese English Chinese Spanish like at
[55:21] a certain point going to run out of
[55:23] space um but maybe you get to pick three
[55:27] languages and after that it cuts you
[55:29] off. So the thing is like eventually you
[55:31] end up having like additional um you
[55:34] know you know features that you want
[55:37] want to add on um which I think is
[55:40] that's fine. Um it's just it's not
[55:42] clear, you know, at that point, you
[55:45] know, once we're ready to add on more
[55:46] features. Um do we change we could
[55:50] change task.md to to keep following this
[55:53] plan and and maybe that's the way to
[55:55] that's probably a good thing to do is to
[55:58] stay more structured. Um or you you know
[56:02] at this point the agents are pretty
[56:03] good. You could probably just say you
[56:06] could you could delete your dash.m MD
[56:08] and all that stuff and and just start
[56:11] adding new features.
[56:14] Uh so it's doing
[56:17] okay. So now it's modifying the test.
[56:20] And here's the other thing is like when
[56:22] you write the test at this phase, I mean
[56:24] it it's nice because checks things
[56:25] works, but if you're still an active
[56:28] if you're still actively trying to
[56:30] figure out what you want, then having to
[56:33] modify tests at this point can be
[56:35] actually fairly annoying because every
[56:37] time you make a change, you got to
[56:39] rewrite those tests. D like tests are
[56:42] great when you know what you want, but
[56:44] if you don't know what you want and you
[56:46] want to just be able to iterate
[56:47] something on more freely just based off
[56:48] of like, oh, this is what it looks like,
[56:50] something like this, which is fun, then
[56:51] I would wait until like I'm like, okay,
[56:53] yeah, I really like this before adding
[56:56] the test just to speed up the
[56:57] development time, right? So, here we go.
[56:59] So, that's that's faster. All right. So
[57:02] now, okay. Now I want um add
[57:08] internationalization
[57:11] add support for multiple languages.
[57:17] So that user can select if they want
[57:21] both English and Spanish
[57:25] have check boxes for each language.
[57:30] wood English selected by default.
[57:33] Also,
[57:36] uh vary the emojis, the human emojis
[57:39] more
[57:41] to have more skin tone diversity.
[57:42] They're all yellow right now to have
[57:44] more skin tone diversity. Okay.
[57:49] All right. Let's make this a little
[57:50] nicer. We still haven't done phase six.
[57:54] Um,
[57:55] but I don't even think we want um a lot
[58:00] of these. I don't know if we want any of
[58:02] these. Probably just this one. Page six.
[58:05] Um,
[58:14] there there's my phase six. Now,
[58:15] [laughter]
[58:20] uh, I see a question. Do I code in Rust
[58:23] as well? I have never coded in Rust. No.
[58:27] Uh I guess if enough people ask me then
[58:29] we'll do a live code where I learn how
[58:30] to code in Rust.
[58:34] Um I and I have some colleagues that
[58:36] have definitely um picked up Rust. Uh my
[58:39] colleague Alfredo Deza, he um recently
[58:42] moved on from Microsoft to do his own
[58:45] thing, but he was doing quite a lot of
[58:46] Rust.
[58:48] And uh obviously Rust is very popular in
[58:50] the Python community with UV and rough
[58:53] and tai all written in Rust and many
[58:56] other Python packages. Uh so sure it's
[58:59] something I'd want to you know learn one
[59:01] day.
[59:03] Uh you know that's with LLMs ideally
[59:06] it's easier for us to dip in and out of
[59:10] uh you know of different languages uh
[59:13] even if we're not experts in them,
[59:15] right?
[59:18] So you see it's creating the to-dos
[59:19] because it's I also have the to-dos tool
[59:21] from VS Code. So it has both this
[59:24] task.md and it has like the to-dos for
[59:26] each of the tasks it's doing. Uh which
[59:28] is fine. I'm just not sure at this point
[59:30] whether you actually need the to-dos
[59:32] tool in VS Code. So sometimes I just
[59:34] turn it off.
[59:36] All right. So it did a bunch of edits.
[59:38] So now you can see we have
[59:42] uh we have Spanish translation
[59:46] and oh we've got difficulty. That's kind
[59:48] of fun. Oh that's good actually. So
[59:50] maybe we would add a filter for whether
[59:52] you want like which levels of difficulty
[59:54] you want.
[59:56] And uh let's see. We did food
[01:00:02] uh actions
[01:00:04] holidays and then okay good. So, we got
[01:00:07] more um more diversity in this skin tone
[01:00:11] emojis here. That's nice. Okay. All
[01:00:14] right. And now it is uh updating the
[01:00:17] front end to
[01:00:19] support that.
[01:00:26] And
[01:00:29] so, I think we've done we did all the
[01:00:32] Okay, so we did all the all the steps.
[01:00:35] Let's just take a look at what else they
[01:00:37] have. So specify initializes specify
[01:00:40] specify check. So this is all the um the
[01:00:44] agents it works with um
[01:00:49] nougat here. Oh, here you go. Initialize
[01:00:52] project in the current directory instead
[01:00:54] of create a new one. So that might be an
[01:00:56] option if you do want to try spec kit in
[01:00:59] an existing repo. Uh it will bring in a
[01:01:02] lot of files. Um, but I don't think it
[01:01:04] should override anything because they're
[01:01:05] all pretty unique. Um,
[01:01:08] and it should confirm, too, because
[01:01:10] notice there's a force. So, you know,
[01:01:12] it's not going to force by default. Um,
[01:01:18] yeah. So, you could you could use it
[01:01:19] that way. And then here are the
[01:01:22] commands. We used a lot of them. We
[01:01:23] didn't use clarify because we just
[01:01:26] didn't use that at the right time.
[01:01:28] Um,
[01:01:30] we didn't really properly use features.
[01:01:32] Maybe feature I don't exactly understand
[01:01:34] the branches. If we were supposed to
[01:01:36] make a new branch at some point,
[01:01:37] [laughter]
[01:01:38] we didn't do it. All right. So,
[01:01:40] development phases, zero to one
[01:01:41] development,
[01:01:43] uh generate from scratch, creative
[01:01:45] exploration, parallel imputations,
[01:01:46] iterative enhancement, brown field. That
[01:01:48] phrase always cracks me up. Uh it's like
[01:01:51] a field full of manure. Uh but, uh add
[01:01:54] features iteratively. So, it claims that
[01:01:56] you could use it for brown field as well
[01:02:00] for existing projects, legacy projects
[01:02:02] as you'd say.
[01:02:04] And there we go. Okay. And there's John
[01:02:08] Lamb. He's the new maintainer now that
[01:02:09] Den has gone to anthropic. All right.
[01:02:12] So, here we go. We've got some
[01:02:15] We've got some new stuff here. All
[01:02:18] right. Languages. We can add on espanol.
[01:02:21] Where's my espanol at? All right. Let's
[01:02:23] try clearing the cache. There we go. Uh,
[01:02:26] we're using, you know, JavaScript that's
[01:02:28] could be cached in the browser. So,
[01:02:30] that's that's kind of fun. Uh, if I do
[01:02:32] print cards.
[01:02:36] Okay, that's looking that doesn't look
[01:02:38] so good. Look at that. Uhoh. Uhoh.
[01:02:44] Print CSS not so good.
[01:02:46] Uhoh.
[01:02:49] The print CSS is splitting across page
[01:02:53] breaks. What it needs is something
[01:02:55] called um there's a CSS property for
[01:02:57] when to break the words. It's like what
[01:03:00] is it? Word break or something like
[01:03:02] that. Let's see what it ends up doing.
[01:03:05] So that's that's a blocker. We need
[01:03:08] that. And then also like it's not using
[01:03:11] the space very well because right now
[01:03:13] I'd have to print out page two to get
[01:03:15] these ones. But I feel like they would
[01:03:17] fit here. So, it should do a better job
[01:03:20] at that. Uh, let's see.
[01:03:24] Okay. So, that's fun.
[01:03:28] Um, oh, it's because of using shadowdom.
[01:03:31] All right. So, shadow nom is like the
[01:03:34] weirdest part of using web elements. So,
[01:03:36] I'll show you again the um web elements
[01:03:39] that we have. JS. Okay. Components. All
[01:03:41] right. So, we have like this um this is
[01:03:44] called the shadowdom. The idea is that
[01:03:47] the CSS from the outside doesn't reach
[01:03:50] in to the inside. And sometimes that's
[01:03:52] good, but then sometimes that's bad. So,
[01:03:55] um, you have to decide when you're
[01:03:56] making web elements if you want to use
[01:03:58] the shadow DOM or if you want it so that
[01:04:00] those web elements are just like in the
[01:04:04] original DOM and are inheriting the CSS
[01:04:07] of the page. Uh so in this case it did
[01:04:09] decide to add the this one the break
[01:04:13] inside avoid page break inside avoid and
[01:04:16] it added it to the shadowdom CSS. The
[01:04:18] other approach would be that we could
[01:04:19] stop using shadowdom and um and have the
[01:04:24] the CSS from the main page go back go
[01:04:27] into those elements. And so that's just
[01:04:30] something you have to decide when you're
[01:04:31] using uh web elements. All right. So now
[01:04:34] let's try it out and then we'll print.
[01:04:38] Okay, that does look a lot better. Looks
[01:04:41] a lot better. That's great. So basically
[01:04:44] it looks like it is fitting
[01:04:46] uh basically as much as it can. Um it's
[01:04:50] interesting that it does three rows on
[01:04:52] the first one and four on the second,
[01:04:54] but you know, things happen. Uh maybe
[01:04:58] because we're not using monospace,
[01:05:00] there's some or the emojis might be
[01:05:02] slightly different sizes. Uh but this is
[01:05:04] pretty reasonable. Like I could cut this
[01:05:06] out pretty well.
[01:05:08] All right.
[01:05:11] So that
[01:05:13] uh that looks good. Oh, maybe we'll just
[01:05:15] say add a
[01:05:17] slider.
[01:05:19] Um or so we need we need some sort of UI
[01:05:25] or
[01:05:27] specifying whether you want easy,
[01:05:31] medium, and hard.
[01:05:33] Um what do you suggest? Give me some
[01:05:36] ideas. Give me ideas.
[01:05:40] Maybe asky diagram them. [laughter] I
[01:05:43] saw someone tweet today that they think
[01:05:45] it's a good idea to have the coding
[01:05:48] assistants like generate a mockup in
[01:05:49] ASKI. Oh, this is great. Actually, this
[01:05:52] is a good idea. I'm going to tell him
[01:05:53] that I copy him. Okay. All right. So,
[01:05:55] here's a few options.
[01:05:58] Um, so we say, okay, checkbox pill,
[01:06:01] difficulty, easy, medium, hard. That's
[01:06:05] consistent. Toggle buttons more visual.
[01:06:08] The slider is fun, but it is harder to
[01:06:11] implement the right. And then single
[01:06:13] drop downs. Easy only, easy plus medium,
[01:06:15] medium plus hard. All right. Well, this
[01:06:18] is really cool, though. I really like I
[01:06:19] I think that's that's that's a fun thing
[01:06:21] to do. So, here, pro tip is when you're
[01:06:25] looking for UI feedback, have it make an
[01:06:27] asky diagram because wow, it did really
[01:06:29] it did a really good job of that. I'm
[01:06:31] very impressed, actually. Okay, I'm just
[01:06:34] going to screenshot. All right. But
[01:06:35] wait, with all that said, I'm probably
[01:06:37] just going to go okay, option A.
[01:06:45] All right. And
[01:06:47] um
[01:06:49] I think at this point
[01:06:54] um
[01:06:56] we've explored spec kit pretty well and
[01:07:00] um so probably going to end the stream
[01:07:05] soon, but I uh you know I thought it was
[01:07:08] really interesting to finally try out
[01:07:11] stuff kit and see the approach it takes.
[01:07:14] I uh you know it was interesting to see
[01:07:16] how they did the agents and the prompts,
[01:07:18] how they did the handoffs. I think
[01:07:20] handoffs are are cool, right? So you
[01:07:22] know just use like think of specit as uh
[01:07:25] you know it's inspiration, right? Like
[01:07:27] so what would work for your organization
[01:07:31] or for your personal method of
[01:07:32] development? What could you take from
[01:07:34] spec kit that you like? Right? Like so
[01:07:36] maybe you know maybe you don't need all
[01:07:38] of these things but maybe you like the
[01:07:39] idea of having the plan and the task or
[01:07:43] something like that. Oh, there's also a
[01:07:44] task to issues.
[01:07:48] So, here it's going to look at all the
[01:07:50] available tasks and then make uh make
[01:07:55] issues in this. Under no circumstances
[01:07:57] ever create issues in repositories that
[01:07:58] do not match the remote URL.
[01:08:01] That's an interesting one as well, isn't
[01:08:03] it? Okay.
[01:08:05] All right. So, let's see. I think the
[01:08:06] thing is that I don't even have a remote
[01:08:08] right now.
[01:08:09] Um,
[01:08:11] let's commit.
[01:08:13] All right. So, we added Oh, yeah. Let's
[01:08:15] check on these. Okay. Difficulty,
[01:08:18] easy, medium, hard. We could remove the
[01:08:21] hard
[01:08:24] or even remove the medium for my
[01:08:26] toddler.
[01:08:29] All right. So, that that's cool. Um, we
[01:08:33] could try doing task to issues. So,
[01:08:35] let's try. So here if I do task to
[01:08:37] issues right now
[01:08:40] what's it going to do? It should error
[01:08:43] because there's no git origin yet. Also
[01:08:46] this tools it it um the tool is not
[01:08:49] imple is not written correctly. It
[01:08:51] should be
[01:08:53] uh just github slash I think
[01:08:56] github. There we go. GitHub issue right.
[01:09:00] All right. So it is I'm the terminal
[01:09:02] tool is currently disabled. Okay. Oh,
[01:09:05] yeah. Because now that we're in this
[01:09:07] one, the only tool it has is
[01:09:12] issue, right? So, it it needs we need to
[01:09:16] give it access to the terminal. So,
[01:09:17] we're just going to give it access to
[01:09:20] the
[01:09:24] terminal.
[01:09:25] Let's see
[01:09:27] which one's the terminal run in
[01:09:28] terminal. Okay. Try again.
[01:09:34] Um, so I guess that's kind of a bug with
[01:09:37] this one because it says that it needs
[01:09:38] to run this, but you can't run this
[01:09:40] unless you have access to the terminal.
[01:09:42] So maybe we'll do a little pull request
[01:09:44] to spec kit. All right, so it's checking
[01:09:46] here. It sees that there is no remote
[01:09:48] origin. Uh, so it should say that we're
[01:09:52] going to add one
[01:09:55] and it tells me to do it. Okay, you do
[01:09:57] it.
[01:10:00] It's your job.
[01:10:03] I'm just the manager.
[01:10:05] Um, it's going to add an origin.
[01:10:08] I never made that repo, though. Wouldn't
[01:10:10] I have to make that repo on GitHub?
[01:10:13] Or can you just
[01:10:15] can you just add an origin even if you
[01:10:17] haven't made the repo? [laughter]
[01:10:20] We'll find out soon. So, does that um
[01:10:25] Okay. So, what is Let's see if this
[01:10:28] origin exists now.
[01:10:31] All right. All right, it's creating
[01:10:32] issues for the incomplete tasks.
[01:10:35] Yeah, that repo doesn't exist.
[01:10:38] How is it going to All right, we'll find
[01:10:40] out soon.
[01:10:42] All create issues for the incomplete
[01:10:44] tasks.
[01:10:46] And I think it's going to fail.
[01:10:51] Let's find out.
[01:10:57] Yeah, it doesn't exist.
[01:11:00] All right, let's help it out and make a
[01:11:02] new repo.
[01:11:07] Okay, new
[01:11:09] repo. Repo repo. Always got a new day, a
[01:11:12] new repo. That's what I always say. All
[01:11:14] right, new
[01:11:17] and spec kit demo. Is that what we
[01:11:20] called it? Specit project. Speck kit
[01:11:23] project.
[01:11:27] sample project using spec kit.
[01:11:34] Okay. Start with template. No template.
[01:11:37] No read mean no license. No jump start.
[01:11:41] Just create the repo. Okay. All right.
[01:11:45] So now we have the repo and let's try it
[01:11:50] again.
[01:11:52] There's look at all these. Okay. Lots
[01:11:55] and lots of issues here. Okay. allow
[01:12:01] and it's failing on that.
[01:12:04] Cannot read properties of undefined.
[01:12:08] Oh, it's having a hard time. Try again.
[01:12:11] Try again.
[01:12:15] Let's see.
[01:12:23] Wait, I made uh I I made the repo for
[01:12:26] you.
[01:12:33] Create a new push an existing. All
[01:12:35] right, we did that.
[01:12:39] All right, create a new.
[01:12:44] Okay, so now I think it's working. Uh if
[01:12:47] we go and look at the issues
[01:12:51] so we can see issues. I know I haven't
[01:12:53] even pushed the code yet but create
[01:12:55] GitHub pages deployment workflow. And so
[01:12:57] then I could assign that to Copilot,
[01:12:58] right? So we can start you know you can
[01:13:00] like move
[01:13:02] um from one to the other. I don't even
[01:13:05] know what the quick start MD is. Quick
[01:13:07] start.md.
[01:13:09] Uh so this is making sure that
[01:13:12] everything works. Okay. Uh add image URL
[01:13:16] and image license.
[01:13:23] Interesting. Okay.
[01:13:29] Probably want to just do a little allow
[01:13:31] all for. Okay. We're just going to say
[01:13:32] allow tools from GitHub MCP server in
[01:13:36] this session since the only tool that
[01:13:38] we've allowed is issue right anyway and
[01:13:40] it's just doing it in this repo. All
[01:13:45] right. So, what do we got?
[01:13:48] Image emoji toggle support image URL.
[01:13:52] All right. I think these are all part of
[01:13:54] adding Wikipedia support.
[01:13:57] How many is it going to add? Are these
[01:13:58] from like phase? Oh, this is from
[01:14:01] future. Okay. Well,
[01:14:04] it's going to add a lot of tasks then
[01:14:06] because I think there was a lot in the
[01:14:07] future. Let's see. Here we go. Update.
[01:14:11] Okay. Okay. So, he's basically going
[01:14:12] through each of these and adding a task.
[01:14:14] So, that's an idea of something that you
[01:14:16] could do if you wanted is to have an
[01:14:18] agent that could turn to-dos into um you
[01:14:22] know into GitHub issues. And this could
[01:14:24] be part of a workflow as well. Um
[01:14:28] and uh but here it's you know I'd rather
[01:14:30] do these issues locally especially the
[01:14:32] future ones because a lot of those
[01:14:34] actually should be done um should be
[01:14:36] done like altogether. It'd be kind of
[01:14:38] weird to delegate them to co-pilot. Um
[01:14:43] uh so uh yeah, some of them you could
[01:14:46] like number one. Um but the rest of them
[01:14:49] actually would be better to do locally.
[01:14:50] I just wanted to try that out.
[01:14:53] All right.
[01:14:56] All right. It looks good everyone. So
[01:14:57] I'm going to close the stream now. I'll
[01:15:02] um I'll push the actual code to the
[01:15:05] project as well, so you can check that
[01:15:08] in a few minutes. And thank you as
[01:15:11] always for joining the stream and uh and
[01:15:16] saying hi in the chat. All right, bye
[01:15:19] everyone.
[01:15:22] [snorts]

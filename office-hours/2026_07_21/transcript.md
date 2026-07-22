[00:00] Welcome to our weekly Python plus AI
[00:03] office hours. This is where we talk
[00:06] about what's going on this week at
[00:08] Microsoft GitHub, the industry, uh
[00:11] anything I'm working on, whatever you're
[00:12] working on and have questions about and
[00:15] we will try to learn things together.
[00:19] So, uh usually start off with going
[00:22] through some news to see if that sparks
[00:26] some discussion or some questions. Um
[00:29] but at any point if you have questions
[00:31] just put it in the chat on the side and
[00:35] I will be looking at the chat uh
[00:37] throughout throughout the session. Um so
[00:42] let's see where should we start with uh
[00:44] I did publish a blog post earlier this
[00:47] week. Uh actually I published a couple
[00:49] of blog posts but starting with this
[00:52] one. Um, this is about building MCP
[00:55] servers that return images and um
[00:59] interactive apps.
[01:02] Uh, so that might be interesting to you
[01:04] if you're building uh MCP servers
[01:08] and um there's some good questions on
[01:11] there. And then the other blog post was
[01:15] about an upcoming event we have. Here we
[01:18] go. There it is. So MCP live. So once
[01:21] again on the MCP
[01:23] everything MCP right now. Um so uh this
[01:27] is going to be a live stream on uh what
[01:31] is it? September
[01:33] 9th from 9:00 a.m. to 1 p.m. PT and um
[01:38] we're going to have a good mix of people
[01:40] that are MCP maintainers, core
[01:43] maintainers and uh that also people who
[01:46] are maintaining you know MCP servers in
[01:49] production. Uh so that that should be
[01:52] good to hear from
[01:55] all these people there. So you can
[01:56] register for that from the link there.
[02:00] Um we're also going to do some inperson
[02:02] events. So we've got one planned for San
[02:04] Francisco and then another one planned
[02:05] for Bengaloo.
[02:08] Um let's see if there's anything else
[02:10] MCP related while we're on the MCP
[02:13] front. Uh
[02:18] uh I think that's all
[02:22] on M front. We'll also of course have
[02:26] next week's really what I've been doing
[02:27] most of the last few weeks is preparing
[02:30] for this uh Microsoft IQ deep dive live
[02:33] stream series that's going to be next
[02:35] week Tuesday, Wednesday, Thursday. And
[02:37] so we're doing Foundry IQ, we're doing
[02:39] work IQ, we're doing fabric IQ. Uh, I'm
[02:42] trying to really get them working from
[02:43] lots of places. So, I'm trying to make
[02:45] Foundry agents, Foundry hosted agents
[02:48] that are able to use all of the IQs in
[02:51] combination and even be able to publish
[02:54] them to Teams and use them there. So,
[02:56] I'm I'm trying to show um, you know, all
[02:59] the ways you might want to build on them
[03:02] and that's with my colleague Acha who's
[03:04] going to be doing the work IQ session
[03:06] and I'll do Foundry IQ and Fabric IQ. Uh
[03:10] this is my first time going really deep
[03:11] into fabric IQ. So I've been going
[03:13] through the learn certifications uh for
[03:17] that to try and learn more about it and
[03:20] uh yeah it's good to it's always good to
[03:22] learn something new. So register for
[03:25] those if you haven't yet.
[03:28] Okay so those are our upcoming events.
[03:32] Um other things I've done
[03:35] this week uh is I am trying out using
[03:41] Foundry to do synthetic data generation.
[03:45] Um there is like a new SDK for doing
[03:48] that like you start up this like
[03:49] synthetic data evaluation job. So I'm
[03:52] using this for the rag repo as your
[03:55] search openi demo and um
[04:00] you know we're it's [laughter]
[04:04] I'm going to use it as much as I can but
[04:06] you know synthetic data generation is
[04:08] very hard. So I'm I've you know using
[04:11] this as a basis but then I've done a lot
[04:15] uh on top of that because it's it's just
[04:18] really hard to really get good synthetic
[04:22] data. Um let me Right. So I've got
[04:28] pretty long um so what I've done is
[04:32] basically like uh I've got one path that
[04:35] generates single hop ground truth and
[04:38] then another one that generates multihop
[04:40] ground truth and it's a lot harder to
[04:44] generate multihop. So multihop is when
[04:46] you need to like go to multiple
[04:47] documents and um I've been you know so
[04:51] I've got like this multihop one. So
[04:53] multiop questions, you know, need to be
[04:55] answered across multiple documents. And
[04:58] it's just it's very hard to get good
[05:01] synthetic questions, right? Like this is
[05:04] like technically a multihop question,
[05:06] but it's a horrible question because
[05:07] it's really just two different trivia
[05:08] questions like which species was
[05:10] described blah blah blah and which
[05:12] species described by Thompson 1869.
[05:14] Those are just two questions mashed up
[05:16] together. So that is these are all bad
[05:20] questions actually, right? These are all
[05:21] just, you know, taking two questions and
[05:24] mashing them together. Um, versus uh
[05:27] where's a a better one? Multihome
[05:30] multihop natural domain agnostic 50. I
[05:33] think it's this one. All right. So,
[05:37] so these are better ones. Um, I need a
[05:40] species that's active year round, but I
[05:42] also want that's migratory. Which of the
[05:44] birds? No, that's not a good one.
[05:46] [laughter]
[05:48] Um maybe you know it's just so hard to
[05:52] find good multihop questions.
[05:54] Um
[05:56] but these are at least a little bit.
[05:58] Okay, this one. If I sort these tax by
[05:59] the number of listed subspecies, which
[06:01] one comes first? And how does that
[06:02] compare? Ah,
[06:05] all right. It's
[06:07] if I compare a California goal and a
[06:09] California scrub jay, which one is more
[06:12] flexible and where it gets its food and
[06:15] what does that imply about the feeding
[06:16] sty? So, this is a kind of reasonable
[06:19] multihop question, right? Where I'm
[06:21] trying to like it's a trying to like
[06:23] compare these two birds. Like, it's not
[06:25] a perfect question because it's still
[06:27] pretty unnatural in terms of how it's
[06:29] worded. Um, but at least, you know,
[06:32] comparing two things is is a bit better.
[06:34] Or this one's good, too. Between red
[06:36] flower buckwheat and red flowered
[06:37] buckwheat, which are in fact two
[06:38] different species, which one supports
[06:41] more butterfly and moss species? Like
[06:42] this actually is the kind of question I
[06:44] would legitimately ask? Um, yeah. So,
[06:48] it's just hard. It is very hard to come
[06:50] up with um good multihop questions. The
[06:53] single hop questions are, you know, they
[06:55] they tend to be um a bit a bit easier,
[07:00] right? How big is this tree? What do the
[07:02] larvae do? What do they feed on? Right?
[07:03] Like that's all, you know, it's all
[07:05] fine. Like single single, you know,
[07:08] single topic questions are pretty
[07:11] straightforward. Um, and these are all
[07:13] ones that were generated via that new
[07:15] SDK. And they're actually pretty like
[07:17] they're a lot more natural than the ones
[07:18] I was trying to um generate for
[07:20] multihop. Um, and so they tend to be
[07:24] like a little more casually, these ones
[07:26] are more casually written, right? Where
[07:28] is it found? General range. Anyway, so
[07:31] the question was,
[07:33] um, how do you prevent the machine from
[07:35] learning the pattern used to generate
[07:38] the synthetic data? Um, I mean, it's all
[07:41] coming from LLM, right? So, you know,
[07:45] um,
[07:47] I it doesn't I I don't think there's any
[07:49] really learning happening here, right?
[07:51] because these are all different systems,
[07:52] right? So, first I'm using a system in
[07:55] order to generate the synthetic data and
[07:57] you know that's using a particular LLM
[08:00] and um it is doing it based off of the
[08:03] Azure AI search index
[08:06] um and it's kind of like getting a bunch
[08:08] of random pages and and clustering them
[08:12] um
[08:14] uh and then you know and then we get out
[08:16] back out this data right and then the
[08:18] next step is to evaluate this right so
[08:20] this is the question and answer
[08:21] according to at synthetic data
[08:23] generation stage. Then we evaluate which
[08:26] means we take this question and we send
[08:28] it to our actual app and then we see how
[08:32] does the response from the actual app
[08:34] compared to the truth right and we see
[08:37] like you know do they cover everything
[08:39] or whatever. Um, so it's not going to be
[08:42] able to like really learn anything,
[08:45] right? Because there's not like um it
[08:47] has no ability to update its it's its
[08:50] its own system prompt or whatever. Um
[08:55] but um yeah, so I don't I don't I yeah I
[08:58] don't think there's really any learning
[08:59] happening here. Um but you know when
[09:00] this goes into the app, this gets turned
[09:03] into a search query. the search query
[09:05] searches we get back the answer and then
[09:07] you get back you know um the truth now
[09:10] if we wanted to like you might want to
[09:12] do some sort of hill climbing and
[09:13] learning right and then and then you do
[09:15] have the risk right so if I was going to
[09:17] run like we have this new agent
[09:18] optimizer so let's say I did run the
[09:20] agent optimizer and these were the avals
[09:23] then there is certainly a risk like
[09:25] anytime you run some sort of
[09:26] optimization where like because imagine
[09:29] we run the agent optimizer and it
[09:31] optimizes for being able to answer all
[09:33] of these questions and be able to do a
[09:35] good job of it that we of course will
[09:37] have the risk that then um when it sees
[09:40] something completely different it may do
[09:42] a bad job. Right? So um you know if it
[09:45] if if we adjust the system prompt too
[09:47] heavily for this data specifically and
[09:51] we hill climb against this data and
[09:53] these evals uh then yeah there
[09:56] definitely is a risk. So generally like
[09:57] you know you want to um you know you
[10:00] want to like one you want to use like a
[10:02] data science mindset where when you're
[10:04] if you are doing any sort of
[10:05] optimization you would hold out part of
[10:08] your data and you would optimize against
[10:10] you know the 50% of your data and then
[10:13] you would um compare to the other 50%
[10:16] and say like okay like you know you try
[10:18] to figure out if you did overfitting
[10:20] right uh then the other thing you want
[10:22] to do is just whenever you after you
[10:24] actually have something in production
[10:26] you get new data from users, you have to
[10:28] keep updating
[10:30] um your you know your your your actual
[10:33] data that you're evaluating against to
[10:35] make sure it reflects what the users are
[10:36] asking right
[10:39] um so so yeah so in this case there is
[10:42] no learning happenings so I'm not
[10:45] worried about that but if I was doing
[10:47] optimization which is you know
[10:49] recommended then we would need to be
[10:52] much more careful about
[10:54] um you know making sure we weren't
[10:56] overfitting.
[10:59] Yeah. No, I mean I think that your
[11:01] question is still is still relevant like
[11:03] because especially as we move toward um
[11:06] as we move toward uh agent optimization,
[11:08] right? Let me find the foundry agent.
[11:12] Oh, here we go. Optimization. Um
[11:16] so this one basically let me find the
[11:19] optimize hosted agents. Okay. So right
[11:22] with with this what you do like let's
[11:24] say you have like a hosted agent using
[11:25] like agent framework
[11:28] um you need to what's called externalize
[11:30] your agent configuration right because
[11:32] the things it's going to optimize are
[11:34] the tool descriptions and the system
[11:36] prompt because that's really like what
[11:38] is an agent it's system prompt with
[11:39] tools right um so what you need to do is
[11:43] ex make it make that information the
[11:45] system prompt and the tools be artifacts
[11:49] that can be improved, right? So, you
[11:52] know, here we put the system prompt in a
[11:54] markdown file. Um, and the optimizer
[11:57] can, you know, optimize that. Uh, then
[12:00] we put tools.json in a JSON schema file
[12:05] and the optimizer can improve these tool
[12:08] descriptions because tool descriptions
[12:09] are basically little mini prompts that
[12:11] are attached to the tools, right? Uh, in
[12:13] theory, you could even optimize the
[12:14] descriptions. I [clears throat] don't
[12:15] know if it of each parameter. I don't
[12:17] know if it does in this case, but like
[12:20] all of this really everything in a tool
[12:22] is a form of prompt. Uh, and then you
[12:26] could optimize skills if your agent was
[12:28] using skills. So all of those things
[12:30] that your agent is using have to be
[12:32] externalized and put in a format that is
[12:34] a common format, a standard format that
[12:36] they can then be improved, right? So we,
[12:40] you know, have our config
[12:42] um and we say, um,
[12:46] you know, you, I guess you, yeah, let's
[12:48] see. So you, you bring in your system
[12:52] prompt, you bring in your tools, your
[12:54] skills.
[12:56] Okay, so here we have right there's our
[12:58] complete
[13:00] um example here
[13:06] with our agent. Okay. And then
[13:10] uh and then what happens is that during
[13:12] optimization
[13:14] it's going to you know modify prompts
[13:17] and functions and then pick a winner and
[13:21] um figure out which is the best.
[13:24] So that's going to you know it needs to
[13:27] do that against some sort of evaluation.
[13:29] uh so you need some you know set of task
[13:31] and that's where you know coming up with
[13:34] that data set is tricky and that's what
[13:36] I'm trying to do in the other one is
[13:37] like you know come up with some
[13:38] synthetic data um so they do have this
[13:42] generate that will try to come up with a
[13:44] seed data set here
[13:46] and but then you know you're probably
[13:49] going to when you really going to do
[13:50] something for production then um you
[13:54] know and you have production data uh
[13:57] then you can actually
[13:59] uh custom your customize your data set,
[14:01] right? Uh so you really want to have
[14:03] good Yeah, they've got some good
[14:05] examples here of what makes a great data
[14:07] set. Write prompts like real users
[14:11] [laughter]
[14:12] bad. The response should be good.
[14:16] Good response. It must explicitly
[14:18] mention 308 refund window. Yes. [snorts]
[14:20] And uh yeah, and then you can go and run
[14:24] it. Let's see if they have the results
[14:25] here. Interpret results.
[14:29] um it like shows you the scores that you
[14:32] get across the evaluations and then you
[14:34] can bring in that configuration.
[14:37] [snorts]
[14:38] Um,
[14:40] so, um, let me link to that if you want
[14:43] to see this. Optimization,
[14:49] the optimizer is very early days. So, I
[14:52] think most people aren't
[14:54] I don't think most people have tried
[14:55] optimizer yet. Like, we've only started
[14:57] bringing it into, you know, our labs and
[15:00] and talks and demos and all that stuff.
[15:03] Uh, I haven't actually really used it
[15:04] myself. I've only seen other people use
[15:06] it. So, um, you could try that. It's
[15:09] also similar is if you use DSpy, like if
[15:12] you're doing something with like
[15:13] structured outputs, DSpy works really
[15:15] well for that and I I showed that in my
[15:18] my workshop at the AI engineer worlds
[15:21] fair. Um, and here we yeah, we you know,
[15:24] we we um tried to get the optimal prompt
[15:29] for a particular result. Um, so this
[15:32] one's so DSpy is really good if what
[15:35] you're trying to do is basically
[15:36] structured outputs and like entity
[15:38] extraction, classification, all of those
[15:40] tasks, then you might want to check out
[15:42] DSpy. Um, but if you have like a full
[15:44] agent that has tools and skills, then
[15:47] you, you know, check out the agent
[15:48] optimizer.
[15:53] Um, let's see what else. Um,
[16:01] I made some releases to the rag repo.
[16:04] We're just trying to modernize
[16:05] everything in the rag repo. Um, because
[16:09] there's so many we're using so, you
[16:11] know, kind of because this repo's been
[16:13] around for so long because it came out,
[16:14] you know, right when chatb came out, you
[16:16] know, there's just a lot of stuff to
[16:17] modernize. So that's why I'm, you know,
[16:19] modernizing the synthetic data
[16:20] generation, the evaluation. I'll move it
[16:23] to agent framework soon. So, uh, we've
[16:25] made a lot of releases over the last few
[16:27] weeks to modernize it.
[16:30] Okay, what else?
[16:33] Uh, we've got some GitHub Copilot stuff
[16:36] here. So, we've got Gemini 3.6 Flash. I
[16:41] haven't tried that out. I admittedly
[16:43] have still been on 5.6 Soul, even though
[16:46] I was told I should do try other models,
[16:49] smaller models. Um, but there it is. 3.6
[16:51] six flash medium cost.
[16:55] Uh so you could try that out.
[17:01] Um and that should be available pretty
[17:03] much everywhere.
[17:05] Uh let's see. Copilot usage metrics,
[17:08] RGA. So lots of stuff around usage
[17:10] metrics because everybody's always
[17:12] asking about their token metrics. Uh
[17:15] co-pilot code review adds more
[17:18] customization.
[17:20] Oh, I didn't know about this. This could
[17:21] be useful. Uh because I do I use code
[17:24] review all the time. Um so
[17:28] so custom instructions are always read
[17:30] from the head branch instead of the base
[17:32] branch. Okay. Custom setup steps.
[17:37] Oh, this is nice. So you can configure
[17:39] the environment available using a YAML
[17:42] file.
[17:43] I think I thought we had Okay, great.
[17:45] This is what I thought we had the
[17:47] ability to do. So um so that way like if
[17:49] you find that when you when you assign
[17:51] you know when when it's like you can
[17:53] look at the session for when it's doing
[17:55] a code review and if it's keeps using
[17:57] bad tooling then you could set up a
[18:00] specific environment so that's always
[18:01] using the correct tooling, right? Um but
[18:05] you don't need to do that unless you
[18:07] like unless you realize there's a need
[18:09] for that. But you could, you know, as
[18:11] you're, if you assign a code review and
[18:13] you, you know, look at the results, you
[18:16] might realize like, oh, it needs a
[18:17] better code review support. Uh,
[18:20] firewall.
[18:23] Um,
[18:25] and then runners. Okay. So, that's
[18:28] good if you're using the code review and
[18:31] you need more customizations.
[18:35] And then of course there's copilot
[18:38] app has these canvases. Um so you can
[18:42] create a custom canvas for things. Uh I
[18:45] could could actually demo that. So this
[18:48] is not a custom canvas. This is like a
[18:50] web page here. But let's say
[18:53] um
[18:56] okay. All right. So here um so with
[18:59] canvas so we do create canvas. Okay.
[19:02] Create canvas.
[19:04] Um, and I'll say, uh, make a interactive
[19:11] data table where I can sort and filter
[19:15] all the candidates.
[19:18] Um, so this is for a repo I made a few
[19:20] days ago to try and help find a new
[19:23] family for my nanny because, um, my kids
[19:27] are both about to be in public school.
[19:30] So, uh, I've got this repo that looks
[19:33] through all of these listings of people
[19:35] looking for nannies and then uses an LLM
[19:38] to compare them against my my my own
[19:40] nannies, uh, criteria and then the LM
[19:43] identifies candidates. Um, and right now
[19:46] it just stores them in like a markdown
[19:48] table, but you know, a markdown table
[19:49] isn't that easy to use. So, what I can
[19:51] do instead is say, "Hey, can you make a
[19:55] canvas instead?" Um, and so you can see
[19:59] it's loading. So this is a built-in
[20:00] skill in Copilot app. So whenever you're
[20:02] using Copilot app, you can have it
[20:05] create a canvas. Um, and it can tie
[20:07] those canvases to a session. It can tie
[20:09] it to a repo. You can even have global
[20:11] canvases. Oh, and it just asked, so
[20:13] where should this interactive? Um, yes.
[20:15] So in this case, I would want it for
[20:18] this repository because it's something
[20:20] that I'd always want to use in this
[20:21] repository, right?
[20:23] Um,
[20:26] so now it's it's putting together this
[20:28] this canvas here
[20:35] and it ends up basically making this.
[20:37] Yeah, it's going to make a JavaScript
[20:38] file. So a canvas is really a JavaScript
[20:41] file that u makes kind of an interactive
[20:45] web page that the agent can access.
[20:50] Uh, so people are using it for all kinds
[20:51] of stuff. So if you go to awesome
[20:53] co-pilot
[20:56] awesome co-pilot
[21:00] here let's see
[21:04] I think we have canvases publish polish
[21:06] connected canvas all right where are the
[21:11] um I think let's try here canvas there
[21:14] we go canvas extensions okay so these
[21:17] are a bunch of examples of
[21:20] canvases is Oh, let me link to this one,
[21:22] too.
[21:24] Uh, so here,
[21:28] uh,
[21:30] where's the There's a bunch of them
[21:32] here. Hub.
[21:34] Oh, searching for hub on a GitHub page
[21:36] doesn't work. Okay, [laughter]
[21:39] workhub. This is what I was looking for
[21:40] because this uh this is my colleague was
[21:42] showing this the other day. So, a
[21:44] generic cross repo command center. Um,
[21:47] so if you kind of want to if you working
[21:49] on a bunch of repos, this is what my
[21:51] colleague uses to keep track of
[21:54] everything across the repos. I'm kind of
[21:56] too scared to use this because I feel
[21:58] like it would show way too many issues
[22:01] and I think it's nice if I just stay
[22:03] blissfully unaware of uh some of the
[22:05] issues just because I have so many so
[22:07] many repos. Um, but no, maybe we'll try
[22:10] it. Let's see how our canvas is doing
[22:12] here. Um,
[22:15] so let's see. It says it's canvas is
[22:19] going to do this. All right. So, it's
[22:21] still
[22:23] uh working. So, yeah, it made the canvas
[22:28] and
[22:29] it's just checking through the
[22:31] formatting of it here.
[22:34] Okay. So, it's going to open the table.
[22:37] Here we go. Okay.
[22:42] So this is this is the canvas. Um can I
[22:47] make this bigger? Okay. All right. So
[22:50] you see it basically built a um you know
[22:53] built a web page for me. And so you I
[22:55] could also of course have this just be a
[22:57] web page that lives in the repo. The
[22:59] difference with a canvas is that in fact
[23:01] the agent has access to it. And you
[23:03] could even have the canvas trigger
[23:04] things that the agent can do, right? So,
[23:06] I could say like, oh, you know, when I
[23:09] click a button here, um, you know,
[23:11] you're going to, uh, you're going to do
[23:15] another analysis of this of this, uh,
[23:18] nanny candidate, right? Um, so that's
[23:20] what's, you know, different about this
[23:23] is that yes, it's a web page, but has
[23:26] built-in integration with Copilot. So
[23:28] that anything you could ask Copilot to
[23:31] do in chat, you could trigger that via
[23:34] this, you know, this canvas here.
[23:38] Uh,
[23:42] just checking. Oh, I should add a date.
[23:44] Date would be helpful. Then I could sort
[23:46] by date. Okay. So, that's one canvas
[23:49] there.
[23:51] Let me minimize that. All right. Looks
[23:54] good. Um, I have another one
[23:58] where social media
[24:08] was looking for it.
[24:12] Uh,
[24:14] post on my Twitter. Does this one have
[24:16] the canvas?
[24:19] Oh, yeah. Here we go. So, this is
[24:21] another one. And this one does actually
[24:25] um basically interact back. So, this is
[24:28] one I made for posting um to Twitter,
[24:32] Blue Sky, or Mastadon. And it's using an
[24:34] MCP server. Um but it doesn't use that
[24:37] directly from the web page. It actually
[24:40] will have the agent do that. And it's
[24:42] just a bit nicer because if there is any
[24:44] sort of errors then the agent can take
[24:46] care of the errors right so you know
[24:48] advantage of having an LLM on top is
[24:50] that if there's any sort of um you know
[24:53] if something doesn't work smoothly then
[24:56] you can have the LLM
[24:58] take care of it. Um and then I like to
[25:01] use automations quite a bit in Copilot
[25:03] app. So you know that um you know the
[25:06] find the nanny finder. Uh, so it's
[25:10] actually, oh, it did add two more.
[25:12] Great. So, every every day it looks to
[25:15] see, uh, you know, it looks to find if
[25:17] there's any new people looking for mana
[25:19] n man n man n man n man n man n man n
[25:19] man n man n man n man nannies. Um, and
[25:21] so now I can go and check out the new
[25:23] ones that it found each day. Um, so
[25:26] that's really helpful. I have another
[25:28] one that
[25:29] uh updates my
[25:32] links in a repo because I'm like losing
[25:34] track of all my links. So it goes
[25:36] through and just every day it looks at
[25:40] my tweets and collects links from my
[25:42] tweets and then puts them into the repo.
[25:44] So now I have a repo that is just my
[25:46] bookmarks and we'll see if this ends up
[25:49] you know working well. But that's my
[25:50] current approach, right? Um and then of
[25:52] course every day I run my LinkedIn agent
[25:56] and it goes through and um accepts uh
[26:00] network requests on LinkedIn. So I do
[26:04] find automations really helpful. It's
[26:06] just an easier cron job, right? So you
[26:08] know it's like being able to run a cron
[26:10] job every day except you have the
[26:11] advantage of an agent. So the agent can,
[26:13] you know, easily um identify any issues
[26:16] that are happening. It can uh you know,
[26:18] it can compensate for any issues and try
[26:21] to try to recover
[26:24] um give you next steps. So uh yeah. So I
[26:28] do think that's that's really helpful if
[26:29] you haven't tried it yet. Let's see.
[26:32] Okay, let's just try the Jameshub and
[26:33] see what happens. All right, we are
[26:36] installing in GitHub Copilot app.
[26:41] All right, external plugin.
[26:44] Okay,
[26:45] let's try this. Install plugin. Install.
[26:56] Okay. So now
[27:00] we have
[27:03] the workhub and so how do we use it?
[27:07] [laughter]
[27:08] I don't [clears throat] now I got to see
[27:09] how to use it. So what do we do? Uh what
[27:12] it does.
[27:13] Okay. And then what do we do?
[27:17] [snorts] This is my first time
[27:18] installing from here. Okay. Click then
[27:20] run that plug-in. Install. Okay. Oh, I
[27:23] see. So then I need to do all right
[27:25] let's do workhub
[27:28] or install wait copilot plugin install.
[27:37] Okay. All right. Now I just got to
[27:39] figure out how do I All right. Make
[27:42] maybe I'll just say make a
[27:45] workhub
[27:48] templates. No. Uh home. Um, make All
[27:52] right, let's just try this. Make a
[27:55] workup. I'll give feedback afterwards
[27:57] that it's unclear how to actually
[28:00] um how to use these once you've
[28:04] installed them.
[28:10] What is my work? I'm setting up the
[28:12] workhub and giving this chat a clear
[28:14] name. Okay. All right. So, it did find
[28:17] it did find that workhub. So, that's
[28:19] good. Um,
[28:22] all right. So, it's setting up my
[28:23] workhub.
[28:25] Okay.
[28:27] All right. And then,
[28:30] okay. So, it's giving me like an
[28:31] overview
[28:33] of all my current sessions. So, this is
[28:36] like querying all the current sessions.
[28:40] Uh, let's see. Discover
[28:43] repos and projects.
[28:46] Okay. Okay. So, I found a bunch
[28:51] of things here.
[28:55] Okay. All right. I'll just
[29:00] Okay. Start tracking selected.
[29:04] Okay. So, then we can see stale
[29:06] releases. Oops.
[29:09] Okay. Oh, yeah. Because I just don't
[29:11] even have I should just disable releases
[29:13] from all these. I see. That's a stale
[29:15] release. I've never done releases for
[29:17] most of mine, so I just need to disable
[29:19] releases. That's cool. Uh and then
[29:23] uh open issues.
[29:26] Okay, that's a really old one. Um yes,
[29:30] this is a good way of finding out what,
[29:33] you know, what is going on across them.
[29:35] So there we go. So that's cool. Um,
[29:40] and you know, if I wanted to, I could,
[29:42] you know, start a session on one of
[29:44] these from from here. Oh, it says I
[29:48] could clean up a lot of my sessions,
[29:50] too.
[29:54] Uh, if you can't hear anything, that's
[29:56] usually an issue with Discord. Uh,
[29:59] because if it's only one person, that
[30:00] usually means you do need to restart
[30:02] your Discord.
[30:06] All right. So, that's one example of a,
[30:09] you know, a canvas. Um,
[30:13] so it can be fun to use these. It can,
[30:15] you know, it's a different, it's really
[30:17] a very different way of interacting,
[30:19] right? The idea is that you don't always
[30:20] use chat for all of your interactions
[30:23] with an agent. There might be other ways
[30:25] you want to interact with an agent as
[30:26] well.
[30:28] Um,
[30:32] what else is going on? Oh, this one I
[30:34] thought was really cool.
[30:37] This is just this was just a cool tweet.
[30:40] Um, so this is what is a multimodal LM
[30:43] thinking as it watches a video. Uh, so
[30:49] these are the kind of, you know, if
[30:51] you're trying to translate the image
[30:53] patches into tokens,
[30:56] then this is what they would look like.
[30:59] Um, and some of them make sense. A lot
[31:02] of them just say Tik Tok [laughter]
[31:04] because I guess it's been heavily
[31:06] trained on Tik Tok videos.
[31:08] Uh but it's it's interesting
[31:12] to see people took some fun screenshots
[31:15] of this. So
[31:17] I'll just share that just because it's
[31:19] fun.
[31:21] Uh let's see what else. Um
[31:25] yeah, I mean the really what I've been
[31:28] doing is just everything with uh with
[31:33] Foundry hosted agents. Uh so I got you
[31:36] know like getting publishing teams
[31:38] working. Um let me I can actually switch
[31:42] into my
[31:44] uh where is it?
[31:49] Let me show my agents and apps.
[31:53] manage your apps.
[31:56] Okay, this one.
[32:05] Okay. Yeah, here we go. All right. So,
[32:07] here's an example of a Foundry hosted
[32:10] agent that I published to Teams.
[32:14] And you can see, you know, it does have
[32:16] me do a Foundry login.
[32:20] And once it has that, once I've done
[32:21] that, then it's got the credentials it
[32:23] needs. And then I'm using work IQ inside
[32:28] that agent um in order to get back
[32:33] get back uh responses, right? Uh so then
[32:36] it's able to search through and it
[32:39] finds, you know, it finds teams chats
[32:42] and uh and yeah, but we can integrate,
[32:44] you know, all sorts of things with our
[32:46] agent. Um there's a long
[32:50] a notebook here of everything you can
[32:53] put in a
[32:55] foundry toolbox. Let me find it. Forge
[32:59] notebook. There we go.
[33:06] So, here um there's quite a few things
[33:10] you can put inside a toolbox. Um, this
[33:13] isn't even really comprehensive, but um
[33:16] the like the toolbox makes it easier to
[33:18] manage uh connections that require OOTH.
[33:21] So, it's it's nicer than if you had to
[33:25] do it yourself directly. Uh, but you can
[33:28] add web search, code interpreter, file
[33:30] search. Those ones are easy. Uh, you can
[33:32] add arbitrary remote MCP servers like
[33:34] Foundry IQ. Um, any open API spec could
[33:39] become a toolbox connection. A2A.
[33:42] Haven't tried that one yet, but I am
[33:44] doing work IQ and work IQ is an A2A.
[33:46] They use the A2A protocol now. So, um
[33:50] that's the the one I just showed is
[33:52] using this work IQ A2A inside Foundry
[33:55] Toolbox.
[34:01] Then, Fabric IQ. I'm working on getting
[34:04] that working.
[34:06] Uh skills. So, you can add skills to
[34:08] your toolbox. Didn't try that yet.
[34:11] Um,
[34:13] yeah. So, there's quite a lot that you
[34:16] can do with the toolbox and it does make
[34:19] it much easier
[34:21] to
[34:23] uh to yeah to bring together these
[34:26] things and have easier off for them.
[34:32] Um,
[34:34] anything else? Any questions people
[34:36] have? Let's see.
[34:44] OpenAI did some sort of renaming. So now
[34:47] ChatgBD and Codeex are like the same
[34:48] thing. I I didn't really keep track of
[34:51] that. Maybe some of you have um
[34:54] uh I because I don't use Chat GD
[34:56] anymore. So um or and I don't use codeex
[35:01] since Copilot app does everything I
[35:04] need. Uh so I don't I haven't really
[35:06] kept up with
[35:08] Okay. chat GBT work. Oh, and then
[35:11] there's this chat GB work. Oh, this kind
[35:14] of sounds like
[35:16] what is it?
[35:19] Yeah. Um, turn ideas into action.
[35:24] So, maybe chatd work is
[35:29] what is it doing?
[35:32] I assume it has better connections,
[35:38] but what is it really? [laughter] Okay,
[35:41] [gasps]
[35:41] I guess it's like co-work
[35:45] download
[35:48] uh use cases.
[35:52] All right, so maybe it has better
[35:53] integration with productivity tools.
[35:56] Um,
[36:00] this is definitely a marketing page. I
[36:02] need like a page for
[36:06] normal people. [laughter]
[36:10] Anyway, so there's something called chat
[36:12] work. Maybe some of you have tried it.
[36:13] Um, okay. So Eddie says, "I've been
[36:16] using the goal feature in entropic
[36:18] codeex, but does not increase the
[36:20] results I want regardless of the model I
[36:21] use. My goal is to use GBD to help
[36:23] become a millionaire. [laughter]
[36:26] >> [gasps]
[36:26] >> Oh gosh. Um, I actually was asking on
[36:30] Twitter this week about financial stuff
[36:32] because I actually um did use GPD. I was
[36:35] using GPD 56 for financial questions
[36:38] this week and my goal is not
[36:42] my my goal wasn't necessarily become a
[36:44] millionaire. Um, but I was saying that
[36:45] generally like these things are pretty
[36:47] good. But then someone said um what did
[36:50] they say?
[36:52] Oh yeah, this guy. So he says it indexes
[36:55] too hard on traditional FI and low
[36:57] returns.
[36:59] Um so he's learning everything from
[37:02] invest Brandon, right? This self-made
[37:04] multi-millionaire.
[37:06] So I was saying like, okay, well, you
[37:08] know, maybe just point the LLM at um you
[37:12] know, at at this person's stuff um and
[37:14] then that might do good a job. Uh
[37:16] although he says, you know, you get
[37:18] details once you pay for it. Uh, so
[37:22] yeah. So I think if you are using an LLM
[37:26] for financial advice, it is going to be
[37:28] more conservative. I'm okay with that
[37:30] because I I tend to be more conservative
[37:32] myself. Um, but if you're, you know,
[37:35] trying to like maximize potential gains
[37:38] and are willing to be lesser
[37:40] conservative, then you're probably going
[37:41] to, you know, need to ground the LLM in
[37:47] um in specific strategies that come
[37:49] from, you know, come from those people,
[37:51] right? So, you know, you could try
[37:53] making something like
[37:55] um an idea wiki that uh is based off of
[37:59] like this guy's videos, right? For
[38:00] example.
[38:03] Um,
[38:04] and you're saying it hasn't generated
[38:06] any income. Is this a joke or I mean I
[38:09] presume that either if you wanted it to
[38:11] actually generate income, you would have
[38:12] to either give it a connection to your
[38:14] bank account, which you could do if you
[38:16] really really really trusted it. Um, or
[38:18] you would just be following its advice.
[38:20] So, uh, in my case, I'm just following
[38:22] the advice. Uh there are cases where I
[38:24] do give direct connections and those are
[38:26] you know the two examples I have of the
[38:28] automations where um you know the the
[38:31] nanny finder does have access to this um
[38:34] website that has all these nanny
[38:35] listings on it but I only give it access
[38:38] to that website right I'm very
[38:39] restricted and then the same thing with
[38:41] the LinkedIn agent is that it only has
[38:44] access to LinkedIn right so when I when
[38:47] I set up dedicated agents I only give
[38:50] them access to the cookies for that
[38:53] particular website.
[38:57] Um, yeah, Pierre points out that
[38:58] Notebook LM just changed to Gemini
[39:00] notebook. That's correct. I almost put
[39:02] that on the the news. Um, I don't think
[39:04] I Yeah, I didn't end up putting it
[39:06] there. Um, but that was in the um it was
[39:11] in the newsletter that had some of these
[39:13] other things. So, yeah, Gemini. I think
[39:15] that's probably better. It's called
[39:16] Gemini Notebook because I always thought
[39:18] Notebook LM I don't know. It sounds like
[39:20] too nerdy of a name. Gemini notebook
[39:23] sounds more general purpose.
[39:26] [laughter]
[39:27] Uh
[39:31] I see we're sharing our goals in order
[39:32] to be a millionaire.
[39:35] Um
[39:40] yeah, mine uh I what I did do was that
[39:43] let's see I exported um it can be really
[39:46] like I I went to my bank and I exported
[39:49] a CSV of all my transactions because I
[39:52] was trying to understand why my bank
[39:53] account's so low this summer. So I
[39:55] exported all my transactions from the
[39:58] you know credit account and the checking
[40:00] account and you know sent that to GP56
[40:02] and said okay like analyze all this like
[40:06] you know what do you think of this like
[40:07] what are you know is there something I'm
[40:08] spending too much money on like blah
[40:10] blah blah. And then after that I was
[40:13] like okay well I need to I need to get
[40:15] some more cash. So here's what my
[40:17] Fidelity looks like and my Vanguard and
[40:19] my Morgan Stanley. So, I just like
[40:21] screenshotted those and then um sent
[40:24] there. And then it was like um it was
[40:26] actually really helpful because I I'm
[40:27] not that good at finance. So, it was
[40:29] like, "Oh, you need to figure out your
[40:30] cost basis." And I was like, "Okay,
[40:31] well, what is a cost basis?" And then
[40:33] they explained what a cost basis is. And
[40:35] I know like I should know that stuff,
[40:36] but I just I'm not that good at finance.
[40:38] So um you know so it it it you know it
[40:42] helped me figure out um the cost basis
[40:45] for all my stocks and then suggested it
[40:47] even suggested exactly which um set of
[40:52] stock what do you call it shares which
[40:54] set of shares to sell based off the cost
[40:56] basis and on my goals. So, I do think
[41:00] there's a lot you can do and um you
[41:02] don't have to give the LM direct access
[41:04] to your account if you're willing to do
[41:06] a little like exporting and screenshot
[41:08] sharing. Um but if you do if you did
[41:10] want to have it as like a constant um
[41:13] you know something that was constantly
[41:14] every week checking, that's where you'd
[41:16] want to set up like an MCP server or
[41:18] just do what I do with um playright and
[41:21] and cookies. Uh and so that then you
[41:24] know on a on a on a weekly basis then it
[41:29] can do go and do that that check for
[41:32] you, right? Um
[41:35] and and then maybe like at least you
[41:39] know it could make recommendations that
[41:42] week. Um I'm sure there's also like into
[41:45] it like there must be companies that are
[41:47] already doing this having like an agent
[41:48] that gives you recommendations. There's
[41:50] also the question like in response to my
[41:52] tweet, people are like, "Well, if
[41:53] everybody is using LMS for their
[41:55] financial advice, what happens to the
[41:56] market?" So, I don't know.
[42:03] Let's see if I can use Gemini Notebook
[42:04] since we're talking about Gemini
[42:06] Notebook, too. I don't think I've ever
[42:08] actually used Notebook. LMO
[42:12] Gemini Notebook
[42:15] understand anything. Should use that to
[42:18] understand how to become a billionaire.
[42:19] Let's see if we can set it at Okay, keep
[42:22] me updated. No, I'm already getting
[42:24] updates about it. Um, okay. Can I Let's
[42:28] see.
[42:31] I want [groaning]
[42:34] the investment strategies from
[42:39] So, this is like a way of making an idea
[42:41] wiki, huh? Kind of like Andre Karpathy's
[42:44] idea wiki. Kind of, right?
[42:47] Um,
[42:48] all right. Let's see if it's able to.
[42:51] There we go.
[42:54] Fast research completed. Okay. All
[42:56] right. Let's try import. Okay. This I've
[43:00] never used this before. So, this is this
[43:02] is first time here.
[43:07] Okay. So, I imported.
[43:10] Okay. It's doing something now. Um,
[43:13] system analysis. Okay. and educational
[43:17] long-term wealth building for million
[43:19] secured puts. I don't even know what
[43:20] that means. [laughter]
[43:22] [gasps]
[43:24] Um, okay. And then I can ask follow-up
[43:26] questions. Um, what mutual funds should
[43:32] I buy according to Brandon?
[43:37] It looks like there's fun stuff over
[43:38] here though. So, we have audio overview,
[43:41] slide deck, video overview. So, it's
[43:42] basically like all different ways of
[43:43] learning. I do think like I was using
[43:46] co-pilot really heavily this week for um
[43:48] helping me learn fabric IQ. Uh let me
[43:52] see work web. Um
[43:57] yeah,
[43:58] so I would always open it to the side of
[44:01] um the fabric docs and be like okay I
[44:04] you know I can't understand data
[44:05] warehouses. How would you compare it to
[44:06] things from other clouds? Right? So it
[44:09] was constantly helping me like
[44:11] understand, oh, is TSQL specific to
[44:13] Microsoft? How does Spark SQL compare?
[44:16] So trying to because when you're trying
[44:17] to learn something new, it helps to
[44:19] compare it to stuff you don't that you
[44:22] um already know like PowerBI. I don't
[44:24] even actually use PowerBI, right? So I
[44:26] was like, how does that compare, right?
[44:27] And like I know stuff like Tableau. Um
[44:31] so yeah, I do think like LLMs are like
[44:33] super helpful for learning, right? as
[44:35] long as you're actually asking it, you
[44:37] know, asking questions and and um you
[44:41] know, pushing back when you don't
[44:42] understand it. Um okay. Right. So here
[44:46] I'd be like, what is an ETF? Okay. All
[44:48] right. But then we can do other things,
[44:50] right? So you could do flashc cards,
[44:52] mind map. I of course want to make the
[44:54] mind map. Um, investing strategies from
[44:58] Brandon.
[45:17] I assume it grabs the transcripts for
[45:19] all these, too.
[45:24] This is pretty cool.
[45:26] All right. Investing mind map. Let's
[45:28] see.
[45:31] Okay.
[45:33] Investing strategies. Well, is it going
[45:36] to be more the big four? Oh, cute.
[45:40] Look at that.
[45:43] 40% S&P, 40% NASDAQ, 20% individual
[45:47] quality stocks. I'm not doing anything
[45:49] correct. [laughter]
[45:51] I don't know what a secured put is or a
[45:53] call option. Um,
[45:56] oh, good. Now I can find out what
[45:57] secured put is. Long duration.
[46:01] I I would have to do a lot of um
[46:06] Okay. Don't gamble. Don't gamble
[46:08] everyone.
[46:10] Risk management schmuck insurance.
[46:15] What is that? Oh, and then you can click
[46:17] on each of them to find out more.
[46:20] Well, that's pretty fun
[46:24] for his owning BR as a foundational
[46:27] layer.
[46:28] Okay.
[46:34] Oh, so he actually says 80% of your
[46:36] portfolio should be in the those
[46:37] indices. Okay. All right. So, yeah,
[46:42] this is cool.
[46:44] Um,
[46:46] do some flashc cards.
[46:50] Um how stocks how to in we'll just do
[46:54] the same thing investing strategies
[46:57] branding.
[47:08] I think I'm going to fail at all the
[47:10] flash cards.
[47:35] What? What is the secure put?
[47:42] Um, let's see.
[47:45] still generating. All right. A secured
[47:48] put puts sells a put option contract. I
[47:52] don't know what any of that means.
[47:56] What is the primary driver of stock
[47:58] prices in the long term?
[48:02] Okay. All right. So, this is the what
[48:03] does the river represent? I don't know.
[48:06] Okay.
[48:13] Yeah. All right, pretty cool. Um, I can
[48:18] see some good learning use cases and
[48:21] research cases here.
[48:24] All right, I think it's a quiet week
[48:27] this week. Um, but next week we'll have
[48:31] the, you know, the IQ series and next
[48:34] week there's going to be an office hours
[48:35] after every session. So, we'll have
[48:37] office hours Tuesday, Wednesday, and
[48:39] Thursday. Um, Wednesday will be with
[48:41] Aicha, but it'll be interesting because
[48:43] Aicha is in Dubai and apparently in
[48:46] Dubai you can't use Discord voice. So we
[48:51] I think um one of us is going to be the
[48:54] voice for AICHA and AICHA will be in the
[48:56] chat. Um but I didn't realize that Dubai
[48:59] um had that blockage. So there will
[49:01] still be an office hours but it'll be um
[49:04] maybe more text based because of the
[49:06] Dubai restrictions which is interesting.
[49:08] Uh, but yeah, we'll have office hours
[49:10] every day next week after the live
[49:13] streams at 10 a.m. each day. So, it'll
[49:15] be 10 a.m. live stream, 11 a.m. office
[49:17] hours. So, we'll do Tuesday Foundry IQ,
[49:21] Wednesday work IQ, and Thursday Fabric
[49:24] IQ.
[49:26] All right,
[49:28] so we'll close it up for today. Um, as
[49:33] always, uh, I will, you know, put the
[49:37] transcript and links and everything up
[49:39] on this link here, which is linked from
[49:41] my github.com/pamelafox,
[49:44] so you can usually find it the next day,
[49:46] everything we talked about and all the
[49:47] links. Um, I did also, there was a
[49:50] request last week for
[49:53] um the skill that I use to
[49:58] um to generate this. So I now I've got
[50:01] everything now everything is in this um
[50:05] should all be in this folder now. GitHub
[50:09] prompts.
[50:10] Wait, where is it actually? Let me find
[50:12] it. Office hours. Maybe I haven't pushed
[50:15] yet. Get status
[50:18] get GitHub posts.
[50:22] Oh, there it is. Python AI officers.
[50:25] Oh, wait. Let me just check. Okay, this
[50:28] one. Oh, this is the skill. All right.
[50:30] So, this is what generates
[50:33] templates.
[50:36] There we go. All right.
[50:39] Yeah. So, there was a question last week
[50:40] about how do I generate the weekly news
[50:42] web page and
[50:45] this is the skill for it. I did not
[50:48] directly write the skill. I just update
[50:49] it when I don't like something
[50:52] as is often the case for skills.
[50:55] Okay. All right. Thanks everyone for
[50:57] joining and I'll see you next week. Bye.

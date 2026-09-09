[00:00] Welcome everyone to our weekly Python
[00:03] plus AI office hours. This is our week
[00:06] of September 8th.
[00:08] As always, the way we'll do this is
[00:11] that, you know, I've got these um you
[00:14] know, our news roundup for the week. So,
[00:16] we'll start with this and see what it is
[00:20] that people want to talk about. If you
[00:23] have any uh questions, comments, things
[00:26] that you want to share, just go ahead
[00:28] and post it in the chat and uh and we'll
[00:33] we'll talk about it. All right, so news
[00:38] for this week. The big news uh was
[00:41] Astra. Yeah, [laughter]
[00:43] so Justin said it in the chat as well.
[00:46] Yeah, Astra is the big news. Um we've
[00:49] got, you know, multiple things about
[00:50] Astra here, right? So Astra uh rolled
[00:54] out to GitHub copilot. So I have used it
[00:57] both in the GitHub copilot app. It
[00:59] actually put together the these news
[01:01] here. So you can see uh it was
[01:03] interesting. I didn't mean to use it to
[01:04] generate the news round up because I did
[01:06] felt like it was a bit slower um or
[01:09] maybe it was just because it was being
[01:10] more comprehensive. Uh but it's always
[01:12] interesting to see what happens when you
[01:14] you know use a different model. Uh so
[01:16] I've tried it just for a couple things
[01:18] because it came out for Microsoft
[01:20] people. We didn't get it till I think it
[01:22] was like Friday afternoon or sometime
[01:24] late. So yeah, so we've got Astra and
[01:27] GitHub Copilot. Uh so you know check
[01:30] check that out. Um but then also we have
[01:33] it in Foundry, but in Foundry that is in
[01:36] like a limited I think that you do need
[01:40] to request request access for it. Um
[01:47] I thought that it was somewhat limited.
[01:49] Um,
[01:51] no preview. Interesting. It's not
[01:53] mentioning it's limited, but I thought
[01:55] that people told me elsewhere
[01:59] um that um you know that we couldn't
[02:02] access anywhere. So, let me actually
[02:04] just check to see if I can deploy it yet
[02:06] because I thought I thought that maybe
[02:09] it was limited, but maybe I'm thinking
[02:11] of a different one. Uh
[02:14] see in Foundry models. Okay, so let's
[02:18] see.
[02:20] If I can actually uh get it in here.
[02:24] [snorts]
[02:27] Find a one of my own foundry resources.
[02:32] Nope. Too slow. Let's just grab one
[02:34] here. Uh [clears throat]
[02:39] we have a lot now. Okay.
[02:45] You know, sometimes this is a good one
[02:47] that has access to things. All right, so
[02:49] let's go to models
[02:52] and Oh, that was weird. Okay, that
[02:56] didn't work. Um
[02:59] Oh, this is one I made last week. All
[03:01] right, let's try this one. Build
[03:04] build
[03:06] models.
[03:10] They What happened? Did they deploy? Did
[03:13] they delete our tenant and not tell us?
[03:16] Okay, things are being a little odd
[03:18] today in Foundryland. I don't know if
[03:21] this is a weirdness.
[03:24] Okay, let me try this one. Discover
[03:27] build models.
[03:30] Models.
[03:32] We'll do deploy a base model. Okay, here
[03:35] we go.
[03:38] Astra. So, I do see Astra here.
[03:42] And here we go. It says it's generally
[03:45] available context window a million. All
[03:48] right. So, deploy
[03:51] default settings. Okay. So, yeah, looks
[03:54] like we are able to deploy Astra from
[03:56] Foundry as well. Uh it doesn't look like
[03:59] there's a form for it. Um so, yeah. So,
[04:02] you should be able to use it. So, here
[04:05] I've got it in Copilot and we can see it
[04:08] in Cop Copilot. says very high cost.
[04:12] [laughter] Um, and [clears throat] we
[04:13] can see like the credits. I am told it's
[04:15] more token efficient. I think that's
[04:16] what my colleague said. Uh, you can see
[04:18] I was using it for
[04:20] um I was using it for this co-pilot app
[04:24] session as well. So you can see Astra
[04:26] here. Uh, so Astra came up with this
[04:29] this whole weekly news roundup
[04:32] and uh and yeah, and there's just the
[04:35] general Wow, they went really fancy with
[04:36] their launch blog post, huh? So, you
[04:39] know, there there's a lot of benchmarks
[04:40] in the blog post here. We've got
[04:42] terminal bench, arc AGI.
[04:46] So, they claim this is why I guess so
[04:48] Jensen had a tweet, Jensen Hong from
[04:50] Nvidia where he said that it is AGI. I
[04:54] disagree that it's AGI. Like I think,
[04:56] you know, this is just one benchmark
[04:58] that is called AGI and it has some
[04:59] interesting, you know, problems in it,
[05:01] but they're all problems that you can
[05:02] solve with programming. So I think Astra
[05:04] is very good at programming and
[05:06] programming problems. I I don't I do not
[05:10] personally think it's AGI. If any of you
[05:12] think it's AGI, defend it in the chat.
[05:16] Um Frontier Math, you know, also you
[05:18] very very good at math 100%.
[05:22] Uh they really wanted to max out these
[05:23] benchmarks. Terminal bench not as high.
[05:26] Um and then automation bench uh so quite
[05:29] high there. So, you know, I think it's
[05:32] obviously very good at using programs,
[05:35] programming to solve problems. So, I
[05:37] think it'd be particularly powerful for
[05:38] agentic coding and also just when paired
[05:41] with a code interpreter for like general
[05:43] agents. Uh, oh, here it's also I guess
[05:46] been trained very well for computer use.
[05:48] So, that would be good to test as well
[05:49] if you have computer use agents. Um,
[05:53] they so they had various examples. Now,
[05:55] on my Twitter timeline, everybody's
[05:57] using it for making 3D games with
[05:59] Blender. Uh, so if any of you enjoy
[06:01] [clears throat] making 3D games or also
[06:03] 2D games, I saw a lot of 2D games. So,
[06:05] for some reason, everyone, you know, is
[06:08] really having a great time using it to
[06:09] make Blender and games.
[06:12] Uh, so Justin says he had it run a
[06:15] project where it took 10 seconds to
[06:16] connect to computer and now it doesn't
[06:17] take more than one. Um, so the ability
[06:19] to review large problems seems to be a
[06:21] major improvement. Yeah, I think that I,
[06:23] you know, I haven't really tested it on
[06:26] large problems, you know. So, I think if
[06:28] you have a it's something that you
[06:30] generally um test on, then that's good,
[06:33] right? So, you know, planning like it
[06:35] should just be better at at planning it
[06:37] on its own, not necessar like so maybe
[06:38] you don't actually like uh Burke tweeted
[06:40] that he doesn't do an explicit planning
[06:42] step anymore with Astro or Fable because
[06:45] he trusts the agents to to know that it
[06:49] should come up with a plan itself,
[06:51] right? So you don't necessarily have to
[06:53] prompt it to do that. You don't have to
[06:54] like use a specific plan mode or
[06:56] planning process or planning skill. Uh
[06:59] you know it seems like the agents are
[07:01] tuned uh trained to to do planning
[07:05] themselves. Um so very good at tool use,
[07:08] computer use. Uh so you know there's
[07:11] various examples here.
[07:14] Uh
[07:16] and then
[07:18] yeah and then there's some improvements
[07:20] from the API side as well. Um so I was
[07:24] looking at um for example if you look at
[07:26] the OpenAI docs one of the updates is
[07:29] that now you can do midterm steering. So
[07:31] that means while a response is running
[07:34] uh you can just steer it in the middle
[07:36] of that response right because right now
[07:37] we have something called steering in um
[07:41] you know in our let me see if I can show
[07:43] it uh like when you're when it's working
[07:46] on something when you like hover over
[07:48] this uh send button you'll see the
[07:50] option to steer or cue. So steering is
[07:53] you know sending a message while it's
[07:54] still working. Queuing is queuing up a
[07:56] message go later. Uh so we already have
[07:59] steering in GitHub copilot but the way
[08:00] it's currently implemented is steering
[08:04] sends a message like after a tool call
[08:07] uh but if there's like a tool call
[08:08] that's taking a really long time or just
[08:10] a thinking process is taking a really
[08:12] long time the steering can't interrupt
[08:14] that currently except now it can right
[08:16] so that is something significant from
[08:18] the API side that they've added to Astra
[08:22] so that you know hopefully VS code can
[08:24] take advantage of that I don't know if
[08:25] it already is taking advantage of that
[08:27] but That would mean that VS Code if
[08:29] you're or or the Copilot app if you're
[08:32] working with Astra and you send a
[08:34] steering message it should be able to
[08:35] just immediately send that uh to the
[08:39] model right um
[08:42] uh and just you know it's and this only
[08:44] works because of websockets right
[08:46] because this relies on having
[08:47] birectional communications so you have
[08:50] to be having a websocket connection uh
[08:53] but VS code does take advantage of
[08:55] websockets so it hopefully Um, if it's
[08:58] not already, VS Code should be able to
[09:00] use me use midterm steering. Uh, that's
[09:02] a good question I can ask the VS Code
[09:04] team is, do we have this mid uh midterm
[09:07] steering? And same for Copilot app. Uh,
[09:09] they're increasingly sharing the same
[09:11] code base, so should help.
[09:14] Uh, so yeah, so that's Astra.
[09:20] Um, so, you know, really curious to hear
[09:22] people's experiences with it. as saying
[09:25] like I don't particularly see a big jump
[09:26] for me but I haven't tried it with like
[09:29] you know super hard tasks um you know
[09:32] I've tried it with things where soul was
[09:34] good and and that's what other people
[09:36] saying as well like you know soul is
[09:37] already very good right so do you need
[09:41] uh do you actually need Astra right so
[09:43] don't just use Astra for everything um
[09:46] uh you know so I think you figure out
[09:48] you know where it's good maybe use Astra
[09:50] at the beginning to come up with a
[09:51] really good plan and then maybe you pass
[09:53] it off to soul
[09:55] that would be one one possibility of how
[09:58] to use that. Uh and and I have a lot of
[10:00] colleagues that are also trying to use
[10:01] like Luna and Terra more because we're
[10:03] getting more uh limits enforced and more
[10:06] of our budgets enforced. So, you know,
[10:09] maybe you do your upfront planning with
[10:11] Astra and then you pass it off to to one
[10:14] of those smaller models.
[10:17] Uh so there is Astra related to that was
[10:22] um I you know we talked about this last
[10:25] week was the hugging face incident.
[10:28] There was an update like there's an
[10:29] update that there was more attacks that
[10:32] happened uh or not necessarily attacks
[10:34] but basically like hijacking wiks all
[10:38] over the web. Uh so this came out last
[10:41] week about all these incidents. So uh
[10:44] really what we see is the agents, you
[10:46] know, OpenAI was running these agents to
[10:48] test things out. They were just not well
[10:50] sandboxed. So this really shows you the
[10:52] importance of a very good sandbox. Um so
[10:56] you can see uh that they were able to
[10:59] hack something that was built off of CGI
[11:02] and PHP um which used get requests to
[11:05] change data. and the sandbox allowed
[11:09] allowed um all get requests because it
[11:11] assumed all get requests um were you
[11:14] know okay but you can't assume that you
[11:16] can you can easily implement an HTTP
[11:18] server that uses a get request to change
[11:20] data right so you know generally a get
[11:23] request is for reading and a post
[11:25] request is for changing but you can do
[11:27] all sorts of things on your own server
[11:29] right and there are these servers that
[11:31] um you know let you change things with
[11:34] get requests right so the sandbox box
[11:36] allowed that through and then also they
[11:39] did this crazy rewrite. I still don't I
[11:40] don't entirely understand it but it was
[11:43] like the agents were limiting the
[11:46] traffic based off of domains but then it
[11:48] was able the agent was able to edit its
[11:50] own etc host file um in order to make it
[11:55] look like a valid thing. So that that
[11:56] would be the other thing to check is can
[11:58] your agents in their sandbox can they
[12:00] edit their etc host file such that they
[12:03] can bypass the proxy.
[12:05] So I thought this was really interesting
[12:07] like I and also one thing I was playing
[12:08] with last week was the new container app
[12:10] sandboxes. So, I haven't done this yet,
[12:12] but one thing I want to do is point um
[12:15] you know, point GitHub copilot at this
[12:17] this blog post here and say, "Hey, um
[12:20] you know, uh can you try to break out of
[12:24] your sandbox with these techniques?" And
[12:26] I'm going to assume it can't because I
[12:27] think our our container app sandboxes
[12:30] are implemented better than um however
[12:35] they implemented, you know, this one
[12:36] because I don't think they I don't think
[12:38] they implemented it super well. But it
[12:40] really shows you that you have to do a
[12:42] very very good job with sandboxing. Like
[12:45] that's a big takeaway. I also one thing
[12:47] that I would recommend is um Dwarash's
[12:52] um
[12:54] uh let me find the no it um he had
[12:58] Darwash Patel had a
[13:02] interview with AA from this yeah
[13:12] uh this interview with AA Kotra from
[13:15] Meter they're the ones that did the
[13:18] investigative report into the agent
[13:21] incident. And this is a really inter
[13:25] interesting chat with, you know,
[13:26] basically the person who did the
[13:27] investigation. And she finishes up with
[13:30] some recommendations for how to um, you
[13:34] know, properly sandbox sandbox agents.
[13:40] Okay. Uh, all right. So, that's on the
[13:42] astronome. I did see there was a
[13:44] question in the chat about
[13:50] any resources on evaluating workflows.
[13:55] So a workflow I usually think of that as
[13:58] being a um you know like a a chain
[14:04] together of um of of calls. Some of them
[14:09] to LM, some of them maybe not to LLMs.
[14:12] Uh let me see if I have done an
[14:15] evaluation of a workflow. Normally I've
[14:17] done evaluations
[14:19] of um
[14:22] agents uh posted agent framework demos.
[14:25] Let me look at this one. Uh
[14:33] yeah, I think this was of the agent. Um
[14:37] yeah, so with workflows, workflows are
[14:39] going to be a lot more um you're going
[14:42] to like want to customize your
[14:45] evaluations. Uh so you may want to do
[14:50] uh probably want to come up with a
[14:52] custom custom evaluator. Um there are
[14:55] some like I mean Foundry has all these
[14:58] built-in evaluators like task
[14:59] completion. Um there's all these tool
[15:02] call specific ones. That one you
[15:04] probably wouldn't use because that's
[15:05] very specific to an agent calling tools.
[15:07] Uh intent resolution that is, you know,
[15:10] pretty generic. Task adherence is also
[15:13] generic, right? So there are generic
[15:15] ones like intent resolution, task
[15:17] adherence. Um so you could start off
[15:19] with those built-in ones. Um but you you
[15:23] pro you I think generally you want to
[15:25] come up with your own evaluation. So it
[15:26] really depends what your workflow is
[15:27] doing, right? Is your workflow, you
[15:29] know, what is the output from your
[15:31] workflow? Do you have a you know exact
[15:34] expected output like is the output a
[15:36] natural language response? Is the output
[15:37] a classification? Is it an extraction of
[15:39] data? Like I don't know what your
[15:42] workflow looks like. Um but generally
[15:44] like if your output is structured data
[15:46] then you can just write in a val which
[15:48] is like hey for this input we're going
[15:50] to you know get these outputs. Um if
[15:52] your output is natural language
[15:55] responses, well then you have to use LM
[15:57] as judge and then you really need to
[15:59] have a lot of good um examples of the
[16:02] input and output and uh you know how the
[16:06] ways it can fail, right? Um in Foundry
[16:08] there's two different ways to help you
[16:10] like make better evaluators. So if you
[16:11] go to evaluation there is the uh custom
[16:14] rubric evaluations here, right? So you
[16:18] could create this rubric evaluation and
[16:20] this one you can, you know, it'll
[16:22] actually try to um help you come up with
[16:25] the evaluator and you can even point it
[16:26] at your uh at your
[16:30] um you know at your traces in as your
[16:33] monitor and it'll come up with it. Um
[16:37] uh or um the other thing you can do if
[16:40] you want to start more local Microsoft
[16:43] assert is a open-source
[16:48] um you know basically an open source way
[16:50] of doing something similar that does try
[16:52] to help you with the bootstrapping
[16:54] process right because one like sometimes
[16:55] people struggle with trying to figure
[16:56] out like a bunch of um synthetic data to
[16:59] start off with and so assert will come
[17:01] up with different like user personas
[17:04] um and different lots of different
[17:06] situations and suggest uh an evaluation
[17:08] rubric. So, um you know, I think you're
[17:11] you're going to come up with something
[17:12] custom. It's easy if you're workflow
[17:15] outputs structured data. Um not as easy
[17:19] otherwise because you do need an LM as a
[17:21] judge. Um you know, and I would check
[17:23] out these more the more recent ways of
[17:25] doing eval which would be um these kind
[17:28] of rubric based evaluations. So, both of
[17:31] these assert and
[17:35] Um
[17:37] and foundry rubric evaluations
[17:40] can be [clears throat] ways you can do
[17:42] it. But you can also like really like um
[17:45] you know you can you can build your own
[17:47] eval framework as long as you're
[17:49] following best practices for evals right
[17:52] like what matters most is like are you
[17:53] following best practices right so you
[17:55] can also um Hamal Hussein has this eval
[18:00] skills
[18:01] uh
[18:03] uh agent skill and MCP server
[18:07] um eval skills okay right so if you want
[18:12] to you know you can use our specific
[18:13] thing offerings and they're nice because
[18:15] they integrate well with foundry but you
[18:17] can also just make sure you're doing
[18:18] best practices best practices because
[18:20] these you know the modern models they're
[18:22] very good at coming up with eval so a
[18:24] lot of times I just end up writing my
[18:26] own evals and I just try to follow um
[18:30] you know best best frameworks here right
[18:33] so if you're writing your own evals then
[18:36] what you can do is you know uh install
[18:39] this uh agent skill I think it also has
[18:41] MCP server now and um yeah and it can
[18:46] help you through the general process
[18:48] right and use all the best practices
[18:51] that they have learned from um you know
[18:55] coming up with evals. Uh so a lot of it
[18:58] is being able to look at look at the
[19:00] actual data look at the problem um and
[19:03] [clears throat] and come up with with
[19:05] good evals for it.
[19:09] Uh the hardest part is just coming up
[19:11] with the data, right? It's great if
[19:13] you've got good data to start off with.
[19:15] A lot of people don't. That's why, you
[19:17] know, assert tries to help with coming
[19:19] up with that data. Um if you do already
[19:22] have data, then you know, you're able to
[19:24] do error discovery on it. So you can
[19:26] look at your traces to find the failure
[19:28] modes. Uh so that's really the hardest
[19:30] part is figuring out what your data is
[19:32] going to be that you're basing these
[19:34] emails on and figuring out the success
[19:36] and failure modes.
[19:40] All right, let's see. Uh, sure. Yeah,
[19:44] let's Okay, so other what other news do
[19:47] we have for this week? Um, so going
[19:53] uh let's see, going back to uh aentic.
[19:58] Well, what do people want to talk about?
[19:59] [laughter]
[20:00] I do want to show image editing because
[20:02] I do love the MI image models because
[20:05] we're always talking about like the
[20:06] LLMs, but the the MAI image model is
[20:09] just so good for photograph stuff. So,
[20:12] um I updated my image editing skill in
[20:16] my presentation skills repo. Um but
[20:19] really I use this image editing skill
[20:21] for for all kinds of things. I just
[20:24] stuck it here. Um, but this is
[20:26] generating images using MII image 2.5.
[20:29] And it's got kind of a little convenient
[20:31] script for doing it. And it can do it
[20:33] based off of just a prompt or also of an
[20:36] input image, right? So, if we go here,
[20:39] we can, you know, see a little a little
[20:41] Python script for it. Um, so I was using
[20:44] it this week. Actually, this was pretty
[20:47] fun. like my contractor was working uh
[20:51] at my house and I I wanted him to
[20:55] uh install a new fence in the garden and
[20:57] I was having a hard time trying to
[20:59] describe like you know what I wanted
[21:00] that fence to look like. So while he is
[21:02] there I was just iterating um you know
[21:05] back and forth uh with you know with the
[21:10] with him with the model. So the way I
[21:12] set this up is that you know I created
[21:13] that image skill that knows how to use
[21:15] an MII image model from Foundry
[21:18] installed that skill and then in Copilot
[21:21] using soul I was like okay soul you're
[21:24] going to you know use this to I was like
[21:26] you have an image gen skill right like
[21:28] you always like want to start off and be
[21:30] like make sure your skills are are
[21:31] installed of course you can also click
[21:32] on the skills but the customize menu
[21:35] here and check and so here we can see
[21:37] that it had an image skill but I always
[21:39] like to ask the model
[21:41] Um and then uh and then first I had to
[21:44] modify the skill to accept images blah
[21:46] blah blah set it up. Okay. All right. So
[21:49] then I was like um uh I told it to I
[21:54] don't see the original query but I told
[21:56] it to you know start making a fence
[21:58] right and doing a lot of iteration with
[22:01] it. So here what I'm using is I'm using
[22:03] soul to come up with the prompt for the
[22:09] skill. Right? So you can see here soul
[22:12] decided on the right prompt right and
[22:14] soul decided whether it was going to run
[22:17] this prompt on an existing image or
[22:20] whether it was going to run it without
[22:22] like because I we started off with this
[22:24] an input which was just um not that the
[22:27] bare input was this right um so we start
[22:31] off with just this and say hey right I
[22:33] want a fence on this and then you know
[22:36] soul would decide whether to pass in
[22:38] this bare image or pass in one of the
[22:40] ones along the way, right? Because these
[22:42] are all these like images it came up
[22:44] with along the way. And so I'd be like,
[22:46] "No, I want, you know, change this,
[22:48] change this, change this." Uh, so it was
[22:50] it was nice to have an LLM helping with
[22:54] the prompt for the image model and
[22:56] experimenting with different things.
[22:58] Now, this image is really interesting. I
[23:00] just want to zoom in on it. This is
[23:02] clearly one where it had been based on
[23:04] previous inputs because you see I don't
[23:06] know if you can tell at this resolution
[23:08] but it it's all triangulated in the back
[23:10] here. And I think this is this is one of
[23:12] the risks of like passing in continually
[23:15] passing in the input from the last one
[23:16] is that eventually it became like
[23:19] tessillated like this looks like a
[23:20] triangle tessillation right so uh you
[23:23] know it was fine for the purposes but uh
[23:26] you know it's just very interesting to
[23:28] see what happens when you're you know
[23:30] iterating with these models and agents.
[23:33] Uh and then so Bernard says can you
[23:35] create a 2D CAD drawing from it to
[23:37] constructing it? This is probably where
[23:39] I should use Astra because when I worked
[23:41] with that contractor before, I did have
[23:43] to make a CAD um drawing in, um this
[23:46] program, uh SketchUp, and I had to do it
[23:50] from scratch. It was a lot of work. Um I
[23:53] do have a background in 3D modeling, but
[23:54] it' been like 20 years. Um so, uh okay,
[23:58] so Justin says, "Open SCAD." Okay, I
[24:01] haven't used that one. Um,
[24:04] my contractor asked me for a list of
[24:06] supplies and I gave him the list but I
[24:08] was like I don't think the measurements
[24:09] are right. Like I think if I wanted
[24:11] correct measurements I should have put a
[24:12] tape measure down or like added a tape
[24:14] measure after to make it clear because
[24:16] that was one of the struggles is that it
[24:18] felt like the agent didn't understand
[24:20] like three feet tall, right? I kept
[24:22] saying three feet tall and I'm like nope
[24:24] that's too tall, right? So I think it
[24:26] really would have helped to have you
[24:28] know a banana for scale something for
[24:30] scale where like you know this is what
[24:31] it is. Uh so Justin says people are
[24:34] using open SCAD uh with uh Astra. That
[24:38] would make sense. I was saying like
[24:39] Astra is good at 3D models. So you know
[24:42] that could be if I really if I did truly
[24:44] need a 3D model of this um then I could
[24:48] try um presumably it it has its own
[24:51] scripting language, right? A lot of
[24:53] these 3D programs have their own
[24:54] scripting language. Like when I was in
[24:56] college, I would use uh Maya with Mel,
[24:59] which is its embedded language, or 3D
[25:01] Studio Max with Maxcript. And of course,
[25:04] Blender has its own scripting language,
[25:06] and that's why everyone's going crazy
[25:07] with with Blender. So I would try um
[25:11] yeah. So you could try like generate
[25:15] um an open sk
[25:17] with it. Um and and work through the
[25:22] things. Um let's see. I don't know how
[25:25] quickly I can open it. Um
[25:28] okay, I'll open it in the background for
[25:30] fun. I was telling people I was like,
[25:32] "Oh, I don't have a 3D thing on my to-do
[25:34] list." But maybe I do have a 3D thing on
[25:35] my to-do list. [laughter] All right. So
[25:38] we see a question is is GPD6 Astra only
[25:40] available through the agents endpoint
[25:42] and not through the messages endpoint.
[25:43] Well messages do you mean enthropic
[25:45] messages? We would never have any open
[25:47] AI models available through messages. Uh
[25:51] it's generally foundry uh sorry
[25:53] responses foundry models discover. Oh
[25:56] that compare thing is so bad. Uh sorry I
[26:00] let me let me look at it. Um yeah like
[26:03] the checklist of stuff. Uh models. Okay.
[26:06] So, let's do like if we look at Astra,
[26:11] what does it say? Um, it says chat
[26:15] completion and responses. Yeah. So,
[26:17] that's what I would expect is that
[26:18] generally the OpenAI models, we always
[26:20] support the chat completion API, which
[26:22] is the older API, and then the responses
[26:23] API, which is the newer API, which is
[26:26] the one we recommend with um when you
[26:29] can. It's got a lot of benefits to it.
[26:31] And I've ported all of my samples over
[26:32] to responses API.
[26:34] Um the messages endpoint is just for the
[26:38] enthropic models because it's enthropic
[26:40] messages. Like if we look at this one,
[26:42] it'll say messages
[26:45] uh here, right? Because that is the
[26:48] enthropic messages API and that's how
[26:51] Enthropic wants you to use all of their
[26:52] models because it has uh customization
[26:55] specific to enthropic models and
[26:58] features that you can enable with it.
[27:02] Uh oh, he's saying it shows a bit
[27:04] different. Okay, so let's try a
[27:05] comparison. Yeah, I have to warn you the
[27:07] comparisons don't are not perfect. I
[27:10] complain about them all the time. So
[27:12] probably this will just give you another
[27:13] thing to complain about. So let's try it
[27:15] out.
[27:17] Um so Fable, so you did like Fable 5.1.
[27:21] Okay, so here. Yeah, I mean look at
[27:24] this. Like it claims like input for
[27:26] Fable is code, but not for this one.
[27:28] Like that's I mean obviously you can
[27:30] input code into both of them. Um okay
[27:34] token output messages
[27:37] agents. Okay. I think what this means is
[27:42] um okay [clears throat] I'll tell them
[27:43] that this
[27:46] I see it doesn't say responses here. All
[27:49] right. The good news is I'm on campus
[27:52] now so I can directly find the people.
[27:54] I'll see if they're on campus today. Um
[27:57] yeah. Why is it not showing?
[28:00] Maybe agents is now the code word for
[28:04] God, that's confusing. Okay. All right.
[28:06] I didn't know that they'd change this.
[28:08] This this basically if I was going to do
[28:10] this, I would have messages, no, chat
[28:12] completions, yes. Responses API, yes,
[28:14] for the open ones. And then, yeah, I
[28:17] don't know why this is showing agents.
[28:18] This is so confusing.
[28:21] Okay, I will I will uh talk to the team
[28:25] afterwards.
[28:27] to ask what the heck that's supposed to
[28:29] mean. Um
[28:31] may because maybe that's supposed to
[28:33] indicate compatibility with the foundry
[28:36] prompt agents. That might be what that's
[28:39] supposed to mean because it's true that
[28:41] you can I I believe it's now true that
[28:44] you can use both these models with
[28:45] Foundry prompt agents. Um but that is
[28:48] that is definitely confusing and the
[28:50] fact that we're not seeing responses API
[28:52] or chat completions API called out here
[28:54] at all. So, I don't Yeah, I don't know
[28:56] how a mere mortal is supposed to
[28:58] interpret this. I don't even know how to
[28:59] interpret that.
[29:01] Good call out as your AI agent. Okay.
[29:05] Yeah, I think they're basically saying
[29:07] prompt agents, right? But I think I just
[29:09] think that's confusing. Um, there's got
[29:11] to be a better way we can do that.
[29:15] Uh,
[29:17] yeah, I will certainly bring that up.
[29:20] And then I think we don't have the
[29:22] benchmarks yet just because 5.1 only
[29:24] just got added. Yeah. So, so there if we
[29:27] go back to this one. Okay. So then we
[29:29] can see benchmarks. [snorts]
[29:32] Cool. All right. Great call out. Thank
[29:34] you for that. Didn't know that they had
[29:36] messed with that some more. Um yeah,
[29:39] don't put too much faith in the
[29:42] in this, right? Like
[29:45] uh I don't know. I just think it's often
[29:48] not perfect. Um especially like here,
[29:51] right? Um I think this stuff should be,
[29:53] you know, reasonable.
[29:56] Uh cool. Any Let's see what else. Okay.
[29:59] Um
[30:01] so
[30:04] yeah, lots of stuff actually. I mean
[30:05] there's uh Hydro Fusion. I don't know if
[30:08] anybody looked into that yet. I saw a
[30:11] demo of it last week. I didn't try it
[30:12] out yet. Um Oh, right. I didn't try it
[30:15] out yet because it's only in the Copilot
[30:16] CLI. They didn't add it to the other
[30:20] things yet. So that's why I haven't
[30:21] tried it yet. Um, but if you are a user
[30:23] of the copilot CLI, then you can enable
[30:26] this. You have to turn on experimental.
[30:28] So it's very very experimental. This is
[30:29] like from our research team, right? So
[30:32] you can turn it on uh update your CLI,
[30:36] turn on experimental, change your model,
[30:38] and select hydrofusion. So it's being
[30:40] treated as like a model selection, but
[30:42] it's actually more of an orchestration
[30:44] selection. So what it does is that it
[30:47] does some task routing and says like
[30:49] okay I'm looking at this task and I
[30:51] think it's this kind of task right it's
[30:53] a code generation task it's a debugging
[30:55] task whatever and then it decides is it
[30:57] going to use a single model to solve it
[30:59] is it going to use a cascade where it
[31:01] does a draft and then it has a judge
[31:02] model and then potentially repairs it um
[31:05] or is it going to do a rubber duck where
[31:06] it has a draft and then it has a um a
[31:09] critic and a repair. Those actually
[31:11] sounds really similar to each other
[31:13] [laughter] after I've said it. So um not
[31:17] exact they sound so similar right
[31:19] optional repair versus revision. So I
[31:22] don't know those sound very similar um
[31:25] and then it implements it right. So this
[31:27] is kind of another take on auto. Auto
[31:29] just does model selection. This is an
[31:31] auto that's selecting an orchestration
[31:33] pattern because there's a lot of people
[31:34] that have basically kind of implemented
[31:36] them that this sort of thing themselves.
[31:38] Um but um you know they're trying to see
[31:42] if this is something they can do for
[31:45] everyone. Um and you know they see some
[31:48] improvements with the with the
[31:50] benchmarking. Uh but the thing is if
[31:53] you're already doing a lot of
[31:55] customization of your models and your
[31:57] sub aent usage and your planning and all
[32:00] that stuff, you may not like necessarily
[32:02] see improvements from this um because
[32:05] you're already customizing stuff so
[32:06] much. But for the many people who don't
[32:08] do any sort of customization at all,
[32:09] they kind of just just go with the
[32:12] default. The goal is that Hydro Fusion
[32:14] would pick the right orchestration. Uh
[32:17] and I think they'll add more
[32:18] orchestration patterns over time. And
[32:20] ideally, I think they're hoping to add a
[32:22] way that you can kind of build your own
[32:24] orchestration pattern, but that might be
[32:25] hard to route to. So, we'll see. Um
[32:28] [clears throat] yeah, so the question
[32:30] is, will Hydra Fusion be rolled out to
[32:31] GitHub Copa chat in the future, too?
[32:33] Yeah, as far as I understand, it will.
[32:34] That was a big question. um that we
[32:38] uh had during the the team um that they
[32:44] want to bring it out to
[32:48] the rest of co-pilot. I'm just seeing if
[32:50] they mention that here
[32:52] in the post. Okay, they don't promise it
[32:55] in the post, but it did seem like when
[32:58] we asked them about it that they said
[33:01] they were, you know, working on bringing
[33:03] it to the other the other places as
[33:06] well. I'll just double check that we
[33:08] didn't like get it agent.
[33:12] Yeah, I think it would show up here. Um,
[33:15] so yeah, I think that should be in the
[33:17] works. Um, I don't use the cop cli at
[33:20] all anymore because we have the copilot
[33:22] app and to me the copilot app is the the
[33:25] nicer approach. You get this nice UI and
[33:28] you know you get the the terminal like
[33:30] uh you you can see everything. You can
[33:32] see the terminal, the web browser, all
[33:33] of that stuff. So for me there's, you
[33:36] know, not um a good reason for using the
[33:39] Copot CLI anymore. I think you have to
[33:41] really like CLIs to use a copod CLI
[33:43] because you get the same harness from
[33:45] the copod app and you get the same um
[33:48] you know multi- aent stuff, right? So I
[33:50] use a copod app whenever I'm doing these
[33:52] kind of like short little things that
[33:54] are you know easy and I don't have to
[33:56] dig into the code.
[33:59] All right. Uh
[34:02] what else I want to mention?
[34:06] Um Nvidia is acquiring hugging face.
[34:08] That'll be fun. Um, Python 315 is going
[34:13] to be released in October. Uh, so we
[34:16] should be moving on. If you're on like
[34:18] Python 312, that's like old news, right?
[34:20] So try and move closer and closer to
[34:22] 315. Of course, a lot of packages often
[34:24] aren't ready yet in in, you know, when a
[34:28] thing first comes out. So, usually I'm
[34:30] like one one um version behind so that I
[34:34] can have all the packages ready. Oh,
[34:36] this was exciting. skills over MCP.
[34:41] Uh so skills over MCP because everyone's
[34:44] always asking about MCP versus skills.
[34:46] So this is a proposal
[34:49] to um integrate skills into MCP so that
[34:55] an MCP server could expose skills as a
[34:58] kind of resource. Um, and so if an MCB
[35:03] server knew for sure that there were
[35:06] particular skills that it wanted anybody
[35:08] using that MCB server to be able to
[35:10] access, then they could expose that as
[35:13] skills. Um, so that has been approved
[35:16] and that's, you know, now they're going
[35:17] forward with, you know, making it
[35:19] formally [clears throat] part of the
[35:20] spec. Justin says, "Agent plugins suck."
[35:23] I agent, right? So Justin reported some
[35:26] issues with agent plugins. I did get
[35:27] back, I didn't message this yet to
[35:29] Justin. Um, I did get back a response
[35:33] from the because we found we we tested
[35:37] out agent plugins
[35:39] um, you know, a few weeks ago. Um,
[35:42] sorry, my Twitter mentions are very
[35:44] random. Um, and I chatted about it with
[35:48] Max. There we go. Okay. All right. So,
[35:52] here was the answer. So, okay. So, for
[35:55] context here, a few weeks ago, we tried
[35:57] out agents plugins. So agent plugins is
[35:59] another approach where you can if you
[36:02] you know have some skills, you have some
[36:04] MC servers, you can bundle them together
[36:06] into a single plugin and you have a
[36:08] manifest that makes them stalled, right?
[36:10] And so we were trying it out in all the
[36:12] clients that came claim they're
[36:14] compatible like Cursor, GitHub,
[36:15] Grockbot, uh Curo, VS Code. So we were
[36:18] trying in chat GBT because Justin had
[36:20] played with it. Um and so you know we
[36:23] found a bunch of issues with chat GBT.
[36:25] So this is uh Max from OpenI. He says
[36:28] for chat web um they only support
[36:31] importing plugins from c from GitHub for
[36:34] business and enterprise workspaces.
[36:37] Um and for desktop it says you should be
[36:40] able to prompted to import an agent
[36:42] plugin
[36:44] um
[36:46] into your plugins folder. Okay. So we
[36:48] were struggling with two things was one
[36:50] was just how to import it at all from my
[36:52] GitHub repo and then two was making sure
[36:55] the agent plugin exposed both skills and
[36:57] MCP. So I don't know if this was a full
[36:59] response for the issues we ran into. Uh
[37:02] so yeah I think the support for agent
[37:04] plugins um are not not as um consistent.
[37:13] I think this the the the yeah the
[37:16] support is not as consistent for how do
[37:18] you install agent plugins um which which
[37:21] of the clients supports them. Um you
[37:25] know hopefully that improves. Uh yeah
[37:27] the nice thing about MCP servers
[37:29] exposing skills is that that should
[37:31] hopefully be more consistent.
[37:34] Um yeah, so I was saying like that yeah
[37:36] the import approach is is very it was
[37:40] hard to figure out how to import right
[37:42] everybody has a because this is
[37:43] generally an issue with um also with MCP
[37:47] like you know anytime you know you can
[37:49] define how the agent protocol works like
[37:52] how things go over the wire but as soon
[37:55] as there there's a UI for something it's
[37:57] really hard to define a standard for
[37:58] that because you know agent interfaces
[38:01] are so different um and you can have
[38:04] like best practices. So I think it would
[38:06] be nice for users generally if there's
[38:08] more consistency. Uh but yeah for I
[38:11] think for chatd is particularly
[38:12] confusing because they don't support it
[38:15] the same across everywhere. Um and for
[38:19] right so they don't even chapd web I
[38:22] wasn't even able to do it because I
[38:23] don't have a business or enterprise
[38:25] workplace right. Um
[38:28] and then for you know for codeex you can
[38:33] do it. Um but that means you have to
[38:35] download the app.
[38:38] Uh okay so Justin says if MCP supports
[38:41] skills that would solve the problem you
[38:43] have. Yeah. So if you're shipping a
[38:44] single MCP server and those skills are
[38:46] tightly bundled bundled with that MCP
[38:48] server then you know this should this
[38:52] should be you know what um you know what
[38:56] you what you need right let me link to
[38:59] the discussion here um the and so then I
[39:05] would think we would only use agent
[39:07] plugins where you know you're bunding
[39:09] together uh multiple MCB servers
[39:12] multiple skills
[39:13] or you know there's some reason why you
[39:15] want to have like kind of different
[39:16] permutations of bundles because you may
[39:18] not always want particular set of skills
[39:20] the MCP server but if it is a tightly
[39:22] coupled skill for that MCP server then
[39:27] uh you know it makes sense to expose it
[39:30] over MCP uh so I'm sure it's going to
[39:32] take some time for everyone to catch up
[39:34] uh all the clients to catch up but
[39:36] generally things do work pretty pretty
[39:39] um quickly oh Vizo I'm going to see him
[39:42] today. He's going to present tomorrow
[39:44] for MP's stream. So that's cool that
[39:47] he's involved on this one. I think Sam
[39:50] Mororrow has also been Yeah. So Sam
[39:52] Mororrow, he's also presenting tomorrow
[39:53] and Katie and Claire. Oh, look at all
[39:56] these people we and Den. All right. So
[39:59] yeah, tomorrow we have the MCB live
[40:01] stream and we have basically like all
[40:02] these people presenting for that MCB
[40:05] liveream. Um
[40:08] uh lots of people here with good
[40:09] opinions. Uh so uh yeah, so that'll be
[40:13] exciting. I think Sam has been working
[40:15] particularly over this because he uh Sam
[40:18] from the GitHub MCP server uh was asking
[40:20] me for some ideas about what skills
[40:23] would you want to see in a GitHub MCP
[40:24] server. So if any if any of you also
[40:26] have ideas like what what skills like
[40:28] really really belong in the GitHub MCP
[40:30] server, right, that are so generic that
[40:33] you know every or like a large
[40:35] percentage of people using the GitHub MP
[40:37] server would want to use those skills.
[40:38] Uh that would be good feedback for the
[40:40] GitHub MCP team in terms of deciding
[40:43] what to expose because I think it's hard
[40:44] because skills like I always recommend
[40:46] people like you know check out my skills
[40:48] but then fork them for your own scenario
[40:51] so that you can really really
[40:52] personalize them. Um because skills you
[40:55] know skills are so to me they're very
[40:57] personal like you want like if you have
[40:59] a certain you know ex like output you
[41:02] want like you really want to tweak it
[41:04] for it. Um, so it I think it is a bit
[41:06] tricky to figure out what are the skills
[41:08] that are generic. Um, but I think you
[41:10] you'll find some like when you see
[41:12] patterns across users that are using an
[41:14] MCP server, you can see patterns and
[41:17] what skills might be useful for them.
[41:21] All right. Uh, let's see. Um,
[41:28] I thought just this was really fun. Um,
[41:31] linguistic drift. I was ranting about
[41:33] this last week. Like I have I think that
[41:35] the code that's coming out of modern
[41:37] LLMs is pretty darn good. The text, like
[41:41] the English copy, like the natural
[41:44] language responses, uh the written, you
[41:46] know, the things that they're writing is
[41:48] not good. And I'm getting very
[41:51] frustrated with people who are like
[41:52] entirely writing their readmes and their
[41:54] docs and their blog posts and all of
[41:56] this with an LLM and then not doing an
[41:58] edit pass at all and just passing it off
[42:00] to me and expecting me to read, you
[42:02] know, this horrible u LLM dialect. I was
[42:06] like, I don't want to read this LLM
[42:08] dialect, right? Uh so this was
[42:10] interesting blog post where um you know
[42:13] he this guy from podantic he analyzed
[42:16] the word seam in particular because this
[42:18] is one of those words that you know we
[42:20] see in LLM speak that we don't naturally
[42:23] actually use that much um typically as
[42:26] software engineer and also the word
[42:27] boundary I'm like I'm done with the word
[42:30] boundary like it doesn't mean anything
[42:31] to me anymore I don't know so uh you
[42:34] know here he tracked like the use of
[42:36] seam over time
[42:38] and you you can see it like shoot up in
[42:41] the last year, right? Like in GitHub
[42:43] code and comments because it's coming
[42:45] from the LLMs and he tried to figure out
[42:47] what was the the patient zero and it
[42:50] looks like it's opus 4.6. So basically
[42:52] for some reason opus 4.6
[42:54] picked up on this word seam and it
[42:57] became part of its reinforcement
[42:59] learning and you know it started output
[43:01] it and then once OPUS 4.6 six was
[43:03] outputting this word seam then it became
[43:06] part of the training data for the next
[43:08] you know the next LM right and this is
[43:10] one of the issues with this is why we're
[43:11] seeing what they're calling linguistic
[43:13] drift right like that are you know the
[43:16] LMS are outputting text that is being
[43:19] incorporating into you know GitHub code
[43:23] which becomes part of the training data
[43:24] for the next one and then the LM thinks
[43:26] oh everybody uses the word seam I'm
[43:28] going to use the word seam too and right
[43:30] so increasingly we're having a harder
[43:32] time understanding this LLM speak
[43:33] because that's not the way we would have
[43:35] written it, right? And that's the other
[43:37] edit like issue with just letting LM
[43:40] just write and not edit it is
[43:43] contributing to this linguistic drift,
[43:45] right? Um, and so it just gets like
[43:48] worse and worse and worse to the point
[43:49] where eventually we're just not even
[43:51] going to understand [laughter]
[43:52] what they're saying at all. I barely
[43:54] understand it now. Um uh yeah, so they
[43:58] did a bunch of a bunch of work into it
[44:01] and then they made actually a tool
[44:03] called um
[44:07] they made a tool called vocab guard uh
[44:10] just for pragmantic AI or you can use it
[44:11] separately. Um and it tries to it
[44:15] attempts to see if it detects that the
[44:19] um you know the output is using you know
[44:24] LLM speak um you know something like
[44:28] seam and [snorts] then you know rewrites
[44:30] it. So I don't know that vocabguard is
[44:32] actually the right approach to this but
[44:33] I did think this was a very cool uh
[44:36] investigation and exploration and I
[44:39] think we should all keep this in mind
[44:42] that um you know I I that LLMs are
[44:46] increasingly creating really nice code
[44:48] that generally aderes to best practices
[44:51] um but the text
[44:54] is getting weird and getting hard to
[44:58] understand and Um you should uh always
[45:02] have a um either be actively countering
[45:06] that with you know system prompts like
[45:08] you know use simple English or use this
[45:10] kind of English or act like Hemingway
[45:12] like people have different approaches.
[45:14] Uh also somebody said that Muse Spark
[45:17] actually has good output right and they
[45:18] like Museark. So, you know, just really
[45:21] take a careful look at the actual pros
[45:23] that's coming out from these models and
[45:25] whether you, you know, want to rely on
[45:27] that pros.
[45:30] Uh, oh, let me link to this, too.
[45:34] What else? We got a few minutes left.
[45:38] Um,
[45:44] um, all right. So, we'll just talk about
[45:49] the Oh, oh, I do want to mention too
[45:51] because remember we played around with
[45:53] Copilot in Teams. So, let me see if I'll
[45:58] let you try to Okay, I want to try and
[46:00] show you because I did actually I have
[46:02] been using Copilot in Teams a bunch more
[46:06] to really like put it to the test. Um,
[46:08] and I made like a channel for it and
[46:10] stuff. So, let me try. Okay, I'm gonna
[46:14] try and uh
[46:16] get it open without
[46:19] showing. Okay. Blah blah. All right.
[46:22] Don't look at anything. Okay. Discover.
[46:23] [laughter]
[46:24] Uh how do I Okay. Here we go.
[46:27] All right. Here we go. So, here is a um
[46:32] a channel that I made with GitHub. Say
[46:37] GitHub. Hi. Um and you know it's I set
[46:40] it up with my a particular repo right so
[46:43] now I have a channel that is tied to a
[46:45] particular repo and then anytime I um
[46:50] want to get it to do something and I
[46:52] added my colleague to this repo right
[46:53] like so I can be like okay GitHub uh
[46:56] make a script make a PR so one thing I
[46:59] found out a few things like one is you
[47:01] have to explicitly tell it to make a PR
[47:04] um [clears throat] because originally it
[47:05] would like do the changes and not make
[47:06] PR so now I'm like okay make a PR,
[47:08] right? Um, and then make a PR, right?
[47:10] So, similarly, and so now my colleague
[47:12] can do the same thing. Okay, make a
[47:13] script, make a PR, blah, blah, blah.
[47:14] Right now, what we ended up having was a
[47:17] bunch of issues where it couldn't get
[47:18] past the uh firewall because by default,
[47:21] it does have a firewall on it. And so,
[47:25] there's a couple options. You can enable
[47:28] explicit domains in that firewall and
[47:29] say, "Hey, you can access this and
[47:30] this." And I started off with that, but
[47:32] then we needed so many domains for this
[47:34] hugging face um model that we were
[47:36] downloading. it's embedding model. So I
[47:38] ended up just disabling the firewall
[47:39] entirely just because this is you know
[47:41] whatever like it's just a personal repo.
[47:43] It doesn't have any secrets on it blah
[47:45] blah blah. So we disabled entirely and
[47:47] then we found out we had to create a
[47:50] brand new thread so that it wouldn't um
[47:53] you know so it would be free of the
[47:55] firewall, right? So um you know so then
[47:59] it did it was able to
[48:02] um you know get through and and make the
[48:05] PR right. So there were certainly some
[48:08] hiccups here right so figuring out the
[48:09] firewall
[48:11] um realizing you have to at GitHub for
[48:13] everything right because I mean it's
[48:15] kind of good because if you don't at
[48:16] GitHub then it might just accidentally
[48:18] pay attention to what you're saying to
[48:19] your colleague. So you have to at GitHub
[48:21] explicitly every time you want it to pay
[48:23] attention and you have to explicitly
[48:25] tell it to make a PR. Um so I have given
[48:27] a bunch of feedback to the team like hey
[48:29] can we have like per channel
[48:31] instructions like because in my
[48:32] instructions I'd probably be like oh
[48:33] always make a PR. Um we also want to be
[48:36] able to check like configure models.
[48:38] Right now it's always using like I think
[48:40] it's auto selecting like sonnet or soul
[48:42] in this case. Um I think we told it um
[48:47] we gave it some instructions that we
[48:48] wanted to use soul and then it paid
[48:50] attention but uh yeah so uh but it's
[48:53] cool like yeah as Bernard said this is
[48:55] the new pair programming right so this
[48:56] is someone who I would normally pair
[48:58] program with and hop on a call but now
[49:00] we can do this async pair programming
[49:03] and just whenever we have time uh you
[49:05] know this is like a repo I'm prepping
[49:06] for a presentation a month from now and
[49:09] he had some ideas for it so you know
[49:10] whenever we have time we're like okay
[49:12] let's let's go ahead and send some
[49:14] requests um to it and then we can talk
[49:17] over it in this in this form. Right? So,
[49:19] I think this is a great format like
[49:21] every if you're you know a lot of times
[49:23] when you're working on a demo or
[49:25] presentation you can create a channel
[49:26] for it add your co-presenter you know
[49:29] whoever is working on that demo with you
[49:31] [snorts] and then um be able to easily
[49:33] talk over it and just assign delegate
[49:35] stuff to GitHub and still have your
[49:37] human conversations there. Um, so yeah,
[49:41] for I think this is really good at at
[49:43] least this is a really good fit for
[49:45] these small collaborative repos. For the
[49:47] larger repos, of course, you do want to
[49:49] have a lot of discussions in the actual
[49:50] repo itself in the issues and
[49:52] discussions especially like public
[49:53] repos. But for these like little repos
[49:55] where I already would have been using
[49:57] chat to talk about the repo, we might as
[49:59] well add GitHub to the chat too so that
[50:02] we can, you know, bring GitHub in.
[50:05] Uh, so yeah, so you know, check that
[50:07] out. you might find
[50:10] um that you have some good use cases for
[50:12] it. And you can do the same thing in
[50:13] Slack. And I would actually say in
[50:14] Slack, it's a a feels like a bit slicker
[50:17] of an experience. Um so, you know, you
[50:20] can try it in both places.
[50:23] All right. Okay. So, two minutes left.
[50:25] So, what do we have coming up? Tomorrow
[50:26] is MP Live. Uh so, hopefully you'll all
[50:30] be joining for that. That'll be on the
[50:31] VS Code channel starting at 9:00 a.m.
[50:33] going for 4 hours straight. and we're
[50:35] going to have a bunch of MCB maintainers
[50:37] talking about all kinds of things. So,
[50:38] please come bring your questions uh
[50:41] bring your energy, your enthusiasm,
[50:43] and uh that should be fun. Um and s
[50:49] there's a few events in the Bay Area. I
[50:50] don't know if any of you are in the Bay
[50:52] Area, but there's some coming up. Uh
[50:54] online, we have a co-pilot summit
[50:56] that'll be similar like all day live
[50:58] stream. We'll be talking about Microsoft
[51:00] IQ. I have an AC container app sandboxes
[51:03] live stream. That's what I was, you
[51:05] know, talking about. I was working on
[51:06] that last week. That should be fun if
[51:08] you want to explore multi- aent swarms
[51:10] and sandboxes.
[51:13] And yeah, and then there's GitHub
[51:14] Universe and there's Microsoft Ignite in
[51:16] November if any of you are coming to
[51:18] that. And we're going to have a bunch of
[51:19] sessions at that.
[51:21] All right, everyone. That is all for
[51:24] today. I will um put the recording up
[51:27] for this uh hopefully tonight uh so you
[51:32] can get it. You can always get
[51:33] everything from um you know from
[51:37] just go to my GitHub and click on there
[51:40] the top link. It will have the
[51:42] recording, the transcription, all of
[51:44] that stuff.
[51:46] All right, thank you. Bye everyone.
[51:54] How do I disconnect? Okay.
[51:58] [laughter]
[51:59] [gasps]
[52:03] Okay.

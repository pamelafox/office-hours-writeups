[00:00] Welcome to our weekly office hours for
[00:04] this week, July 7th.
[00:08] So, as always, we are recording the
[00:11] office hours so that afterwards I'll put
[00:13] up the recording on YouTube unlisted and
[00:17] I will also transcribe what we talked
[00:19] about so that we have this as a giant
[00:22] FAQ.
[00:24] If you have any questions, comments,
[00:26] things you want to talk about, just put
[00:28] them in the chat.
[00:32] I'll be the only one on audio since
[00:33] that's what works with my recording
[00:36] software. Um, but you can put anything
[00:39] in the chat. I'll be watching the chat
[00:41] the whole time.
[00:43] Let's see. I have GitHub Copilot
[00:45] generating
[00:47] the weekly office hours news for this
[00:50] week. It's still doing that right now. I
[00:54] actually already had it do it, but I was
[00:56] using the auto mode and it used GP53
[00:58] codecs and GP53 codeex is just not good
[01:03] for
[01:05] for this sort of thing. So, it can work
[01:08] for some things, but you know, for
[01:12] for I guess making more creative writing
[01:16] type things, 53 codeex doesn't doesn't
[01:19] work very well. Uh, okay. So, here it
[01:22] is. So, it's at
[01:24] over here. All right. Let me open this
[01:26] up.
[01:31] All right. Okay. So, let's see. We start
[01:34] off with the news for this week. And,
[01:39] uh, what do we have here? Um so the most
[01:42] uh one of the exciting things that I
[01:45] noticed um was that Kimmy 2.7
[01:49] is now in um is now available in
[01:53] copilot.
[01:56] So let's see where we have the news
[01:58] about Kimmy.
[02:00] There we go. So Kimmy 2.7 now generally
[02:03] available in Copilot. This is our first
[02:07] openweight model that's in like part of
[02:09] the default model picker
[02:12] and it's you know it's hosted on Azure
[02:14] so you can also deploy it from Foundry
[02:19] and yeah and so it's available
[02:21] everywhere. So you know it's not as good
[02:23] as like you know Opus 4.8 eight for
[02:25] example, but it's I think it's
[02:27] considered to be on like on par with HiQ
[02:30] and you know there are you know you can
[02:31] legitimately use it for some scenarios.
[02:34] I know they did a lot of really
[02:36] interesting evaluations when they were
[02:37] trying to figure out you whether they
[02:40] could actually launch 2.7 code and
[02:42] co-pilot. I think there were some issues
[02:45] with long looping like infinite looping
[02:48] like sometimes these openweight models
[02:50] do get stuck in stuck in these loops
[02:52] that you know they're they just keep
[02:54] going and going and they never stop and
[02:56] obviously you don't want that since that
[02:57] affects your token budget right so they
[03:00] you know made some improvements to the
[03:02] the harness to do some steering and some
[03:05] interception so that you know it
[03:06] wouldn't loop forever and so now you can
[03:08] try out 2.7 code
[03:11] so that is uh that's pretty cool. The
[03:16] other thing uh GitHub models is being
[03:18] retired. That was something that we used
[03:19] quite a bit in our live stream series.
[03:21] Um you know it was great for getting
[03:23] started but it wasn't making any money.
[03:26] So it is getting getting retired.
[03:32] Let's see if there's anything else.
[03:39] Okay. So I think those are the big
[03:40] things from that from the GitHub change
[03:43] log. A new blog post that I thought was
[03:46] cool was from the um VS Code blog. And
[03:52] so this one is about tuning GP 5.5
[03:59] uh for VS Code and where they do
[04:02] different AB tests. So this is what's
[04:03] neat about VS Code is that they do
[04:05] actually
[04:07] do AB tests and so you can actually see
[04:09] you know what how they how they do AB
[04:11] tests. So this is interesting especially
[04:13] if you you might be thinking about doing
[04:14] something similar with your own
[04:15] applications is splitting traffic
[04:19] and seeing it. Now this you can only run
[04:21] AB tests if you have significant amount
[04:23] of users that are you know going to use
[04:26] a feature. So VS Code has enough people
[04:28] that are using GBD55
[04:30] that they're able to get significant
[04:32] numbers, but you do need enough people
[04:34] using a feature for to get significant
[04:38] numbers from an AB test, especially if
[04:41] the results are are subtle.
[04:44] So you can see like how they split up
[04:45] the test in terms of what percent got
[04:49] each of it. And then you can see the two
[04:51] different treatments, right? So you
[04:53] know, this was one prompt change. you
[04:55] know, they're basically they're trying
[04:56] to get GB55
[04:58] to
[04:59] avoid broad expiration. That's something
[05:01] that 55 does sometimes and you know,
[05:03] that takes a lot more time. It takes up
[05:05] more tokens. So, they wanted it to more
[05:09] assertively and only do what's needed
[05:13] and these, you know, these are the two
[05:15] different prompts that they tried out.
[05:17] And so, it's interesting also to see
[05:18] what sort of things they measure, right?
[05:20] So they look at commits and how like
[05:24] whether people keep their commits
[05:25] around, how long it before they edit,
[05:28] all these really interesting things. So
[05:31] I I think it's always fascinating to see
[05:33] the results of evaluations in AV tests.
[05:37] And we were thinking actually, you know,
[05:39] of um pointing our repo at this blog
[05:42] post and seeing if it inspires it to try
[05:45] like a different different prompt when
[05:47] it sees, you know, because something
[05:48] that worked better better for VS Code
[05:51] might also work for other people that
[05:52] are using GP55. So that's why I think
[05:54] it's really cool.
[05:56] Uh okay, so that is a cool blog post.
[06:02] What else?
[06:05] GitHub copilot vision. Oh, this was
[06:08] cool. Um, you know, this came out at at
[06:10] build, but I didn't realize that we had
[06:13] this blog post because this this shares
[06:16] more of the um technical implementation
[06:18] for how web IQ is implemented. So, web
[06:21] IQ is a new approach to getting web
[06:23] results from Bing
[06:26] and um and they really tried to optimize
[06:29] it to be really fast. It is really fast.
[06:30] I have used it. Most people haven't used
[06:32] it because it's incredibly expensive
[06:34] right now, but we did use it for our
[06:36] build lab because we had special access
[06:37] for it. So, everybody who came to the
[06:39] build lab could try it out and it is
[06:41] very very fast. So, they are using
[06:45] they're using a few different
[06:48] kind of sources. So, let's see. They
[06:51] have structured evidence. They have a
[06:53] disk ANN. So diskn is the vector
[06:56] indexing
[06:58] algorithm that is used on cosmos tob and
[07:01] postgress and it was came from Microsoft
[07:03] research and you know it's like very
[07:06] fast
[07:07] vector approximation search algorithm.
[07:10] So that's how they do the vector search
[07:12] and then they also have hairrier
[07:15] embeddings and hairrier embeddings is
[07:16] this embedding model that is open that
[07:19] you can actually run you can run it
[07:21] yourself. I think you can get it from
[07:23] hugging face. Let me see. Hugging face
[07:26] carrier. And apparently it runs just on
[07:28] the CPU.
[07:32] So it could it can be a cool thing to
[07:34] try out for for local embeddings.
[07:38] I know a few people trying it too. So
[07:42] see retrieval, clustering, semantic
[07:44] similarity, classification, bitex
[07:47] mining. I actually don't even know what
[07:48] that means. And reranking.
[07:52] So
[07:54] yeah, so that's cool. So Web IQ does use
[07:57] Harry embeddings, but you could also use
[07:59] Harry embeddings yourself. Um especially
[08:02] if you're doing something
[08:04] local there.
[08:07] So yes, that's that is neat blog post
[08:11] there.
[08:14] Now I was at the AI engineer world's
[08:16] fair last week. So at the World's Fair I
[08:19] gave four different no I gave seven I
[08:23] gave seven different sessions at world's
[08:25] fair
[08:27] about different topics and um let me let
[08:31] me bring up the schedule
[08:34] see what I talked about okay
[08:38] so let's see we did some workshops with
[08:40] foundry with foundry so um you know we
[08:44] did
[08:46] you know building models with Foundry
[08:49] hosted agents. Uh yesterday, actually,
[08:51] if you're doing Foundry hosted agents, I
[08:52] did just update this repo here, Foundry
[08:57] hosted agent framework demo. So, this is
[08:59] now using the latest version of
[09:01] everything. So, I upgraded all the
[09:03] Python packages. I upgraded the MCP
[09:06] versions. I updated the SDKs, the APIs,
[09:08] blah blah blah. New version of hosted
[09:11] agents. So, this shows you, you know,
[09:14] how to use Foundry models. then Foundry
[09:16] IQ, then Foundry Toolbox, and then
[09:19] Foundry Hosted agents using Microsoft
[09:20] agent framework. So, this is all up to
[09:23] date and I tested it last night. So, if
[09:26] you are building Foundry hosted agents,
[09:28] do check out this repo. Um, I also added
[09:31] a lot more on evaluation because I did
[09:33] use this repo for several of my demos
[09:37] last week where I was showing continuous
[09:39] evaluation
[09:42] in, you know, in the portal. Um and so
[09:45] there's a lot of
[09:48] here to help you set up evaluation as
[09:51] well.
[09:53] Uh so yeah so that is
[09:57] up to date there
[09:59] the labs that we did last week. You can
[10:02] also access this. This is one workshop
[10:04] here. This this workshop here was about
[10:07] observability. So this was using um you
[10:11] know setting up a foundry hosted agent
[10:12] and then and then looking at the traces
[10:16] for it and then trying to improve it
[10:17] based off the traces using a skill like
[10:20] a coding agent skill.
[10:23] And then the earlier one is um similar
[10:26] to the repo I just shared which is
[10:28] hosted agents. And then I also did this
[10:31] model swap workshop. Now this was a fun
[10:33] workshop where
[10:35] four different models
[10:38] deployed um and uh basically you know
[10:42] with these four models so I had DVD 555
[10:45] Kimmy 2.6 Deepseek V4 flash and Claude
[10:47] Sonnet 45 oh and I also had Mstro large
[10:51] 3 sorry Mr. large three as well. And so
[10:53] then for each of them, you know, we just
[10:56] tried out different things, right? So
[10:57] like literally, you know, to all to swap
[11:00] between them, you know, I just can
[11:01] comment out a line and then boom, we can
[11:03] try Kimmy, we can try DeepSec, we can
[11:05] try Mistral.
[11:07] So it was pretty interesting to see the
[11:12] the differences between the models,
[11:14] right? So you start pretty simple with
[11:16] just LM calls. Then we tried out rag and
[11:20] I also made examples specifically for
[11:22] entropic models because if you are doing
[11:23] the enthropic models then um you know
[11:28] you you need to use a different API you
[11:30] have to use the messages API. So we're
[11:32] using both the responses API and the uh
[11:36] messages API.
[11:38] We did image input, tool calling, tool
[11:41] calling in a loop
[11:44] and then finally agent framework. So I
[11:46] have pedantic AI, link chain and math
[11:51] and then finally uh well not finally
[11:53] even actually so then we did
[11:54] evaluations. So doing different kinds of
[11:56] evaluations
[11:58] as judge uh then using this new
[12:00] evaluation framework for Microsoft
[12:02] research called assert
[12:05] this is from Microsoft research
[12:07] responsible AI group and it's designed
[12:10] to make it easy to um bootstrap your
[12:13] evaluations.
[12:15] Let me find where was I doing it?
[12:19] Here we go. I'll show you the results
[12:22] from it because it's pretty fun
[12:23] actually. Uh, here we go. Where' I go?
[12:27] CD assert viewer.
[12:30] Oh,
[12:34] here we go.
[12:36] Okay. So, here.
[12:41] All right. So, this is like the local
[12:43] viewer for the assert evaluations. This
[12:45] is on the travel planner agent from this
[12:50] model swap research uh thing here. So if
[12:53] we look at
[12:57] I think we did on link chain one. Okay.
[12:59] So we have like this
[13:01] you know travel planner that can check
[13:03] flights and budget and all that stuff.
[13:06] So what assert does is it figures out
[13:10] you know what like so you just you just
[13:13] define
[13:15] so go here. Let's see examples.
[13:20] I don't know examples
[13:24] evalert
[13:32] here assert. Okay.
[13:35] All right. So if you want to use assert
[13:37] basically you describe your agent and
[13:39] describe you know what makes it high
[13:40] quality right. So you write out this
[13:42] YAML that says okay this is my agent and
[13:45] this is what makes it high quality. And
[13:47] then assert
[13:49] will you know make this more structured
[13:50] and say like okay these are permissible
[13:52] behaviors and these are not permissible
[13:54] behaviors and then the first thing it
[13:57] does it comes up with a test set. So
[13:58] this is a bunch of scenarios.
[14:01] So we look at sorry scenarios here
[14:03] there's 65 scenarios right and they get
[14:06] these fun titles like let's see the
[14:09] cousins first conference kitchen table
[14:12] basketball trip slack thread before
[14:14] standup. So these are all different
[14:16] scenarios
[14:18] that it wants to test
[14:21] for, you know, for for this trip
[14:24] planner. Let's see. The coach, all
[14:27] right, you are in a a debate coach.
[14:29] You're standing outside the school gym
[14:30] and then you open by saying blah blah
[14:34] blah.
[14:35] All right. So,
[14:37] it's just this this whole it's trying to
[14:40] come up with like a whole user persona
[14:42] situation and it's trying to like test
[14:44] different dimensions. So, this one is
[14:46] like tight budget pressure meaning they
[14:47] don't have a lot of um wiggle room on
[14:50] the on the kite and and then this is
[14:54] another dimension there. So, it comes up
[14:55] with the whole test set all these
[14:57] scenarios and props is going to send
[14:59] then it runs those scenarios. So, in
[15:02] this case we ran it against three
[15:03] different models. So deep CV4, Kimmy
[15:05] 2.6, GD55
[15:08] and here we see, you know, how often it
[15:11] violated the policy. So you actually
[15:13] want lower numbers here. So you see the
[15:15] best numbers actually come from GD55
[15:18] because we see that it violated the
[15:21] policy, you know, only, you know, still
[15:24] a lot 37% of the time, 43% of the time.
[15:29] But that's what you want. You do want
[15:30] those low numbers because all of these
[15:32] are about violations. So that's what it
[15:34] does is it figures out what the
[15:36] permissible behaviors are and the not
[15:37] permissible behaviors. It comes up with
[15:39] a bunch of scenarios and it runs it. So
[15:41] this could be particularly useful when
[15:43] you're when you don't have test input
[15:45] yet for an agent and you need some help
[15:47] coming up with that test input and
[15:49] coming up with evaluations
[15:51] and you know you can kind of run it all.
[15:53] This doesn't really integrate with
[15:54] Foundry yet except for using Foundry you
[15:57] know models as the judges. Um
[16:00] hopefully in the future it'll be better
[16:02] integrated with with Foundry. Foundry
[16:05] does have something similar called
[16:06] Foundry Rubric Evaluation. So you could
[16:08] also try that in Foundry itself.
[16:12] So that's assert. So that's a new way of
[16:14] doing eval. So you may want to check
[16:17] that out if you're curious about that.
[16:21] You know when we ran that basically
[16:23] found that 55 was the best for that
[16:26] scenario. And then we talked about
[16:28] prompt optimization using despy. So dspy
[16:31] is a way that you can declare your
[16:34] programs in terms of their signature and
[16:36] then you run an optimizer that says like
[16:39] okay I'm trying to get this you know
[16:41] this output from this program
[16:45] and you give it a bunch of evals and
[16:46] then it'll just keep optimizing the
[16:48] prompt until it comes up with the
[16:51] optimal eval scores. So this is
[16:53] particularly good if you're using LMS
[16:55] for like structured outputs or
[16:57] classification, entity extraction, that
[17:00] sort of stuff. So we did, you know, so I
[17:04] used the example of something that the
[17:07] mistrol model had done poorly on. So
[17:10] that was generating a number list where
[17:12] each line has exact word count and the
[17:14] first letter of the line spell out a
[17:15] target word. So this was harder for the
[17:18] smaller models to do. So we define the
[17:21] signature and then we define um evals
[17:26] for it like metrics to check to see if
[17:28] it did a good job. And then we run this
[17:31] Jeepa optimizer which uses genetic parto
[17:34] algorithms in order to figure out the
[17:36] prompt to try and it keeps trying
[17:39] different prompts until it comes up with
[17:41] the optimal prompt which gets the best
[17:43] score.
[17:44] And so then you store that prompt in um
[17:49] you would store that prompt, you know,
[17:50] you know, lock it in your repo, right?
[17:52] So this ends up this here ended up being
[17:55] the best the best prompt. And so this I
[17:59] didn't write this prompt, right? This
[18:01] was written by an LLM and it was like
[18:06] optimized
[18:07] over time using these genetic algorithms
[18:10] to try and figure out what
[18:12] you know LM is figuring out what to try
[18:14] next in the prompt. So if you use
[18:16] something like DSpy, you don't ever
[18:18] write the prompt yourself. You never
[18:20] edit the prompt. All you edit is the
[18:23] signature and the evaluation and you you
[18:25] know you might rerun that optimization
[18:27] if you're changing your model. You
[18:29] definitely rerun if you're changing your
[18:30] model,
[18:32] but then you just, you know, you just
[18:33] store that prompt in your repo and that
[18:37] prompt becomes like a lock file like an
[18:39] artifact,
[18:41] but not something that you yourself
[18:42] change.
[18:45] So, so yeah, so that's an interesting
[18:47] thing as well. And I, you know, various
[18:49] companies have used DSPY to be able to
[18:51] use smaller models but be able to use,
[18:55] you know, use those cheaper models but
[18:57] be able to get the same performance that
[18:59] you get from the bigger models.
[19:02] So that
[19:05] is the model swap workshop.
[19:08] I don't see any questions or comments in
[19:09] the chat so far, but if any point
[19:11] there's something you want to explore
[19:12] more, just let me know.
[19:15] We also Arun and I gave a talk about how
[19:19] to choose an um agent
[19:23] framework um especially if you're
[19:27] building on top of foundry
[19:29] right with OpenAI or Enthropic
[19:34] so you know how do you you know what do
[19:36] you do right if you're do do you are
[19:38] using HTTP APIs are using the vendor
[19:40] SDKs are using LM agnostic SDKs like
[19:43] light LLM them using agent frameworks
[19:47] and um you know basically I suggested
[19:51] that you know you if you want maximum
[19:52] control you're going to go directly to
[19:55] the the either the responses API or the
[19:58] messages API should not use completions
[20:01] API anymore because that is a legacy
[20:03] format so you should be using either
[20:05] responses or messages
[20:09] and um you could use something like lay
[20:11] lm I don't really recommend it I think
[20:13] if you want LLM agnosticism, then I
[20:15] would just jump to an agent framework
[20:17] because usually those make it pretty
[20:20] easy to to swap the models because they
[20:24] have these levels of abstractions where
[20:26] they can switch between them. But if you
[20:28] do move to an agent framework, then you
[20:29] might lose some of the specific features
[20:32] of each of the APIs, right? So, for
[20:36] example, the anthropic messages API had
[20:38] this really nice citation support. That
[20:40] was something I showed off in um the
[20:43] model swap workshop. So if you're doing
[20:46] rag with enthropic,
[20:48] they specifically have this idea of a
[20:51] content block. So you actually would
[20:52] attach your content chunks using this
[20:56] structured format here where you say,
[20:57] okay, here's the document, here's the
[20:59] text, here's its ID, here's its title,
[21:01] and then you enable citations for it.
[21:04] And you pass in, you know, those content
[21:06] blocks. And then when you get back a
[21:08] response from the LLM, you'll actually
[21:10] get back a response with structured
[21:13] citations. So every block of text will
[21:15] also potentially have citations attached
[21:17] to it, which is just really really nice
[21:20] that you can extract back those
[21:22] citations in a structured form. When
[21:24] we're using the other models like the
[21:26] OpenAI models, we just ask for it
[21:29] inside, you know, some sort of like
[21:31] square brackets and and hope that it
[21:32] gives us, you know, correctly formatted
[21:34] citations and it doesn't always, right?
[21:37] So this is super cool. So that's the
[21:38] thing is like if you want the most
[21:41] control and you want to take the most
[21:42] advantage of the specific features of
[21:46] each API
[21:47] then it helps to be going as you know
[21:50] using as as low level as possible right
[21:54] so that you can you can use absolutely
[21:56] everything in it you know because
[21:58] Enthropic has some other stuff too um
[22:02] you know more parameters uh it's got
[22:05] specific ways of doing caching that's
[22:07] different from opening I
[22:09] u but you know if you're less concerned
[22:12] with the specific features from open AI
[22:15] versus anthropic then you know then you
[22:18] know I'd say just move to a Asian
[22:20] framework and then it makes it pretty
[22:22] easy to swap between models
[22:26] like in my examples here
[22:30] let's see do I swap between them here
[22:33] not in this one okay let me find I have
[22:36] a lot of Foundry okay foundry let's
[22:39] check where is the one for this one okay
[22:42] Python stack foundry models all right so
[22:44] this is the repo
[22:46] for this talk
[22:49] so in this one you can see
[22:52] right
[22:54] you know you can just say like okay I'm
[22:56] using you know the openi responses API
[23:00] and and this one you can pass in any
[23:02] foundry model that supports the
[23:03] responses API which basically is all of
[23:06] the serverless models, the direct models
[23:09] that are not enthropic, you can pass
[23:11] into here and then otherwise um you know
[23:14] if you're using entropic models then you
[23:16] would make the entropic claim and you
[23:19] know you can see how I did that there
[23:22] but then all the all the rest of your
[23:24] code is the same right so you know if if
[23:26] you wanted to be able to switch between
[23:27] you know any of the models on Foundry
[23:30] you know basically this is your code and
[23:32] then the rest of your code is the
[23:37] Um or I have example you know there's
[23:38] also examples here of how you would
[23:40] specifically use just the anthropic API
[23:44] right um
[23:47] or light LLM I'm not a huge fan of it
[23:50] but that is an option that some people
[23:52] use as well
[23:56] uh so yeah that was point of that talk
[24:02] and you know we have various this
[24:06] starters to get you started with those
[24:08] models here.
[24:12] Let's see.
[24:14] Okay,
[24:17] what else? Uh then
[24:21] and then I talked about yeah agent evals
[24:24] and observability. Um, let me
[24:30] observability stuff in foundry.
[24:35] No questions yet. Okay, let's see.
[24:38] Foundry lab
[24:48] agent.
[24:51] What?
[24:54] What
[24:57] does
[25:00] how does it compare to Microsoft
[25:04] search?
[25:08] Let's try this out.
[25:15] You see there's also this new optimize
[25:17] button here.
[25:19] Optimize is now um built into Foundry.
[25:23] something that you can do and that'll uh
[25:26] come up with candidates. Let me find my
[25:29] slides about optim.
[25:33] There we go.
[25:36] Optimize.
[25:39] Yes. So for optimization basically um
[25:42] you use AZD AI agent optimize and it
[25:45] will evaluate your baseline agent your
[25:47] current agent and then it tries to
[25:49] generate candidates
[25:51] figuring out like how it's going to
[25:53] change the prompt the tools etc
[25:56] and then it tries out each of the
[25:58] candidates and then it figures out which
[25:59] of the candidates ranks the highest and
[26:02] then it says okay this you know this
[26:03] candidate ranks the highest
[26:06] and um and then it can deploy the new
[26:08] candidate
[26:09] So that's the optimization loop. Here's
[26:11] the docs for optimiz optimizer. So
[26:14] that's similar to the um you know despy
[26:17] that I was showing, but this is you know
[26:19] built into Foundry and specifically
[26:22] designed for Foundry agents to be really
[26:26] easy to use with Foundry agents.
[26:31] All right, so let's see. So we just did
[26:33] this question here
[26:35] and we can see the evaluations that run.
[26:38] And then we can look at traces.
[26:45] So this trace viewer is
[26:49] is fun. Here there's a little play
[26:50] button so we can watch
[26:53] as it goes through
[26:56] and it tries to do it sequentially. It's
[26:58] a little hard to watch traces
[27:00] sequentially because as it turns out
[27:02] many of these things are done in
[27:03] parallel. you can't necessarily really
[27:06] exactly sequentially um you know watch
[27:08] things if they're if they're going in
[27:10] parallel.
[27:12] You can you can kind of use the play
[27:14] button.
[27:16] Yeah. But you can see like basically
[27:18] this one made multiple calls, right? So
[27:20] it made a call to a web search at the
[27:22] same time that it made a call to
[27:24] knowledge base. So this is AI search
[27:27] knowledge base
[27:30] and you know got back the the results
[27:32] for
[27:34] each of these
[27:41] and then we can also let's check the
[27:44] monitor tab here. Okay, so the monitor
[27:48] tab also has a lot more information in
[27:50] it these days, right? So you can see
[27:54] operational metrics, my cost. I guess I
[27:59] haven't used enough or maybe I'm on a I
[28:01] don't know why it says zero.
[28:06] Yeah, it's set up. And then we have
[28:08] evaluations. So I have different types
[28:09] of because I've got like scheduled
[28:11] evaluations and you can see my scheduled
[28:13] evaluations are actually not doing so
[28:15] well. So I need to like check and see,
[28:18] you know, if I can improve those
[28:20] numbers. Um, there's the there's all the
[28:22] runs. You can see big guy was doing a
[28:25] lot of runs on July 2nd. That's when the
[28:28] talk was. So, it was 4.3 million tokens
[28:33] apparently. Um, and I was just sending
[28:36] lots and lots of data to the agent, see
[28:39] what it would do.
[28:41] And, uh, yeah, we can see tool calls,
[28:44] error rate, evaluation metrics.
[28:47] you can see each specific evaluation
[28:49] score. So there's quite a lot more and
[28:52] then I even set up alerts. So I set up a
[28:54] evaluation pass rate alert because
[28:56] that's something it's basically like
[28:57] pager duty being on call like you know
[29:00] you can get paged if your evaluation
[29:02] rate actually goes too low. So I set
[29:04] that up
[29:06] in Azure monitor. All this is backed by
[29:09] Azure monitor. Here
[29:12] we go to Azure monitor
[29:16] and we can see Azure monitor also has
[29:18] this nice agents view. So this will work
[29:19] with any agents that are using the
[29:22] generative AI semantic conventions. So
[29:25] you can see it it understands tool calls
[29:27] like it sees oh these are all the tool
[29:29] calls you were doing right
[29:32] and it also understands evaluations. So
[29:34] that's using a boundary convention that
[29:37] it's looking at token consumption by
[29:40] model.
[29:42] So, so yeah, you can you've got much
[29:46] more options now for monitoring your
[29:51] your agents if you're integrating well
[29:54] with you know with open telemetry right
[29:56] so I was saying with open telemetry
[29:59] where's it's a different deck for open
[30:01] telemetry okay for open telemetry the
[30:04] important thing is using the genai
[30:07] semantic conventions and agent framework
[30:10] uses these so do most agent framework
[30:12] refuse them and it just means when it
[30:14] emits the open telemetry span that it
[30:17] sets these gen AI attributes right but
[30:21] we always use the standards when we can
[30:23] there's also you know I think the evals
[30:26] must be coming that must be just a
[30:28] foundry convention that we've agreed on
[30:30] so see if I can actually see those eval
[30:33] let's see so I want to see where that
[30:36] comes from
[30:38] see what that trace looks
[30:42] Okay.
[30:48] Right. So here you can see like this is
[30:50] invoking an agent. We got messages
[30:54] name tool definitions
[30:57] and then we have these evaluations.
[31:00] Okay. So it looks like these evaluations
[31:03] are being yeah the evaluations are being
[31:05] being done after the fact on these ones.
[31:10] I don't actually I can't tell here how
[31:12] they're being stored.
[31:14] Um,
[31:16] interesting because we're just seeing it
[31:17] show up here. I don't know how it's how
[31:21] it's
[31:22] and this is a question I need to ask
[31:24] colleagues. Um, how is it actually
[31:27] adding in these evaluations? It must be
[31:29] storing them somewhere,
[31:35] but it doesn't seem like it's storing
[31:36] them in the
[31:39] thing itself.
[31:44] Deleted logs.
[31:53] Oh, here we go. Event name. Okay. All
[31:56] right. So, I found it. So, it's event
[31:57] name genai.evaluation.result
[32:02] and oh, and it looks like it's also this
[32:04] looks like a genai semantic convention.
[32:06] Great. Okay. So, we get a name, a score,
[32:09] a label, an explanation,
[32:11] and this is it's tied to a conversation
[32:14] ID. So, that must be basically how it's
[32:18] joining them, how it's finding the
[32:21] relevant evaluations. it. I would assume
[32:23] it's doing, you know, like kind of like
[32:25] a um join on this conversation ID.
[32:31] Yeah. Okay.
[32:36] So, that's cool. Um, so you definitely
[32:39] want to set up good observability for
[32:42] your agents. I'm just going to
[32:45] screenshot this so I remember how this
[32:47] works.
[32:50] Um,
[32:56] see maybe someone's gonna type a
[32:57] question soon. Okay.
[33:00] Uh, yeah. So, Adam asked, "Have Foundry
[33:03] Evals and optimizations you just showed.
[33:04] Is it correct to assume that my agents
[33:06] need to be hosted on Foundry or Azure so
[33:09] that Foundry can run evals as needed?"
[33:11] Um,
[33:13] uh, so that's a good question. So
[33:15] actually one of the demos that I did
[33:16] show last week was
[33:19] this one from my colleague. I'm going to
[33:21] have to switch tenants for this. Um so
[33:25] this is one they showed for a
[33:28] build session, a build demo session and
[33:32] it's actually got agents not it's
[33:36] bringing in agents from
[33:39] from other places as well uh from uh GCP
[33:42] and AWS.
[33:44] we get the repo for it. Um,
[33:49] okay. So here,
[33:52] right, so this was the actual full demo
[33:55] session
[33:58] any agent any cloud standardized tracing
[34:00] with foundry and open telemetry and then
[34:02] this was the this is the repo as the
[34:06] code. So you can see in this repo we
[34:08] have stuff like
[34:12] ADK which is Google I believe
[34:19] langraph I think was on
[34:23] was it on AWS? Yeah AWS. So they've got
[34:27] several agents running across GCP and
[34:30] ADWS and foundry
[34:33] and they had you know a um
[34:37] so we have type external
[34:39] so this one is not actually hosted on
[34:42] foundry but um it's using open telemetry
[34:46] for the observability right so this is
[34:48] bangalaroo so if we look at the actual
[34:51] code for this what you can see is that
[34:55] it's bringing in this
[34:58] telemetry. It's using this Microsoft
[35:00] telemetry
[35:02] distro uh distribution and it's
[35:05] configuring it
[35:08] and adding in it's adding in various um
[35:11] tracers to to make sure it's tracing
[35:13] everything.
[35:17] So, the goal is to try and make it easy
[35:20] to be able to use any of them. I think
[35:22] it really depends on the cloud and the
[35:25] framework, right? This one's ADK on AWS,
[35:29] but they were able to get it working. So
[35:32] in theory, if you use open telemetry and
[35:34] you use these, you know, semantic
[35:36] conventions, right? I'm saying here the
[35:38] semant the geni semantic conventions and
[35:40] you can do it using um the goal is that
[35:44] you can use this Microsoft open
[35:46] telemetry distro
[35:49] in order to do that. Okay, so from
[35:51] Microsoft open telemetry use Microsoft
[35:53] telemetry that was the ling ling graph
[35:56] example.
[35:58] So the goal is for that to become easy
[36:00] to use because then um you can actually
[36:04] see traces
[36:06] from across systems. We're not seeing it
[36:08] here but then if you go to where's the
[36:11] deep agents agent framework?
[36:15] I think this one deep agents
[36:16] orchestrator. Let me go to app insights.
[36:19] Let's open an Azure monitor.
[36:24] Uh
[36:26] foundry has some level of cloudnosticism
[36:28] for the evals and and observation. Let
[36:31] me get time range last 30 days.
[36:36] Okay,
[36:39] I think I need to get more than 30 days
[36:41] because now Okay, let's do 60 days.
[36:43] Okay, there we go. Okay. So what we can
[36:46] see here is that there's a bunch of
[36:48] agents and some of these are the ones
[36:51] that are not hosted on our cloud. Right.
[36:52] So Bangladu
[36:54] is not you know not hosted on Foundry
[36:58] but it is using the open telemetry.
[37:01] So the goal is that because some of you
[37:03] you know might have agents running
[37:04] elsewhere but you might still want to
[37:05] use our observability and eval.
[37:10] So the hope is that you can. It's
[37:11] obviously a lot easier if you're if
[37:13] everything's hosted on Foundry, but in
[37:16] theory with open telemetry,
[37:20] you know, it shouldn't be required for
[37:22] that to be the case. So if we look at
[37:24] one of these
[37:26] traces here, this is interesting because
[37:28] it starts off with the steep agents
[37:30] orchestra. This one is hosted on
[37:32] Foundry.
[37:33] We can see, yeah, this is the Microsoft
[37:36] Foundry project ID. And then that goes
[37:38] to a different place like lingraphph. It
[37:40] goes off to lingraph. Lang graph is not
[37:44] you know is not hosted
[37:48] on foundry
[37:50] that this one's um
[37:53] what is it Google and then we have bingo
[37:56] and this one is on AWS
[38:01] but they all were able to show up here
[38:03] because
[38:05] you know because they're all using the
[38:06] the open telemetry and they're emitting
[38:10] to to this um to this insights.
[38:17] So the goal is that yes, you can do
[38:19] that. Um I think it's how easy it is is
[38:23] going to depend on which framework
[38:24] you're using, which cloud you're using.
[38:27] I would consult this repo to figure it
[38:30] out. Um or also just chat with
[38:34] the, you know, um these folks, it's Honi
[38:38] and Nagumar. They're the two that work
[38:40] on it. They're very nice.
[38:42] So, you can probably ask questions this
[38:44] repo or if you don't hear from them,
[38:46] just let me know. I can ping them as
[38:48] well. But yeah, that is the goal. So,
[38:53] you said you're facing the same issue.
[38:55] Any best practices, documentation, or
[38:57] any relevant skills available to use?
[39:01] Um,
[39:04] well, uh, yeah, it depends how you're
[39:06] getting how you're doing the connection,
[39:08] right? So if you're doing agent
[39:10] framework usually that makes it really
[39:12] easy to get logs into app insights like
[39:15] you don't have to do very much at all
[39:17] but it depends yeah it depends what
[39:20] framework and what what cloud so for
[39:24] agent framework for the easiest thing
[39:27] would be agent framework with foundry
[39:29] hosted right so for that all I had to do
[39:31] was what did I do I did enable
[39:34] instrumentation
[39:36] which is actually already enabled by
[39:38] default Um, but you know, I just called
[39:40] that anyway. And then I did um I do
[39:44] anything else. I think I already had app
[39:47] insights set in here uh as an end
[39:50] variable. So that was all that was all I
[39:52] had to do was just that because I
[39:54] already had the app insights connection
[39:56] string and so if you have the app
[39:58] insights connection string like it'll
[40:00] just be taken care for you, right? So
[40:02] that's the easiest.
[40:04] But you know if you're doing other
[40:06] things like in the other repo I also use
[40:09] um I use the configure Azure monitor to
[40:11] get it to app insights. Um in this repo
[40:14] here they're using the Microsoft
[40:17] open telemetry
[40:20] distro.
[40:24] Let's do the langraph one.
[40:29] So they put everything this telemetry
[40:31] py. The one thing you might want to do,
[40:32] you know, you could you can po point
[40:35] your agent at whatever is the the most
[40:37] similar thing and um say, "Hey, can you
[40:41] bring in telemetry? Here's an example
[40:44] of one that sets it up."
[40:48] Does look to me like it's more complic I
[40:51] guess I'm a little surprised at how
[40:53] complicated it looks. Um I wonder if
[40:56] we're going to make any of this easier
[40:59] because I'm surprised
[41:01] I'm surprised that we need this. I think
[41:03] the heart of it is here. Right here,
[41:07] you know, from Microsoft telemetry, use
[41:09] Microsoft telemetry, but there's a lot
[41:11] of other stuff too.
[41:13] Okay.
[41:15] Find your open calls.
[41:19] Oh, this one you need on AWS Lambda.
[41:23] Feels like there's a lot of extra
[41:25] complexity here that surprises me.
[41:34] I might ask them more about that. There
[41:37] are skills for foundry observability
[41:40] generally. Uh that was what we did in
[41:45] the lab 540 is use the foundry um
[41:50] toolkit extension for VS code. And if
[41:52] you install that then it does come with
[41:56] skills. Um let me find the
[42:00] a screenshot.
[42:02] Screenshot
[42:12] screenshot of the skills.
[42:23] Here we go. What Microsoft Foundry
[42:25] skills do you have? So this one has
[42:28] observe trace eval data sets
[42:31] troubleshoot. Right? So the trace skill
[42:34] might be might be a good one to try. I
[42:38] don't know if I have my
[42:41] if I have my extension installed. What
[42:44] foundry toolkit skills do you have?
[43:00] Okay,
[43:03] it mentioned those ones but not the
[43:05] specific ones I think because I have it
[43:07] installed. So if I it okay update tools
[43:16] authenticate.
[43:18] Let me do it again.
[43:22] Whoa. A bunch of machine learning stuff
[43:25] there.
[43:27] Toolkit. Oh, no. This is the one. Okay.
[43:30] Pound. Open. Trace. Get custom
[43:33] usage. Read cell.
[43:38] There's so many.
[43:40] Where's the one I just did?
[43:49] What is all this stuff? Evaluation.
[43:51] Evaluation. Model quota.
[43:55] Dean learning MCP service entry points.
[44:00] Oh, continuous evals. This does seem
[44:02] like it's about Foundry model catalog
[44:05] list. So, I think this has a funny
[44:07] title, but I think this is actually the
[44:09] Foundry Foundry one. So, we got all the
[44:12] evaluation stuff project
[44:15] get. I don't see traces there.
[44:21] All right, I'll ask my
[44:23] colleagues if they have any additional
[44:25] suggestions for skills. Uh, this is
[44:28] foundry toolkit.
[44:30] See if I have it. Restart required.
[44:33] Restart extensions. Install
[44:37] and then let's reload the window.
[44:42] Okay.
[44:45] have to see
[44:48] if it needs to restart. Hi,
[44:53] the router GB54 mini because I gave it
[44:55] the easiest question in the world.
[44:58] That's why you shouldn't start your
[45:00] sessions if you're in auto mode. Do not
[45:03] start your sessions with high because it
[45:05] will route you to a super easy model and
[45:08] now it's 53 codeex and then the rest of
[45:10] your session will use codecs unless you
[45:12] change it otherwise. So,
[45:15] Anyway, be careful about starting off
[45:17] with just high. So, Foundry toolkit for
[45:20] VS Code
[45:23] be like, okay, what foundary skills do
[45:25] you have?
[45:29] Anything for traces?
[45:32] Let's see if it can find it.
[45:35] I don't use the foundry skills that much
[45:37] myself. Um,
[45:42] okay. It can help with
[45:45] few things, but yeah, I don't see that
[45:47] helping that much with App Insight. So,
[45:50] I'll ask Ki about
[45:54] I I would probably find the most similar
[45:56] code to what you want to do and then
[45:59] just point
[46:00] C-pilot at code
[46:03] and, you know, have it implement it.
[46:10] Let me ask
[46:27] agent skills.
[46:36] I just sent them some questions,
[46:39] so we'll see.
[46:44] All right. Okay.
[46:47] Uh, I'll see if Ponchi sends any
[46:51] any more ideas on that.
[46:59] Yeah. So, for evals, you should be able
[47:01] to run the continuous evals as long as
[47:05] um, let me go back to this one. The
[47:07] continuous eval are based off of your
[47:09] app insights traces, right? So I would
[47:12] think that as long as you could get the
[47:14] traces into app insights that you would
[47:17] be able to do the continuous evals. So
[47:19] here this is like okay this is my
[47:21] continuous eval.
[47:26] And they're still running. I should turn
[47:28] them off at some point but you know so
[47:30] these are running based off of
[47:33] insights traced right. So
[47:37] I would think that you should be able to
[47:39] use continuous evals
[47:42] as long as you can get into app
[47:43] insights.
[47:45] Let me double check.
[47:57] As long as you get craft cloud agent
[48:01] traces into
[48:04] the cells,
[48:08] we could run continuous eval.
[48:15] Okay. All right. Uh any info on hosted
[48:20] agents in GA?
[48:23] I have not heard anything
[48:27] about that.
[48:29] Assume they're still listed as
[48:33] preview blah blah blah blah blah.
[48:41] It's interesting. They actually don't
[48:42] say that they're preview here.
[48:44] Normally we put like a big preview
[48:47] thing. Okay. One time components
[48:51] time contract item marks preview are
[48:53] currently in public preview. Okay.
[48:57] How do we mark it preview?
[49:02] We didn't mark anything as preview.
[49:04] Okay.
[49:08] All right. I'm going to message I will
[49:12] send a message to the team that it's a
[49:16] bit unclear
[49:18] what things are in preview. So,
[49:24] foundry hosted agents GA maybe. Are they
[49:28] GA? Is that why I'm not seeing it?
[49:32] New.
[49:35] Oh, this says Microsoft founder eating
[49:37] services GA.
[49:39] Did we go GA
[49:42] out? It was mentioned it would be GA at
[49:44] the end of June. Okay. And someone else
[49:45] says they're DHS says they're GA. All
[49:47] right. Looks like we went GA. I think we
[49:49] need to update our docs. Um, okay. Where
[49:52] did we put it?
[49:54] Code act. This is some random
[49:57] announcement post.
[49:59] April 22nd. All right. So, building run
[50:02] June 2nd. June 2nd. Foundry.
[50:06] Those are featured posts. I want latest
[50:07] posts.
[50:09] Nick
[50:17] June,
[50:19] wouldn't we have done an announcement?
[50:20] Okay. Cloud is not available. Foundry
[50:22] can aadians to the GA. Oh, this fulfills
[50:25] the GA in June 2026 commitment and
[50:27] build. Okay. Foundry agents can now
[50:30] publish to teams. That's GA.
[50:37] Was that the only thing we were waiting
[50:38] for? G
[50:42] what picked up? Okay.
[50:45] Autopilot agents and public preview.
[50:48] Okay.
[50:50] Okay. So, publishing went.
[50:59] Okay. So, that's the only thing it says
[51:01] is GA. So that mean maybe that means
[51:02] that everything else already was GA.
[51:05] Let's see.
[51:07] Still missing a few private v-net
[51:09] injection. H okay. So you think that
[51:12] would be mentioned
[51:15] ship to production deploy. Okay. So we
[51:18] have deploy with a private ACR. I
[51:20] remember that one.
[51:22] This also gonna
[51:26] Okay. So this one also doesn't have the
[51:29] word preview anywhere in it. All right.
[51:31] I need to
[51:34] I need to message the team about that as
[51:37] well. Okay.
[51:41] I'm trying to see you know as Desh said
[51:46] that we're missing some private V-Net
[51:48] injection. I'm seeing where we wrote
[51:51] that deploy configure virtual networks
[51:53] at a private network. Okay, great. So
[51:55] this one
[51:57] limitations limitations
[52:03] the sound.
[52:10] Okay. Well, there's some limitations
[52:11] here.
[52:16] This one for background.
[52:29] configure a network environment.
[52:32] Create a resource.
[52:36] I'm just trying to see does this work
[52:37] with hosted agents.
[52:50] Hosted agent for hosted agents. The
[52:53] virtual network configuration must be
[52:55] included when you first create the
[52:57] Foundry account. Adding network
[52:59] injection to an existing Foundry account
[53:02] after creation isn't supported for
[53:03] hosted agents. Okay, I think that's
[53:07] that's what Desha is referring to there.
[53:10] And then support for ACR depends on when
[53:14] the foundry project was created.
[53:16] Projects created after June 24th support
[53:18] a private ACR.
[53:20] Ah, okay.
[53:23] Okay, so it looks like things have
[53:26] improved quite a bit, especially if you
[53:28] can start from scratch
[53:32] and it does look like most things are GA
[53:40] and um like there just like some new
[53:42] like optimize is in preview because that
[53:44] just came
[53:47] Yeah, um not not seeing a lot of things
[53:51] that are marked at
[53:55] preview. So the build addition recap is
[54:01] okay. It said hosted agents are expected
[54:03] to reach general availability by early
[54:05] July.
[54:08] I'm getting a little confused to be
[54:10] honest. Um because
[54:14] I can't it okay early July it'll be now
[54:20] but it's not announced anymore. Did did
[54:23] Deness do you have an announcement for
[54:25] hosted agents being GA because I can't
[54:27] find it here. Okay let's look. Oh and
[54:31] I'm also over time. All right. Hosted
[54:32] agents
[54:35] GA July.
[54:38] Okay. So that says it's GA but then
[54:40] where
[54:42] OGA in July.
[54:45] Okay.
[54:53] >> I don't know.
[54:55] I don't see it. I'm going to message uh
[54:57] Nick and ask him. He's the author of
[55:00] this blog post.
[55:02] I'm going to ask him to confirm what the
[55:06] situation is since
[55:09] I'm a little confused.
[55:11] I guess I would thought there would be a
[55:14] blog post specifically about it.
[55:20] All right. Okay. Um I will follow up on
[55:23] a few things and I will um if I find out
[55:27] anything, it'll be posted. I usually
[55:30] just do it as an update in the session
[55:33] thread here, right? Because normally I
[55:35] post these tonight or the next day. And
[55:39] so if I find out anything between now
[55:41] and then, then I will just post an
[55:43] update the QA.
[55:47] All right,
[55:49] tweet. Thank you everyone. Hope you have
[55:52] a lovely rest of your day and I will see
[55:55] you next week. Bye.

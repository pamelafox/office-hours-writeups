[00:00] Welcome everyone to our weekly Python
[00:03] plus AI office hours. Uh the way this
[00:06] office hours works is that
[00:09] I you know have a bunch of like news and
[00:11] updates we can talk about here from
[00:13] what's happened in the last few weeks
[00:15] but also if you have any questions or
[00:17] comments just put them in the chat. Um,
[00:21] we don't do audio in this office hours
[00:23] because of the way I record it on uh on
[00:26] Streamyard so that people can watch
[00:28] later because a lot of times people
[00:29] aren't able to make the actual office
[00:31] hours, but they do want to see what we
[00:33] chat about. Uh, so if you do have any
[00:36] questions, comments, things that you
[00:38] want to share, just go ahead and stick
[00:40] them in the text chat.
[00:42] So, welcome everyone. today. This was a
[00:45] huge week because we had Microsoft Build
[00:47] last week and we announced so many
[00:50] things. Um there's this there's this
[00:52] really long list here, Matt's Build 2026
[00:56] list. So, this is the one um that you
[00:59] should if you want to see absolutely
[01:02] everything um that was announced at
[01:05] Build. It is a really really long list.
[01:08] Um so, let me like there was a lot of
[01:10] stuff on the hardware side. I'm not as
[01:12] into that. Um, but lots of people are
[01:14] excited about that. The stuff that I
[01:18] really wanted
[01:20] to show is um the Foundry IQ.
[01:25] Foundry IQ. Okay. This
[01:30] because we talk about that a lot here.
[01:32] So, Foundry IQ, also known as Azure AI
[01:35] search. The really exciting thing here
[01:37] is well, a couple things, but one thing
[01:39] that's huge is serverless. So this is
[01:42] because I know we often get asked about
[01:44] the pricing level for Azure AI search
[01:48] because you have to have like this
[01:49] dedicated search instance but now
[01:51] they're they have this serverless
[01:53] offering so the pricing is a lot more um
[01:58] a lot more reasonable. Oh, am I sharing
[02:00] the Oh, you're right. I'm sharing the
[02:02] discord window. Thank you. Let me
[02:07] let me share the right window.
[02:09] Need this one. Okay, thank you. All
[02:12] right,
[02:17] here.
[02:18] There we go. There's the one. That's the
[02:21] blog blog post for all the Padra IQ
[02:23] Azure AI search stuff. So, yeah, this
[02:26] pricing model should be a lot better for
[02:28] getting started for variable workloads.
[02:31] You know, just you won't have to pay a
[02:33] minimum of like 200 a month, right?
[02:35] That's kind of how it was before in
[02:37] order to get all the good stuff from
[02:38] Azure Search. So now there's serverless.
[02:41] It's still in preview right now. So they
[02:42] don't even have billing enabled for it
[02:44] yet. So it's just for like to try out.
[02:45] But I would imagine that we'd get
[02:47] billing, you know, hopefully by ignite.
[02:51] Um yeah, it's a good question from Nico.
[02:53] Does serless tier include all the
[02:54] premium features like agentic retrieval
[02:56] etc. Um so yeah let's look ahead at the
[03:01] limits
[03:04] because there is
[03:07] a current limit um
[03:12] changes next.
[03:14] Where did they put the limitations? Um
[03:19] um
[03:21] currently in preview
[03:26] no billing.
[03:29] Yeah, actually I think everything is um
[03:34] let's see I think everything might be
[03:37] enabled. Serverless preview the current
[03:40] preview limit. Oh, so it does have more
[03:42] limits, right? Because because it is in
[03:44] preview. So the limits are uh on stuff
[03:48] like how many indexes can you have, how
[03:50] many objects can you have like how much
[03:51] you know how much um you know stuff can
[03:53] you send in it but in terms of features
[03:57] as far as I can see it basically all the
[03:59] features are supported like in like
[04:01] semantic ranker like I already I got
[04:03] asked specifically about semantic ranker
[04:04] already so that that's supported
[04:07] retrieval should be supported so yeah so
[04:10] I think the idea is for you to be able
[04:11] to try out everything um but you know
[04:13] not be able to move your production. You
[04:15] wouldn't want to move anything
[04:16] production to it yet since it's just,
[04:18] you know, we don't have billing for it
[04:20] yet. So, you're wanting some limits on
[04:22] like just actual how much you can send
[04:24] in it, many and how many indexes you can
[04:27] make. But in terms of the features, you
[04:28] should be able to try out all the
[04:30] features.
[04:33] So, yeah, hopefully that will get GA
[04:36] soon enough so that we can start using
[04:38] that for everything. Foundry IQ also
[04:41] added new knowledge sources. So you can
[04:43] connect with work IQ, fabric IQ and um
[04:47] you can also connect to web IQ because
[04:49] an MTP endpoint. So uh that's what our
[04:52] lab was about at build. Um so you want
[04:56] to see like how to do it step by step.
[04:58] We have you know making a standard
[05:01] knowledge agentic knowledge base and
[05:03] then um adding web IQ then adding fabric
[05:06] IQ then adding work IQ. So basically we
[05:10] add all so now Microsoft has four IQs
[05:13] which are really all just different
[05:14] kinds of um retrieval mechanism. So
[05:17] we've got founder IQ which is kind of
[05:18] your generic retrieval mechanism which
[05:21] is Azure AI search and so that you can
[05:23] connect lots of sources to it. Then we
[05:25] have web IQ which is basically an agent
[05:28] optimized Bing search index and that
[05:32] one's very limited right now so most
[05:34] people do not have access to it but we
[05:36] were able to use it in the lab just to
[05:37] give people an idea and it's quite good
[05:39] and quite fast. Then we have fabric IQ.
[05:42] So if you have stuff in Microsoft fabric
[05:44] you can make this ontology for it and
[05:46] then query it. You can also make
[05:48] something called a data agent. And then
[05:51] um we have work IQ um which can you know
[05:55] check all your teams chats and emails
[05:58] and and all that stuff. So you can
[06:00] connect that to Foundry IQ as well.
[06:03] Um so yeah so now there's built-in
[06:06] support for that in Azure AI search.
[06:11] Let's see. Foundry IQ knowledge bases
[06:13] are now GA. That's great. Um they they
[06:17] uh actually did some research about
[06:19] better recall from using the agentic
[06:22] knowledge bases. So here's Matt's blog
[06:24] post about it.
[06:28] Just enjoy the article. It just flashed
[06:30] out. Okay. So, so lots of cool research
[06:33] here um into the precision and recall
[06:39] and uh yeah, but those are the big
[06:41] things was um the the serverless and the
[06:46] new knowledge sources.
[06:48] So, check those out. Oh, let's see.
[06:50] There might be some follow-up questions
[06:52] about that. So, I'll pause.
[06:55] Oh, let me link to the lab, too. If you
[06:57] want to check out the lab,
[07:00] you can try running the lab yourself,
[07:02] but you won't be able to run the Web IQ
[07:03] notebook because pretty much nobody has
[07:05] access to Web IQ. You have to like ask
[07:08] permission for it and have a minimum
[07:10] spend of $10,000 a month. I'm guessing
[07:13] you haven't signed up for it yet, but I
[07:16] don't know. I don't know what you all
[07:17] what budgets you all have,
[07:21] but check that out.
[07:24] Oh, yes, I see. Yes. Good call from
[07:27] Justin. I already even have I have that
[07:31] blog post already open in my browser.
[07:33] Justin, because it just got it just
[07:35] dropped like what an hour ago. So, we
[07:39] can start talking about this already. Um
[07:41] I all I really all I did so far is look
[07:43] at the pictures. So, Enthropic did just
[07:45] drop their first mythos class model for
[07:48] public use which is Fable 5.
[07:51] And the benchmarks look really good. Of
[07:53] course, you know, we always have to take
[07:55] benchmarks with a grain of salt. Um
[08:00] because, you know, it's like the the
[08:02] models often learn the benchmarks over
[08:05] time. It's in the data yada yada.
[08:08] But you could believe that that it's you
[08:10] know, it's quite good. Um and it is now
[08:15] cloud fib. Wow, they have some cool
[08:17] demos here. protein complexes.
[08:20] Misaligned behavior.
[08:23] Let's see. So, it has the least
[08:26] misaligned behavior. Early feedback. Oh,
[08:28] cursors using it. Fable five. New
[08:31] safeguards.
[08:33] Interesting. So, they've got a system
[08:35] card. I always like looking at the
[08:36] system card. Oh, and a risk report
[08:38] separately.
[08:39] Safety classifiers. So, it looks like
[08:41] they've done a lot of um
[08:44] reinforcement learning on the safety
[08:46] front because they were concerned about
[08:48] that.
[08:49] It's great how much they have about the
[08:51] safety stuff.
[08:54] And I guess there's trusted access for
[08:56] Mythos 5. So, what's cool is that you
[08:58] can already get
[09:00] you can already if you go here to your
[09:02] co-pilot picker, you can already pick
[09:05] Fable 5, right? So here I've got fable
[09:09] five.
[09:11] We'll just say um evaluate all the
[09:14] results and determine
[09:18] what
[09:20] settings we should release as the new
[09:24] default. All right. So let's just see
[09:25] how Fable 5 does with picking up this
[09:28] current thread I have going.
[09:31] So yeah, try that out. Well, I don't
[09:33] know what the pricing what is the
[09:34] pricing indicator for this
[09:37] that thinking effort. Oh, this is cool.
[09:39] Oh, we can like set the thinking effort.
[09:42] That's quite high.
[09:44] Um,
[09:46] I was actually just running evaluations
[09:48] on our rag repo to figure out what GPT
[09:50] model we're going to um
[09:53] we're going to change it to. And I I was
[09:57] experimenting with none, low, and
[09:59] medium. I didn't even try high because
[10:01] try is so slow.
[10:06] Uh 1,000 in. Oh, okay. You So, people
[10:08] are giving me the pricing. Okay. I
[10:10] couldn't figure out where to get the
[10:11] pricing here. Maybe because I am not on
[10:13] like a real plan. I'm like on the
[10:16] unlimited plan.
[10:20] So, okay. So, Fable 5 replied, "Oh, here
[10:23] we go. That used 47 credits." And I
[10:26] think a credit is basically a penny.
[10:29] That was $4. That was kind of expensive,
[10:32] huh? That was a $4 request. That's too
[10:35] much. Okay.
[10:38] Um, let's see. Top three hurt citations.
[10:42] Okay. All right. So, it just
[10:47] perto optimal. My gosh.
[10:50] Okay. Recommendation. Okay. All right.
[10:54] Well, it's a nice response. Um, so it
[10:56] doesn't look like you want to use Fable
[10:57] 5 for everything because that was a $4
[10:59] request. It was quite fast though. You
[11:01] can see that was really fast. So it was
[11:04] able to blow through those $4 quite
[11:06] quickly. Um, but also because this is
[11:08] like I just threw a lot of context at it
[11:10] because this is a really long um thread
[11:13] I've been doing with evaluating.
[11:15] So if you did a brand new session with
[11:17] table five like it might be a good one
[11:19] for planning like maybe start planning
[11:20] with table five and then you know when
[11:23] your context is low and then move to
[11:25] another one for implementation
[11:27] double the price of 4.8.
[11:30] All right I feel like I should switch
[11:32] back to auto now maybe
[11:37] um uh to to save some money but that was
[11:40] fast and it was it was good. Um it was
[11:43] it it caught on to caught on to
[11:46] everything. Um
[11:49] so yeah and it would have been cheaper
[11:51] if id changed the the um you know the
[11:54] settings here, right? I could have done
[11:56] low and that would have been faster. And
[11:59] then um oh and you can switch between
[12:01] the context side of 200k or 1 million
[12:04] but then that can increase your cost.
[12:06] Okay. So that's apparently an option now
[12:08] in
[12:10] in um in VS Code. So let me change back
[12:14] to auto for now. Um cool. All right. So
[12:19] Pablo has a comment about web IQ. Um
[12:23] regarding web IQ or the risk associated
[12:25] anytimes access you know agents access
[12:28] external data. Do you get any answer
[12:29] about that? Um more agents separating
[12:32] comprehensive testing. Um yeah. So let
[12:37] me go to my slides from
[12:41] from the actual
[12:44] talk PowerPoint PowerPoint.
[12:50] Let me look at open reset. Okay,
[12:55] because I did try to talk about this a
[12:58] little bit during the lab, right? So
[13:01] with web IQ
[13:04] and and also with other like so this is
[13:07] what's the called the lethal trifecta
[13:08] right from Simon Willis
[13:11] um where we have a combination of access
[13:13] to private data ability to externally
[13:16] communicate and exposure to untrusted
[13:17] content right and the web results are
[13:20] really the untrusted content because you
[13:24] know a web page could have basically a
[13:28] jailbreak attacked in it some like some
[13:31] sort of prompt poisoning in it to try
[13:34] and get it to do something and
[13:36] especially if you add on
[13:38] any sort of like arbitrary MCP server
[13:40] that has right access then you actually
[13:42] can externally communicate that's really
[13:44] um really bad
[13:46] so yeah it depends so if you like
[13:50] because this is a trifecta right so you
[13:52] know if you have a combination of just
[13:54] access to private data and web search
[13:56] results then you know then you're then
[13:58] you're good right you don't have you
[14:00] don't have this one. Um and then and
[14:03] then you're kind of okay because what's
[14:05] the worst it could do? Like it can give
[14:06] you a bad result like it can give you an
[14:08] inaccurate result, right? So you do want
[14:10] to you know do some red teaming in terms
[14:13] of accuracy but the thing that's really
[14:15] bad is that when you also bring in the
[14:17] ability externally communicate. Um so
[14:20] like in the current version of work IQ
[14:22] that Foundry IQ uses, it does actually
[14:24] apparently have write access. So it
[14:26] could even send an email. That's
[14:28] obviously bad, right? So, they're going
[14:30] to migrate the work IQ to use the um
[14:34] just the readonly
[14:36] um thing. So, then you don't have the
[14:38] ability externally communicate. But in
[14:40] some ways also just answering a question
[14:42] is kind of the ability to externally
[14:43] communicate. Right? If you're making an
[14:44] app and it's trying to answer questions
[14:47] and it has access to private data and
[14:49] untrusted content, then there's
[14:51] definitely a risk that a web page result
[14:53] could poison the answer so that it is
[14:56] incorrect, right? And that is
[14:58] communicating an incorrect answer to a
[15:01] user. Um, so yeah, so you do have the
[15:04] risk. Um, but what we recommend is using
[15:08] the the guard rails in in Foundry,
[15:11] right? So if we go over
[15:15] here, um
[15:20] let me let me also check.
[15:29] Let's see.
[15:33] Sign in again. Foundry always makes me
[15:35] sign in again.
[15:43] Uh,
[15:46] let's just set up some custom
[15:49] guard rails here. Right. So, Foundry
[15:52] Experiments project. Good. All right.
[15:54] I'm going to go to build guard rails.
[15:58] Okay. And then we can make a new
[16:01] guard rail. Um,
[16:04] they changed it again. Okay. All right.
[16:06] So what we're going to enable is
[16:08] jailbreak and you can say block. You can
[16:10] also do what you want to do for web is
[16:12] indirect prompt injections, right? So
[16:15] this is going to block based off of tool
[16:19] responses. So it's going to check the
[16:20] tool responses, right? So if there's a
[16:22] tool response from, you know, like web
[16:25] results or web IQ or founder IQ, then um
[16:29] then it can block. Then we've got
[16:32] content harms. We just enable that. I'm
[16:34] not going to do a block list. Um, you
[16:36] could do protected materials if you
[16:38] cared about that. EI risk type.
[16:44] Yeah, you can even use guard wheels to
[16:46] basically run the LM evaluators
[16:49] in line. That's going to add latency for
[16:51] sure. But you could also Yeah, you could
[16:53] you can bring in groundedness as a as a
[16:57] guardrail now. So you but that that
[17:00] definitely increases latency. So the
[17:01] thing I wanted to do was enable
[17:03] jailbreak and indirect prompt
[17:05] injections.
[17:08] So then we would say okay we're going to
[17:10] enable it here
[17:13] and then here create. Okay.
[17:18] So if we so Pablo says if we acted it
[17:21] would you get logs of all detected
[17:23] events? Um I set it up in block mode. So
[17:26] you would get an actual content filter
[17:29] error and you'd have to decide how you
[17:32] want to like handle that in your in your
[17:34] code. So for example,
[17:38] I'll show you how
[17:42] you know what you could do there. Um
[17:48] error. Okay.
[17:51] All right. So you'd say like okay if the
[17:54] error if you get an error and it is the
[17:56] content filter error then um you know
[17:59] you can you can log it a certain way
[18:01] right so you know it's just it like
[18:04] there it depends how you're using the
[18:06] the agent how you're logging things but
[18:08] it is an actual error that comes back
[18:11] from the Azure OpenI
[18:14] responses API so
[18:18] so you know you usually if you're making
[18:20] a userfacing navigation you do want
[18:21] actually catch the error and show
[18:23] something nice to the user, right? So,
[18:24] we, you know, we actually show something
[18:26] nice to the user. But if you don't catch
[18:28] the air, then it will just be a straight
[18:29] up error and it'll show up on your error
[18:31] log and it'll have, you know, a certain
[18:32] shape to it um where it's noted as a
[18:35] content filter. So, that's if it's
[18:37] blocked. The other mode is if you just
[18:39] annotate only. So you can I I said to
[18:43] block for mine, but you can change it to
[18:45] annotate only, but then you have to be a
[18:48] lot more diligent and actually
[18:51] there there, you know, you would get it
[18:53] in your open telemetry, assuming that
[18:55] you're you've got open telemetry enabled
[18:57] on all of your um agent calls using, you
[19:02] know, if you're using agent framework,
[19:04] that's very easy to enable the open
[19:05] telemetry. But then you would really
[19:06] have to set up like a custom dashboard
[19:08] that looked for the annotations inside
[19:12] the responses. Um, it would be like in
[19:15] the content, there's a content filter
[19:17] block in the JSON and then there's a
[19:18] prompt filter block in the JSON.
[19:22] So yeah, I typically do block. You do
[19:25] annotate, you're going to have to be a
[19:26] lot more diligent.
[19:31] So what you could do is block and then
[19:34] you know look to see at all the block
[19:36] things and see if it's being too
[19:37] aggressive, right? This this is always
[19:39] the the balance, right? Like it's safer
[19:42] to block as many things as possible, but
[19:44] then you can have it where it's too
[19:45] aggressive, right? So I've certainly had
[19:48] my request be blocked due to like um
[19:50] like sexual like if I ask like medical
[19:52] questions that sometimes gets blocked
[19:54] for for sexual.
[19:58] So, some people will like change this
[19:59] blocking level to to lower depending on
[20:02] what the thing is. But also, if you're
[20:04] doing an app about like work stuff, you
[20:07] probably don't need to be asking medical
[20:08] questions, right? Is the hardest is when
[20:10] you're doing like a general chat app
[20:12] that's trying to answer any question,
[20:14] then it's it's, you know, it's you have
[20:16] to kind of let more things by because
[20:18] people could be asking medical questions
[20:19] and maybe you're okay with that, right?
[20:21] Um but if you are doing a very work face
[20:23] work um specific app then a lot of times
[20:26] you can actually block more. I've also
[20:29] seen that some of my web results get
[20:31] blocked due to these filters and that's
[20:33] interesting.
[20:36] Um so
[20:39] yeah, so I would say um do that and then
[20:42] of course set up uh the red teaming,
[20:44] right? So we have the red teaming
[20:45] evaluation and now that's that's easier
[20:48] to do. Um, and so you would set up the
[20:52] red team and
[20:55] um, you know, check to see. Now, I
[20:57] wonder if they have a red team kind of
[20:58] specifically around because you're most
[21:01] concerned about Oh, yeah. Good, good,
[21:03] good. Attack strategies, indirect
[21:05] jailbreak. Okay, so they have a specific
[21:07] attack strategy for indirect jailbreak
[21:09] and that is exactly
[21:12] exactly what we want. I actually haven't
[21:14] tried running that yet. Um, but they
[21:15] have that example here. So, um, so what
[21:19] I would say is make an make a red
[21:21] teaming run that uses indirect jailbreak
[21:24] and test that. I don't know exactly what
[21:27] it's going to, you know, throw at your
[21:28] thing and if that's going to look
[21:30] similar
[21:31] to, you know, what
[21:34] um what your agent might see, but I
[21:39] think that's a good start. Um, so Pablo
[21:43] says, so Pablo wants the agent to solve
[21:45] a task. It can create a skill MCP find
[21:48] information go into the insid content
[21:51] detect issues but not block.
[21:56] Okay. I mean you can you can also run
[21:58] the guard rails in annotate mode. That
[22:00] that would be the other approach. As
[22:02] long as you're then basically when you
[22:04] get as long as you're wrapping it with
[22:05] some code then you can check to see
[22:07] every time the response gets back just
[22:10] look for the content. Um, so you
[22:12] wouldn't look for the error. You would
[22:13] just look for the um the actual content
[22:18] filter block. Let me see if we have the
[22:21] JSON. And then you would decide what to
[22:23] do, right? Like if you want to give a
[22:25] warning, if you want to log it, however
[22:27] you want to do it. Configure. Okay. I
[22:32] don't want is it not click anymore?
[22:35] Content filter. Content filter results.
[22:39] I wanted to see. Okay.
[22:41] Where is it? Opening eye two years ago.
[22:44] Nope.
[22:48] Let's see if we can put Foundry Guard
[22:50] Rails responses API annotate. I want to
[22:53] see exactly what it looks like in
[22:56] annotate mode.
[23:01] Guard rails for agents versus model.
[23:06] Uh
[23:08] indirect attack levels. Okay,
[23:16] evol
[23:19] intervention points. All right, let's
[23:21] see. Intervention points.
[23:26] >> I want to see exactly
[23:29] what the JSON looks like. Code examples.
[23:32] Okay,
[23:35] little dump JSON. There we go. Thank
[23:37] you. Okay, this is what I was looking
[23:38] for. All right. So, view annotations.
[23:41] Here we go.
[23:44] Um,
[23:47] so you're going to get back content
[23:49] filter results
[23:51] is using chat. That's actually using
[23:53] that is really old. It's using
[23:56] completions. We don't use completions
[23:57] anymore.
[23:59] Okay. Sorry. I have to
[24:02] let me talk to the team. Um, because we
[24:05] should change this to use the responses
[24:06] API.
[24:08] Um
[24:10] because this is we're trying to
[24:13] encourage
[24:14] at at least check completions but it
[24:16] should be something similar. So you
[24:17] should get back content filter results
[24:19] and you can see what it detected right
[24:22] detected true or detected false and then
[24:25] you can decide what to do with it.
[24:29] But um I will say we should do some
[24:32] updates there.
[24:36] All right. Um okay. So, so all right.
[24:39] So, let's look at some of the other
[24:41] questions we have here. All right. So,
[24:45] great. We got a question about OpenClaw.
[24:49] All right. Now, here's the thing.
[24:51] OpenClaw Dev, I actually am technically
[24:54] a maintainer on this repo.
[24:57] So, I should I you you would think I
[24:59] would have deployed it by now. I haven't
[25:01] had a time to deploy it yet, but we are
[25:03] going to be showing this in a few weeks
[25:05] at a conference. So, it is definitely on
[25:07] my to-do list to deploy this. Actually,
[25:09] I also haven't deployed OpenClaw yet. I
[25:11] did deploy something else from OpenClaw
[25:13] yesterday, which I'll show in a second,
[25:14] but yeah, I haven't done it yet. Um, I
[25:17] definitely want to do it really soon.
[25:19] Um, I think we just did it with Okay.
[25:22] Oh, it's got its own. Okay.
[25:25] And I think it's wrapping for a D. All
[25:28] right. So, yeah, please do give this a
[25:31] go and file any issues. Let's see if we
[25:32] have issues. Oh, we do have some issues.
[25:34] Okay.
[25:37] Okay. Five days ago action. All right.
[25:40] So,
[25:42] um,
[25:43] yeah, give it a go. I'll give it a go,
[25:45] too. File issues. Um,
[25:51] because Yeah. And this uses the new,
[25:53] this was the other thing I wanted to
[25:54] talk about was ACA sandboxes. So, I
[25:57] believe this is using the new ACA
[26:02] sandboxes, which are
[26:06] super cool. Where's the Let me see.
[26:09] This one.
[26:12] I think this deploys there. Unless it's
[26:14] only going to Kubernetes. Let's see.
[26:19] Cloud sandbox
[26:24] architecture as your container apps host
[26:27] the open cloud effl container host
[26:30] layers drop. Let me ask let me ask my
[26:33] colleague Arun
[26:38] and
[26:41] is is this
[26:49] all right let's ask about that um
[26:55] and then okay you were wondering okay so
[26:58] your question was can it be run on a
[26:59] cloud PC See,
[27:02] this is a dumb question, but what is a
[27:04] cloud PC? Is that
[27:07] Is that a dev box? I'm just a silly Mac
[27:10] user.
[27:12] What is a cloud PC? Cloud PC.
[27:18] It sounds like a Windows in the cloud. I
[27:21] We have something called dev boxes.
[27:22] Maybe that's that's what a dev box is.
[27:25] Or maybe that's something else. Oh, M365
[27:28] cloud PC. Okay, thank you.
[27:33] Let me ask
[27:35] Windows 365 and All right, I'll just
[27:38] ping the maintainer
[27:42] run
[27:46] PC.
[27:55] All right. Um, it it says it can be on
[27:59] Microsoft execution containers for a
[28:01] local Windows machine, but you're you're
[28:03] asking if it can be on a cloud PC. Okay.
[28:05] Well, um Oh, it's like a dev box. Okay.
[28:07] All right. So, I just asked um
[28:12] Yeah, because then that's that would be
[28:14] safer, right, to it in that sandbox
[28:16] environment.
[28:18] And you I guess you want to use more of
[28:20] the Windows stuff versus the the Linux
[28:22] stuff on the ACA.
[28:26] All right. Well, maybe we'll get a reply
[28:27] from Arun
[28:30] during the office hours and I can let
[28:32] you know. The thing I did deploy
[28:34] yesterday which is
[28:37] useful which is from the open claw team
[28:39] is the go CLI. This is for Google and
[28:42] it's funny I guess talking about Google
[28:43] in office hours but I still I use a lot
[28:45] of Google because that was my first job.
[28:48] So for my personal stuff is all on
[28:50] Google. Google calendar, Gmail, right?
[28:52] All my family stuff is on Google
[28:57] and um so this was really helpful. I
[29:00] used this yesterday
[29:02] set this all up. Um so this is from
[29:04] Peter from OpenClaw and it's just like a
[29:08] very agent friendly. So it's kind of
[29:09] like work IQ, right? Like work IQ would
[29:11] be our equivalent. Um though this is a
[29:13] little more programmatic and specific,
[29:15] right? Whereas his work IQ is actually
[29:16] an agent itself. But this is just it's a
[29:18] command line CLI for Google stuff. But
[29:21] it does work well with Copilot. So you
[29:23] can use it with OpenClaw because
[29:25] obviously they made it with OpenClaw and
[29:26] a lot of people are using it with
[29:27] OpenClaw and um Telegram.
[29:30] But I haven't set up OpenClaw yet
[29:32] because I'm trying to decide what
[29:33] computer it's safe to do it on.
[29:36] But I did use it um with GitHub Copilot
[29:41] and I used it to schedule put my kids
[29:44] summer camps on a Google calendar and so
[29:46] that was helpful because that's just
[29:47] kind of a annoying to do all that and
[29:49] then I made a custom skill for it just
[29:53] to make it really
[29:55] easy for it to do.
[29:58] Um, so yeah. So that's something that
[30:01] could be nice combining combining um
[30:05] with
[30:06] with these claws and agents and stuff.
[30:10] Let me link to my skill.
[30:13] Um,
[30:15] and that I only set up on my other
[30:17] machine. Um, so just to keep things
[30:22] keep things separate. Okay, so
[30:26] let's see.
[30:28] So there's some questions about
[30:32] how much Okay, so there's questions
[30:35] about ML engineering versus AI
[30:37] engineering.
[30:39] Um, and yeah, the debate about ML
[30:42] engineer versus AI engineer. I think at
[30:45] this point basically we all need to know
[30:48] AI engineering, which is we all need to
[30:50] know how to incorporate LLMs into our
[30:55] our code bases, right? Just like before
[30:56] we needed to know how to use regular
[30:58] expressions. We think of a regular
[31:00] expression as being like a supercharged
[31:02] or like a think of an LLM as being like
[31:04] a supercharged regular expression,
[31:06] right? Very good at patterns.
[31:08] So, you know, we should all know how to
[31:10] incorporate LLMs into our into our code.
[31:16] So, if you're building a backend app,
[31:18] what does that look like? If you're
[31:19] building automation scripts, what does
[31:21] that look like? So at this point I think
[31:23] AI engineering is just required skills
[31:26] for a software engineer. Um because
[31:28] there just might be a time where you're
[31:30] like oh because I can think of lots of
[31:31] times when I was doing software
[31:33] engineering where like actually if I had
[31:35] had access to an LLM that would have
[31:37] been the way to architect something
[31:40] right um and I would have just I would
[31:44] have just you know gone for the LLM
[31:46] instead. like there's some features that
[31:48] I spent years trying to trying to work
[31:51] on like for Khan Academy and in
[31:53] retrospect if id had an LLM
[31:56] I would have just been able to do it. It
[31:57] would have just worked. It would have
[31:58] been amazing. Um so yeah, I think at
[32:01] this point everyone should have um the
[32:04] ability to incorporate LMS into
[32:07] workflows. I think if you're a dedicated
[32:09] AI engineer that means like that is like
[32:11] the main thing you're working on is that
[32:14] you're going like really really focused
[32:16] on building um AI centric workflows
[32:21] but I just think generally everybody
[32:23] needs that that capability. Now ML
[32:25] engineering I do think that's when I
[32:27] think of ML engineering I do think of
[32:28] that as being like okay you're actually
[32:30] fine-tuning the models you're you know
[32:33] you're maybe you're setting up
[32:36] yeah I think of that as actually you're
[32:38] you're using some amount of fine-tuning
[32:40] pietorch etc and there you have to like
[32:43] really understand the math and the
[32:45] training and all that stuff
[32:48] yeah as mushroom man said ML is much
[32:50] deeper in the mathematics
[32:52] and AI engineering uses models to solve
[32:54] problems
[32:55] Yeah, I ag I agree on that. I'm
[32:58] certainly not an ML engineer. I'm more
[33:01] of a an AI engineer now.
[33:07] And just because I my my background is
[33:09] not in uh data science, but I think that
[33:12] there is an overlap in that we all need
[33:15] to be running evaluations, right? And I
[33:17] don't think most people are running good
[33:19] evaluations, right? So just how we all
[33:21] had to learn how to write like unit
[33:22] tests and integration tests now we need
[33:24] to all be running um evaluations and red
[33:26] teaming and that does overlap with the
[33:29] data science aspect of ML because we all
[33:31] do need to think a bit like a data
[33:32] scientist like I've been running these
[33:34] these evals over
[33:38] you know over the the last few days um
[33:42] right to try and figure out like okay
[33:44] what you know I'm you know I'm using
[33:48] this particular um LLM in this
[33:52] application. Okay, there's a new LLM
[33:55] out. Do I want to change to that LLM?
[33:57] So, here I do have to go about this with
[33:59] a bit of a more of a data scientist
[34:02] perspective. Um, now ideally we would
[34:05] have enough people working in
[34:06] organizations that maybe we could work
[34:08] with data data scientists to be able to
[34:12] set up these evaluation workflows
[34:14] because they're both there's like a big
[34:17] overlap here between the software
[34:18] engineering side and the the data
[34:20] science side. So that's where I think
[34:22] lines are getting the most blurry. And
[34:24] um that's definitely a skill that I
[34:26] think it's helpful for all of us to have
[34:27] so that when these new models come out
[34:30] or when there's a a new feature or
[34:33] something, some prompt caching or a new
[34:35] prompt technique or whatever, we can try
[34:37] it out. We can run our evouse and we can
[34:39] decide, okay, that's going to be the new
[34:43] the new thing that we use.
[34:48] Um let's see. Okay, so Justin says, "Are
[34:52] there any
[34:54] voice evals
[34:57] besides me calling?" Um, wait, besides
[35:02] me calling, are you is you calling the
[35:04] eval?
[35:06] I'm having a hard time parsing that. Um,
[35:09] you deploy GPTI real time as your phone
[35:12] and it does tool. You're using GP
[35:14] realtime as your phone. That's cool. Um,
[35:18] I haven't messed with the latest
[35:20] real-time models. I wanted to do like a
[35:22] magic mirror on the wall for Halloween
[35:24] as an excuse to use them, but I probably
[35:27] won't get around to it. Um,
[35:30] so yeah. Um, let's see.
[35:34] I've seen startups in the voice space do
[35:37] evals
[35:40] called
[35:41] um, let me see. Agent Con Silicon Valley
[35:47] Let me try and find the
[35:50] startup that does voice stuff
[35:52] specifically.
[35:56] I'm hoping the new like the the original
[35:58] realtime models were a little rough. I'm
[36:00] hoping they're better a lot better now
[36:02] because I last time I played with the
[36:04] real time ones was like a year ago. Um,
[36:08] Veilance. Okay. Veilance AI
[36:15] coach. Interesting. Did they like
[36:20] age
[36:22] or is this a different one? There's so
[36:24] many. Veance AI AI. Emotion AI for
[36:27] voice. Okay. AI for emotional
[36:29] intelligence. What bookmarks do they
[36:30] benchmarks do they use?
[36:41] solutions voice agents.
[36:44] Let's try to see if they have some good
[36:46] benchmarks here.
[36:56] Okay, I don't see what benchmarks they
[36:58] use.
[37:00] The other one would be the Sierra Tow 2
[37:03] have a voice benchmark
[37:06] um voice dlux.
[37:09] Let's try this one. Is a specialized
[37:11] extension? Okay, so this might be the
[37:13] thing. Oh, this is on deep wiki. So tow
[37:17] that's the benchmark from Sierra. They
[37:19] develop customer support agents. So
[37:22] they're like the Okay, here we go. So, T
[37:25] voice towel voice
[37:29] benchmarking full duplex voice agents on
[37:32] real world domains.
[37:36] Maybe check this one out. Oh, yeah.
[37:38] You're linking the docs. Very good. Um,
[37:45] so, but it looks like there's a repo for
[37:47] it. So, to bench now supports the think.
[37:49] Here we go. This one. Oh, three. T3
[37:55] bench. Okay. So, this might I'm trying
[37:57] to see if it's also in the GitHub
[38:04] in their GitHub or they it might be that
[38:07] it's only Here we go. There's their
[38:08] GitHub
[38:13] voice. Okay. Yeah. So, I think this
[38:16] would this would be what I would run.
[38:18] Um, agent framework also has integration
[38:20] with how to bench, but I don't know if
[38:21] they specifically have the voice
[38:23] integration. Let's check that
[38:28] packages
[38:30] and sender lab
[38:33] and how to
[38:37] go.
[38:40] Okay. So, I think their their howto is
[38:43] looks like
[38:45] limited to just
[38:48] right now. Let's see if there's any
[38:52] dates for that voice. Yeah.
[38:57] No, no one's filed a thing for it. Okay.
[38:59] So, I would say um for voice evaluation
[39:04] then
[39:05] how to bench looks like your
[39:09] best thing. Now they they're specific to
[39:12] domains, right? Airline, retail,
[39:13] telecom, banking knowledge because
[39:15] they're very much focused on customer
[39:17] support. And I guess these are the big
[39:18] industries.
[39:20] I don't know how well it's going to work
[39:21] for a generic a generic one.
[39:26] But it looks like it'd be fun to try
[39:29] and see.
[39:34] We can also check. Wait, does Foundry um
[39:37] foundry evaluations
[39:40] Um voice I don't know if we have
[39:42] anything built in for voice. How do you
[39:44] evaluate voice live agents? Okay. So we
[39:48] have voice live but I think voice live
[39:49] is different from real time right. What
[39:52] is voice live? Voice live API blah blah
[39:56] blah. Voice live API gives a transcript.
[40:00] Um maybe voice live wraps on top of
[40:03] these things. Low latency kings and
[40:05] narrows features of the voice live API.
[40:08] GPD5.
[40:10] I feel like this must be from the Azure
[40:12] speech. Oh, here we go. Model GPI. Oh,
[40:14] they don't have real time 2 on here.
[40:16] Interesting.
[40:18] Know if that's up to date.
[40:22] Real time mini voice live pro because
[40:26] you said you're using real time too,
[40:28] right? So I don't know if that's just
[40:31] that it's behind.
[40:34] So I think voice live looks like it's
[40:35] wrapped on top of it basically. So, if
[40:37] you are using voice live, then we do
[40:40] apparently have
[40:42] a um
[40:46] built-in evaluator for it. Oh, this is
[40:50] fun. So, you your data set is actually a
[40:52] wave file. That's fun.
[40:54] >> You have a um
[40:56] your data set is a wave file. Then it's
[41:01] B. It looks like it's going to trans
[41:02] transcribe and then and then evaluate
[41:06] the idea real time
[41:12] the evaluation.
[41:16] Okay. And then you it looks like you can
[41:18] basically these are all of our standard
[41:20] evaluators like intent resolution, task
[41:22] adherence.
[41:24] So you you can evaluate the standard
[41:28] one. So I think it's basically like as
[41:29] it says up here it's doing you know it's
[41:32] taking care of the transcript
[41:35] of it and then and then sending it to
[41:37] the evaluators.
[41:44] All right. Um
[41:50] cool. Well let me see if we have Nope.
[41:54] Okay. All right. So, I would say give
[41:57] that a go. Though, it is interesting
[41:58] that it doesn't mention GO GPT real time
[42:01] 2. I don't I'm not sure how Wait, how
[42:03] recent is real time 2? When was that
[42:05] launched?
[42:07] Real time to speech speech.
[42:11] Let me ask
[42:24] Yeah. Okay, so I think a question for
[42:27] the product team is well when does when
[42:31] is voice live going to support real time
[42:32] 2 or maybe it already does and the
[42:34] documentation needs updating.
[42:39] Um let's see. Yeah. Yeah. In terms of
[42:42] learning AI engineering and ML
[42:44] engineering, I always just link to my
[42:48] blog post about I learn about generative
[42:51] AI. Um, this has kind of a mix of ML
[42:54] engineering and AI engineering,
[42:58] but basically for ML engineering,
[43:00] Sebastian Rashka has fantastic
[43:02] resources. So does Andre Karpathy. Those
[43:04] are my two for ML engineering, but
[43:07] saying like I'm not deep into ML
[43:08] engineering. I just learn enough to
[43:10] understand what's going on. Um, but then
[43:12] there's AI engineering is a great book
[43:14] by Chip. And then you know of course
[43:17] there's um you know we've given lots of
[43:20] video series here
[43:23] I'll there's even more than this so I'll
[43:26] I need to update this with with more of
[43:28] our series but
[43:31] that is my usual link for learning
[43:35] uh let's see turbo quant I didn't turbo
[43:39] quant did turbo quant come up few weeks
[43:42] ago vector turbo google's turbo quant
[43:45] for vector search
[43:48] rest vector index. Oh yeah, I feel like
[43:51] this did come up a few weeks ago. Let me
[43:53] check to see if we talked about like
[43:56] what we
[43:58] what we decided about if we discussed
[44:01] it. Let me see. Turbo because I feel
[44:02] like I asked my colleagues about this
[44:05] restfit turbo quant right um
[44:10] then f the thing is we also we have disk
[44:13] ANN at Microsoft from Microsoft research
[44:17] so I don't know how turbo quad compares
[44:21] to
[44:24] um
[44:27] let's see
[44:34] And then okay, I'm just seeing where
[44:36] I've asked about it.
[44:43] All right, I didn't get any replies last
[44:45] time. I asked my colleagues about
[44:48] getting asked about
[44:53] it might be that it's you know that
[44:55] discann
[44:58] uh discann like has similar performance
[45:01] improvements.
[45:09] matching.
[45:21] So you just build it. So I guess maybe
[45:23] this would work
[45:26] with an open source embedding model
[45:29] online inest. Okay. No train step. Oh,
[45:31] so you could use it for because whenever
[45:33] you're looking at an indexing algorithm,
[45:35] you want to see whether it's something
[45:36] that you can add new data on the fly.
[45:40] Um,
[45:44] uh, and it looks like you can, it says
[45:46] online ingest. You're local, so you
[45:49] could use it with like Nomic embed or
[45:51] Harrier. Apparently, Harrier is quite
[45:53] good. That's a new embedding model. Uh,
[45:55] you can do
[45:57] Okay, you can do a filter. That's good.
[46:03] Hybrid results.
[46:05] Restrict result to candidate set
[46:09] dense rerank. Okay. Framework
[46:12] integrations lang chain llama index
[46:14] haststack agno. I remember agno
[46:19] rust recall
[46:21] versus fee. So this is comparing it to
[46:24] fee. I never use fee because fice is I
[46:26] think in memory only. um it's not so
[46:29] good for like production. So what we
[46:31] want to know is how does it compare to
[46:33] other things like diskn
[46:36] HNSW but maybe it's not supposed to be
[46:40] okay we compare default production grade
[46:43] really okay
[46:45] um I think we'd want to know how it
[46:47] compares to
[46:49] to other stuff so I don't know if it's
[46:51] necessarily going to give you
[46:52] improvements over like Azure AI search
[46:55] because Azure I search does implement
[46:56] compression already like both
[46:58] quantization and
[47:01] Matrioska representation learning
[47:03] compression. So the two different kinds
[47:05] of compressing vectors. So we already
[47:07] have that. Um but maybe this is like
[47:09] maybe this is the best if you were going
[47:12] to do something on a single machine
[47:15] because that's kind of seems like what
[47:16] it's designed for. So if you wanted to
[47:19] have like a massive index on on your box
[47:22] and still get fast
[47:26] singing. I guess also I could even use
[47:28] it when we're, you know, doing local rag
[47:31] demos. Your local no managed service.
[47:35] Okay. So I guess it could also be a good
[47:37] option when I'm doing a demo of rag
[47:40] locally to use turbo quant instead of
[47:42] using like
[47:45] brute force cosign or or fee.
[47:51] Uh but I don't yeah I don't know about
[47:53] it for whether it's it's going to give
[47:55] us improvements over our production
[47:57] options right now because oh also some
[48:00] other cool wait let me that reminded me
[48:02] of some other cool stuff so so there's
[48:04] PG
[48:05] durable
[48:07] um so this is from the Postgress team
[48:10] where are you going no go to Bing
[48:15] sorry Oregon Trail
[48:18] why would I be searching that it's crazy
[48:20] okay PG durable Here we go. Okay, so
[48:22] this is a new thing from the Microsoft
[48:24] team. And then because what remind me of
[48:28] this is that they also just added a
[48:30] BM25. Um, let me see. Is it is it in
[48:34] Matt's book of news book?
[48:38] This one. Okay. Postgress
[48:41] be secure.
[48:43] Uh, this one. Okay. So, bill 26 roundup.
[48:49] Um,
[48:52] okay. Let's see what's in the roundup
[48:54] here for Postgress.
[48:56] There we go. So, we got Okay. Um, okay.
[48:59] No. PG duck DB. PG IBM.
[49:03] This duct DB IBM.
[49:06] No, I wanted
[49:09] Oh, I like this one. Automatic entra
[49:12] token refresh libraries. That's quite
[49:14] helpful, actually. That's specifically
[49:15] for Python. Nice. I didn't know about
[49:18] that. Um, okay. Pre-upgrade new
[49:21] built-in.
[49:23] Where is the
[49:25] new BM25? I think they're using the time
[49:28] scale one. So, I think basically like
[49:29] time scale as a BM25
[49:34] PG tech search. So, I think that Azure
[49:37] Postgress now supports PG text search.
[49:42] So, now on Postgress. There we go. There
[49:44] we go. Okay. Come on.
[49:48] That was February. I think it's been
[49:50] updated.
[49:58] Okay, we don't have docs about it. So,
[49:59] let me just ping ping them about it
[50:02] because I thought that that was updated
[50:03] now.
[50:05] Um,
[50:06] got
[50:15] And let's see.
[50:30] All right. Let me ask about that. Um
[50:32] because what I was trying to just say is
[50:34] that I think if you're using um vector
[50:37] search in production on Azure I think
[50:40] you're going to get pretty good
[50:41] performance from either the Azure search
[50:44] HSW implementation or on all the other
[50:46] databases they're using diskn and diskn
[50:49] is fairly performant. That was
[50:53] my my the takeaway.
[50:56] All right so
[50:59] um cool. All right, we are now at time
[51:03] here. I see there's some nice links in
[51:06] the chat to help people with their ML
[51:08] engineering and AI engineering. Um, I
[51:13] don't I don't think we covered
[51:16] much of these links at all. Let me see
[51:17] if there's anything else. So, we talked
[51:19] about Fable.
[51:21] That was the big thing there. Oh,
[51:23] there's new MAI models. So, do check
[51:25] those out because now we've got our own
[51:27] um like LLM and code models. So that's
[51:30] another thing to try in VS Code is the
[51:32] new MAI models if they're available. And
[51:35] um the GitHub co-pilot app got some
[51:37] updates as well. So do check that out.
[51:39] Now you can make like custom canvases
[51:41] for custom UI like or whatever you want
[51:44] to do with it. And then coming up um if
[51:47] you're in SF you're probably not. We
[51:49] have the engineer world's fair but
[51:51] virtually we have the Postgress
[51:53] conference. So I'll have a talk for that
[51:56] one. Uh so that'll be streaming live and
[51:59] we are planning our next series um live
[52:02] stream series will be in Microsoft IQ
[52:04] series. So doing Foundry IQ, work IQ and
[52:07] Fabric IQ. So looking at end of July for
[52:11] that one. So stay tuned. Uh oh, and
[52:15] right now it's agents link actually. So
[52:17] if you all aren't doing agents league,
[52:19] you might want to check that out because
[52:20] there's like a lot of prizes in it. Um,
[52:24] so here is, let me get the agents league
[52:26] information. Here we go. Ends um
[52:31] June
[52:33] 14th.
[52:35] Let me get the link.
[52:38] Here we go.
[52:42] Check out the agents link hackathon. My
[52:43] colleagues are running that right now.
[52:45] And then the question was, what are AI
[52:46] credits? I assume you're meaning maybe
[52:49] talking about co-pilot credits. And I
[52:51] think they're basically equivalent to a
[52:53] penny.
[52:55] So here this is a $4.7.
[53:00] Um yeah, so they do get burned really
[53:03] fast. Um we are looking into like token
[53:06] efficiency modes. So
[53:09] um there's a VS Code issue about it. If
[53:11] you do have any like comments on that,
[53:14] let me see. We're just chatting out
[53:15] about
[53:18] this one. explore an efficiency mode
[53:23] and um there's some discussion there. Um
[53:28] I know some developers are so if you're
[53:29] on like co-pilot pro or pro pro plus
[53:32] then you're probably seeing that you're
[53:33] using your your plan a lot faster. So
[53:37] I've been following various peoples that
[53:38] are trying to figure out the most token
[53:39] efficient models like Nicholas was like
[53:41] oh Gemini 3.1 Pro is one of the least
[53:43] token hungry models. Um, so yeah, so the
[53:46] VS Code team is trying to figure out how
[53:48] to help people out with with using less
[53:51] tokens um because right now models use
[53:55] too many tokens. So yeah, so both you
[53:59] both want to like use models that um are
[54:03] like cheaper but that just have a lower
[54:05] like multiplier, but also you want to
[54:08] use models that don't waste tokens. So,
[54:12] for example, like um you know, like
[54:14] maybe GBD55 does like way too much code
[54:16] exploration at first, and that uses a
[54:18] lot of tokens. It's lots of tool calls.
[54:20] It's adding lots of context to the
[54:21] context window. So, we have to figure it
[54:24] out.
[54:28] All right.
[54:29] Yeah. From token maxing token
[54:31] optimization. Uh yeah. So I think John
[54:34] that's basically what they're thinking
[54:35] of like is having a different instead of
[54:38] auto mode having more of a lowcost mode
[54:40] that would um would really try to
[54:44] optimize for it. Um but if you have any
[54:46] ideas
[54:48] add it to add it to that thread there.
[54:53] All right. Okay. Thank you everyone. So
[54:56] is recording is still going. Um, so I
[55:00] will post the recording and transcript
[55:02] of everything we talked about in the in
[55:06] the forum um here so you can find
[55:10] everything later for easy reference.
[55:15] All right, thanks everyone. Great chat
[55:17] today. Bye.

[00:00] Welcome to our Python AI weekly office
[00:03] hours. It is March 31st.
[00:06] So close to April 1. See what exciting
[00:09] things people decide to do on April 1.
[00:13] And uh I see some good waves in the
[00:15] chat. I see a good Clippy. Where's my
[00:18] Clippy? I have my Clippy sticker right
[00:20] here. Some of you might know that I got
[00:22] to dress up as Clippy last week at the
[00:24] MVP Summit and that was one of the best
[00:26] moments of my life. I'm trying to I'm
[00:29] trying to let them dress up as Clippy
[00:31] again for Microsoft Build in San
[00:33] Francisco, but I don't know if they're
[00:34] going to bring the Clippy costume down
[00:35] or not. Anyway,
[00:39] so let's start off with the news like we
[00:41] always do. Um, there is for those of you
[00:45] working on agent framework in Python,
[00:47] they just did a new release candidate
[00:49] for it. That's RC6.
[00:51] RC6, as I've been told, should be the
[00:54] last one before going G8. Um, so
[00:58] assuming that there's no issues in RC6,
[01:01] then uh hopefully the next one is going
[01:03] to be the GA version. That's what I
[01:06] hear. So that's very exciting. Uh, some
[01:11] big uh things going around the internet
[01:13] in terms of GitHub this week. So um one
[01:17] thing was that GitHub changed the um
[01:22] privacy policy a bit to be so that now
[01:29] will the beginning they will begin using
[01:32] interaction data so inputs outputs co-s
[01:35] snippets all that context from co-pilot
[01:38] free pro and pro pro plus users to train
[01:40] and improve AI models unless you opt out
[01:44] so if you I'm actually like fine with it
[01:46] because everything I do is public
[01:48] anyway. But um also and if you are at an
[01:52] organization and the organization um
[01:56] uses um you know is like private repos
[01:59] and stuff then let me actually find the
[02:01] cop FAQ though because that's more
[02:03] helpful community.
[02:06] Uh here we go. So, you have additional
[02:08] questions. A lot of them are covered in
[02:09] this one, which is that FAQ.
[02:15] Um, because there's a lot of followup
[02:17] questions on this one.
[02:20] Um, so if you do want to opt out, let's
[02:24] see. Train out.
[02:28] How do we do it? Okay, so co-pilot. So,
[02:31] I'm in Copilot Enterprise. Oh, since I
[02:33] have copied enterprise, that means that
[02:35] um I
[02:38] am not opted in anyway because that's
[02:42] not affected by this. Okay. All right.
[02:44] So, yeah. So, if that if that is
[02:47] something you care about, then um
[02:49] definitely look into that and
[02:52] opt out if you would like to.
[02:55] Uh so, John says, "What is the GA
[02:58] version? Can't we not install agent
[03:01] framework?" Um so at Microsoft they have
[03:04] this terminology called you know they
[03:06] have like private preview public preview
[03:08] GA and I guess this terminology is used
[03:12] across the industry now apparently
[03:14] Google started it. Um, so you know the
[03:17] idea is that some companies when once
[03:19] something goes GA that's an indication
[03:21] from Microsoft that hey like this is
[03:23] something that you know is fairly stable
[03:25] that we feel comfortable with you using
[03:28] and for some companies they will only
[03:30] use things that are GA. I use a lot of
[03:33] things that are preview because I'm
[03:34] always using like you know the latest
[03:36] and greatest. Um but you know it's it's
[03:39] it's it's a way that we mark things.
[03:42] It's like before we used to say like
[03:43] alpha and beta and I guess we don't say
[03:45] alpha and beta anymore. Instead we say
[03:47] you know preview public preview and then
[03:50] GA. So right now agent framework is
[03:52] basically in public preview like you can
[03:54] definitely install it. We did entire
[03:56] series on it. We've got lots of packages
[03:58] uh you know samples that use it but they
[04:01] have been changing the interface quite a
[04:03] bit and um you know in as they've been
[04:06] getting feedback right. So having
[04:08] something in preview is also a way of
[04:09] getting um you know getting feedback for
[04:12] it. Um so what you can see with agent
[04:15] framework is that it's gotten closer and
[04:17] closer to GA because the last few last
[04:21] months has been release candidates.
[04:23] Right? So we have we've had six release
[04:25] candidates and I've been told that RC6
[04:29] should be our last release candidate
[04:31] before the real 1.0.0 and that one would
[04:35] not be marked as a pre-release. that
[04:36] would be marked as t of release right
[04:39] and then hopefully that's the point at
[04:41] which you'll see that it is GA generally
[04:44] available
[04:45] uh let's see my screen sharing stopped
[04:47] all right thank you we will restart the
[04:50] screen right looks good over there and
[04:53] looks good there okay
[04:57] all right so there you go um
[05:02] so those are the only like news I had
[05:05] listed for for this week. Um, I did see
[05:08] some like cool Let me go to my bread
[05:11] box. So, I'm trying to like save like
[05:14] bookmark research now. Um, so this was
[05:18] pretty cool. Someone made a um Oh, let
[05:23] me get the actual link.
[05:26] Here we go. Okay. All right. So this is
[05:30] developer that is working on text to SQL
[05:34] and wanted to figure out which models
[05:37] were really good at it. So he developed
[05:39] his own benchmark and he ran it on both
[05:41] the frontier models and on the local
[05:43] models and so yeah so I thought this was
[05:46] just generally I was interested in this
[05:49] because I was trying to find some good
[05:50] local models for agents and really
[05:53] really struggling um to find some good
[05:56] local models that would work on my
[05:58] machines for for agents. My machine is
[06:00] pretty underpowered. So you know I went
[06:02] to this website can I run.ai
[06:05] AI and you know as you can see here I
[06:08] don't have a lot of options for my
[06:10] machine since I am on you know it's a
[06:12] Mac M1 with 16 gigs RAM. Um so you can
[06:15] see basically 3.18B and Quen 3.59B are
[06:19] my two you know options here. Um so you
[06:23] can see that I do now have both of
[06:26] those. This is 8B and this is Quen
[06:28] 3.59B.
[06:29] And so I did use Quen 3.59B a lot
[06:33] yesterday and it does technically work
[06:36] for for agents. Um but there you know
[06:40] the the the quality output was not
[06:43] nowhere near um you know what I expect
[06:45] out of you know Frontier LLM. So
[06:49] sometimes it would output Chinese even
[06:51] though you know none of my input was
[06:53] Chinese. I think that's because it was
[06:56] trained in China. So it has a lot of
[06:58] China data in in its data. And then
[07:01] sometimes it would just forget the
[07:02] original user question, right? I ask a
[07:04] question, but then it would go off and
[07:06] do a tool call and get a response and uh
[07:09] it would forget what my original
[07:11] question was. Right? So I was
[07:13] disappointed by the 9B. Apparently the
[07:14] 27B is pretty good. Um that's what it
[07:18] that's what it says here. um that the
[07:20] 27B is an amazing model, but you you
[07:24] know you have to try it for your
[07:26] particular use case.
[07:30] That does remind me of something I went
[07:31] to this cool meetup
[07:34] the other week and met the creator of
[07:37] this thing, Optimize Anything. So
[07:40] optimize anything uses this thing called
[07:42] jea which is a prompt like prompt
[07:46] optimizer that uses genetic algorithms
[07:49] and tries to try to figure out like what
[07:51] is the what is the thing I should try
[07:53] next right so instead of trying
[07:54] everything it tries to decide what you
[07:56] know what is the best thing to try next
[07:58] and so you basically get efficient
[08:00] prompt optimization and it's not just
[08:02] for prompts it's also like if you're
[08:04] doing structured outputs it's used a lot
[08:05] for structured outputs uh in in this one
[08:07] it's even using for skills like not even
[08:09] LM stuff, right? So, optimize anything
[08:11] is the ability to use Jeepa for
[08:12] anything. Before people were mostly
[08:15] using Jeppa for improving prompts and
[08:17] structured outputs and that sort of
[08:19] stuff, but people get really nice
[08:22] results from it.
[08:24] So, do uh yeah, check that out.
[08:30] And
[08:32] yeah, let's see.
[08:34] Do I know if anyone in Microsoft has
[08:36] already tested Turbo Quant for local
[08:39] models?
[08:46] I I'm just looking what Turbo is. Uh
[08:50] so this is from Google. This is 11 hours
[08:52] ago. Gosh.
[08:55] Oh, wait. What is it? KV cache. What
[08:58] should you Okay.
[09:00] AI compression.
[09:03] Oh, I do not know. It looks like this
[09:05] came out pretty recently, so I'd have to
[09:09] ask and see if anyone is is checking it
[09:13] out.
[09:17] Uh, let's see what else I've been
[09:19] working on. Yeah, and any point you have
[09:21] questions, you just put them in the chat
[09:22] and
[09:24] uh and try to answer what I can. Um, we
[09:26] did just announce our next series. Uh so
[09:30] do
[09:31] check it out if you're let's see what
[09:35] did we call it agents. There we go.
[09:37] There's the series. Okay. So this is our
[09:43] next live stream series and this one
[09:45] will have office hours as well. So it'll
[09:47] be a three-part series at the end of
[09:49] April about hosting agents on Foundry.
[09:54] Uh so we'll show how to host agent
[09:55] framework, link chain lane graph and
[09:58] then how to do quality and safety
[10:00] evaluations.
[10:01] So for those of you who are you know
[10:03] building agents with these frameworks
[10:04] and trying to decide how to deploy them,
[10:06] this is one option for you. You still
[10:08] have other options as well. You can host
[10:10] you know directly on container apps uh
[10:13] or app service or that sort of thing. Um
[10:15] but uh but this looks this is a nice
[10:18] option because you get built-in access
[10:20] to Foundry tools and Foundry Evals and
[10:22] all that good stuff. So do register for
[10:26] that series if you haven't yet. That
[10:29] should be good.
[10:31] Um
[10:34] I'm always working on porting chat
[10:35] completions API to responses API. I
[10:37] think I talked about that. I talked
[10:39] about that last week. So that's an
[10:40] ongoing project. And then this week I'm
[10:43] particularly working on fax mcp plus
[10:46] entra off basically exploring all the
[10:49] different ways that we can do entra off
[10:52] like because some of them are more
[10:54] secure than other options. And uh I got
[10:58] a yeah I got a new option working today
[11:00] that I'm excited about that only works
[11:02] for VS Code but you know VS Code is it's
[11:06] a pretty good place to have something
[11:07] working because it's that's where a lot
[11:09] of people you know want to use their MCP
[11:11] servers.
[11:12] Um, so yeah, if anyone's curious about
[11:15] that, we can dig into that. And we have
[11:17] a lot of upcoming events. MP Summit is
[11:19] happening tomorrow, I think, or uh
[11:22] Thursday and Friday this week. We've got
[11:24] some online conferences. Cosmos DB,
[11:26] POET, Pyon's in LA. Code with Claude,
[11:30] we're working with them on that
[11:31] conference that's in SF New York City
[11:33] and Tokyo. So, we're going to put
[11:34] together a workshop for that. And then
[11:36] there's build in June in San Francisco.
[11:39] Have I used the work IQ server? Yes, I
[11:42] have. It is configured in my uh in my
[11:45] co-pilot CLI. Let me open up my copilot
[11:47] CLI and
[11:54] coil.
[11:58] All right, let me just
[12:03] show you this. I just was deleting a
[12:05] key. Okay, so this is um yeah, so I
[12:09] configured it so I can use work IQ from
[12:12] Copilot CLI. Uh so that's just running
[12:15] the the command work IQ. So right now
[12:18] it's a it's like a you know not an HP
[12:21] server. It's a standard input output
[12:23] server. So you actually like you don't
[12:25] have to have the command installed
[12:27] locally. Oh, you can only see in the
[12:29] browser. Let's see. Oh, yeah. All right.
[12:31] It didn't do the whole screen. All
[12:32] right, let's do the whole screen. There
[12:34] we go. All right. Very good. Okay. All
[12:37] right. So, this is what I did was um I
[12:39] went into my co-pilot
[12:42] copilotedspeconfig.json.
[12:45] Um and so here you can see what I've got
[12:48] configured. So there's a mix of HTTP
[12:51] servers and standard input output
[12:53] servers. So right now work is a standard
[12:55] input output server. Maybe in the future
[12:57] it'll be an HTTP server. We'll see.
[13:01] So yes, so it should mean that then if I
[13:03] do copilot
[13:06] it we should be able to use work IQ from
[13:10] it.
[13:14] Okay.
[13:16] And then it's loading this MCP servers.
[13:20] All right. Like um do I have any
[13:26] um meetings today?
[13:32] All right. So, this is a kind of
[13:33] question that should go out to work IQ.
[13:37] Yeah, you can see the reasoning
[13:38] actually. I should use the work IQ tool
[13:40] to check the readings. But first, I need
[13:41] to check if the ULA has been accepted.
[13:43] Okay. All right. So, then it's going to
[13:45] say ask work IQ. So, that's the tool
[13:47] from the SP server. And says do I want
[13:50] to use the tool? I'm going to say yes.
[13:52] And of course, we can you can auto
[13:54] approve it if we want.
[13:56] And now it's going to actually make that
[13:59] tool call.
[14:05] So it's checking it.
[14:09] Uh I'm on Opus 4.6 on high reasoning.
[14:12] Now you can configure, that's the other
[14:14] thing that's cool in um you can
[14:16] configure the the reasoning level really
[14:18] easily now in VS Code with Copilot. So
[14:21] like Opus, I actually changed this to
[14:23] medium.
[14:26] today.
[14:28] So, that's fun. Okay, so I have five
[14:32] uh meetings today.
[14:34] That's a cute little visualization.
[14:39] Looks like I'm not going to that one. It
[14:40] already always overlaps.
[14:42] Not three-way overlap right now. Uh oh.
[14:46] Yeah. So, I will have to make sure we
[14:48] close up today at 12 o'clock because I'm
[14:50] going to chat with Jeremiah who is the
[14:52] fast MCP maintainer.
[14:54] So if you have any we have any pending
[14:56] questions on fastmcp
[14:59] we'll be chatting with him right after
[15:00] this one.
[15:04] So yes, so work IQ you can use for
[15:07] checking. It only has readonly access
[15:10] last I checked. So that's a bit
[15:12] limitation but it can certainly it can
[15:14] read your calendar events. It can search
[15:15] through your teams chats. It can search
[15:17] for through your shareepoint right. So
[15:19] sometimes like
[15:22] talk about MCP
[15:24] find my MCP powerpoints. Right?
[15:28] It's basically the same as using if
[15:30] you're chat it's really like the same as
[15:32] using copilot to ask these questions
[15:34] like copilot and teams um but it's kind
[15:36] of convenient because you can use it
[15:38] from other places right so here I can
[15:39] use it from copi cli and you know since
[15:41] mcp server we can use it for um you know
[15:45] many any of our clients on our desktop
[15:47] that support servers um you do have to
[15:49] off to it so there's like an off stage
[15:51] when you're setting it up and then once
[15:52] you've off then you can use it
[15:57] and now it's searching of The hard thing
[15:58] is, you know, making sure it actually
[16:00] uses work IQ at the time. Currently,
[16:02] this is searching my directory, which is
[16:04] a fair place to search, right? So, I'd
[16:06] probably have to say like, you know,
[16:07] checkoint or something like that. Um,
[16:11] yeah. So, John asked
[16:14] the this series is not on consecutive
[16:16] days. That's because April 28th is
[16:18] Cosmos DB conference and I am giving a
[16:21] talk for Cosmos DB conference and just
[16:24] that's Yeah. So we were we're going to
[16:26] have it on a Monday, a Wednesday, and a
[16:28] Thursday. So on Tuesday, you can still
[16:32] come and watch. We talk about stuff.
[16:35] It'll be Cosmos DB comp, and there'll be
[16:38] lots of talks about Cosmos DV. So it'll
[16:41] be a full week. Um, but yeah, it is a
[16:44] bit funny this time where it goes from
[16:45] Monday, Wednesday, Thursday.
[16:48] Yeah. So Pablo asked, "Does Microsoft
[16:50] have anything to check agent skills for
[16:52] security and effectiveness?"
[16:54] Um so well those are so the two
[16:57] different things there. So first let's
[16:59] talk about effectiveness because that
[17:00] one I can answer more
[17:03] um more quickly. So this is sensei which
[17:08] is from my colleague Shane
[17:10] and um
[17:14] it iteratively improves skills and he
[17:17] just added remember I was talking about
[17:19] Jeppa he did just add Jeepa to it so
[17:22] that sounds really fun. I haven't gotten
[17:24] a chance to try this yet. Um,
[17:27] but uh, but I think it it it seems like
[17:31] it could be really helpful. He's been
[17:32] using this on like Azure skills, ACD
[17:34] skills, boundary skills, that sort of
[17:36] thing. Um, so it'll check for, you know,
[17:40] it'll check for basic things and then
[17:43] it'll it works on improving, verifying.
[17:46] Yeah, definitely need to try this out.
[17:48] So, so that would be for effectiveness.
[17:50] Um the thing I don't know is how does it
[17:52] actually verify verify run tests. Okay.
[17:57] So I guess that you Oh, so these are
[17:59] like tests to make sure whether it'll
[18:00] trigger or not. That's quite
[18:01] interesting. Okay, that's a good that's
[18:04] a good test actually because that's one
[18:06] of the biggest issues is like whether
[18:07] something's going to trigger. Okay. Um
[18:11] so yeah, so a lot of it Okay, so this is
[18:14] about skill collision. Yeah, because in
[18:15] the in Azure we've got like now like a
[18:19] lot of skills that we're uh you know
[18:22] accumulating
[18:24] and so this can help you with that.
[18:28] The other one is Waza
[18:32] and that's also from Shane.
[18:37] So Waza let's see what the difference.
[18:39] So this one this one is more
[18:42] specifically on I think that like so
[18:44] this one sensei was about skill
[18:46] collision.
[18:47] Um this one is about I think just the
[18:51] skill like kind of standalone right uh
[18:54] so you can okay so it also will help you
[18:57] make a new skill with an evaluation
[18:59] script. So that's nice because you know
[19:01] one of the things is a lot of times we
[19:02] don't run tests or evaluations and then
[19:04] it can feel hard to write evaluations
[19:06] after the fact because you have to like
[19:07] figure out how to do an eval framework.
[19:09] So if you use WAZA then you know your
[19:12] skills will come preset with
[19:16] um with eval. So it might be good just
[19:19] to get into have it or at least try WAZA
[19:21] out and see if that's something you want
[19:23] to do. Okay. So this will so WAZA check
[19:27] checks for front matter adherence that's
[19:29] just compliance with best practices
[19:31] token budget so if you want token limits
[19:34] if your skills are getting way too big
[19:36] an evaluation
[19:38] uh suite whether it has an oh and then
[19:40] there is advisory check okay I I don't
[19:43] think any of this is necessary security
[19:45] I'm not seeing anything here on the
[19:47] security side per se let's see security
[19:53] TCP
[19:55] Yeah. So, let's see if that's an open
[19:58] feature request. Um,
[20:13] um, I don't think that's for the
[20:14] security either. So, yeah. So, I think
[20:16] it's the kind of thing that, you know,
[20:18] you you could be checking for. And I and
[20:20] we might this might be something that
[20:22] you could see us adding to like
[20:23] Microsoft Defender or something. I don't
[20:24] know if Defender would ever do it. I
[20:27] imagine people are working on additional
[20:29] tools. These are the ones I know about
[20:30] because this is what we're using for
[20:31] like our public um collections of
[20:34] skills, right? This is in the Let me
[20:37] find the um
[20:40] repo for it that has all the skills.
[20:43] Okay. I think
[20:46] they're under
[20:53] uh skills.
[20:56] Microsoft as your skills. Microsoft
[20:58] Azure skills. Okay, that's what I was
[21:00] looking for. Uh here we go.
[21:04] So,
[21:08] this is the Azure Skills
[21:12] Bundle plugin. And so a plug-in is a
[21:14] collection of skills, MCP and MCP
[21:16] servers. And
[21:19] um I think that these are also loaded by
[21:23] the GitHub copilot for Azure.
[21:29] So yeah, so this one there's quite a few
[21:32] skills in it and I think these are the
[21:35] kind of ones that they're trying to
[21:36] improve using Waza and Sensei. So that's
[21:40] what I know about right now. Um I think
[21:42] it's a good question about
[21:45] about security. um if there's
[21:47] particularly things you know um that
[21:50] you're concerned about like are do you
[21:52] want to check for
[21:54] you know like the the what it can do to
[21:56] your local the problem is like the
[21:58] security also comes down to where are
[21:59] you running the skill right what
[22:01] environment right because you can you
[22:04] know if you run a skill in an isolated
[22:06] docker container then you know it's you
[22:08] know some stuff it does is fine but if
[22:10] you run the skill and it's in just on
[22:12] your machine and it has access to prod
[22:14] credentials and stuff like that then you
[22:17] know then it can wreak havoc. An agent
[22:20] can do anything and you know as long if
[22:23] if an agent has the ability to do
[22:25] something then it can do it and you can
[22:27] you know put in your prompts what you
[22:28] think it should or shouldn't do. But
[22:30] really like when it comes to security,
[22:32] you really want to lock down security at
[22:33] the environment level and say, "Hey,
[22:35] like you know, the agent is not allowed
[22:37] to run this command. The agent is not
[22:39] allowed access to these credentials,
[22:41] right?
[22:42] You don't want to rely on security, you
[22:45] know, just in your prompt like, oh,
[22:47] don't do this or do do that." like
[22:49] that's, you know, nice to have there,
[22:52] but the security needs to be locked down
[22:54] at the level of what what commands is
[22:58] this agent allowed to run? We what what
[23:02] does it access to?
[23:06] All right, good. Good question there.
[23:11] Uh, let's see. See someone typing. See
[23:14] if there's anything else.
[23:17] there. Okay, we covered everything in
[23:20] the slide. Oh, yeah, my that's a good
[23:23] point. The the um the Mirage problem.
[23:27] So, let me find
[23:30] Here we go.
[23:33] Yeah, I posted this last night. Um,
[23:37] so
[23:39] this is where they tested a bunch of
[23:42] multimodal
[23:44] uh LLMs and they found that some
[23:48] interesting results where the LMS even
[23:51] if they didn't provide an image, the LM
[23:54] would pretend it's not an image. This
[23:56] was the screenshot I showed because I
[23:57] thought it was useful, right? So
[23:59] especially with you know um medical
[24:01] diagnosis, right? So identify the type
[24:03] of tissue present in this hisystology
[24:04] side right and you can actually get like
[24:09] the LM can say based on the visual
[24:11] evidence evidence this slide shows
[24:13] cardiac muscle tissues
[24:15] so this is basically a mirage it didn't
[24:18] actually see an image it just you know
[24:21] it just thought it image and you know
[24:24] thought is that this is because of the
[24:25] way that they're trained um where
[24:27] they're often trained with either text
[24:30] like they don't they're not always
[24:32] trained with just images. It's usually a
[24:34] mix of text and images. What you want is
[24:37] for it to say this, right? No image was
[24:39] included. That is what you that is what
[24:41] you want. Um so it's a it's like a
[24:44] special kind of hallucination. And they
[24:45] found other like interesting things too
[24:47] like it seemed like you know some of the
[24:49] benchmarks the success is is not
[24:52] necessarily due to the images like we
[24:53] look at it the benchmark and think it
[24:54] means that they looked at the images but
[24:57] it's not actually.
[24:59] So they they you know figure out a way
[25:02] to basically figure out which questions
[25:05] in a benchmark were compromised and then
[25:07] they clean clean the benchmarks to
[25:10] remove the compromised questions and
[25:12] then they re-evaluate the um VLMs based
[25:16] off of those those benchmarks. And you
[25:20] can see that the performance goes down
[25:25] um for most of them for all of them goes
[25:27] down once they you know once they do
[25:30] that. Um so yeah so and your question
[25:32] was have I seen any so I don't I've
[25:36] definitely seen weird things. So I was
[25:38] interested this because I was talking
[25:39] about multimodal rag with my colleague
[25:42] and apparently what like the rumor is or
[25:47] whatever is I shouldn't spread rumors
[25:49] but um
[25:51] you know we have this um this one the uh
[25:55] well let's look at the the original one
[25:58] vi
[25:59] this one. Okay. So, we have the
[26:03] um I'm trying to find it just under AI
[26:05] vision embedding
[26:07] um
[26:09] Florence.
[26:14] So, we have this Florence model and the
[26:17] Florence model powers
[26:20] the
[26:21] Azure AI vision API. I'm just trying to
[26:24] remember what its current name is.
[26:25] Sorry. Um,
[26:27] previously known as computer vision, now
[26:29] probably known as foundry vision. Who
[26:31] knows? Okay. Azure vision and foundry
[26:32] tools. Okay. All right. So I there's a
[26:35] notice. Yeah. So this is deprecated. The
[26:38] image analysis service is deprecated and
[26:40] we retired in 2028.
[26:43] Um, so that's specific to the image
[26:48] analysis.
[26:50] So it says use document. Okay. And image
[26:53] embedding. So yeah. So, it looks like we
[26:55] are This is what makes me sad because I
[26:57] think this means that they are getting
[26:59] rid of the embedding SDK.
[27:03] Um, because they're saying that if you
[27:05] need multimodal embeddings, you should
[27:06] use cohhere embed. I guess that's also a
[27:08] multimodal one.
[27:13] >> Yeah. Yeah. So anyway, so uh it looks
[27:16] like if you are relying on the Florence
[27:19] model as in Azure AI vision that we you
[27:22] may want to move off of that model
[27:24] because it looks like it is uh it looks
[27:27] like it's I think it's all getting
[27:28] deprecated. Um which is interesting. Um
[27:32] so basically like they're moving away
[27:34] from this you know dedicated because
[27:36] this is like a dedicated model right? So
[27:38] it looks like the general trend is away
[27:40] from these like dedicated vision models
[27:42] and towards you know more generic
[27:45] multimodal LLMs and vending models. So
[27:48] that is that's sad to me because I have
[27:51] built on top of that model and I um you
[27:54] know I liked it and that's how we built
[27:56] multimodal round. So in multimodal rag
[27:58] we would both we would do two things. We
[28:00] would compute the im like the embedding
[28:02] of the image itself and then we would
[28:04] also generate a text description of the
[28:07] image. And then when you do the search
[28:09] you can search both off of you know
[28:11] standard search of the text description
[28:13] and the all the content and you can do a
[28:16] multi vector search of the image. So
[28:19] that way if there was something in the
[28:22] image itself that wasn't described in
[28:24] the description you still had a chance
[28:26] of finding it right. And then when you
[28:28] actually answer the question, you
[28:29] include the images and the text
[28:32] description and the content. So I have
[28:34] seen interesting things like where that
[28:36] where it like really seems like it wants
[28:38] to reference the text description versus
[28:40] the image. You know, it makes you wonder
[28:42] like is there even any point including
[28:44] the image? But of course like a textual
[28:47] description
[28:48] isn't going to describe everything about
[28:51] a picture. So I, you know, I think
[28:52] that's still useful. But um I do think
[28:54] if you're doing something like
[28:55] multimodal rag, you might want to, you
[28:57] know, really look at that and look at
[28:59] your prompt and look at whether like
[29:02] what it decides to reference. Maybe you
[29:04] want to have it specifically say like,
[29:06] you know, did you did you figure this
[29:07] out based off the image or based off the
[29:09] description. Um because I have seen some
[29:11] weird stuff there is once you start
[29:13] giving both the textual description and
[29:15] the image itself, like sometimes you
[29:17] have to really really force it to look
[29:19] at that image like it really wants to
[29:20] look at the textual description. So
[29:23] definitely definitely interesting things
[29:25] once you start mixing in uh images and
[29:28] textual descriptions of images.
[29:31] Um
[29:33] okay I see John asks why are people
[29:37] saying MP is dead? Is it because of
[29:38] skills? I think we covered this uh I
[29:41] think we actually covered that pretty
[29:42] extensively last time. Let's just look
[29:44] at our our office hours. So here's our
[29:47] this is our um collection of questions.
[29:50] So here
[29:52] um okay yeah so you know this is what I
[29:56] said last time MCU is not dead although
[29:59] there is a funeral for it tomorrow in
[30:01] New York City but it's a joke um so yes
[30:05] so this is what I said what I said
[30:07] before is um you know skills are are
[30:12] really useful especially for coding
[30:14] agent
[30:16] um but MCP is particularly useful when
[30:18] off is involved when you're you
[30:20] doing this you know not just in your
[30:23] local environment in like you know
[30:24] deployed environment across a whole
[30:26] organization
[30:28] and they also the MCB people are working
[30:31] on um there's like a working group
[30:33] that's that's trying to figure out how
[30:35] to
[30:37] um add skills let me find if I can find
[30:40] it because I met somebody from that
[30:41] working group
[30:44] working in scoop skills over MCP this
[30:46] must be it
[30:55] See?
[31:01] Yeah. So, they want to try and figure
[31:02] out um
[31:05] Oh, here we go. Step 2076.
[31:10] All right. That got closed, but maybe
[31:11] there's a new one now.
[31:14] Okay. Let's see. Where's the main?
[31:18] Okay.
[31:19] they they're trying to figure out how to
[31:21] make skills be a
[31:24] first class,
[31:26] you know, something that can be
[31:29] discovered from an FCP server,
[31:31] >> right? So, in addition to having tools
[31:33] and resources and prompts, then you
[31:36] would have skills as well.
[31:40] So, yeah, so when it makes sense for an
[31:42] MC server to provide skills, it could
[31:43] provide skills. Um but uh there's a lot
[31:46] of times when you you know want to have
[31:49] a tool where the tool is you know has
[31:52] authentication involved with it. It's
[31:55] got you know decorators that say whether
[31:57] it's a destructive tool. Um it can it
[32:01] can do formal back and forth with the
[32:03] user with elicitations.
[32:06] You can do MCP apps using you know uh
[32:09] using MCP tools. So there's, you know,
[32:13] you just want to use them all. And now
[32:15] with the agent frameworks, all the agent
[32:17] frameworks pretty much have support for
[32:18] skills, too. So if you were just porting
[32:20] something over that was using skills,
[32:23] you could just say, "Hey, agent
[32:25] framework, here's my skills. Load them
[32:26] in."
[32:30] Let's see. I got another question about
[32:32] Turbo Quant that was already that was
[32:34] asked earlier. No, I have not looked at
[32:35] TurboQuant at all. It sounds like I'm
[32:37] going to have to ask my colleagues if
[32:40] they have if they've looked into it.
[32:47] All right. Um, what other questions we
[32:50] have?
[32:59] Let's see. The other thing that's cool
[33:00] is that
[33:02] it
[33:05] go
[33:07] so I went to a conference a few weeks
[33:09] ago called Pi AI and the the talks are
[33:13] now up to up on YouTube for it. So that
[33:16] includes my talk but also um other
[33:19] people's talks. Let me see if I can find
[33:20] like a there we go. Hi AI
[33:25] videos.
[33:33] There's more than this because they just
[33:34] put up my talk too.
[33:39] Where is Okay,
[33:42] maybe they're not listing them for some
[33:44] reason because this one Oh, they put on
[33:45] the pedantic channel. Okay, I'll have to
[33:48] ask them why mine's on the
[33:50] collaborations. All right.
[33:52] Well, anyway, they're getting a they're
[33:54] they're slowly getting the PAI talks up.
[33:57] So, there's some I think you can see
[33:59] most of them off the pier. So, I uh
[34:02] let's see. I really liked this one from
[34:04] Till. He's from Mother Duck and he made
[34:08] an MCB server for Mother Duck and it was
[34:10] very interesting to see the evolution of
[34:12] the MCB server and he's in that skills
[34:14] working group. So, that's actually the
[34:15] reason I know about the skills working
[34:17] group is that we talked about that when
[34:18] I met him. Jeremiah is who is the fast
[34:21] MCV maintainer and I I liked his talk as
[34:23] well. This is who I'm talking to at 12
[34:25] o'clock after this office hours. I
[34:28] didn't see these two but they're
[34:30] probably good. I did I really liked
[34:32] Hamal's as well revenge of the data
[34:34] scientist and that's about evaluation
[34:36] and that's also the this he wrote it up
[34:39] as a blog post too.
[34:42] So check out those talks and there
[34:44] should be more. Oh and this open source
[34:45] in the age of AI panel that was quite
[34:47] interesting as well. That's good stuff.
[34:50] Okay. Uh,
[34:52] so Nomi said, "Oh, okay. Yeah. So this
[34:56] is
[34:58] all right. So it looks like turboquat is
[35:00] really affecting the inference serving,
[35:02] right? So um, you know, as a application
[35:06] developer, it's not something uh I'm
[35:09] usually using unless I'm like I guess if
[35:12] you're I don't know if it would affect
[35:13] like BLM. I have deployed BLM on
[35:18] serverless GPUs for running you know
[35:21] small language models. Maybe it would
[35:24] affect that. I don't know. Let's see.
[35:26] Turbo quant.
[35:31] Oh, there's already a plugin for it.
[35:33] Okay. Let's see.
[35:40] Was this just like four days ago? Okay.
[35:43] All right. So, yeah, I guess this would
[35:45] practically affect if you were doing
[35:47] something like um deploying a container
[35:51] app serverless GPU
[35:54] with um with VLM, then maybe this um
[35:58] this plug-in
[36:01] would help get better performance.
[36:05] I don't know if this will get like put
[36:07] straight into
[36:10] first open source turquo implementation.
[36:12] Wow.
[36:14] pretty cool. Um,
[36:24] you could do because we did this
[36:25] serverless TPUs demo with the LLM
[36:30] that's using like following this
[36:33] tutorial here.
[36:35] You can deploy all these Nvidia models
[36:37] on a serverless GPU pretty easily.
[36:41] Maybe it would help that stuff. Oh,
[36:42] there was also Alama just said that they
[36:44] Let's get the Alama blog. Lama just said
[36:47] they made it easier to do or faster to
[36:51] do
[36:53] um
[36:55] Macs. They said better support for Macs.
[36:58] There we go. Llama's now powered by MLX
[37:01] on Apple Silicon in preview. Uh so
[37:04] that's exciting if you are on a Mac like
[37:07] me. I don't know if it's actually gonna
[37:09] accelerate on on M1, right? Because it
[37:12] says it says on all well, okay, it says
[37:15] on all Apple silicon devices. Uh oh,
[37:18] then I guess particularly on the M5 then
[37:20] you get the GPU neural accelerators.
[37:22] Okay. Um so how do we get the new one?
[37:26] Alama 19. All right, let me just try
[37:29] this.
[37:35] Let's see what is my llama version right
[37:37] now.
[37:39] 18. So we're going to download
[37:43] when 3.5
[37:45] release accelerates.
[37:48] Oh, well you have to do it. Okay. Please
[37:51] make sure you have a Mac with more than
[37:52] 32 gigs of unified memory. Nope.
[37:56] All right. So doesn't help me so far.
[37:59] But if you do have a Mac with 32 gigs of
[38:01] unified memory, uh then try that out.
[38:23] I see some discussion about how Turbo
[38:25] Quant will help. I I have not looked
[38:27] into it.
[38:31] Let's see.
[38:36] It says compression, but would we
[38:38] actually be paying for less tokens? Why
[38:39] would we Why would we be paying for less
[38:41] tokens?
[38:44] Because of cashing.
[38:57] Oh gosh.
[39:01] A lot of vector
[39:06] here. Okay.
[39:08] If you if you've looked into it, do
[39:10] share your insights.
[39:14] Uh let's see the beginning. Okay.
[39:24] Oh, they're using Okay, so it's just
[39:26] it's vector quantization. Oh, so
[39:28] probably. So, this would also be a good
[39:30] question for all of the vector search
[39:32] like for Azure AI search. Uh let me all
[39:36] right let me just
[39:41] right because if they've done if this is
[39:43] better quantization
[39:47] let me see
[39:56] all right I'll I'll ping a few folks
[39:57] about turboquan probably AI search and
[40:00] then just AI boundaries
[40:04] so DH asks, "When can you see agent
[40:06] framework durable agent in Azure
[40:08] function series?" It's a good question.
[40:10] I actually just got asked
[40:13] about durable in um from the durable
[40:17] team. Um and
[40:21] uh I haven't had a chance to
[40:25] I haven't had a chance to play with
[40:26] durable execution yet. Um let me see
[40:30] what they Let's see. there. Okay. So
[40:35] maybe
[40:37] if I can if there's interest in that um
[40:39] because this is this is what they were
[40:42] hoping I could dig into. So maybe we
[40:46] would be able to
[40:48] The thing I don't know is whether this
[40:49] is compatible with the Foundry hosted
[40:51] agents because there was a question
[40:54] about this at MVP summit last week about
[40:56] the durability and I think that this is
[41:00] not yet compatible with Foundry hosted
[41:02] agents but I will I'll double check. So
[41:05] I think you'd have to if you want to do
[41:07] this this is with um with Azure
[41:09] functions right so you would be
[41:11] deploying
[41:13] deploying your agent on
[41:16] on Azure functions
[41:18] and then you get the durability.
[41:22] So I don't
[41:24] don't think we can show it. Maybe I can
[41:26] get um maybe I can get Nick to come to
[41:29] the office hours. How about what if we
[41:31] do that? I could get Nick to come to the
[41:33] office hours
[41:35] and maybe he could show it because we'll
[41:38] have office hours after each of them
[41:44] and so then and then we could take a
[41:47] look at this. So you get serverless
[41:49] hosting session management um you do get
[41:52] that from foundry hosted agents now too
[41:55] but deterministic multi- aent
[41:57] orchestrations
[42:00] with the automatic checkpointing that's
[42:03] that sounds pretty fun and that's
[42:05] something that is maybe the hardest do
[42:07] and then human in the loop as well
[42:13] that would be pretty cool to see that
[42:14] demoed
[42:22] Uh, so check out the the blog post. Um,
[42:25] if you haven't read this yet, maybe you
[42:27] already have given that you asked about
[42:29] it.
[42:31] And you know, maybe I can get Nick to
[42:33] come to the office hours.
[42:46] I see we're getting the chat GPT summary
[42:48] of the paper. The question is would
[42:49] those um with that caching do we are we
[42:53] thinking that that means that our the
[42:56] token usage would actually be lower or
[42:58] just that LM the pricing will get lower
[43:01] just because on our side it's cheaper to
[43:03] do right
[43:05] um because I don't know how often you
[43:07] know when we add stuff like caching like
[43:09] whether that ends up affecting the like
[43:12] how often does it actually affect your
[43:14] developer facing token usage counts.
[43:18] So Desh is you're waiting for support
[43:20] for private networking in hosted agents
[43:23] in foundry.
[43:26] I thought we had that. Okay, let me see.
[43:30] Um
[43:33] I'm trying to remember what we what we
[43:36] showed at the MVP summit last week.
[43:39] Okay. So, boundary
[43:43] hosted agents
[43:46] thinking which
[43:56] I'll just ask my colleague about that.
[43:58] Um,
[44:03] do you know status of private networking
[44:08] support
[44:10] for foundry hosted agents?
[44:17] All right, I will ask
[44:20] about that.
[44:23] Uh, I know that they're working on quite
[44:25] a few things for hosted agents. So I
[44:27] would expect by build that we see a lot
[44:30] more capabilities um
[44:34] than what there is today. There's quite
[44:36] a few people working on it. See a
[44:38] question. Who is she? Who's she? Are you
[44:41] talking about me or someone else?
[44:43] My name is Pamela. I am a P Python
[44:47] advocate at Microsoft.
[45:00] All right, we have a few more minutes
[45:03] for
[45:04] um anything else. Let's see if we can
[45:07] see anything about
[45:13] menicus.
[45:37] Okay, I'm just looking to see if it says
[45:40] anything about
[45:42] private networking.
[45:53] I don't see it. Um
[46:02] ility evaluate and test
[46:04] publish hosted agents. Oh my gosh, this
[46:07] is such a long doc. Okay. Publish
[46:09] considerations
[46:10] identity management version control
[46:12] authentication.
[46:16] Okay. Limitations. Okay.
[46:18] Ah, there we go. Okay. Currently, you
[46:22] cannot create hosted agents by using the
[46:23] standard setup within network isolated
[46:26] founders. For more information, see
[46:27] configure virtual networks
[46:37] known limitations
[46:44] capabilities blah blah blah.
[46:48] So this is for foundry agent service but
[46:51] we're we're wondering about um
[46:55] hosted agents
[46:58] uh private you can't create.
[47:02] It's weird how it says for detail
[47:04] configure virtual networks but I think
[47:06] it's saying that you can't do it.
[47:09] I'm trying I don't like this is a weird
[47:11] wording because it it makes me wonder
[47:14] whether you can do it just with a lot of
[47:16] work or if you just can't do it. I think
[47:17] it just means we can't do it. But let me
[47:19] just check.
[47:26] I just ask.
[47:35] >> All right. Uh yeah, I'll I'm chatting
[47:38] with some folks about it now. Um, you
[47:41] know, I think it's the that kind of
[47:42] limitation is something I would expect
[47:44] to see go away, you know, by in
[47:47] hopefully in a few months. Usually
[47:49] things happen at Build. Um, but don't
[47:51] quote me because I don't actually
[47:52] remember what exactly is going to happen
[47:54] at Build. And also, I'm not supposed to
[47:55] be saying anything. No, I really don't
[47:58] remember. But um given how important
[48:00] private networking is and given that
[48:02] we're Microsoft and a lot of people come
[48:03] to us because of our private networking,
[48:06] it would seem like it would be a high
[48:07] priority to have that have that work.
[48:12] Okay, last four minutes. Of course, now
[48:14] we get lots of questions.
[48:16] Any tips to maximize the quality of
[48:18] GitHub copilot auto output? It is locked
[48:20] to the codeex model. Oh, the GitHub sub
[48:24] student subscription was cut off from
[48:26] selecting opus and sonet models. Wow.
[48:29] Um,
[48:31] uh, I actually don't use auto because
[48:33] I'm always using opus. Sorry, it's very
[48:35] spoiled of me. Um, let me
[48:40] let me ask
[48:42] let's see, I'll find some someone to ask
[48:45] that I have a better response in the
[48:46] future because I have not
[48:49] have not done anything with that.
[49:08] Okay. All right. Posting the BS code
[49:10] channel.
[49:12] I think that Burke, if you're on
[49:14] Twitter, I would tweet that to Burke
[49:16] Holland because he was talking about um
[49:18] he's like our VS Code advocate and he
[49:21] was uh talking about autoload. So, I
[49:25] think he's a lot more familiar with it
[49:27] than I am.
[49:30] Uh also Pierce Boggin, right? So, if you
[49:33] are on Twitter, these are good folks to
[49:37] uh to hit up with VS Code stuff. they're
[49:42] always um you know really helpful. Uh so
[49:46] here we go these two
[49:49] and then we have a question how to start
[49:51] in AI AI world um AI engineering uh
[49:55] audience level AI engineering by Chip
[49:58] Huin is great book um but you might want
[50:00] to start with our Python AI series first
[50:02] at least that's what I've been I've been
[50:04] told um let me how I learned generative
[50:08] AI so here is my blog post about how
[50:09] I've learned generative AI so that
[50:12] includes the AI engineering book um AI
[50:17] news practicing
[50:20] and um the you know the video series
[50:22] that we put on.
[50:25] So yeah, I do like AI engineering. Um
[50:28] but you may want to start off with um
[50:32] like the Python AI series and then read
[50:35] the Python the AI engineering book.
[50:39] Okay. All right. I do have to go now
[50:41] because I'm gonna hop on a call with
[50:43] Jeremiah from FastNcp
[50:46] and uh yeah, but I will looks like we're
[50:49] still got our recording going. That's
[50:51] good. Um, so I will post the recording,
[50:54] I'll post the transcript, all the Q&A
[50:55] and all that into our in our thread so
[50:58] that you can reference answers

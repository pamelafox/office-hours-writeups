Reading inline script metadata from `get_transcript.py`
[00:00] Welcome to our weekly office hours for
[00:03] Python and AI. It is February 17th.
[00:08] And yeah, in this office hours, uh we
[00:12] usually start off with talking about
[00:13] recent product updates, news, articles,
[00:16] etc. And just uh answer any questions or
[00:20] explore any new tools that people want
[00:22] to explore. Uh, so if you do already
[00:26] have questions, go ahead and post them
[00:29] in the chat. And in the meantime, I'll
[00:32] talk through some of the recent news.
[00:35] Uh, the first news is an easy one is
[00:39] that uh, Claude Sonnet 4.6 is a new
[00:42] model. Uh, we had Opus 4.6 last week.
[00:45] Sonnet is like Opus, but it's uh, like a
[00:49] smaller model, but still fairly capable.
[00:52] So, some people prefer using Sonnet. I
[00:54] think it's probably cheaper and faster.
[00:56] So, that's available in Foundry models.
[00:59] I assume it would be coming to Cop-lot
[01:02] soon. I didn't see it this morning when
[01:05] I checked my model picker. Oh, screen
[01:08] sharing. Oh, the screen died. Thank you,
[01:11] Discord. Thank you for letting me know.
[01:13] Let me re share the screen.
[01:17] All right. Thank you. Yeah, just let me
[01:18] know when that happens. Uh because
[01:20] Discord likes to end the screen share.
[01:26] Um I see a question. How many parameters
[01:28] does Sonnet and open 4.6 have? I don't
[01:31] know that does does Claude actually pub
[01:33] do anyone does anybody publish their
[01:35] parameters anymore for priority models?
[01:37] Let's see. This is the article that um
[01:40] Enthropic had about it. Uh so let's see
[01:43] if if um we can see anything about
[01:48] parameters here. Um
[01:53] yeah, I don't think that they actually
[01:55] publish
[01:57] publish their parameters. Um but you can
[02:00] see so obus 4.6 does the best on almost
[02:05] everything. Um, but for some reason,
[02:08] Sonnet is particularly good at financial
[02:11] analysis and office tasks for this
[02:13] particular benchmark. You have to take
[02:14] every benchmark with a grain of salt,
[02:16] right? Hopefully, we've all learned
[02:17] this, but because the benchmarks, you
[02:19] know, they capture what they capture,
[02:20] but they obviously miss things. So, you
[02:22] always have to try stuff for your
[02:24] particular
[02:25] um use case. Um, so yeah, now it um it
[02:33] does, it says it's better at long
[02:35] horizon planning. It does have a 1
[02:36] million token context window at least on
[02:38] anthropic. As to whether that has it on
[02:42] um you know on on Foundry uh we'd have
[02:45] to check. Let me see. Uh Microsoft
[02:48] Foundry models
[02:51] and
[02:55] let's see deploy.
[02:59] Okay. Do we have it listed? Okay. So it
[03:02] does list the 4.6 six in this
[03:04] documentation
[03:06] here. Does it say if we get the 1
[03:10] million
[03:12] token context
[03:18] 4.6 six. Okay, this one mentions 1
[03:21] million token and this one also mentions
[03:23] 1 million.
[03:25] So, both of them Oh, here we Okay. And
[03:27] then Oh, but these are and then we have
[03:29] the API quotas um and default
[03:34] um rate limits. Okay.
[03:40] All right. So, it claims that they even
[03:43] on Foundry that they have the context
[03:45] window. Yeah. Here it also says that the
[03:47] context window is is 1 million here. So
[03:54] um yes. So that implies to me that if
[03:56] you're using it programmatically you do
[03:57] get that 1 million context window.
[04:05] Um and just checking are people able to
[04:08] see the stream? I see some comments in
[04:10] the chat. Uh it's showing me the stream
[04:12] on my end. So sometimes with Discord,
[04:17] Discord is known to be buggy. Um,
[04:22] so assuming that someone besides me can
[04:25] see the stream. Someone can confirm
[04:27] that. Uh, I did see a question. Any
[04:29] update on Enthropic and it's available
[04:31] over Azure for CSP
[04:34] clients.
[04:37] So for this question, can you remind me
[04:40] what the acronym CSP stands for?
[04:45] Um, let me just see. Uh, we have a lot
[04:49] of acronym clouds. Is it this one? Cloud
[04:52] solution provider.
[04:54] Is that what CSP stands for? I've
[04:56] actually never heard of this. Oh, okay.
[05:00] All right. Thank you. So, the
[05:01] clarification here is um I'll just paste
[05:05] this into here. To use cloud models in
[05:07] Max Foundry, you need a paid Azure
[05:09] solution from the billing account in a
[05:10] country or region where entropic offers
[05:14] a model. Cloud solution providers are
[05:17] restricted.
[05:19] Oh, okay. I did not know about that. Uh
[05:22] let me just go ahead and ask the product
[05:26] team
[05:27] um about that. Give me h one sec.
[05:34] One, two, three.
[05:41] All right.
[05:55] Okay.
[10:08] It keeps going from where it was before
[10:11] that we didn't lose the previous
[10:14] one. Says um I think it I think it's
[10:17] going to work. Okay. Still recording.
[10:19] Okay.
[10:22] All right. Okay.
[10:25] We're back. All right. I'm hoping
[10:27] usually we think it has to do with the
[10:29] um what do you call DHCP because we have
[10:31] a Pi Hole and it like you know whenever
[10:34] it refreshes to try and find a new IP
[10:37] address for my Mac I think sometimes
[10:39] it's failing. Anyway, got to figure it
[10:42] out. Okay. Yeah. Um All right. So, we're
[10:46] talking about Enthropic. Yeah. So, um
[10:48] yeah. So, right now you're supposed to
[10:50] use Enthropic message API. There is like
[10:52] a like a non-documented responses API
[10:56] compatibility layer for the anthropic
[10:58] models, but we're not supposed to talk
[11:00] about that.
[11:02] Um, it says that my stream has failed.
[11:05] Uh, okay. We'll we'll just stop
[11:07] streaming and stream again. We'll just
[11:09] keep doing it till it works. Okay. I
[11:12] just re reshared the stream again.
[11:17] Uh, and it's showing the preview to me.
[11:21] Uh okay great let's see what questions
[11:24] happen we're going okay so um
[11:28] so someone said trying to create a
[11:30] foundry recent with a student plan is it
[11:33] possible you cannot that might be
[11:36] restricted generally it's really hard to
[11:38] use the genai stuff with um you know
[11:42] with both the student accounts and the
[11:44] free accounts like with the free account
[11:45] you get very limited capacity like 1
[11:48] million tokens per it and uh you know
[11:51] obviously we need to make that better so
[11:52] that people can can try
[11:55] um one thing you can do for now is you
[11:57] can use GitHub marketplace models
[12:01] these are basically foundry models um
[12:06] and uh yeah you just get free amount of
[12:09] rate limits so whenever we do live
[12:11] streams and workshops we always use the
[12:13] GitHub um marketplace models now these
[12:16] ones don't get the the new models. Um
[12:20] but um you know uh it's it's a good
[12:23] start. You can do quite a lot with these
[12:25] models. Um there's other stuff in
[12:27] Foundry that you can't use from models
[12:29] uh from from GitHub models like agents
[12:31] and whatnot, but you can use the LMS.
[12:35] All right. So, okay. So, keeping going.
[12:38] Yes. So, there is a question about
[12:39] webmc. I have that on my list, too. Oh,
[12:44] and linking to the wrong URL for it. So
[12:46] here's the web MCP
[12:49] uh article here. So let's talk about
[12:51] that. And you know um a lot of times
[12:55] office hours is the first time where I
[12:56] get to dig into something. Um so I think
[13:00] that this is basically like an easy way
[13:02] for a website to make itself available
[13:07] to AI agents, right? Because right now
[13:09] people are using like Playright,
[13:11] Selenium, whatever like browser
[13:12] automation tools in order to try and
[13:14] interact with websites and it's very
[13:15] painful. It does not work well and a lot
[13:17] of times you run against like the
[13:19] websit's um you know CDN protection like
[13:22] rate limiting bot protection all that
[13:24] stuff which makes sense the websites are
[13:25] trying to protect themselves from bots
[13:27] but if a website truly wants itself to
[13:29] be usable by agents WebMCP would be a
[13:32] way that they could do it right. Um so
[13:35] let's see. So, how does it actually
[13:37] work? Uh, this doesn't really tell me
[13:41] how it works.
[13:43] What is built-in AI?
[13:47] Web platforms API. All right, we need
[13:49] like a web MCP stick. How does WebMP
[13:53] actually work?
[13:59] If anyone's found a good Okay, I think
[14:02] this is the one I just Yeah, this looks
[14:04] really similar. Thank you. Um
[14:09] as tools.
[14:12] Okay. So, web pages that use MC thought
[14:14] as MCP servers. It actually reminds me a
[14:17] lot. Some of you might remember NL web.
[14:20] That was a project from Microsoft which
[14:22] was to make websites accessible
[14:24] basically like for um search and rag and
[14:28] chat in the browser. And I thought this
[14:30] was a good idea, but it required people
[14:32] to like um adopt like semantic HTML and
[14:35] stuff like that. And uh I think it might
[14:37] have just been I feel like it might be
[14:40] too maybe too hard. Um and this was
[14:43] before we had the standard of MCP. So
[14:45] now that we had standard of MCP, this
[14:48] probably makes more sense because we can
[14:50] build on top of that standard instead of
[14:52] trying to like make up, you know, a
[14:54] different standard. I'll share NL web
[14:55] for those curious about digging into
[14:57] that. Um
[15:00] uh but uh okay so how
[15:03] I want to see how it really really
[15:05] works. Websjs
[15:08] is enables webpage to provide agent
[15:11] specific paths in their UI. Okay.
[15:16] All right.
[15:18] Uh use cases filtered templates. Okay.
[15:23] So maybe your website would expose
[15:26] JavaScript functions that would be very
[15:30] common that an agent would want to use,
[15:32] right? So like, you know, I have that
[15:34] tool that goes on LinkedIn and tries to
[15:36] accept notifications. You could imagine
[15:38] that LinkedIn if they wanted to would
[15:41] expose, you know, like a list
[15:42] notifications, right? Um,
[15:46] okay, that makes sense. uh that you know
[15:51] would require some amount of effort to
[15:54] implement. I thought that WebMCP would
[15:56] maybe be a little bit more
[15:58] um automated, but this seems like you'd
[16:01] have to kind of custom design for each
[16:04] website. What is it? You know, what are
[16:06] the tools that people want to use? Uh
[16:08] but that means it can be a better a
[16:11] better experience.
[16:14] So, uh yeah, I think that's good. Um, I
[16:19] think the interesting thing is whether
[16:20] the these websites that have WebMCP if
[16:24] they're going to
[16:26] uh if they're going to like disable
[16:28] their bot bot limiting, right? Uh
[16:31] because I keep running into so we get I
[16:33] got the question last week about um how
[16:36] to make sure that LinkedIn doesn't flag
[16:38] you as a bot if you're automating with
[16:40] LinkedIn. And then later that week, I
[16:42] ran my LinkedIn agent and I got flagged
[16:45] for automation and I had to stop running
[16:47] it. So it basically LinkedIn after about
[16:49] like 200 automated um acceptances that I
[16:53] ran it, it it threw up a dialogue and
[16:56] said, "Oh, it looks like you're
[16:57] automating, you know, you're using an
[16:59] automated system. Like that's not
[17:00] allowed." And you know, so um I
[17:03] basically paused and I haven't rerun the
[17:04] agent since then because I'm kind of
[17:06] afraid. So the thing is like a lot of
[17:08] websites do um you know do protect
[17:12] themselves with some uh some amount of
[17:16] uh bot detection rate limiting etc. Um
[17:20] and uh so in you know in addition if you
[17:22] are going to enable WebMCP you may also
[17:25] need to tweak any sort of bot protection
[17:28] mechanisms you have um in order to allow
[17:32] what you want to allow right uh and I
[17:35] think there's a good question as to how
[17:37] many websites are okay with being
[17:38] automated like LinkedIn doesn't like
[17:40] getting automated u but other websites
[17:42] might be completely okay with it right
[17:46] yeah I mean Nambdi says the agency seem
[17:48] to be smarter and mimic human browsing.
[17:50] I would argue that like my LinkedIn
[17:52] agent was mimicking human browsing, but
[17:54] I think that I I don't know like how
[17:56] LinkedIn encodes it. They might say
[17:57] like, listen, if you've done more than X
[17:59] activities within this time frame,
[18:01] that's more than a human can reasonable
[18:03] do. So, they probably like defined
[18:04] thresholds and said like a human would
[18:06] never accept 200 notifications at once.
[18:09] I could argue that I could like I could
[18:11] be like really bored on a train and just
[18:13] sit there going accept, accept, accept,
[18:14] accept, accept, accept. Um and you know
[18:18] and it might be like oh this is
[18:19] automated right? So the other thing is
[18:21] it just might be detecting like just
[18:24] repetitive patterns like that seem too
[18:26] predictable and how much time they
[18:28] takes. So I actually don't know what
[18:30] algorithm LinkedIn was using to detect
[18:31] that I was using automated system. It
[18:33] was either just the max number of
[18:34] requests I did in a duration or it might
[18:37] have just been like uh kind of like a
[18:39] fingerprint of like oh this is like this
[18:41] kind of activity with the like the
[18:44] constancy of the duration and the timing
[18:46] looks like an automated activity.
[18:50] Uh so yeah lots of really um interesting
[18:54] things here.
[18:57] Um okay so DHS says the web MCP officers
[19:01] are Google and Microsoft. Oh, that's
[19:03] great. I did not know that. Uh,
[19:05] fantastic. Okay. Yeah. So, that looks
[19:08] that looks really fun. That could be
[19:10] that could be the future. I uh I'm very
[19:13] very positive on MCP. In fact, a lot of
[19:16] my upcoming talks are about MCP. Uh so,
[19:19] I look forward to digging more into MCP.
[19:21] I just think it's a night it's really
[19:23] nice to have a consistent way of um you
[19:28] know of having this interaction layer so
[19:30] that we can define approval and and all
[19:33] that with MCP.
[19:36] Um all right okay so web MCP
[19:41] uh so try that out. I don't think it's
[19:43] an edge yet is the thing. Uh, so it's
[19:45] interesting you say Microsoft authored
[19:47] it because as far as I understood there
[19:49] was no implementation in Edge yet or at
[19:52] least someone just posted in our channel
[19:54] about it.
[19:57] Edge. Edge. Edge. Edge. Edge is kind of
[20:00] a hard word to search for. Um, yeah. So,
[20:04] I don't know that Edge has support for
[20:05] it. Edge is based off of Chromium, but
[20:08] um
[20:09] uh I don't where do we find out
[20:10] compatibility browser
[20:13] compatibility
[20:16] edge? Nope. Okay.
[20:19] I don't I'm not sure where to check to
[20:22] see. Um but according to my colleague
[20:23] who posted about it just this morning,
[20:26] Edge doesn't support it yet.
[20:30] Uh
[20:32] okay. All right. So,
[20:36] web MCP. So, that's so that's very cool.
[20:40] Can all dig into that. Uh, what else is
[20:43] going on? Is that we've got Oh, wait. I
[20:45] saw a question from John. Uh, John is
[20:48] playing with Microsoft agent framework
[20:50] right now. As far as use case, do you
[20:52] have insight for what are good example
[20:54] agents kit can be built using agent
[20:57] framework? Um, yeah. So, it's a good
[21:00] question. That's a good time for me to
[21:01] plug the fact that our agent framework
[21:03] starts next week.
[21:06] And uh please sign up for that if you
[21:10] haven't yet. And in that series, we'll
[21:14] be digging into uh all the ways of
[21:18] building agents. I have been working on
[21:22] all the content for this. Um I have a
[21:25] very large PR that adds like 60
[21:27] different example agents. Um, so there's
[21:30] a lot you can do with these agents and
[21:33] with the workflows. As for your question
[21:35] like what are good use cases, it it just
[21:38] I think it really depends on your
[21:40] domain, right? A good use case for an
[21:41] agent is one where there's some like
[21:45] there's some step that requires I would
[21:47] say okay a good use case for an agent so
[21:49] remember an agent is something that uses
[21:52] tools in a loop, right? So we know that
[21:54] a great use case is coding, right? like
[21:57] aentic coders are amazing. They're, you
[21:59] know, they're slowly replacing most my
[22:02] all my coding is basically via a gentic
[22:04] coding, right? So obviously that's a
[22:06] really good um use case, but what else
[22:08] is a good use case for a for an agent,
[22:12] right? Um so something where it hacks
[22:14] access to tools and it uses the tools in
[22:17] a loop in order to achieve the goal. Um
[22:20] so the other really good use case right
[22:23] now is uh you know doing research,
[22:25] right? doing a lot of research like
[22:28] looking up this looking up this looking
[22:29] up the next thing right so I you know I
[22:31] use it when I'm doing um you know
[22:34] researching like a customer support
[22:36] issue right so you get a bug report or a
[22:38] customer support issue and you want to
[22:39] see has this been reported before what
[22:42] could the actual bug be like what
[22:44] changes led to it right so that's the
[22:46] kind of thing that you can um you know
[22:49] empower an agent with access to uh you
[22:53] know to lots of things and it can
[22:54] research arch a uh you know research a
[22:58] report and and come back um you know
[23:01] with a with a good analysis right so I
[23:03] think a a good use case right now for
[23:07] agents is you know domain specific
[23:09] research where you empower that agent
[23:11] with all like connected to all these
[23:14] places where it could do research
[23:16] documentation
[23:17] um issues support tickets uh etc right
[23:22] um then the reason I recommend research
[23:25] is because we still have the issue of
[23:28] hallucination, right? So, um you know,
[23:31] if you're when you're doing research,
[23:33] you know that the output is going to be
[23:34] like a research summary with citations
[23:36] and that you can you know use that for
[23:39] next steps and so you inherently have
[23:40] like a human in the loop there that can
[23:42] do verification. Um, if you're going to
[23:45] do if you're going to use an agent to
[23:47] actually take action and do something on
[23:50] your behalf based off what it's found,
[23:52] then you need a either a high degree of
[23:54] confidence or you need to add um, you
[23:57] know, a human human in the loop, right,
[23:59] which we talk about here. Um, and so
[24:03] there I think you can, you know, you can
[24:05] do more. You can actually like um
[24:09] uh you can you know take actions like um
[24:14] post on social media. I don't it just
[24:16] depends on your domain what you're going
[24:17] to do. Generate reports like email
[24:19] people whatever. Um but you just you
[24:22] need to have way more confidence if
[24:24] you're going to take actions and and
[24:26] confidence if you're going to do actions
[24:27] that are right actions than like right
[24:30] operations then yeah then you need a lot
[24:32] more confidence.
[24:33] Um I don't you know I don't have
[24:35] examples of
[24:37] uh things that people are doing in
[24:40] production. If you have any examples of
[24:41] agents you're using in production please
[24:43] share them because people are always
[24:44] asking me like how are people using this
[24:47] in production. Um but right now you know
[24:49] I I definitely recommend you know
[24:52] research and triage as a use case that
[24:56] many of us can use uh because we get a
[24:59] lot of like input uh from users and
[25:02] customers and whatnot and that that we
[25:04] can then uh have research be done on.
[25:10] Um so Nomi says you could use it for low
[25:13] impact decisions like recommendations on
[25:15] Netflix. Yeah. So if you're for your
[25:17] personal like if you're doing like a
[25:18] hobbyist agent then you know just like a
[25:20] hobby hobby thing for your personal life
[25:22] then there's like lots of you know
[25:24] things um you know you could do there
[25:27] where just something for fun um as Nomi
[25:29] says like recommendations
[25:32] um and uh
[25:36] yeah the interesting there is like
[25:37] whether you need it to have access to
[25:39] lots of like how many different tools
[25:40] does he even need access to at that
[25:42] point but um you know if it's if it's
[25:45] something kind of bonus like you know
[25:46] like a planning that's why lots of
[25:48] people do like planning agents right
[25:49] like I I have like you know like a
[25:51] weekend planner agent like what am I
[25:52] going to do with my kids okay first
[25:54] check and see if the museum's open then
[25:55] check this events calendar and like so
[25:57] it's like feeding it a bunch of context
[25:59] says like okay what are our possible
[26:01] options now think about it now you know
[26:05] make a plan make a schedule um
[26:08] so I think that's that's something fun
[26:10] you can do too um where it's low risk
[26:13] Right.
[26:19] All right. Uh, okay. So, what else is
[26:22] Yeah, I see various questions about
[26:23] Discord streams. Yeah, I think the
[26:26] stream is still running. Um, and we are
[26:28] still recording. So, you know, I will be
[26:30] posting the recording afterwards with
[26:33] the transcript and the write up of
[26:34] everything we we talked about. Um, you
[26:36] know, hopefully we captured all of it
[26:39] despite the internet hiccup in the
[26:41] middle there. Um, so yeah, there's only
[26:46] so much I can do about Discord. Um,
[26:50] okay. So, what else we have going on is
[26:53] uh last week we announced Agentic
[26:56] Workflows with GitHub. This is like a
[26:58] preview thing you can check out and you
[27:00] download this CLI. GH
[27:04] A
[27:07] W
[27:08] uh GH AW GH A W
[27:12] G H A W. Yeah. So you can do G GH
[27:16] extension install GitHub GH AW and then
[27:20] compile. So how this works is that you
[27:23] create a markdown file and the markdown
[27:26] file has some front matter here which
[27:28] says like okay we're going to run this
[27:29] daily. Here's the permissions that looks
[27:31] familiar if you've seen GitHub actions
[27:33] before. Um here's the allowed outputs so
[27:37] you can say what it's allowed to do. So
[27:38] that's nice. That's like guardrails. And
[27:40] then these are the tools it's allowed to
[27:42] use. So this would be the GitHub MCP
[27:44] server, right? And you can imagine other
[27:45] MCP servers as well.
[27:48] And then you have the actual
[27:49] description, right? So it says you're
[27:50] going to create a daily status report.
[27:52] Da da da. And so then it's when you run
[27:55] ghaw compile
[27:57] then it's going to actually turn this
[28:00] into a a um you know an generated
[28:05] workflow. And I remember looking at
[28:06] something like this like what like six
[28:08] months ago that someone recommended. And
[28:10] so now you know I think this is
[28:11] basically you know getting built into
[28:13] the GitHub CLI.
[28:15] And um so the generate so then you would
[28:18] like check the generated workflow into
[28:19] your repo but you wouldn't look at the
[28:21] generated workflow right and this is
[28:22] like generally this trend we're seeing
[28:24] is that we're apparently trusting the
[28:27] description like using markdown for
[28:30] describing some code that we want then
[28:32] compiling that into a lock file and not
[28:37] looking at that generated code right
[28:39] just treating that as a lock file and
[28:41] then checking it in which seems kind of
[28:43] wild to me but if they've thought
[28:45] through the safe outputs and the tools
[28:47] and the permissions then you know that's
[28:49] why that's done in the front matter
[28:51] because that then they can enforce that
[28:53] you know that that you know the guard
[28:55] rails are done programmatically and then
[28:57] the actual like implementation like what
[28:59] exactly it's going to do like that's you
[29:01] know the wishy-washy English text here
[29:03] so that's kind of interesting mix of
[29:06] programmatic guard rails with natural
[29:08] language for the workflows right
[29:11] um so yeah so they have various examples
[29:15] here of of things you can do. Uh it says
[29:19] start with lowrisk outputs. You know, we
[29:21] were just talking about lowrisk for
[29:22] agents as well like comments, drafts,
[29:24] reports. Um before going straight to
[29:27] pull requests, I don't know where I
[29:29] would store the report. So where would
[29:31] you wait where do you store daily report
[29:33] and then where do you put re create a
[29:35] daily status report? But then where
[29:39] I'm super curious. So I guess you post
[29:41] that in discussions
[29:43] this fire on cylinders. Okay, it feels
[29:46] like that could be my concern is be
[29:48] noisiness especially with daily report.
[29:51] Um
[29:52] uh yeah I I think the big you know big
[29:55] thing here would be noisiness. So you
[29:56] want to do something that is helpful for
[29:58] you that you know um is improving things
[30:02] without adding too much noise, right?
[30:04] Um,
[30:07] and you want to be really specific.
[30:10] Um, you want to make sure humans stay in
[30:13] the L loop. It says pull requests are
[30:15] never merged automatically. That makes
[30:18] sense. Uh, and
[30:22] uh
[30:24] don't don't use it as a replacement for
[30:26] all your workflows. Okay.
[30:29] All right. So, yeah. So, there's some
[30:31] good ideas here. Uh I have not tried uh
[30:37] making one
[30:39] yet. Um but it does seem like it could
[30:43] lower the barrier to um you know being
[30:46] able to do helpful maintenance tasks for
[30:50] repos um checking that things are
[30:52] staying good. Uh so do check that out
[30:57] and give feedback. Uh it says you can
[31:00] give feedback in the community
[31:02] discussion or in the discord. So they
[31:04] have their own discord which I didn't
[31:06] know about. Um so definitely try that
[31:10] out and give feedback.
[31:13] All right. Let's see. We had a question
[31:15] from John. Can we talk more about agents
[31:17] skills app? Maybe how are they different
[31:18] from system prompts? Okay. Yeah, good
[31:20] question. And also that does lead me to
[31:24] the other two articles that I was going
[31:26] to mention. Right. So there's skills
[31:28] bench
[31:30] um and then evaluating agents.mmd. So
[31:33] let's just throw these in the chat too
[31:35] since we're talking about um skills and
[31:40] agents. MD or just markdown files
[31:43] generally. Okay. So blah
[31:48] and skills.
[31:51] That's the same. Did I just put the same
[31:54] link for everything? Let's see. Yeah, I
[31:56] did. Oh, here we go. Okay, here we go.
[32:00] Okay, so both of these are evaluating
[32:03] like you know how well agents are able
[32:05] to benefit from from these um you know
[32:09] from these these useful things like
[32:12] skills and agents.mmd.
[32:15] Uh so to clarify like what are they? Um
[32:17] so agents.md like actually I was just
[32:19] writing an I just wrote this an hour
[32:21] ago, right? So this is instructions for
[32:23] coding agents and um I I finally added
[32:28] it because I was tired of repeating
[32:30] myself in in the chat and reiterating
[32:33] things, right? So I wanted to make sure
[32:35] it knew this is about Microsoft agent
[32:37] framework. This is for the upcoming
[32:38] series. So I wanted to make sure it knew
[32:39] the abbreviation that we use internally
[32:41] at least which is math. Uh make sure it
[32:43] knew where the repo was because
[32:45] sometimes it was struggling to remember.
[32:47] uh find the change log because it's
[32:49] changing all the time and a lot of times
[32:51] I need to point it at the change log and
[32:53] then remind it how it could check the
[32:55] documentation. Um and then what we were
[32:58] just doing was Spanish translations.
[33:00] Um so we were we're trying to be really
[33:03] specific and say this is what you
[33:04] translate, this is the um this is the
[33:08] kind of Spanish you use informal and
[33:11] this is what you need to keep in sync,
[33:12] right? Um, so that's that's a you know
[33:16] pretty minimal agents.mmd, but really
[33:18] like your agents.mmd should be pretty
[33:21] minimal. your a like I would your agents
[33:23] at MD should be what the information
[33:25] your agents need to know in order to do
[33:28] a better job but not just like an
[33:30] overflow of information because what
[33:31] this um research found here is that when
[33:35] they you know just made agents.mmd files
[33:38] especially when they used LLMs to
[33:40] generate the agents.mmd files it would
[33:42] just be too much information and then
[33:43] the like the coding agents would kind of
[33:46] get uh distracted and do too much
[33:50] exploration and then not, you know, not
[33:52] reach the goal as quickly or just not
[33:55] reach the goal at all. Um, so they, you
[33:58] know, they recommend that you, you want
[34:00] to make sure that your agents.mb is has,
[34:02] you know, actually useful information
[34:05] and nothing more, right? Um, so if
[34:08] you're going to be like really rigorous
[34:09] about it, what you can do is like add
[34:10] something to your agents. MD, try a task
[34:13] and see if it gets better. And then you
[34:14] can even like undo it and try it again.
[34:16] Like you could actually be scientific
[34:18] about it. Um uh or what I do is I just
[34:21] wait I just see what the coding agent
[34:23] struggles with and if it struggles with
[34:25] something like okay I'll add it there.
[34:26] So that's agents.mmd. So check out the
[34:28] research on there. Now for skills um so
[34:30] for example I have uh skill here. So
[34:33] your skills can be in
[34:34] either.github/skills
[34:36] or aagents.skills. So that's the new
[34:38] standard is going to be agentskills.
[34:41] Um here I've got it in githubskills but
[34:44] I'll move it eventually once everyone
[34:46] supports it. I think for copilot CLI
[34:49] it's only claude/skills and
[34:51] github/skills. So eventually we're going
[34:54] to standardize about where these skills
[34:55] are. Um but basically you make a folder
[34:57] for each skill and that folder has a
[34:59] skill.md and then any associated Python
[35:02] files. Now this one doesn't have an
[35:03] associated Python file because I just
[35:04] didn't need it. Um but then in the skill
[35:07] you've got the name and the description.
[35:10] Um oh I guess you can even have an
[35:12] argument hint. I didn't even know about
[35:14] that.
[35:16] Um, that's fun. Um, so, um, yeah, and
[35:20] this is the o this is the only
[35:22] information that will get sent to the
[35:24] LLM when it's deciding what skills to
[35:26] use. So, you want this information to be
[35:27] really helpful. Um, so the LM can decide
[35:30] to invoke a skill. And if the if the
[35:33] agent decides to invoke a skill, then
[35:34] it's going to pull in the entire
[35:36] skill.md.
[35:38] And sometimes that skill.md will refer
[35:41] to, you know, a local Python file. Uh in
[35:43] this case it didn't need to um but it
[35:46] can
[35:47] uh uh so how is this different from a
[35:50] system prompt? Well a system prompt
[35:52] you're sending the whole prompt every
[35:53] time right? So the difference here is
[35:54] the skill the only thing that's sent
[35:56] every time is this front matter here
[35:58] right this metadata. The rest of this is
[36:01] not sent. So you can have you can feel
[36:03] free to have a lot of description here.
[36:06] You can have associated Python file. You
[36:08] can have resources assets etc. like you
[36:10] can have a lot of stuff in a skills
[36:11] folder and you don't have to worry that
[36:13] you're adding too much to the context
[36:16] because all that's going to get added is
[36:18] this metadata here. Um so uh it works
[36:22] when you know when there's things that
[36:24] sometimes it needs to use but it doesn't
[36:26] always know to use. Now what I often do
[36:28] is that I will make custom prompt files
[36:30] that tell it to use a specific skill
[36:32] just to make sure it's going to use it.
[36:34] So for example um review slides um this
[36:37] is how I'm keeping my slides in date uh
[36:40] in sync with the code and um basically I
[36:44] say review the given slides for
[36:46] consistency right so I like drag a PDF
[36:48] into the repo and then I just say
[36:50] slashreview slides and it says use the
[36:53] markdown skill right so what you can do
[36:56] is so here's the thing I could just if
[36:59] this was the only time I would ever use
[37:01] the skill I could totally just inline
[37:03] this entire skill. So there's definitely
[37:06] a spectrum here where you can totally
[37:09] just inline skill. So for example,
[37:10] actually I did inline a skill here,
[37:12] right? You see this review PR comments.
[37:15] Um this here is all code markdown that I
[37:18] copied and pasted from a skill in
[37:20] another repo. And this is skill that
[37:22] knows how to reply and resolve because I
[37:24] decided, you know, this is the only time
[37:25] I'm using it. I'm just going to copy and
[37:28] paste it. So, so that's the thing is
[37:30] like it's it's kind of fun to decompose
[37:32] them because then if you had multiple
[37:35] instances where you might want to use
[37:36] that same skill then you know you don't
[37:39] have to copy paste God's prompts but if
[37:41] you're literally only going to use that
[37:43] in if it's only some markdown like this
[37:46] one like I you know then you can just I
[37:48] could just put it exactly in here right
[37:51] and then and then boom I don't need to
[37:53] tell to use the skill right the benefit
[37:55] of skills is the reusability ility um
[37:58] across multiple prompts, multiple tasks.
[38:02] Uh so you could just say like, oh, as
[38:04] soon as you know, as soon as I have to
[38:06] use a skill across two different tasks
[38:08] or two different prompts, then I'm going
[38:09] to move it into a skill.
[38:13] Does that does that make sense? Um I
[38:16] think there's like a lot of like and
[38:18] also between like I mean between all
[38:19] these things like because I was also
[38:21] debating this one like agents at their
[38:22] Spanish translations, right? I ended up
[38:24] putting this information here, but I
[38:26] debated putting it in this update
[38:28] translations prompt right now that
[38:30] because you know the nice thing about a
[38:32] prompt is I specify the model because
[38:34] GBD 5.2 has better Spanish than the
[38:37] other models uh according to Gwen. So I
[38:40] wanted to make sure I was remembering to
[38:41] use the recommended model for this
[38:44] prompt. Um but I still wanted the agents
[38:47] like it's better if information like
[38:50] this isn't agents.md because then
[38:52] everyone will look at that, right? Like
[38:53] so if we're using any sort of other
[38:56] coding agents and not using the prompt,
[38:58] you know, it's going to see what's in
[39:00] agents. MD, right? So um so you also
[39:02] have to consider what goes in your
[39:04] specific prompts versus what goes in
[39:06] your agents.mmd. But for this one, I
[39:07] said, okay, you're going to update
[39:09] according to agents.mmd. And I kept this
[39:11] pretty light. Really, the whole goal of
[39:13] this prompt was just to enforce the
[39:15] model, right? So that might be another
[39:17] reason why you might use uhprompt
[39:21] is to enforce the model if the model is
[39:24] very important. Uh I usually don't
[39:25] specify the model um but for
[39:30] translations in particular that is very
[39:33] dependent on on model right
[39:37] uh so yeah so that gives you a good
[39:40] range of of things here. Um I see a
[39:43] puppy waving. Hi.
[39:46] All right, let's see. Um,
[39:51] all right. Uh, so do Pablo says to what
[39:54] extent with tool Okay, tools that
[39:57] execute in the local machine creating
[39:59] simple agents and code
[40:02] um
[40:04] uh might not be these tools allow more
[40:06] features than the coding frameworks.
[40:09] Um, so the interesting thing is, yeah, I
[40:11] think now you have to decide like when
[40:13] are you going to like build a full fancy
[40:15] like agent or workflow? When are you
[40:18] going to like if it's just for developer
[40:19] automation like are you just going to
[40:21] write some skills, write some, you know,
[40:24] prompts, whatever. Um, and then here's a
[40:26] new debate is when do you use the
[40:28] copilot SDK? Because now we have the
[40:30] copilot SK. The copilot SDK is basically
[40:32] a general agent harness. So, you know,
[40:36] I'm doing all this work here on the um
[40:38] you know, on agent framework demos, but
[40:40] I could do everything with the copilot
[40:42] SDK, too. Not everything. I could do a
[40:44] lot of the agent stuff with the copilot
[40:46] SDK. The workflows would be harder. Um
[40:49] so, we definitely have a you know, kind
[40:52] of a decision point that we have to
[40:54] decide when we're whenever we're doing
[40:55] something is like, okay, is this is this
[40:58] a prompt? Is it a workflow? Is it a you
[41:02] know, a fancy agent that I'm going to
[41:03] run and deploy in production? Is it an
[41:05] agent I'm going to run locally? Um, is
[41:08] it something I'm going to write with a
[41:09] copilot SDK? So, it kind of just builds
[41:12] on top of some stuff that's already in
[41:13] the repo. And I think we just have to
[41:16] keep in mind all those options. And it's
[41:18] usually best to start with whatever is
[41:20] the lightest weight, right? Like it's
[41:22] always best if you don't have to
[41:23] maintain a full, you know, script, you
[41:26] know, better if you don't have to
[41:27] maintain it. Um, so if you can achieve
[41:31] something and it's on the same quality
[41:34] as, you know, writing a full fancy agent
[41:37] and if you can do that just with a
[41:38] prompt, then you know, great, right? Um,
[41:43] so I would say like you start with
[41:44] whatever's the lightest weight that gets
[41:46] what you need to get done and then once
[41:48] you run into the limitations of that,
[41:50] that is when you uh, you know, you
[41:54] consider your other options, right? like
[41:56] to further codify something to make it
[41:59] into a more programmatic
[42:03] uh you know a more programmatic agent or
[42:05] workflow.
[42:09] All right. Um so Justin says Justin's
[42:12] been using skills lately after my office
[42:14] hours leaks found much success using
[42:16] skills and prompting the agent to use
[42:17] those skills. Okay, awesome. Yeah,
[42:19] definitely check out um that skills
[42:21] bench. Oh, related to skills should
[42:23] check. We should link to this one.
[42:27] GitHub Microsoft skills. So these are
[42:29] skills particular for like useful for
[42:32] people using Microsoft technologies. Uh
[42:34] I only just saw this the hour ago an
[42:36] hour ago, but um so this gives you Okay,
[42:40] what does it give you? Um
[42:45] okay, so here we go. So it's got the
[42:48] it's got a bunch of Okay, AZD
[42:50] deployment. So if you're using the addd
[42:51] CLI um copilot SDK I just mentioned so
[42:55] making it easy to use that GitHub issue
[42:57] creator. Oh man I'm using copilot all
[42:59] the time to make issues now like it's so
[43:01] good if you ever like if you're using an
[43:03] open source for example with agent
[43:04] framework right um so I've been using
[43:06] agent framework a lot and when I run
[43:09] into a bug um then uh I
[43:14] um actually they've closed all mine
[43:16] let's see uh let me see
[43:19] uh
[43:24] close,
[43:26] open, close.
[43:28] Here we go. Um,
[43:31] how do we check the author? Author.
[43:35] There we go. All right. So, here's an
[43:37] example of an issue that um, you know,
[43:40] Copilot just filed for me, right? So,
[43:43] hopefully this like Okay. I want to make
[43:45] sure if you're filing bugs on open
[43:47] source repos, please do it responsibly.
[43:49] So try and dig, you know, you know, make
[43:52] sure it's really really um an issue with
[43:54] the thing. But I do think that once you
[43:56] know it's actually a bug with the thing
[43:58] that Copilot can do a really nice job um
[44:02] filing an issue report, right? So uh so
[44:05] that's a nice use case for it. Uh MCP
[44:08] builder podcast generation
[44:11] skill creator. So that's kind of meta,
[44:13] but it's make it easier for you to make
[44:14] skills. And apparently this someone was
[44:16] just posting that this one will actually
[44:18] like improve your skills too. Like it
[44:21] will um it will analyze your skills to
[44:25] see if they're good. So that's Oh, that
[44:27] is really fancy. Uh so uh yeah. So check
[44:32] that out. I guess once you install it,
[44:34] you can pick which of the skills
[44:37] which of the skills you want um and um
[44:41] and you know load them selectedly.
[44:46] All right. So, Desh says they were
[44:47] experimenting with Foundry Hosted
[44:49] agents. It runs on Microsoft Manage
[44:52] Infra and not in my subscription. Uh
[44:55] Desh is pretty disappointed. Okay, so
[44:57] Foundry hosted agents.
[45:00] Um wait, when you say it runs on
[45:02] Microsoft Manage infra, not your
[45:03] subscription, I guess to me that sounds
[45:04] like the same, right? Your subscription
[45:06] is Microsoft managed. Um, so basically
[45:10] like a foundry hosted agent like goes
[45:12] through a hosted agent runtime. Are you
[45:16] saying that the issue is that that
[45:17] hosted runtime isn't necessarily like in
[45:19] your resource group? Because maybe
[45:21] that's the case. Uh, admittedly I don't
[45:23] use the foundry hosted agents much um at
[45:27] all because I prefer, you know, like
[45:29] doing something like agent framework
[45:31] instead. Um,
[45:33] but uh yeah. So okay. All right. So
[45:38] okay
[45:40] so is it not running
[45:43] so if you create a foundry project in
[45:45] like west us and you create a hosted
[45:47] agent there are you saying that the
[45:49] hosted agent runtime that it's using to
[45:51] like execute the tools and and do the
[45:53] loop are you saying that that one is not
[45:55] in west us like it's not colllocated
[45:57] with your resource group is that what
[45:59] you're saying and is there some docs on
[46:01] that
[46:03] because that would be interesting to
[46:07] But okay. And then let's see. Do I have
[46:11] anything? Oh yeah. So related to
[46:13] boundary thing. I think Oh, we mentioned
[46:15] Sonic 4.6. Okay. So I think we've we've
[46:18] seen the news. So can go and look at um
[46:23] questions. All right. So Hatman Stack
[46:26] has a rag question. Is anyone actually
[46:29] solving ranking for mixed me media or we
[46:31] all just going to be running boost
[46:33] factors for a while? Oo, that's a great
[46:35] question. I did actually ask about that
[46:37] the other day because I'm working on um
[46:39] an MP server that uses AI search with
[46:43] images of the clothing in my closet,
[46:47] which is really fun. Um but um I
[46:51] realized I couldn't use the re-ranker
[46:55] with it. So my proposal was that um
[47:00] because the reanker only looks at text.
[47:01] So what I'm going to do is add um media
[47:05] description to my ingestion pipeline
[47:09] and that way the reranker can operate on
[47:12] the description of the media. So right
[47:14] now like um as uh as far as I know if
[47:19] you wanted to use re-ranking with mixed
[47:23] media I think you would want to have
[47:26] media description as um you know as part
[47:30] of your um as part of your pipeline. Let
[47:33] me get a visual. Do I have a visual for
[47:35] that? Let me see.
[47:38] Um yeah, so that's my plan for my
[47:43] um because I was realizing that like I
[47:45] was definitely missing, you know, when I
[47:47] had an image image only server, I was
[47:50] disappointed by some of the results
[47:52] because I would search for a green dress
[47:53] and the first nine of them were green
[47:55] and the 10th one was pink and I was
[47:56] like, well, if I had a reranking model
[47:59] working, you know, I could definitely
[48:00] like look at the reranking score and be
[48:03] like, uh, no, that's not going to work,
[48:04] right? Okay. Okay. So, for example, when
[48:06] we do multimodal ingestion, right, we um
[48:10] we do for every figure, we come up with
[48:13] a description and we add those
[48:15] descriptions to the original text,
[48:18] right? That's how we do it for the the
[48:21] um the rag repo. I think I have a better
[48:25] release for it here. Let's see.
[48:29] Custom skills. Where did I do the new
[48:34] um
[48:38] new approach to multimodal rag.
[48:42] Yeah. Use lm describe.
[48:47] Um so that's what I would suggest as far
[48:50] as I know. No, like at least at
[48:52] Microsoft um I don't think that we're we
[48:56] have reranking
[48:59] um
[49:00] you know working
[49:03] for that. Let me find the one that has
[49:05] the other diagram. Okay, here we go.
[49:07] These are two relevant diagrams.
[49:11] Um but um you know if you describe it
[49:14] and I think that's a good practice to do
[49:16] media description anyway.
[49:19] Uh but it is more effort and it slows
[49:21] down your digestion and your update and
[49:24] all that stuff because you have to
[49:25] describe all the images going in.
[49:32] All right.
[49:35] So,
[49:37] how do you get your agent built with MS
[49:39] Microsoft agent framework to use the
[49:41] online evows in Azure Foundry?
[49:46] It's a good question. I have seen the
[49:48] online evows with the um
[49:51] the actual um foundry agents and those
[49:56] are fun. Let me see if I can
[49:59] bring that up so we can see what we're
[50:01] talking about here.
[50:13] Let's see if I can find my
[50:29] I wish there was an easy way to just
[50:31] find find my projects that have agents
[50:33] in it because I always forget where I
[50:34] put an agent.
[50:39] Let's see
[50:43] as your opening view all resources.
[50:51] Um, project AI project hosted agent
[50:54] test.
[50:56] Well, AI project hosted agent test looks
[50:59] like a good one. This is for my
[51:01] colleague, but hey. Okay. Is there an
[51:03] agent here?
[51:09] All right. I don't I can't like easily
[51:11] find an agent, unfortunately. Um, yeah.
[51:14] So, what are hosted agents?
[51:17] So that's I think this uses AZD
[51:21] to deploy it. Um is it let's see create
[51:25] a hosted agent. Yeah. So it's using this
[51:29] AZD extension to deploy it. Um
[51:36] and deploys to container apps.
[51:39] But the question is whether you can do
[51:41] online. So I was trying to show online
[51:43] about online are cool. The idea is as
[51:45] soon as you you know um issue a request
[51:50] uh to
[51:52] um you know as soon as a request goes
[51:53] through the agent you can run LLM based
[51:56] evaluators on the request to see you
[51:57] know was that grounded was it complete
[51:59] right like so that way you can
[52:01] continuously evaluate your agents in
[52:03] production
[52:05] um
[52:07] I'm just looking okay observability so
[52:09] that's good
[52:12] and what about evaluate built-in an
[52:14] evaluation agent found
[52:16] agent evaluation.
[52:19] Okay, it doesn't say
[52:22] whether it doesn't say whether online
[52:24] evaluation is available.
[52:32] Uh let me let me go ahead and ask um
[52:37] uh let's see which channel
[52:40] should I ask in?
[52:43] Um,
[52:51] okay. I'm gonna ask my colleague, are
[52:54] online evaluations
[52:56] available for hosted agents built with
[53:00] math docs unclear
[53:04] question in officers.
[53:08] Okay, I have asked um I've also gotten
[53:10] some updates about things. Um okay, so
[53:15] Sonnet 4.6 is rolling out to GitHub
[53:17] Copilot right now. Um so here we go. So
[53:21] we that just got that update. So C-pilot
[53:25] is coming here.
[53:27] Um
[53:29] and yes, this this session will be
[53:31] recorded and there'll be a transcript
[53:33] and all that stuff. Uh, let me see if I
[53:36] got what other updates I got. Uh,
[53:43] and
[53:48] okay. Oh, and if any of you are doing
[53:50] Foundry agents, the next model Mondays
[53:53] is going to be talking about Foundry
[53:57] Agents. So, sign up for that.
[54:02] my colleague runs that series so that
[54:05] would be helpful.
[54:08] Um,
[54:12] okay. Yeah. So, I don't know about
[54:13] online evals
[54:15] for the hostry hosted agents yet. I've
[54:17] asked
[54:19] uh my colleague that has been playing
[54:21] with that and chatting with the team
[54:24] and so uh hopefully
[54:27] find out and you can um always ping me
[54:29] on LinkedIn to see if I got an update to
[54:32] the question. Okay. And then I see a
[54:33] followup from the rag question. So with
[54:37] a mixed media corpus in a single index,
[54:39] the HNSW graph holes from filtering hit
[54:43] everything equally. Is anyone working on
[54:45] multimodal reankers that could handle
[54:47] both or splitting into separate sources
[54:50] the way that most people are approaching
[54:52] it? Um, yeah, it's a good question. I
[54:56] will just send it to my
[54:59] colleagues on
[55:02] the RA on the AI search team to see
[55:05] if they know. I don't think I've seen
[55:07] because you know the re-rankers that I
[55:09] know of are the AI search um you know
[55:12] reranker and uh you know I think they
[55:15] have been experimenting with using LLM
[55:17] for that and if they're using LLMs for
[55:19] that then presumably you can use a
[55:20] multimodal LLM um to you know to improve
[55:24] the output and then of course the other
[55:25] ranker is the coherent rerank models. I
[55:29] don't know if any of them are
[55:31] multimodal.
[55:35] I know there's a new one 4.0 because I
[55:37] need to upgrade to it. It's a
[55:40] multilingual model.
[55:43] Rerank, rerank, rerank. It doesn't
[55:45] mention
[55:47] does not mention multimodal support.
[55:51] So yeah, so I think you right now
[55:54] probably you would have to be using a
[55:58] maybe a multimodal LLM to implement
[56:01] re-ranking.
[56:02] Um but uh I'll defer
[56:07] I'll ask my AI search colleagues that
[56:09] might know um know more.
[56:13] All right. Okay. And now that does bring
[56:16] us to the end of our office hours today.
[56:21] Uh just to reiterate upcoming events,
[56:23] the Python agent series starts next week
[56:26] and we're going to have, you know, so
[56:28] many code samples. It's going to be
[56:30] English and Spanish. Uh so definitely
[56:32] check that out. Uh let's see. Microsoft
[56:34] AI tour has been going around the world.
[56:36] I don't even know where it is next. U Pi
[56:38] AI is happening in San Francisco on
[56:40] March 10th and I'll be presenting at
[56:42] that along with Guido and lots of other
[56:44] cool people. MCP summer is in New York
[56:47] City in April and I still don't know if
[56:49] we got any submitted for that, anything
[56:51] accepted for that. Pyon is in Long Beach
[56:54] in May and I did get an MCP tutorial
[56:58] accepted for that. So, if you come to
[56:59] Pyon, we're going to have a tutorial
[57:01] about building your first uh Python MCP
[57:04] server in with Fast MCP and Keycloak and
[57:09] uh whatever other fun stuff we can add
[57:10] to that. So, that I'm pretty excited
[57:12] about. Oh, and last week, yeah, last
[57:15] week was the tech connect in Redmond.
[57:19] This was an internal thing for um Cloud
[57:22] Solution Architects, and I was going to
[57:24] go to that, but then I ended up cancing,
[57:27] so I know I missed a lot of people
[57:28] there. Next year, I think I should go.
[57:31] Um, I do plan to go to the MVP summit.
[57:34] If any of you are MVPs, and I know at
[57:36] least a couple of you are, I don't know
[57:38] if you're coming to the MVP summit, but
[57:39] there is the MVP summit coming up in
[57:41] March. And there's going to be several
[57:44] uh MCP related uh workshops there that
[57:47] I'm gonna be helping with. And uh I did
[57:50] ask if I could dress up as Clippy for
[57:52] that summit, but no one's given me
[57:54] access to the Clippy costume yet. So
[57:56] maybe that's not happening. But I will
[57:57] be helping with uh MCP workshops
[58:00] hopefully with the ACD booth. Uh so if
[58:03] you are an MVP and you're going to be at
[58:04] the MVP summit then I will see you in
[58:08] March um or like March 25th or so at
[58:12] that summit.
[58:15] So it's going to be a busy few months
[58:18] going forward. Uh I have a lot of
[58:21] powerpoints to make over the next
[58:24] four days.
[58:26] Uh all right. Uh so thank you everyone
[58:29] for all the great questions and I will
[58:33] update the um our our uh you know our
[58:36] our thread about office hours will get
[58:40] updated with recording transcript um
[58:46] links all that stuff will all be there.
[58:48] Usually I get it up by uh by the next
[58:52] day.
[58:53] All right, everyone. Great having you
[58:55] all here today. Lots of good fun things
[58:57] to explore. Have a good rest of the day
[59:01] and I'll see you next week. Next week,
[59:03] uh, we're going to have office hours
[59:04] every single day because it's going to
[59:06] be after each series thing. So, it'll be
[59:08] at 11:30 instead of at 11. Right now,
[59:10] this is at 11 my time. It'll be at 11:30
[59:13] to happen right after thing. So, for
[59:15] office hours next week, it'll be
[59:17] Tuesday, Wednesday, Thursday. So, for
[59:18] the next two weeks after this one, it'll
[59:20] be Tuesday, Wednesday, Thursday, 11:30
[59:22] to 12:30 um to answer any questions that
[59:25] people have after each of the live
[59:27] streams. So, my voice will hopefully
[59:30] survive a lot two hours of talking every
[59:32] day.
[59:34] All right, bye everyone.
[59:39] Let's see.

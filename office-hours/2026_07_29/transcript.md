[00:00] All right, great.
[00:02] Welcome everyone to the office hours for
[00:06] the uh for the live stream that I just
[00:09] held about work IQ. Um we've got Paulo
[00:14] here. You want to introduce yourself,
[00:15] Paulo?
[00:16] >> Yeah, thank you. Yes, I'm Pablo Gorsi.
[00:19] I'm a senior developer advocate. I'm
[00:21] focused on Microsoftify compilibility as
[00:24] well as on work IQ and that's why I'm
[00:27] here to try to help you with Q&A.
[00:32] >> Awesome. So, uh yeah. So if you have any
[00:35] questions just um just type them in the
[00:38] chat and and I will I'll get let me give
[00:42] some links for the session just in case
[00:46] people are here that don't know what
[00:48] we're talking about
[00:49] >> and and maybe ju just to be clear I
[00:51] think we are good on the technical side
[00:53] of the story. So we are good uh when it
[00:55] comes to talking about how to consume
[00:58] workq with MCP A2A rest and all that
[01:01] kind of stuff. We are not good on the
[01:04] licensing side or in the copilot credit
[01:07] consumption side because that's not our
[01:08] area of expertise, right Pamela?
[01:13] >> Yeah, I don't know a ton about pricing.
[01:14] I know we did have some questions in the
[01:16] chat about pricing um in terms of the
[01:19] tokens. Uh let me go back and look
[01:21] through look at those questions that we
[01:24] didn't um have answers for. So there
[01:26] were questions how will how will
[01:29] autopilot billing work? And then Bernard
[01:32] asked, you know, who has to pay for the
[01:34] tokens it consumed? Is it the user who
[01:38] invoked it? Um,
[01:41] so those are good questions. I would
[01:44] assume that actually
[01:47] given that your the agent is using
[01:52] your own LLM for answering, I think that
[01:55] you're going to be paying like um
[01:58] [clears throat] the person who
[01:59] provisioned the LLM
[02:01] would be the one paying.
[02:04] >> Well, I can only make assumptions. We we
[02:06] can we can dive deep into this topic
[02:10] maybe in a blog post or something like
[02:11] that because it is a really good and
[02:13] interesting question. Uh I can make
[02:15] assumption but I don't want to guess the
[02:18] answer. So I'll keep it on hold and
[02:22] eventually we can come up with a blog
[02:23] post to dig into it. What do you think?
[02:26] [clears throat]
[02:28] >> Yeah, that sounds that sounds good. uh
[02:32] and let me share there's some questions
[02:34] about so the all the source code um is
[02:37] in the the repo so particularly for
[02:40] there's a lot of excitement for workmate
[02:43] everyone wants to deploy their own
[02:44] workmate so that is inside the the the
[02:47] repo that we have here um and it has um
[02:53] some deployment steps uh I like if you
[03:00] know if you think the readme is
[03:01] sufficient or if there's any notes you
[03:03] want to give because it sounds like
[03:04] several people want to just go ahead and
[03:06] deploy workmate you know right now.
[03:09] >> It's an amazing demo.
[03:12] >> Yeah.
[03:14] >> Um
[03:16] uh so yeah so um so all the code is
[03:19] there if you do like if you try any of
[03:22] our code from the series and if you do
[03:24] have any issues just you can just file
[03:26] an issue on the repo. it'll go to me and
[03:29] Aisha and um you know we can look at it.
[03:31] This this is definitely one of the most
[03:33] complex repos that we've done because of
[03:36] having to um work with all of the IQs
[03:40] and it's it's very hard to get access to
[03:43] all of the IQs in a single tenant. At
[03:45] least for me I I have not even succeeded
[03:48] in getting a single tenant that has
[03:49] every IQ on it. I'm like scrging around
[03:52] to other people's tenants whoever will
[03:53] let me in. Um so yeah so the deployment
[03:57] is a little it's a little um it's a
[03:59] little trickier um in terms of the the
[04:01] code but uh yeah in theory
[04:05] >> uh you should be able to deploy
[04:06] everything if you've got the permissions
[04:08] to do it and for most of these things we
[04:10] have like booleans to turn things on and
[04:12] off right so if you've got access to
[04:13] work IQ great if you don't um then you
[04:17] know then you can do some stuff more
[04:18] manually
[04:19] >> and I see that I replied in the chat
[04:22] that the readme should be enough to
[04:24] being able to run the demo. But in case
[04:26] of any issue, you can reach out to her
[04:28] on LinkedIn or you can find an issue in
[04:30] the GitHub repo. And I'm reading the
[04:32] chat just for the sake of the recording
[04:34] in case someone will watch the recording
[04:36] and will not have the chat live.
[04:40] Yeah, that's a great point. Um, yeah,
[04:43] let me just link to it on LinkedIn so
[04:46] everyone can go add her.
[04:48] I'll go I'll go find Paulo's too.
[04:52] I apparently have a lot of Pablo on
[04:54] LinkedIn. Okay. Well, [laughter]
[04:57] >> but I'm the one and only one.
[05:00] >> Um, I haven't even found you yet.
[05:02] There's so many. [laughter]
[05:04] >> I can share later. Yeah,
[05:07] >> I got it.
[05:09] >> So, any any specific question on the
[05:12] technical part of the story?
[05:15] >> Let's see. Um,
[05:19] I see
[05:19] >> see people writing. We have some
[05:21] questions. Okay. So, Bernard
[05:23] >> has a question. Do you have best
[05:25] practices for these IQ deployments? How
[05:28] to structure or maintain it in a larger
[05:30] environment?
[05:34] >> Well, when it comes to all the IQs, it
[05:36] requires quite some uh uh knowledge
[05:38] because as Pamela was saying, if you
[05:41] want to have an environment with all of
[05:43] the IQs, you need to have knowledge in
[05:45] the foundry area, in the work IQ area,
[05:47] and the fabric area. So you need
[05:49] multiple uh personas to being able to
[05:53] manage and do governance of all of the
[05:55] uh deployment because it's not actually
[05:57] just one service that you deploy but
[05:59] it's actually multiple uh services on
[06:02] top of workloads you have uh in your
[06:05] tenant.
[06:09] >> Yeah, I haven't. So I haven't used the
[06:11] A365 stuff very much because that's
[06:14] around government governance. Have you
[06:16] used the A365?
[06:19] >> Well, you can definitely use A365 to do
[06:22] governance of agents. Um, I don't think
[06:25] you can use it to do governance of
[06:27] fabric IQ and fun IQ unless I has a
[06:30] different perspective, but as far as I
[06:32] know, Agent 365 is really good on doing
[06:35] governance of agents and tools.
[06:39] >> Yeah. Well, I think that's what that is
[06:41] definitely part of what people want
[06:42] because there's a question of like oh
[06:43] wow like work IQ has access to um you
[06:46] know stuff like do action now and get
[06:48] entity and create entity. So how you
[06:51] know how do you have confidence that
[06:53] when you're deploying something that has
[06:54] access to those tools that it's doing
[07:00] what you want it to do [laughter]
[07:02] right and not not doing other stuff. So
[07:04] is that something where A365 would be
[07:07] helpful?
[07:09] >> Well, when you deploy agent with agent
[07:11] 365 and you do governance with that
[07:14] tool, you can also see what kind of data
[07:17] and tools the agent will access. So you
[07:19] have the capability to do monitoring and
[07:22] to inspect what's happening inside a
[07:25] specific agent. When it comes to the
[07:27] content you retrieve through work IQ,
[07:29] well, you simply need to keep into
[07:31] account that whenever you access uh the
[07:34] intelligence of your organization
[07:36] through work IQ, there is always the
[07:37] security uh layer uh in place. So every
[07:41] user as like as I was writing in the
[07:43] chat before in the during the live
[07:45] stream, every user can only access the
[07:48] content they are allowed to uh access.
[07:51] So uh there's no risk of someone getting
[07:54] access to something which is not allowed
[07:57] to uh to see and uh there is also DLP in
[08:01] place. So you have all of the uh
[08:04] security and control on your content as
[08:06] like as you do when you use for example
[08:09] uh copilot and the bit chat of copilot.
[08:14] I think the one thing you it's good to
[08:16] be concerned about would be multi- aent
[08:18] systems because if you have a system
[08:21] that is using work IQ and then another
[08:23] system that's like publishing to the web
[08:26] or something like in theory that is a
[08:28] way that um user data leakage can in
[08:31] theory happen um if if one agent gets
[08:34] some user data and passes it to another
[08:36] agent um or even itself it has its own
[08:39] tool to publish things externally uh
[08:43] then you get into situation where um
[08:45] potentially private data can leak,
[08:49] right? So that I would I would look out
[08:51] for that in deployments
[08:52] >> that that that's a potential risk, but
[08:56] basically it means that you are relying
[08:58] on an agent which is a Troan horse or
[09:00] something like that because it is an
[09:02] agent that retrieves data uh secured and
[09:06] then gives that data to some other agent
[09:08] or uh service.
[09:11] Yeah.
[09:14] Yeah, I I think there was some scenario
[09:16] with um an agent that had like access to
[09:19] a GitHub private repo and then it like
[09:22] posted a comment on like a public repo
[09:23] that like referenced the information
[09:25] from a GitHub private repo, right? So
[09:26] that's an example just even with the
[09:28] even just with the GitHub MCP server um
[09:31] being able to have access to both
[09:32] private and public repos that then uh in
[09:36] theory data can leak between uh private
[09:38] and public, right? So there like so even
[09:41] within the same agent like because
[09:43] there's different levels of um you know
[09:46] publicness about about things like it's
[09:49] just as soon as you give access to right
[09:51] tools there is that risk right
[09:53] >> yeah but at the same time as I is also
[09:56] noticing in the chat uh you can choose
[09:59] which tools are available to which agent
[10:02] so uh again if you do proper due
[10:05] diligence of the agents you deploy in
[10:08] your environment and use tools like
[10:10] agent 365 to do uh governance and
[10:13] monitoring. Uh you will be in control of
[10:17] your content and of your information.
[10:22] >> Okay. And that also she mentions evals
[10:24] and there was a question from Pablo
[10:25] about evals. How shall we evaluate the
[10:27] data retrieved by work IQ? Uh I guess
[10:30] that we would get different results
[10:31] depending on the type and cleanliness of
[10:33] the data that is stored and accessed by
[10:35] work IQ. Um, so maybe I can post in the
[10:38] chat how she's been doing evals, whether
[10:40] she's doing them formally or or
[10:44] casually. Um, and I don't know if Paulo
[10:46] if you've done anything with evals with
[10:47] the work IQ.
[10:49] >> Not recently. So I've done evals with
[10:52] declarative agents but not with work IQ
[10:55] honestly. So let's see if I does have
[10:56] any feedback on that.
[10:59] Yeah, I would say work IQ is interesting
[11:01] because it does like I've se I've you
[11:04] know I've seen a like a really variable
[11:06] quality depending on what kind of data
[11:08] it's getting because when it's for me
[11:10] the worst quality is when it's quering
[11:12] teams chats because it's the most likely
[11:14] to um get kind of lost because teams
[11:18] chats are like the most like the the
[11:20] messiest data in the universe is like a
[11:22] team's chat right because you know like
[11:24] you know we have like our chats with
[11:26] each other and like some of our messages
[11:27] are like one like one you know word or
[11:30] something right like just incredibly
[11:32] incredibly messy data and it matters so
[11:34] much who like the attribution right who
[11:37] said something right so I've seen with
[11:39] work IQ the issues I've seen with team
[11:40] chats is like one just failing to find
[11:42] something because like I have a team
[11:43] chat with somebody who I send like 50
[11:45] messages a day and it is so hard for it
[11:47] to like find comprehensively find an
[11:49] answer in my chats with that person um
[11:51] and then the other issue is just
[11:53] misattribution I have seen some
[11:54] misattribution where it got confused
[11:56] about um you know who who was the person
[11:58] that said this and also who you know who
[12:01] are they talking to now right like you
[12:03] know are they like just knowing that I
[12:05] was the one that said something so I
[12:07] think if you're doing evals of work IQ I
[12:10] would I would consider it on like a kind
[12:12] of a um data type basis right where I
[12:15] think you'll find if you do evals over
[12:17] um something that's asking for calendar
[12:19] events you know you're going to see
[12:21] pretty good results there um but if
[12:24] you're if if you're relying not to on it
[12:27] to search through SharePoint data or
[12:30] Teams chats uh or emails like that's
[12:32] where you know and basically the more
[12:34] messy the data is the harder that job is
[12:37] like that's just a really like you know
[12:39] really hard job to be able to accurately
[12:41] search through all of this messy data
[12:43] and get back a good response um so
[12:46] generally with evals what I you know of
[12:48] you know usually recommend is like you
[12:49] know you want to like really represent
[12:51] the messiness of the you know real user
[12:54] data right so you know when you're um
[12:57] running emails, like if you can like try
[12:59] to simulate um set up like you can set
[13:01] up like a test tenant that has uh you
[13:04] know like really really long teams chats
[13:07] that are really you know messy and
[13:10] slangy and casual
[13:12] um you know that sort of thing like it
[13:14] evals are always the best when you can
[13:17] mirror your actual user situation right
[13:22] >> and I see in the chat a is stating that
[13:24] she's running some custom evals of
[13:26] agents
[13:28] which work with work IQ MCP tools and
[13:31] she is suggesting you to explain how you
[13:34] can do uh foundry agents uh eval when it
[13:39] comes to consuming MCP tools.
[13:43] >> Um yeah so I mean there is the foundry
[13:46] eval uh foundry evals SDK let me find my
[13:50] um
[13:51] examples for that. Um so there you know
[13:54] that's the you know there you can set up
[13:56] evaluations using LLM as a judge and you
[13:59] can have you know you can do custom
[14:02] evaluators and say like like if your
[14:04] agent has a particular job like your
[14:05] agent is do is doing scheduling then you
[14:08] could set up a custom eval which is like
[14:10] you know did this do a good job
[14:11] scheduling did it do it at the right
[14:12] time blah blah blah. Um, but you can
[14:14] also just do generic evals and say like,
[14:16] oh, like um,
[14:19] you know, did was this did this agent
[14:21] provide a grounded response? Was it a
[14:23] relevant response? Um, or with agents
[14:26] you often do like tool calling accuracy
[14:29] like you just say like, hey, did it call
[14:30] the right tool? So those are um you know
[14:33] those are things that you can
[14:36] evaluate
[14:38] um you know that's evaluating like did
[14:42] the a thing is that is more evaluating
[14:44] the agent whereas Pablo was wondering
[14:46] just about I I feel like Pablo wants to
[14:48] evaluate at the more of the retrieval.
[14:50] >> Yeah, that's my feeling as well.
[14:52] >> Yeah.
[14:53] >> Yeah. So I'll I'll link to like this is
[14:55] like a foundry um eval script that I ran
[14:58] on a foundry agent which sets up a bunch
[15:00] of um evals for tool calls. Um but I
[15:03] think if we really want to evaluate
[15:05] retrieval then you know then you would
[15:07] set up a retrieval eval and retrieval
[15:09] eval there what you want to know is um
[15:12] [clears throat]
[15:13] you know like for a particular query
[15:15] what do you expect it to retrieve and
[15:17] did it retrieve it right? So you you
[15:19] know we get those attributions from work
[15:21] IQ. So if you can develop if like Pablo
[15:23] if you can like make the ground truth
[15:24] and say hey for this query I expect to
[15:27] see these attributions
[15:29] um then you can just measure it and see
[15:31] like what's you know what's your recall
[15:33] and precision like how often did it like
[15:35] did it find um all the attributions you
[15:38] expected did it find a partial of them
[15:40] did it find some extra ones that you
[15:42] didn't want it to find right um and then
[15:44] you can uh you know then you could
[15:47] actually do it but then in order to do
[15:48] that you do have to set up you know a
[15:50] ground truth Um and um you know that can
[15:55] take some
[15:58] time to do. Um
[16:01] but uh
[16:03] but yeah like that like that you know if
[16:05] I was measuring um you know retrieval in
[16:09] particular uh then
[16:12] uh then I would be you know I would be
[16:14] looking at that um
[16:16] >> and then and then you can look at your
[16:18] agent agents itself um you know it's
[16:22] because it's useful to value the whole
[16:23] thing too because you know you're if
[16:26] you're if you're using an agent with
[16:28] work IQ then agent is often doing some
[16:30] sort of query rewriting where it's
[16:32] deciding like okay I see this user's
[16:34] question I'm going to turn it into this
[16:36] particular you know call to work IQ
[16:40] um so you also want to be able to
[16:42] evaluate that right so that's what's
[16:43] tricky is that you it's totally useful
[16:45] to evaluate retrieval on its own and see
[16:47] like oh maybe we need to like
[16:48] restructure our shareepoint data like a
[16:50] lot of people have asking been asking
[16:52] like oh like how do we like make sure
[16:54] our shareepoint data is well structured
[16:56] right and make sure it's going to ingest
[16:58] well So um I think it is useful to do
[17:00] that eval of the retrieval
[17:04] on that level but you're going to still
[17:06] need to evaluate the actual agent that
[17:09] is calling work IQ because of that query
[17:11] rewriting because sometimes it's all
[17:13] about like
[17:14] >> you know like I can't get it to like put
[17:17] in the right query call the right tool
[17:18] right like did know so there that's
[17:20] where you get these you know evaluators
[17:22] like tool calling actually did it call
[17:24] the right tool did it call it with the
[17:25] expected arguments right like how well
[17:28] did it do on that. So you you want to do
[17:31] both.
[17:32] >> I I I totally agree. I see another
[17:34] question from Bernard about the
[17:36] debugging of declarative agent is
[17:38] referring to a comment that I sent in
[17:40] the live stream on YouTube. Uh basically
[17:43] when you want to uh the question is how
[17:45] can you enable debugging of declarative
[17:48] agents? uh there is a special prompt
[17:50] that you can provide if I'm not mistaken
[17:53] is dash developer space on uh I can be
[17:57] more precise on that later but uh
[18:00] basically you enable the debug mode in
[18:02] the copilot chart and then when you
[18:05] consume a declarative agent and inside
[18:07] the declarative agent you rely on an MCP
[18:10] tool you can expand the debug
[18:11] information and see uh what tool uh was
[18:15] invoked uh which tool were evaluated
[18:18] ated before choosing the one to invoke
[18:20] and you can also even see the lowlevel
[18:24] uh request and response. So there is
[18:26] quite some uh useful information to see
[18:29] how the declarative agent is consuming
[18:32] the external NCP tool or a rest API and
[18:35] other stuff. Uh so dash developer space
[18:39] on should be the syntax and then you can
[18:41] turn it off once you are done. Yeah.
[18:45] >> Yeah. I just found the article for that.
[18:47] >> Oh thank you. That's cool. Wait, so
[18:49] anyone can just type this? That's it.
[18:50] You just have to type that.
[18:52] >> Yeah, you type that and then you run the
[18:53] agent and you get the debug info.
[18:56] >> That's cool.
[18:57] >> Yeah,
[19:00] I can even open the page on the screen.
[19:02] I mean, and there's no
[19:03] >> Yeah.
[19:06] >> So, yeah. So that's if you've got so you
[19:08] have to do it with like an agent in the
[19:10] chat
[19:10] >> developer on and then you see
[19:12] successfully enabled and then you simply
[19:14] get the uh agent developer info and you
[19:17] get a bunch of information about what
[19:20] happened and why and what. So yeah
[19:22] really really useful.
[19:27] Yep.
[19:29] >> That's cool. Um so AA also on the evals
[19:33] front it says that she runs evals on the
[19:36] same agent multiple times changing the
[19:37] allowed tool list uh that she gets a big
[19:40] change in accuracy when she like you
[19:43] know really restricts the agent to only
[19:45] the necessary tools. So that's a very
[19:46] good tip.
[19:55] Let's see there was also an earlier
[19:58] question from Damian
[20:00] Can we get an AI agent to use work IQ
[20:03] for different tenants? He's thinking
[20:05] about creating a single AI agent that
[20:08] uses the tool for some of their partners
[20:11] so it can work in their tenant.
[20:14] >> Well, as long as you have different
[20:17] connections, I mean when you consume
[20:20] work AQ for example over A2A or MCP from
[20:24] an external agent, you need to
[20:26] authenticate using open authorization.
[20:28] So you need to provide an access token
[20:31] in the messages and you have to retrieve
[20:34] an access token for the target tenant
[20:36] that you are willing to consume. So as I
[20:40] would say as long as you have a pool of
[20:42] connections to the multiple tenants
[20:46] I don't see any issue. Uh now is it
[20:50] worth having an agent which can access
[20:53] content of multiple tenants from a
[20:55] security risk perspective? I don't know.
[20:58] That's something that I'm questioning
[21:00] and wondering, but that's a different
[21:02] topic. From a technical perspective,
[21:04] when you consume workq, you just need an
[21:07] access token. So once you have an access
[21:09] token for a specific tenant, you are
[21:11] good to go.
[21:14] >> What do you think?
[21:15] >> I think one question is like when you
[21:16] say you're making an AI agent, how are
[21:18] you exposing the agents? Are you
[21:19] building a you know your own custom
[21:21] front end on top of it and that you know
[21:23] front end has a login screen, right? Um,
[21:26] and in that case you, you know, have
[21:28] like an Entra app that was allowing
[21:30] people to log in from the different
[21:32] tenants or are you doing publish to
[21:35] Teams? Like one of the things I noted um
[21:37] in my live stream yesterday is that if
[21:39] you're doing a Foundry hosted agent and
[21:42] you do publish to Teams, um, that's only
[21:45] going to work inside the tenant where
[21:48] you published it. Um, because it asks
[21:50] you to log in and it it it's only going
[21:53] to work when it's published there. So
[21:55] there's, you know, probably, you know, a
[21:56] way to get that to work across tenants,
[21:59] but not with the like easy oneclick
[22:01] publish. So,
[22:02] >> um, I think there's just a question of
[22:03] how are you exposing that agent, right?
[22:05] Because most your your customers
[22:06] probably aren't like running a Python
[22:08] script. So, you're probably like putting
[22:09] it besides and like inside some sort of
[22:12] UI and the question is how is that UI
[22:14] going to get the user token. If the UI
[22:16] has a way to have the user log in to
[22:18] their tenant,
[22:19] >> then then that's what you need, right?
[22:21] because a work IQ just needs that user
[22:23] token and definitely however it's going
[22:25] to get that.
[22:25] >> Yeah, remember that work IQ does not
[22:27] work with app only tokens. It only works
[22:30] with delegated access tokens. So you
[22:34] need to have a token of a specific user
[22:37] uh to access the work IQ API whether it
[22:40] is A2A, MCP or REST. So
[22:47] >> we have another question from Andrew.
[22:50] Hopefully you can help with this. How do
[22:51] co-pilot studio agents relate to foundry
[22:54] agents? Uh his impression is that you
[22:56] choose one or the other depending if you
[22:57] want low code or versus full code and
[22:59] that they don't fully interact.
[23:02] >> Well, they actually can interact because
[23:04] when you create an agent with Copilo
[23:06] Studio, uh now I'm talking about the
[23:09] current user experience of Copilo
[23:11] Studio. There is also a new uh and under
[23:13] preview user experience which is still
[23:16] under construction. But in the current
[23:18] one um in copilot studio when you create
[23:21] an agent you can also connect your agent
[23:24] to other agents and those agents can be
[23:27] agent that you can uh consume over A2A.
[23:31] So it can even be work if you like or uh
[23:35] can be a foundry agent uh that you
[23:37] consume over uh A2A or there is a
[23:40] specific option to connect to a foundry
[23:43] agent. So theoretically if you can wear
[23:47] both the hats so you are both a
[23:48] developer and a maker and let's say you
[23:51] want to create some of your agents as
[23:53] copilo studio agents because you find it
[23:55] beneficial to use uh for example power
[23:59] automate flows or some of the
[24:01] capabilities available in copilo studio
[24:03] and at the same time you have or you are
[24:06] developing uh creating agents with
[24:08] foundry uh you can connect them and
[24:10] create a multi-agent architecture to
[24:12] reuse the same technology multiple
[24:14] sometimes. Why not?
[24:19] >> All right. Nice. That's a demo for you
[24:21] to do. Um Damian followed up that
[24:24] they're thinking about deploying the
[24:25] agents to team to teams as an app so the
[24:28] partners could install the agent app.
[24:30] Okay. Okay. Well, then in that case, I I
[24:32] actually don't know how I actually don't
[24:35] know technically how to do that because
[24:36] when I did the one-click publish to
[24:38] Teams from Foundry Hosted agents, that
[24:41] was a like restricted to to um the same
[24:46] tenant where the agent was hosted. So, I
[24:49] I imagine there is a way to publish to
[24:51] Teams, but maybe at that point you have
[24:53] to use like the Teams SDK or or
[24:55] something like that um to be able to
[24:58] have an app that um any tenant could
[25:02] install. I don't know if you've done
[25:03] that before. But so now that I see the
[25:06] comment from Damian, my understanding is
[25:09] that Damian, you're not looking for an
[25:11] agent which will be able to access at
[25:14] the same time the content of multiple
[25:16] tenants, but you are actually looking
[25:18] for a solution to have one agent that
[25:20] you can deploy on multiple tenant and
[25:22] that's totally different story. So and
[25:24] from a security perspective, I
[25:26] definitely like this second option
[25:28] compared [laughter] to the previous one.
[25:30] So if your need is to create an agent
[25:32] that you can deploy on multiple tenants,
[25:35] yes, you can do uh so of course you will
[25:37] have to configure the agent uh to target
[25:40] the specific tenant where you deploy it.
[25:43] But yes, you can you can do that. And of
[25:46] course in every single tenant, your
[25:48] agent will be able to access only the
[25:52] organization intelligence of that
[25:53] specific tenant through work IQ.
[25:57] And do you know what um approach they
[26:00] use to publish to teams such that it
[26:03] it's installable in any tenant?
[26:07] >> Uh the you mean the one in foundry?
[26:12] >> Uh yeah. Yeah.
[26:16] >> Not really. Um I was thinking more about
[26:20] uh agents like declarative agents or
[26:22] compiler studio agents which can be
[26:24] exported and imported on uh different
[26:27] tenants as well as the declarative
[26:28] agents can be deployed on multiple
[26:30] tenants. For example, when you use ATK
[26:33] or the CLI based deployment
[26:36] you can target multiple environments uh
[26:39] like for example you have a dev tenant a
[26:42] a pre-production tenant and a production
[26:44] tenant and you want to do testing on all
[26:45] of these environments.
[26:47] It could also be multiple customer
[26:50] tenants if you like.
[26:54] >> Okay. I've also posted a question to the
[26:57] hosted agents team uh about the best
[27:00] approach to
[27:02] um being able to install on multiple
[27:04] tenants.
[27:06] >> See Bernard is saying for publishing
[27:08] agents are there any security checks or
[27:10] frameworks to check the agent against
[27:11] risky actions in order to avoid security
[27:13] issues?
[27:15] Hm.
[27:17] >> Well, we had a similar question
[27:19] yesterday. I can't remember if Bernard
[27:20] was here in yesterday's one, but we, you
[27:22] know, we did mention guard rails, right?
[27:24] We do have the foundry guard rails that
[27:26] you can put on the LLM that's powering
[27:29] the agent. Um, and the guard there's
[27:32] quite a lot of guardrails now. Like I
[27:34] was surprised actually there's a bunch
[27:35] of new ones um when I was exploring them
[27:39] uh yesterday. Uh, and that's got like
[27:42] they even there's like a PII guardrail
[27:44] now for example, right? Um, so, uh, just
[27:49] want to make sure everybody knows about
[27:50] that. I think Bernard already knows
[27:53] about that because we chat about
[27:54] guardrails a lot in our officers here,
[27:57] but that one has so it has jailbreak, it
[27:59] has indirect jailbreak which is like uh
[28:01] content poisoning like for rag. Um it
[28:04] has you know content harms. It has
[28:06] copyright material. It has PI detection.
[28:09] Um and it also even has like LM as a
[28:12] judge like task adherence and
[28:13] groundedness. Um
[28:17] so those can be applied to the model
[28:20] itself. Uh so any whatever model you're
[28:23] using for your agent, you create your
[28:25] set of guard rails in Foundry. um or you
[28:29] can write it programmatically with bicep
[28:31] and uh assign it to
[28:35] to the LM.
[28:38] Um the question is I guess what other
[28:41] sort of risky action you're you know you
[28:44] want to check for right so
[28:47] um you know we always talk about like
[28:49] the thing is like you're the one who's
[28:51] deciding which tools it has access to
[28:53] right so if you're saying it has access
[28:55] to do action then it has access to do
[28:57] action right so is it that you want to
[29:00] make sure oh it can send emails but it
[29:01] can't send emails to like 100 people for
[29:04] example right maybe you only want it to
[29:05] be able to send emails to like two So
[29:08] you could actually like do something
[29:09] like if you're using agent framework,
[29:11] you could write middleware and say you
[29:13] could intercept the tool calls and say
[29:15] hey uh you know if I see that it's
[29:17] trying to send an email to more than two
[29:20] people I'm just going to cut it off and
[29:22] disallow it. Right? So um you know I
[29:26] guess it depends which tools they're
[29:27] calling and and what sort of action you
[29:30] consider risky in those tools. Right? So
[29:32] the first thing you do is make sure that
[29:33] you're only giving access to the tools
[29:35] that you are comfortable with it. Right?
[29:37] So if you only want to have read only
[29:38] access, then you're going to do like ask
[29:40] and fetch, right? Those are like read
[29:41] only ones.
[29:42] >> Um but then yeah, if you do give it
[29:45] access to do action, maybe you want to
[29:46] be like pickier about which actions it
[29:48] can do. Then maybe at that point you're
[29:50] doing like a middleware that is
[29:52] intercepting the tool calls and saying,
[29:54] you know, this tool call is not okay.
[29:56] Um, I think it depends on whether like
[30:00] whether that to middleware is successful
[30:03] depends on, you know, what those tool
[30:04] calls look like and whether you can like
[30:06] intercept them and reason about them um
[30:09] and their riskiness, right?
[30:12] >> Oh, so Oh, Bernard wants a static
[30:14] analyzer at build time.
[30:18] H
[30:22] meanwhile while you think about the
[30:24] answer I see one guy is asking if there
[30:27] are live demos or videos uh or screen
[30:30] sharing today. Actually this is the
[30:32] office hour following a live stream
[30:35] session that I delivered where there
[30:37] were live demos. Of course, we can do
[30:39] live demos here as well if it is needed.
[30:41] But there will be the recording
[30:43] available on YouTube of the video that
[30:46] live streamed it live streamed half an
[30:49] hour ago.
[30:51] >> Yeah, here's the video for
[30:53] >> Yeah, thank you Pamela.
[30:56] >> A static analyzer. Yeah, I'm going to
[30:58] ask about static I don't I don't know
[31:01] about a generic static analyzer for
[31:04] this. I think that could be like a um
[31:08] an agent skill. I mean it feels like
[31:13] weird to just say like well you can just
[31:14] write a skill for it but I mean honest
[31:16] like you know like we have like
[31:17] dedicated like you know uh security
[31:20] skills and copilot SC like GitHub
[31:22] copilot security skills right so um you
[31:25] know certainly given that I I don't know
[31:27] about a static analyzer particularly for
[31:29] this um let me also chat with the agent
[31:33] framework team like if that's something
[31:36] they're thinking about um but I would
[31:39] you know certainly you know you can
[31:40] write um a skill that's going to uh you
[31:44] know look through and I wonder if
[31:45] there's any existing skills and be like
[31:47] okay you know flag the potential um you
[31:51] know issues that could come from this um
[31:56] but let me ask the agent framework team
[31:58] too if this is something they're
[31:59] thinking about
[32:00] >> and and I see Pablo is uh uh coming back
[32:03] on the quality of the responses of work
[32:06] IQ uh it's a mix of a feedback and a
[32:10] question because said if you have
[32:12] different team members triggering work
[32:14] IQ they are underlying Micro5
[32:16] environment can vary of course because
[32:18] depending on the user permission you can
[32:19] have different uh uh content accessible
[32:22] and what part patterns and configuration
[32:25] do you recommend to scope tools and
[32:27] lockdown source data versions so the
[32:29] team gets standardized reliable results
[32:35] well since the priority I would say the
[32:38] priority is security it is important
[32:40] that every user get back only what is
[32:43] accessible to that specific user. So
[32:47] trying to find a way to give the same
[32:48] answer and the standardized answer to
[32:50] every user regardless their security uh
[32:54] uh permissions
[32:56] doesn't feel like something
[32:59] really good to me honestly. Uh so uh
[33:02] it's in my opinion it is more about
[33:05] configuring proper uh security and
[33:07] governance of the resources you want to
[33:09] target with your agent rather than
[33:12] finding a way to use work IQ to get
[33:14] always the same answer regardless who
[33:16] the user is. What do you think Pamela?
[33:19] >> Um
[33:21] sorry I was on another
[33:23] >> you're multitasking. Sorry. [laughter]
[33:25] Yeah, I did. I got to respond to
[33:26] something else. But what was okay? Um,
[33:30] what P was this what patterns and
[33:32] configurations to
[33:33] >> to give a standardized answer to the
[33:35] user regardless the content they can
[33:37] access.
[33:43] >> I think it's I [laughter] think it's
[33:45] going to be hard.
[33:46] >> Yeah. I mean, if it is generic content,
[33:48] of course, it is easy. But if it is
[33:50] >> because I just know like like I think
[33:51] that's like part of the reason why I
[33:52] struggled so much when work IQ first
[33:55] came out is because my like I was
[33:57] testing it on very messy teams chats and
[33:59] I think everybody else was like testing
[34:01] it on like really clean teams chats and
[34:02] I'm like all right I got like mine are
[34:05] like a lot crazier than yours. Um so
[34:08] what what was your suggestion Pablo?
[34:10] Well, my suggestion is that you should
[34:12] actually work on defining proper uh
[34:15] access control lists on content but uh
[34:19] whatever content is actually accessible
[34:21] only to a specific subset of user should
[34:24] stay like that. I mean uh it is okay to
[34:28] use work AQ to get access to uh generic
[34:31] uh content which is accessible to all of
[34:33] the users but at the same time it is one
[34:35] of the peculiarities of work aq to give
[34:38] every single user the content they can
[34:40] see. So I wouldn't try to find a way to
[34:43] work around this uh uh way of working a
[34:47] work at you.
[34:50] >> Yeah. I mean, I think the thing is
[34:52] probably I would say um it it do your
[34:56] evaluations on the messiest data like
[34:58] the right because if you can get good if
[35:01] you're happy with the results with the
[35:05] the messiest data then you're you know
[35:09] you're going to be okay with it or um
[35:12] you know less messy right because yeah I
[35:14] think with work IQ the the experience is
[35:16] going to be really variable
[35:19] um you also might have like uh
[35:22] colleagues that are like speaking in
[35:24] different languages in their chats,
[35:25] right? And like that might be something
[35:28] that's going to affect um retrieval
[35:31] quality too. Um
[35:35] so
[35:36] >> as well,
[35:37] >> it's a really good question. [laughter]
[35:45] >> I see. I mean the other okay one thing
[35:47] you could do is you could try you could
[35:50] not use so because you know the the more
[35:54] if you want greater reliability then
[35:56] removing the LLM from the mix is one
[35:58] thing to do right and as you see work IQ
[36:00] does have some tools that use LMS and
[36:03] some tools that don't so you might want
[36:05] to say like listen we want very reliable
[36:07] repeatable results and you're probably
[36:10] going to get more repeatable results
[36:12] when you remove the LM from the mix
[36:13] right cuz that LLM layer you you know
[36:16] does add um variability because it's an
[36:18] LLM right it's not a deterministic and
[36:20] also like we might be like changing our
[36:22] prompt behind the scenes um so given
[36:24] like work IQ exposes like a range of
[36:27] tools some of which have an LM some
[36:29] which don't then you know I would see
[36:31] like can you um you know get away with
[36:35] using um you know using the more
[36:38] low-level tools now you might have the
[36:41] issue of more latency because then it's
[36:42] not like paralyzing because you know I
[36:44] think like the ones that LM actually
[36:46] will paralyze calls to like check your
[36:49] team's emails and chats like all at the
[36:50] same time or whatever. Um, so you may
[36:53] end up if you decide to not use yeah to
[36:56] use the more low-level ones, you you may
[36:59] end up wanting to like maybe doing some
[37:01] doing some parallelization yourself. Um,
[37:04] and just so you get like better
[37:06] performance, right? Because if you know
[37:07] you need to check emails, teams, and
[37:09] calendar all at the same time, well, you
[37:11] should be doing those in parallel,
[37:12] right? so that you get all the responses
[37:14] back at once. Um so so it means there's
[37:18] more orchestration that you have to do
[37:21] on your side but you have more control
[37:23] which means more reliability right um so
[37:28] that would be one uh consideration
[37:32] um for the question for Damian's
[37:34] question uh I just chatted with the
[37:37] hosted agents team and they confirmed
[37:39] that if you're using the publish hosted
[37:42] agents from the portal it's not going to
[37:44] work for multiple tenants you have to do
[37:46] it the standard M365 way, which is um
[37:50] this documentation right here. Um so
[37:55] yeah, so you you could do it, but you
[37:57] you need to go and use this approach
[37:59] instead.
[38:00] >> Yeah.
[38:10] >> Okay. What are we missing?
[38:18] I see a comment about uh the complexity
[38:21] of running all of the IQ's on the same
[38:24] tenant. Uh but it is more like a comment
[38:28] honestly. Uh and it is uh also asking
[38:33] for uh any investment to easy the work
[38:37] Avengers assembled.
[38:39] >> Yeah. So I know for me it's been very
[38:41] difficult to get all the everything on
[38:43] one tenant but I I think that's because
[38:45] Microsoft in particular is very locked
[38:48] down. I don't know how many other people
[38:50] are like work down like work in these
[38:52] very locked down environments. So like
[38:54] at Microsoft like we have these like
[38:56] special tenants and for each of these
[38:57] tenants we have to like explicitly get
[39:00] um co-pilot added to it. we have to
[39:01] explicitly get fabric added to it,
[39:04] right? Um, so, you know, hopefully if
[39:07] you're at a company and the company
[39:09] wants you to do something with work IQ
[39:10] or fabric IQ, then you know, they're
[39:13] able to give you a um, you know, give
[39:16] you access to that um, and um, give you
[39:21] like test licenses for test tenants. I
[39:23] assume it is it is it standard practice
[39:25] to use a test tenant when you're doing
[39:28] um, you know, when you're doing stuff
[39:30] like this? I I would suggest to try to
[39:32] use a developer tenant. So to register
[39:35] for the Microsoft 65 developer program
[39:38] and get access to a developer tenant, uh
[39:41] I can try to find the link. Uh let me
[39:46] try to do so.
[39:47] >> Oh, and that's specifically just for
[39:48] like uh M365,
[39:51] not for like fabric.
[39:53] >> Uh yeah, but then you can have a
[39:55] subscription associated to that tenant
[39:57] and you can also play with fabric. I
[39:58] sorry with found IQ. When it comes to
[40:01] fabric, I need to double check if you
[40:03] can also use fabric on that one. But
[40:05] definitely if you want to play with work
[40:07] IQ, you can try to uh you can register
[40:09] to the developer program for max 365.
[40:12] You can get a developer tenant which
[40:14] will come with a bunch of E5 licenses
[40:18] and uh you can then play on that tenant.
[40:23] Of course, you will also need some good
[40:26] quality content to play with it and
[40:28] that's something that we are working on
[40:29] and we are trying to address. So stay
[40:31] tuned. But right now you can at least
[40:35] create a developer tenant. Oh, by the
[40:37] way on the developer tenant you will
[40:39] need to enable a building profile to
[40:42] being able to use the copilot credit and
[40:44] get access to work IQ uh because
[40:47] otherwise you will not be able to use
[40:48] work IQ uh from any third party agent.
[40:53] because the first party agents like
[40:56] copilot itself can access work IQ but in
[40:59] order to use work IQ from third party
[41:01] agents. So uh any agent that you create
[41:04] whether it is a copy studio one or even
[41:06] with third party technologies and
[41:08] non-Microsoft technologies you will need
[41:10] to have a building profile configured
[41:12] and uh the copilot credits uh available
[41:16] otherwise it will not work just to be
[41:19] clear because it's provided on a
[41:21] consumption based plan. So
[41:24] >> yeah I'll link to the docs about
[41:25] co-pilot credits because that actually
[41:27] that was something I ran into like four
[41:28] days ago. my work IQ stopped working and
[41:30] we had to enable the copilot credits on
[41:32] our on our tenant.
[41:33] >> Yeah.
[41:34] >> Um
[41:34] >> Thank you.
[41:35] >> Yeah. Yeah. There's there is a bit of
[41:38] setup involved. Um but it's really fun
[41:40] when you get it working and then you can
[41:41] like automate like I do have a script
[41:43] that seeds emails. I've used that in
[41:45] some environments, right? So you can you
[41:48] know you can like seed um you know you
[41:52] can like programmatically create teams
[41:54] chats and emails and stuff like that.
[41:56] Once again depending on what you know
[41:57] how much access you have um to the
[42:00] tenant but like what is if you have the
[42:02] ability you know if you have a developer
[42:05] tenant where you can you know fully
[42:08] script things and you can like really
[42:09] set up a rich test environment because
[42:12] we've got APIs that can you know make
[42:15] all these datas um all these you know
[42:17] kinds of test data and I got to say like
[42:20] LLMs are pretty good at making test data
[42:22] now maybe sometimes their test data is
[42:24] too clean you kind of got to get them to
[42:25] make it like real real messy test data.
[42:29] Um but um you know it can like you know
[42:32] if I tell LM like hey I need like 200 um
[42:36] you know test emails like boom I've got
[42:38] it a minute later right like and and it
[42:40] can even write it'll even write the
[42:42] script that's going to you know populate
[42:44] my test tenant with those emails. So um
[42:47] just keep in mind like it's increasingly
[42:49] easier to set up test environments. Now
[42:52] the hard thing is making sure those test
[42:54] environments reflect
[42:56] the you know the the messiness of real
[42:59] environments. So the other thing you
[43:00] could do is say like hey actually I want
[43:02] you to like download the you know the
[43:04] entire chat for my real thing here and
[43:06] then like replay in this other tenant
[43:08] there you want to worry about like
[43:09] privacy and whether there's anything in
[43:11] your chat that you don't want on your
[43:12] test tenant. Um but just keep in mind
[43:14] like that GitHub copilot you know with
[43:16] these these um modern LLMs can make it
[43:20] very easy to um set up uh you know test
[43:25] environments. Um I use it quite a lot
[43:28] when I'm running evals to because it
[43:30] just helps me see whether um the evals
[43:33] are doing a good job and whether we need
[43:34] to like change our test data and and all
[43:36] that stuff.
[43:38] >> Yeah, I see an interesting question from
[43:40] John. We have a requirement to build a
[43:41] custom agent where our data is sizing
[43:44] shareepoint, outlook and confluence.
[43:46] Honestly, work IQ is bit confusing and
[43:48] initially thinking to go through
[43:49] Microsoft graph API. Is there any sample
[43:52] demos related to it? Well, uh we can
[43:56] definitely find some demos about how to
[43:58] use Microsoft graph but I want to make a
[44:01] step back. Um AA in the live stream
[44:04] presentation I think highlighted really
[44:08] well the differences between Microsoft
[44:11] graph and workq. Micro graph is mainly
[44:16] uh based on the idea of getting access
[44:19] to data while work IQ gives you access
[44:22] to the intelligence of your
[44:23] organization. So that's a huge
[44:25] difference. If you want to get if you
[44:28] want to retrieve uh just the email
[44:31] message as a complex object with its own
[44:34] properties go for Microsoft graph but if
[44:37] you want to retrieve the connection
[44:39] between an email a team's chat document
[44:42] you have in SharePoint and stuff like
[44:43] that you can't easily do that with
[44:46] Microsoft graph you need to work with
[44:48] work IQ and you need to rely on the
[44:51] intelligence and the context you have in
[44:53] your company and that's why we created
[44:54] work IQ because Microsoft gaff was not
[44:57] enough in the context of the agentic
[45:00] world. So if your need John is to create
[45:03] an agent my feeling is that you should
[45:07] prefer work IQ rather than Microsoft
[45:10] graph because one more thing when you
[45:12] use work IQ you get the uh response
[45:16] already synthetized by the LLM. So you
[45:19] only get the content that matters and
[45:22] you don't get huge amount of content
[45:24] that you need to process and you have to
[45:26] pay tokens for. On the contrary, if you
[45:28] use Microraph and let's say you want to
[45:30] process all of the emails you've got in
[45:32] the last week, you will need to retrieve
[45:35] all of them and to process all of them
[45:37] on your agent on your agent side, which
[45:40] means that you will also have to pay
[45:42] quite a lot of tokens to process all of
[45:44] the content. with work IQ you get the
[45:46] actual answer you're looking for and you
[45:49] don't need to uh pay for all of the
[45:51] tokens to process every single message.
[45:53] So I think it is a different perspective
[45:56] and in your scenario I would rather go
[46:00] for work IQ than uh using Microsoft
[46:10] >> has a another question
[46:13] studio to work IQ for you.
[46:15] >> Well studio has traditional enforced
[46:17] payload caps on tool responses. How are
[46:20] work AQ and CP results handled under the
[46:22] hood and are they payload or truncation
[46:25] differences between running workq and
[46:27] compiler studio versus foundry?
[46:31] Well, uh honestly I don't know if there
[46:34] is a different behavior between copilo
[46:36] studio and asure foundry when it comes
[46:39] to consuming work IQ from a work IQ side
[46:42] of the story. Work IQ is always the
[46:44] same. So, work a Q provides you a
[46:46] unified FCP server and the behavior and
[46:50] the response you get is the same
[46:52] regardless of uh what engine or LLM is
[46:56] consuming it. Then if there is something
[46:59] on the orchestrator side and on the
[47:02] consumption side of the story so in
[47:03] copilo studio or in aure foundry
[47:06] honestly I don't know I don't know if
[47:07] you know something about Asia foundry
[47:09] pamela
[47:12] >> um well a foundry hosted agent wouldn't
[47:15] be doing any sort of um payload caps
[47:19] itself right because a hosted agent is
[47:21] you know sample like doing agent
[47:23] framework using lm and so you're only
[47:24] capping what happen if you reach the
[47:26] context window but that's not even going
[47:28] a cap that's going to like straight up
[47:30] error. Um, if you go over the context
[47:33] window, right? So, typically we'd add
[47:35] some sort of summarization middleware.
[47:37] Um, so, uh, I don't know about Foundry
[47:41] prompt agents whether I don't remember
[47:43] what their sort of um, limits are or how
[47:45] they handle the context window, but
[47:48] yeah, when I do a hosted agent, you
[47:50] know, that's using agent framework with
[47:53] an LLM on Foundry. And so there um you
[47:57] know I it the only thing that can happen
[48:01] is that I go over the context window and
[48:03] then I get an error that says you're
[48:05] over the context window um because it's
[48:08] I I control everything right so it's up
[48:10] to me to decide as the developer like do
[48:13] I want some sort of temp creation and
[48:14] and it is common to do that right so you
[48:16] can do I was saying you could do a
[48:17] summarization middleware um or you could
[48:20] do like um a tool call limit middleware
[48:22] and say like hey like you've gone gone
[48:24] over um you know there's too many tool
[48:27] calls. Let me see actually because agent
[48:28] framework now has this built-in uh
[48:30] harness agent that has some of this
[48:33] stuff built in to make it easier. Let me
[48:36] see.
[48:41] Um, okay. So, the agent harness agent
[48:44] has, oh yeah, it has compaction built
[48:46] in, right? Um, so yeah, you do when
[48:50] you're, you know, basically running your
[48:52] own agent code, you do want to consider
[48:54] what's going to happen if your tool
[48:56] calls mean that you, you know, if your
[48:58] conversation gets too long. Um
[49:02] and so you know uh one approach is to
[49:05] write your own middleware. Another
[49:06] approach in agent framework is to use
[49:08] this new harness agent which does have
[49:10] compaction built in. Um
[49:13] there's there's all sorts of things you
[49:15] could do. Um but I don't expect there to
[49:19] be any sort of truncation happening on
[49:21] the platform side given it's just
[49:23] running your own code in a container.
[49:28] Okay.
[49:30] I see other folks are are typing. So,
[49:34] let's see. [laughter]
[49:46] So, Scorpion in the demo I had workmate
[49:49] and said that separate user could also
[49:52] use it and it would work in the context
[49:54] of that user. She mentioned that
[49:56] workmate would need a Microsoft license
[49:58] such as E5. So my question is when
[50:00] workmate is used in each user context
[50:02] that is need multiple licenses.
[50:05] Uh well maybe I can double check with me
[50:09] the answer but as far as I know whenever
[50:11] you create an instance of an autopilot
[50:14] you need a license for that specific
[50:18] autopilot instance.
[50:21] Am I correct?
[50:31] just a single license even if it is used
[50:34] across multiple people. Okay.
[50:37] But it's a single instance used across
[50:40] multiple people. Right?
[50:47] While if you have multiple instances,
[50:49] you need one license for every instance.
[50:51] Is it correct?
[50:55] typing.
[50:58] Yes. Okay. So, you basically need one
[51:01] license for every instance and if the
[51:03] instance is shared across multiple
[51:05] people then you need one single license
[51:08] for that instance.
[51:27] All right. So, John had a follow-up
[51:28] question.
[51:30] >> Mhm.
[51:32] Uh, if document or data access is
[51:35] restricted to different users initially,
[51:38] I assume based on the user enter ID, the
[51:40] agent will respond to the question. So
[51:42] you mean filtering the answer based on
[51:45] the user access control list. How does
[51:48] access look like for work IQ if it's
[51:50] already returning to summarized uh
[51:53] responses?
[51:56] Well the the behavior is the same. I
[51:58] mean work IQ will give you back an
[52:00] answer based on what you can see as a
[52:02] user. So whether it does the
[52:04] summarization or not, you just get out
[52:07] of work what you can actually access. if
[52:11] I'm understanding your question
[52:13] properly.
[52:20] If you want to expand it a little bit
[52:22] more, John, in the meantime, I see
[52:26] that I is writing. So,
[52:30] okay. One single work item instance can
[52:32] report to me, but Paul and Pamela can
[52:36] also access to it as well. So you would
[52:39] use the same instance across but there
[52:42] might be scenarios where you would need
[52:44] multiple instances then every instance
[52:47] requires an E5 license.
[52:50] Okay.
[53:01] And then I see Pablo is asking about the
[53:04] behavior of work AQ when used in
[53:06] compiler studio versus foundry or any
[53:09] other orchestrator. He says since copilo
[53:12] studio relies on its own manage
[53:13] orchestrator and query de composition
[53:15] and filtering should we expect
[53:17] differences in reasoning quality tool
[53:20] calling sequences or execution speed
[53:22] when quering work aq. I guess the answer
[53:24] is yes because depending on the
[53:25] orchestrator on the LLM you might have
[53:28] different behaviors. Yes. What do you
[53:30] think? Yeah, I mean you're Yeah,
[53:32] definitely like I mean everything
[53:33] changes your
[53:36] the world the world of agents, right?
[53:38] Like there's so many factors. We have
[53:40] the harness. So basically we're going to
[53:41] call say like cop studio is the harness,
[53:43] but then there's also the model that the
[53:44] harness is using, right? I don't know if
[53:46] copilot studio gives you controls over
[53:48] that or
[53:48] >> you can choose the model. Yeah.
[53:50] >> Okay. So then that's going to certainly
[53:52] change it, right? Vast differences when
[53:54] you when you change out the model. Um
[53:58] and so even if with agent framework like
[54:01] um there's the you know agent framework
[54:03] but then I can choose different models
[54:04] with it and that's right. So and then
[54:06] yeah I could even use like the I can use
[54:08] the copilot studio uh SDK is sorry
[54:11] GitHub copilot SDK would be like another
[54:13] harness or I could use the link chain
[54:14] harness. I could use the um deep agents
[54:17] link chain harness right I could use
[54:18] panti. Yeah, all of these like really do
[54:21] affect um the the um you know the the
[54:25] tool calling in particular. Um so uh
[54:29] it's always very interesting to to do
[54:31] comparisons. Um so uh yeah, so if you if
[54:36] you're disappointed with like you know
[54:38] with with um how an agent is calling
[54:40] tools, then you're going to there's a
[54:44] lot of different you know knobs you can
[54:45] tune, right? You can change the harness
[54:47] entirely. You can also just switch out
[54:49] the model and see like oh how different
[54:51] is it across models and then of course
[54:53] you can start doing things like changing
[54:56] your prompt um changing the tools around
[54:59] you know um and doing some sort of
[55:02] middleware planning like there's there's
[55:05] so many different factors that affect it
[55:06] which is why AI engineering is such a
[55:09] fun field that we're all learning so
[55:12] much from probabilistic engineering.
[55:14] Yay.
[55:15] >> Yeah. And I I see a an additional
[55:18] comment from John. So yes, John, you
[55:20] said uh you yes sorry you misunderstood
[55:24] the fact that work can access all the
[55:26] data in a tenant but actually when you
[55:29] consume work IQ through the work IQ APIs
[55:31] whether it is through a way MCP or REST
[55:34] you go to work IQ providing an access
[55:37] token. So you will only get back the
[55:40] content that the user uh that is
[55:43] consuming work IQ in that specific
[55:44] moment can access. So every user can
[55:47] only see the content they can see. And
[55:49] so yes, work aQ potentially can access
[55:53] the the whole tenant, but depending on
[55:55] who the user is, the access token will
[55:58] give you access to what that user can
[56:00] see.
[56:03] [laughter]
[56:06] >> Yes, yesterday was MC parties across the
[56:08] globe. So I went to the San Francisco
[56:10] one. Um and we did also uh like start
[56:14] like formally promoting our um our next
[56:18] live stream uh from one still doing this
[56:21] live stream series but the next uh this
[56:23] will be a 5-hour live stream on
[56:25] September 9th and um and that should be
[56:31] that should be fun. Um, obviously we're
[56:33] like MCP is definitely a big thing
[56:35] because look how much like this isn't
[56:36] even technically an MCP series, but look
[56:38] how much we're using talking about MCP
[56:40] in this series, right? Um, I mean work
[56:42] is also with A2A. So there's different
[56:44] protocols out there, but uh yeah, we're
[56:48] we're we're all in on MCP. So hopefully
[56:51] you can join for our September 9th live
[56:54] stream as well.
[57:01] Yeah, it's a Yeah, that was one of the
[57:02] comments last night like with the new
[57:04] MCP spec like basically it's at like the
[57:06] like now that it's state stateless that
[57:08] you know it's it's more like HTTP and
[57:10] it's like getting it's basically like at
[57:12] that HTTP point it's also based like it
[57:15] uses HTB behind the scenes so it's a
[57:16] little like higher level but
[57:19] uh sweet
[57:21] okay we're at we have one minute so um I
[57:25] think you've covered the questions.
[57:29] Um, so
[57:32] thank you everyone. Thank you Paulo for
[57:34] jump
[57:36] >> and thank you.
[57:37] >> We will and to for being in the chat and
[57:40] for the live stream earlier. Um, so we
[57:43] will um we'll publish these office
[57:46] hours. We'll we'll publish everything
[57:49] from the the resources page. So you
[57:52] check back. I usually have it up by
[57:54] midnight tonight um is when usually
[57:57] everything is up. So you can get the
[57:59] transcripts and the writeups and the
[58:01] slides, everything from that resources
[58:03] page and hope to see all of you tomorrow
[58:06] for fabric IQ. Um this is this will be
[58:10] my first time really talking about
[58:12] fabric IQ and I've learned learned a lot
[58:16] in the last few weeks about it so it'll
[58:18] be fun. Um so yeah I hope to see all of
[58:20] you tomorrow and for the office hours we
[58:22] will have a bunch of people from the
[58:24] fabric advocacy team since I was like
[58:26] okay I can I know enough now to give the
[58:29] you know talk about um how to use it
[58:31] from Python but I'm sure you all will
[58:33] have great questions about fabric that
[58:35] uh I cannot answer. So we will have a
[58:38] bunch of fabric advocates available to
[58:40] answer questions for tomorrow's office
[58:41] hours.
[58:45] All right.
[58:47] Thank you everyone.
[58:48] >> Thank you.
[58:49] >> See you tomorrow. Bye
[58:50] >> bye.

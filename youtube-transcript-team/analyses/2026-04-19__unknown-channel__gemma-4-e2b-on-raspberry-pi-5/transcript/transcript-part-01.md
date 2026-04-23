# Transcript Part 01

```text
After testing the Gemma 4 model on my

0:02

laptop and desktop, I decided to run a

0:05

crazy experiment to try launching Gemma

0:07

4 on my Raspberry Pi 5. Of course, I'm

0:10

not talking about any large versions of

0:12

this model, but rather attempting to run

0:14

the smallest one, E2B. I'm not sure if

0:16

this will work since even the smallest

0:18

model may still require significant

0:20

resources, but it's worth trying. My

0:22

Raspberry Pi 5 is on my home network, so

0:24

I always access it via SSH. I don't even

0:27

have a graphical interface installed on

0:29

it. Just Ubuntu server and a minimal set

0:32

of software that I need. Hi, I'm Nick

0:34

and I've been developing software for

0:36

over 20 years. On this channel, I share

0:39

my experience, insights, and thoughts

0:41

about it. So, I connect to my Raspberry

0:44

Pi via SSH. I have the terminal

0:47

multiplexer T-Max running there. It's a

0:49

very convenient and useful tool if you

0:51

often work in the terminal. T-Max allows

0:53

you to keep sessions running even if you

0:55

disconnect from another computer.

0:57

Definitely give it a try if you're not

0:59

familiar with it. All right, first I

1:01

launch HTOP so you can see the specs of

1:03

my Raspberry Pi. Just to remind you,

1:05

this is version 5. As you can see, it

1:07

has four cores and 8 GB of RAM, most of

1:09

which is currently free since I'm not

1:11

running anything heavy at the moment.

## Installing LM Studio CLI

1:13

Okay, the first thing I need to do is

1:15

install LM Studio. However, since I

1:18

don't need the graphical interface, I'll

1:20

install only the CLI version. You could

1:22

call it a headless version of LM Studio.

1:25

The developers provide a special script

1:26

that handles everything for you. After

1:29

installation, it suggests starting the

1:30

Damon right away. All right, let's do

1:33

that. Now, let's check what commands are

1:35

available. I see a set of commands for

1:37

managing models, some for managing the

1:39

local server, and a few others that I

1:41

don't need right now. In general, the

1:43

commands are pretty straightforward. But

## Setting up SSD storage for models

1:44

before launching anything, I want to

1:46

change where the downloaded models will

1:48

be stored. The thing is, I have an SSD

1:50

connected to my Raspberry Pi. So, I want

1:52

the models to be stored there instead of

1:54

on the SD card. By the way, Raspberry Pi

1:57

5 introduced a simple way to connect

1:59

SSDs and similar peripherals. I've been

2:02

using such a drive for over a year now,

2:04

and it's very convenient. All right, the

2:07

storage location is set. Now, I'm

## Gemma 4 E2B model overview

2:09

downloading the smallest model from the

2:11

Gemma 4 family. This model is called E2B

2:14

and it's about 4.5 GB in size. While

2:17

it's downloading, let me briefly explain

2:20

what it can do according to HooL's

2:21

announcement. First, the entire family

2:24

of these models is designed with

2:25

agent-based workflows in mind. They

2:27

natively support function calling and

2:29

can work with tools. Second, these

2:32

models can handle images and video. And

2:34

the smaller models, including the one

2:36

I'm installing right now, also have

2:38

native audio support. They can

2:40

understand speech directly. And third,

2:42

these models have a context window of

2:45

128,000 tokens and support almost all

2:47

languages. By the way, Gemma 4 is

2:50

released under the fully open and

2:52

commercially permissive Apache 2.0

2:54

license. That means you can do almost

2:56

anything you want with these models. All

2:58

right, the model has finished

2:59

downloading. As you can see, it has

3:01

around 4 billion parameters, which

3:04

should be enough for simple and smaller

3:05

tasks. I'm loading the model now. Okay,

## Loading the model and API server

3:09

it loaded successfully and is ready to

3:11

use. Now I'll launch Hutchtop aen to see

3:14

what changed after loading the model.

3:16

Looks like the model has been loaded

3:18

into RAM. All right, the last step is to

3:20

start the API server so I can interact

3:22

with the running model. I'll use port

3:24

4000.

3:26

All right, the server is running, but

3:27

just to be safe, I'll check if it's

3:29

working properly. To do that, I'll send

3:31

a simple HTTP request to get the list of

3:34

available LLM models. In that list, I

3:37

expect to see the Gemma 4 model I just

3:39

downloaded.

3:40

Nice. The API request was successful and

3:43

I got the list of models and I can see

3:45

Gemma 4 in that list. Perfect.

3:47

Everything is working. However, right

3:49

now LM Studio has started a local server

3:52

that's only accessible on the Raspberry

3:53

Pi itself. I want to use this model from

3:55

my other computers over the local

3:57

network. So, I'll stop the server and

3:59

restart it with an additional host

4:01

parameter, setting it to 0.0.0.0,

4:03

zero, which should make it accessible on

4:05

the local network. H, that didn't work.

4:09

It looks like the host parameter isn't

4:11

available, and I can only specify the

4:13

port when starting the server. But

## Enabling local network access via socat

4:15

that's not a problem. Since this is

4:16

Linux, we have all its power and

4:18

hundreds of utilities at our disposal.

4:20

So, there are plenty of ways to solve

4:22

this. I'll go with the fastest and

4:24

simplest solution using the soet

4:26

utility. It allows you to forward

4:28

network streams within the system, which

4:30

is exactly what I need. I'll forward the

4:32

internal port 4000 where the LM Studio

4:35

server is running to an external

4:37

interface on port 40001. This

4:39

effectively creates a bridge between the

4:41

internal and external ports. Now any

4:43

request coming to the Raspberry Pi on

4:45

port 401 will be redirected internally

4:48

to LM Studio. All right. Now I'll

4:50

disconnect from the SSH session on the

4:52

Raspberry Pi and so to speak return to

4:54

my MacBook. Now I'm in the regular Mac

4:56

OS terminal. I'll try sending the same

4:59

HTTP request as before to get the list

5:01

of available model, but this time not to

5:03

local host, but to my Raspberry Pi,

5:05

which as a reminder is on the same local

5:07

network as my laptop. Nice, it worked.

5:10

As you can see, I received a response

5:12

from the LM Studio server running on my

5:14

Raspberry Pi. And in that response, I

5:16

can see Gemma 4. Now everything is

5:18

finally set up the way I wanted. And we

5:20

can move on to the most interesting

5:22

part, actually testing Gemma 4 on the

5:24

Raspberry Pi. Since the local server

5:27

started by LM Studio fully mimics the

5:29

OpenAI API, it means that any

5:31

application where you can specify a

5:33

custom OpenAI endpoint or base URL can

5:36

work with your local model. This could

5:37

be chat interfaces like chatbox AI or

5:40

open web UI or your editors and IDE for

5:43

example VS code cursor or Z editor. I'll

5:46

be using the last one today. All right,

## Connecting the model to the Zed editor

5:48

I open the settings in the Z editor and

5:50

add a new entry in the LLM section for

5:52

the Gemma 4 model running on my

5:54

Raspberry Pi. Since I added a similar

5:56

entry a couple of days ago for my

5:57

desktop, I'll just copy it and update

5:59

the server URL and the model name. By

6:02

the way, I have a separate video about

6:04

running and testing Gemma 4 on my

6:06

MacBook and desktop. Now, if we go to

6:08

the settings and open the LLM provider

6:10

section, we should see an entry

6:12

corresponding to our Raspberry Pi. And

6:14

here it is. Okay. Now, in the chat at

6:16

the bottom, I'll select the Gemma 4

6:18

model running on the Raspberry Pi so

6:20

that it's used in this session. Let's

6:22

send a simple prompt to check if

6:23

everything is set up correctly and

6:25

whether our local network setup works

6:27

inside the editor. All right, the model

6:29

started thinking. That's a good sign,

6:31

but just to be sure, let's wait for the

6:33

response.

6:34

Nice, the model replied. Let's take a

6:37

look at the reasoning section. Looks

6:38

pretty standard. The usual thinking

6:40

process you'd expect from these models.

6:43

So, what do we have at this point?

6:44

First, Gemma 4 is successfully running

6:46

on the Raspberry Pi, even if it's the

6:48

smallest version. Second, I'm able to

6:50

interact with it from another computer

6:52

over the local network. I think it's

6:54

time to push this model to its limits.

## Coding performance test (Python)

6:56

To do that, I'll connect to the

6:57

Raspberry Pi via terminal and start

6:59

monitoring system resources so we can

7:01

see how much load the response

7:03

generation puts on it. Then I'll give

7:05

the model my standard test task, writing

7:07

a Python function to sort a list of

7:09

objects. All right, the model started

7:11

thinking. As you can see, the Raspberry

7:13

Pi is fully loaded. All CPU cores are in

7:16

use. Now the model has finished

7:17

reasoning and started generating the

7:19

response. I'll show this part in real

7:21

time without speeding it up so you can

7:23

get a sense of the actual generation

7:25

speed. Overall the speed is fairly

7:27

acceptable for simple interactions or

7:29

scripts where response time isn't

7:31

critical. Now to save time I'll speed up

7:34

the rest of the generation because

7:35

producing the full response on a

7:37

Raspberry Pi can take quite a while. At

7:39

the end I'll show the total time it

7:41

took. All right the full response is

7:43

ready. Not only did the model write a

7:45

sorting function, but it actually

7:47

provided two different implementations

7:49

and explained when to use each. Pretty

7:51

impressive. However, the total time

7:53

including the reasoning phase was about

7:55

6 minutes. I think this could be reduced

7:57

a bit by disabling the reasoning mode.

8:00

But overall, you get the idea of the

## Creative task test (Web app ideas)

8:01

performance. Now, for completeness,

8:04

let's try a non-programming task. I'll

8:06

ask the model to come up with three web

8:08

app ideas. After a short thinking phase,

8:11

which I've sped up, the model starts

8:13

generating ideas. What you're seeing now

8:15

is the real generation speed. From my

8:18

perspective, it's about the same as in

8:19

the previous task. I'd say this speed is

8:22

right on the edge of what feels

8:23

comfortable for a human to read in real

8:25

time, but for non-interactive scenarios,

8:28

it's acceptable.

8:30

I'll speed up the rest again and check

8:31

the total time.

8:34

All right, this time Gemma took about 5

8:36

minutes to generate the full response,

8:38

but it produced a lot of text and

8:40

described each idea in detail. In my

8:42

opinion, that's a very solid result for

8:44

such a small model, especially running

## Final results and conclusion

8:46

on a Raspberry Pi. So now you have the

8:49

full picture of running Gemma 4 on a

8:51

Raspberry Pi 5. As you can see, it's

8:53

absolutely possible and the results are

8:55

usable, at least for certain scripts or

8:57

automation tasks. This setup can

8:59

definitely make sense. All right, that's

9:01

it for today. If you enjoyed this video,

9:03

don't forget to like and subscribe so

9:05

you don't miss the next one. See you

9:07

soon.
```

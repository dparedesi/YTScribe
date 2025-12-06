---
video_id: cxXG5fZ5wik
video_url: https://www.youtube.com/watch?v=cxXG5fZ5wik
is_generated: False
is_translatable: True
---

- Thank you. Hi. (audience applauds) Hi everyone. My name's Ammar. I'm an engineer at Netflix
on the data platform team, and today we're gonna talk
about how we moved dozens of databases that were on a third party Postgres-compatible
distributed database to Amazon Aurora Postgres. We'll start by talking
a bit about the problem, like what we actually did and why. Then we'll spend some time
talking about how we did it. And I'll leave you with some, you know, where we are right now and what learnings we have so far. There's a ton of content
and not as much time. So I'm gonna blast through a lot of this, also because I'm slightly
over caffeinated, but fine at the end if you have questions or I can explain things a
little bit more in detail. So I'm on a platform team. We work with a whole
bunch of application teams and these application teams that, you know, run the business. They like work on the, "Stranger Things," season five, you know, production and a whole bunch of other things. No spoilers please. And a lot of these teams
like run, you know, they use our databases and particularly a lot of them ran on this third party distributed Postgres-compatible data store. It's, you know, self-manage, which really means our team
manages it or managed it. And you know, that kinda
comes with its straight offs. It's, you know, self-managed. So we do a lot of work on managing it, upgrading and those sorts of things. And instance replacements. It's Postgres-compatible,
which means, you know, it's usually Postgres, but until it's not. And so, you know, we found
that those trade offs plus it can get kind of
pricey running such a powerful database across the entire fleet. And in most cases you don't need it. And in the past few years, especially Aurora Postgres
has come a long way in terms of feature set, reliability
and even, you know, cost. And so we made the decision
as the central platform teams to move all these databases
over to Aurora Postgres. And it's important to note that, you know, this is the platform
team making a decision for all application teams. And so the more work we
can do, the better it is, because we're asking teams to move. Additionally, it's better for
the company if we take as much of the cycles and execute them ourselves and not make the app teams do it. And so we're gonna go
over like how it works. But you know, in general,
database migrations, there's solved problem. You know, you copy the schema and the data, you validate
it, make sure it's all there. And then all you have to do in theory is to point the application
to new database. And AWS has tooling to help with this. There's something called the
database migration service that we used as a building block. And it can do, you know,
schema conversion and copy. It can migrate data, it
can even validate the data. And then again, in theory, all you have to do is point the application. However, when it comes to
the real world, things start to get a bit more tricky. So like in our case, we had
over a hundred applications of different data sizes. And each application, at least from the database
perspective, is very different. The data shape is very different. The data access patterns are different. And like if you do this naively you can run into different
issues per database and you don't wanna do that. You wanna catch issues
early as much as you can. And these applications are
written in different languages. We can't just build something for Java and like ignore all the
other use cases out there. You have to make sure you build
something, at least for us, for all the languages, that'll work in all languages instead of- And you don't wanna like build something individually in each language. You wanna find a way to support all these use cases together. Additionally, these different applications have different downtime requirements. Some are okay with being
down for, you know, four hours in a weekend. They're cool with that. Others are like, oh, we
can't support more than, you know, two minutes of downtime or 30 seconds of downtime. So it gets kinda tricky. And these applications also
don't exist in a vacuum. For every application database is often, you know, streaming connectors, there's analytics connectors. And again, if you did this naively, we'd migrate the database and then say, "Hey app
team, you're on your own to migrate your like iceberg exports or like Flink jobs and things." And we have a lot of this in Netflix. So you have a whole data platform of all these pieces that you can just plug into your database. And so that's where it
gets kind of tricky. And so now we've talked
enough I think about like what we try to solve and why. Let's talk about how we solved it. And we're gonna go over this
in sort of three sections. First we'll talk about what we did before even involving app teams. Like what sorts of pre-work we can do before talking to this team so we can minimize the back and forth. We'll talk about how we
copy the schema and the data and you know, spoiler alert,
we leaned heavily on DMS for this with some additional
tooling on our end. And then we'll talk about
how we validated the data as you know, all there. And then did, you know,
a liveish cut-over, live to the point where,
you know, reads continue to work throughout the entire process. Writes is what we took
down for a few minutes. So let's jump right into
the pre-flight checks. So this is something we did
before even involving app teams. And we did this across the
entire fleet, you know, hundreds of databases. We did this upfront just so we can minimize it back and forth. We used AWS DMS tooling. They have this thing called
a schema conversion tool. And you can run across on a database and say, "Hey, generate a
report, like will this work with this as a source
and this as a target." So our target obviously
is Aurora Postgres. AWS actually did not support
the source that we use, 'cause it's a third
party piece of software. And so we work with
them to build in support so we could run this migration. So this generated a report with, you know, this index is not gonna
work in Aurora Postgres or you know, these hidden
columns become visible columns. And so we were able to take these and work with the app teams to make sure their schema would work
on the source and target. And so that was pretty helpful. The second piece is, so now
that you have the schema done, you have to worry about the data. So application teams, you know, are executing SQL
statements against all of their like third party databases. We were able to take those, sample them and again, without app team involvement and run them against Postgres
basically to sort of see what this actually work. And so this gave us some confidence that the schema will work and the sort of schema
changes will work as well. We also did the work of
looking at their source cluster upfront and provisioning the
target clusters based on the traffic patterns we saw. So we knew how to size this, you know, Postgres database instance
on the target end. We copied over all the ownership metadata. We copied over all the
authorization information that we needed to make sure their apps
could talk to the database. And not only did we
provision these, you know, final clusters, we provisioned
a temporary cluster as well. And we took that temporary cluster, we copied over the schema and data, which we'll go over in a second
and, you know, validated it and we handed those off
to your application teams, because there's only so much you can do by looking at the schema and the data. You actually have to run
your application to see, you know, how does the database perform, how does all the SQL actually work? And we found a whole bunch
of issues with, you know, implicit cast working in the old database but not working in the new. And so those are sort
of the three, you know, ways we tested this and
again, across the entire fleet before even talking to application teams. The next thing we have to do is the actual schema and data copy. And this is where, you
know, let's say schema copy, we built tooling around AWS DMS. The schema copy is any,
you know, database object. So tables, views, sequences and because we're
switching database engines, some of these have to be converted. You know, it's not always one to one. So this is an example of conversion that we didn't do ourselves,
you know, AWS DMS did it for us and just copy things over. We did however build in verification, 'cause you know, especially because they didn't
technically support this. We found all these edge cases
where things were, you know, getting mangled using copying. So for example, we had
VARCHAR(3) that was converted to VARCHAR(1), which, you know,
what's the impact of that? These were country codes. You can't really have a
country code that is just C, that's not gonna work. And so we found these sorts of things by writing our own schema
verification tooling to sort of double check the work
that you know, we were doing, 'cause you know, we were on the hook for this with our app teams. The next thing to do is
the actual data copy. And this is again where we
built tooling around DMS and DMS does, you know, a
full load, which is a sort of point in time copy over of all the data and the source to the target. It also does CDC, which is
change data capture, which is, you know, as the application is writing to the source database, it's being replicated over to the target. Keep in mind this is a live migration and so we are not shutting
down the application and then like copying the data. We're doing this live, so
applications running the database is run, the source database
is running and the target. And so we copy data and
then start replicating it. We did, similar to earlier, we did build in some tooling on our end. So we built in specifically
some monitoring tooling, 'cause we found that in some cases the task would fail part way through because of a transient issue. And we wouldn't realize
until it's time to cut over and we're like, "Oh no,
database replication isn't happening, we need to abort." And so this helped us find
issues earlier instead of during a cut-over. Now just because the data is all there doesn't mean you're done. You actually have to validate
the data is all there. And remember at this
point we have a source, we have a target, we have
data being replicated from the source to target, but
effectively we have two different databases with very similar data sets. Maybe not exactly the same, but that's what we need to find out. And so we kind of learned
this the hard way, like we found issues up front. So DMS does support validation except one, it wasn't built for this custom, the third
party source database. And two, you know, we wanted to do it without putting pressure
on the source and target, because these are live databases, at least the source is initially. And we also wanted to
make sure this works well for both large and small
data sets in, you know, a reasonable amount of time. And so what we did is we used a lot of existing infrastructure
and we took those source and target databases and
attach them to a data feed. So, you know, think Kafka for example, actually Kafka not in this case, but so we connected to a data feed so that we sort of dumped the data and then also do CDC from there and we sent that to our data warehouse. Now it's in a data warehouse, we don't have to worry about
putting pressure on the source database, because we can
write a giant distributed SQL join across two tables to say,
"Hey, for these two tables what data is different." Like we need to make sure
that everything matches. But again, since this data is
changing over time, we sort of cut off, you know, let's
say five minutes in the past and see if any records have
come within five minutes, ignore them, everything else, let's validate the entire data set. And so we can do this faster and we can do this sort
of out of band as well because we're taking a cutoff
at a certain point anyway. But obviously that's
only part of the problem. The second part is how
do we validate that data that's still coming through
and also the most recent data is still correct. And so this is where
live validation comes in. So we take those same two data streams, which again are processing
data coming into the source from the user and to the target from the source through replication. And we pipe them into
a validator, under foot this is a flink job but a validator that is taking the two streams, source and target and comparing them. So for each record we see in one stream, let's make sure we see the same, the equivalent record on the other stream. And this is a lot faster than
doing the entire data set in one fell swoop. And so this lets us, you'll
see later on, do the cut-over much faster, because we can
be confident that the data before is valid and the data
that is going through is valid. Oh the last bit detail is
like this is the full picture of our validation. We have the data streams going and both the batch validation and online validation
happening at the same time. Okay, we have validated our data, let's talk a bit about the cut-over. And the way we realized we
can do this is, you know, zero downtime for reads and
minimal downtime for writes. But to do this, there's
sort of two pieces of this. There's one is we need
to take the application out of the loop as much as possible. We don't really wanna be sitting
on a call with the app team and coordinating things back
and forth and it's just a mess 'cause they have to shut off the app. So we realize if we can move
them out a little faster, we can do a lot more things on our end. And then the second part
is just automate, you know, it's one thing to do
one migration by hand, it's another thing to do like
a hundred plus migrations. And so let's go over both of these. So for the cover process before I get into it, one thing we tend to do at Netflix is we run
proxies in front of data stores. And we do this in a lot of
cases just to do auth end authentication authorization, but depending on the data
store it might have some other functionality as well. So we realize that in order
to get the application out of the loop, if we handle
things the proxy layer that lets us take the connection,
you know, from the proxy to Postgres and like re-point it to Aurora without the application being involved. To do that you have to make sure that the application will work with both the source and the target. And so at this point we have to make sure that their previous schema checks and SQL checks are passing,
everything there is good, they've done all their
testing with a temp cluster and then we make sure that
they're talking to the proxy. And this makes it so that, you
know, say if they're talking to the proxy, we control the proxy, we can control the cut-over
time and like shut off writes and do all that fun stuff without the application team being involved. And we also to make sure that
using the correct credentials, credentials all work on
the source and target. So this lets us do cut-over without the application being involved. Now let's go over the
actual cut-over process. And this is a lot of steps. So again, I'm gonna blaze through it, but let's see how far we can get. So remember at this point we have source and target replications happening from the source to the target. The first step is, hey, how
long is that replication delay? We don't wanna attempt to cut over if the replication
delay is like an hour, because then you're sitting and waiting for an hour for
replication to catch up. And so what we do is we write
a record into the source and wait for it to show up in the target. It's that simple. And we're using an internal
metadata table that we create so that we don't mess
with the user's data. And we set an arbitrary ish cutoff as a minute. But in reality we saw
in most cases it was 15, 16 seconds of replication delay. And you know, we measure this so we know it's accurate. Once we know that the
replication is happening, we have to run our validation. And I talked about this
earlier, we have batch and online validation. You know, at this point, remember the application's still running, everything is up, nothing's down. And so we just run our batch validation, make sure that the data we
copied over is accurate. Assuming it's accurate, we have to make sure
that the user is still actually talking to the proxy. And this is, you know, us trying to remove all the foot guns from the user, because we found cases
where users were not talking to the proxy or they had
some app that was running, you know, on a batch schedule. And you know, we ran some checks to make sure no one is talking directly, but we also removed direct access and made it so they had
to talk to their proxy. And this made it more difficult for users to like mess things up
later on by, you know, sort of a split brain scenario
talking to the wrong cluster. And then the last step
is, I talked about how databases don't exist by themselves. And so we take all that streaming
and batch infrastructure and copy it over from
the source to the target, 'cause at this point we know
that the data is all there. It's correct, replication's happening. So it's safe to do that. Like all you're doing is
introducing another few seconds. You know, the replication
delays 15 seconds, you're adding 15 seconds of delay to their downstream pipelines. That's fine. No one's gonna care. No one's gonna notice. This gets us to the critical section. At this point we shut off writes and we just sort of did this
by modifying permissions for the user on the source database. And so read is still working
so the application is still up but it's, you know, it's slightly degraded because writes aren't working anymore. And we did, you know, coordinate with app teams on a
downtime window for this. But you know, applications
again up and writes are blocked. And then I talked about
sequences briefly earlier. Sequences are basically stateful
counters in the database and you know, they don't get
copied over our replication. So you have to take the
sequences from the source, then make sure the ones in the target that the values match up to
what they're supposed to be. Sort of a small detail. And then I mentioned earlier we measured replication delay. We now have to wait for
replication to catch up and it's the same process as before, we push a record into the source, wait for the show up at the target. At this point we have blocked write so we know that the record we
pushed in is the last record. So when it comes through,
we know we're done with replication and then
we look at our validation. But this time we look at
only online validation, 'cause we previously
verified batch validation and also online at the time. At this point we're just saying, "Hey, is the data still correct? Is it still not mangled? Do we have confidence that
we can cut-over safely?" Assuming that's true,
we're essentially done, we take the proxy, we update
it to point to the target, which is this case Aurora Postgres. And we also terminate connections
on the source database just to make sure there are
no lingering connections, 'cause a lot of our
stuff is done, you know, our connection time and
so we kill all connections and now the application's
talking to the target, we never turned off write
to the target and so it just magically starts working and that was a cut-over process. That was a lot. And so I'll leave you with how far we are, 'cause we're not done and
learnings we have from this adventure that we've been on. This has been, you know, we
started writing the automation I think December last year. So almost a full year. But we ran our first migration in April. It was kind of janky, some
manual code running on my laptop, some running on Jupyter
Notebooks but we made it work and then we built pieces as we went. But at this point we're over 90% complete. There's a handful of cases that require some special
handling, you know, large data sets that
we'll be finishing off in the next few weeks. But like I'm pretty impressed with this progress on our team. We did not think we'd
be this far right now. Additionally we've seen
this in some cases, not all, we saw in some cases latencies drop. And this is, you know, partly because this is no longer
a distributed store. We're not doing raft
consensus for reads and writes and you know, Aurora Postgres, 'cause you're generally
reading from memory. So you know, there are reasons for that. But this is sort of a side benefit is latencies are generally lower in a lot of cases and you can kinda see it's
pretty obvious from this graph when the cut-over happened. There's a very clear demarcation. And this is critical for us as the data platform
team is we found a number of data corruption bugs and we fixed them all
as far as we can tell. I mentioned earlier that we ran
our attempt cluster creation across the entire fleet. That included validation and that found so well, you know, 10 ish data corruption bugs somewhere with null handling of columns. Some were encoding, getting mangled, some were generated columns not
being copied over correctly. Some were data truncation,
column is just being dropped. And we found all these
upfront, well almost all, there were a couple we found later on. There's one weird one with
statements in a transaction being ordered differently depending
on when they came into replication that we found
when we were doing like test cut-overs because that was CDC related. Our initial process was less
CDC and more just full load. And so I am pretty happy with this 'cause we, you know, we
found all these bugs early on without going back and
forth with the app teams. We worked with the DMS folks, 'cause sometimes it was
edge cases on their end. Sometimes it was engine differences that we had to work around. But we got all these sorted
and validation passed and after all that,
you know, no rollbacks, which is, you know, I'm pretty proud of. We had a couple of fix forward use cases. It wasn't all, you know,
sunshine and rainbows, some of them were just
under scale clusters. Some of them were, you know, metadata didn't get copied over correctly. We fixed all of those but
you know, everything happened and no one had to roll back. And so the last thing
I'll leave you with is that initial fleet wide
dry run we did was amazing, 'cause it saved months of time. Not even exaggerating by doing
this all up front across the fleet, working with the DMS folks, building resiliency into our tooling and that all, you know,
worked really well. We built on top of a lot of
existing tooling, you know, DMS some of our own tooling as well, but we got a lot of value
outta building verification and making sure things
actually worked correctly. And the last piece is I
mentioned earlier, you know, we focused on the lowest
common denominator of sorts and build things that would work across applications, across technologies. But we did spend some
cycles building, you know, specific tooling for like Java Flyway because turned out a lot of
folks in Netflix use that. And so we built some specific
tooling just for that, even though it's not really
applicable to all use cases. But yeah, that's all I have. Thank you. (audience applauds) - Thank you very much.
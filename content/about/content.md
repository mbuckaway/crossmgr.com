+++
fragment = "content"
#disabled = true
date = "2020-02-19"
weight = 100
#background = ""

title = "About CrossMgr"
subtitle = "History and Objective of CrossMgr"
+++

## ABOUT CROSS MANAGER

### The Beginning

A few years back, I was assigned to my first Cyclo Cross race. The experience turned out to be an officiating "perfect storm". To start, the organizer had day-of registration.  Because of unusually nice weather, about 100 additional riders came to ride. Normally, this would be great news - all the better for a great day of racing.  However, there was a tremendous mix of skills in the new riders - some were highly experienced, others beginners. The next problem was the course.  It had been unusually dry, and the course was fast - very fast.  And shorter too, because a loop that was usually used had to be cut out.  Lap times ended up being just over 4 minutes. To add to the challenge, there were 3 starts with multiple categories in each (this is fairly common here in Ontario).  However, the start was on a flat section just before a steep hill into a forest.  It ended up that the fast riders could ride it, but the slow riders had to push their bikes. The problems started right from the gun.  By the time the 3rd start got to the top of the hill, they were caught by the 1st start (lapped already!), and they all crossed the finish line together in a big bunch, so getting all the numbers was impossible.  The number caller disappeared for the first 2 laps in the first race.

Due to the short lap times, there were 9 laps in the 40 minute race, and 15 laps in the 60 minute race.  With the mixed abilities of the riders, a few beginner riders were down as many as 5 laps. My results were a shambles - with so many riders,some multiple laps down, with gaps in the numbers, I had no idea who was where.  I talked to the riders to sort out the top 10.  I was able to piece together some results by the end of the week based on guesswork and deduction. I am grateful that the organizer was apologetic and gracious.

However, I thought there must be a better way.  The idea for CrossMgr was born.

### Here and Now

CrossMgr has grown significately since that first race. The years since CrossMgr, as a program, has expanded to include chip timing from various RFID vendors. It has been used in CX, MTB, Road, and Track races. In Feb 2020, CrossMgr was used to score a 1001 lap race at the Forest City Velodrome in London, ON, Canada. It continues to be used by the Midweek Cycling Club in Toronto, ON, Canada as an active test bed for the software. RaceDB, a web based, registration system was later added to the platform to allow organizers to electronically register riders into a race eliminating paperwork. Electronic number board generation was added to RaceDB to allow race organizers to electronically register riders, and print their numbers out on the spot.

The CrossMgr ecosystem has expanded to include utility applications that include:

* TagReadWriteMgr - to bulk read and write RFID tags
* SeriesMgr - to manage a bike race series
* PointsRaceMgr - to manage Track points races
* CallUpSeedingMgr - to manage callsup at Road, CX, and MTB races
* SprintMgr - to manage track sprint tournaments
* StageRaceGC - to manage the over race general classification of a stage road race
  
### The Design

CrossMgr is a cross-platform Python desktop application. Current builds support Windows, MacOSX, and Linux. RaceDB goes one set farther and supports running inside a Docker container making it deployable in the cloud.

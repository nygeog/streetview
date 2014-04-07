Danny, 

I had a chance to look at this today -- it looks like there are six segments that do not merge. In each, the FIPS # appears to be about one digit off. 

Here is a list of the FIPS numbers from both datasets (fipstxt is the file on which I ran the analysis fipstxt_danny is the file that Danny sent)

     +-----------------------------------+
     | segid       fipstxt   fipstxt_d~y |
     |-----------------------------------|
 50. |   156   04013111601   04013111501 |
 69. |   175   17031160900   17031160400 |
101. |   207   31055007431   31055007430 |
113. |   219   42003470400   42003470300 |
118. |   224   06095252607   06095252608 |
     |-----------------------------------|
126. |   232   36061005100   36061004700 |
     +-----------------------------------+

Sorry to continue to be a pain...

-mike


Okay - so this brings up some ‘joy’ on Census boundaries being based off street centerlines and general census digitizing accuracy issues. Also, what should have been updated on the initial tract ids - what I did this most recent round - was I added 20 feet to the right of the segment to place on the side that the street viewer is ‘looking.'

I’ll need to do some digging (I found that 2nd round so I can start too look in that 1st round of random points) but I think the first intersect was done with Esri 2000 Tracts. Some of these make sense if the Esri tracts were used rather than the Tiger lines for 2000 (released later 2009,2010).

156 segment falls in 111601 - right 20 feet falls in 111501
175 segment falls in 160900 - right 20 feet falls in 160400
207 segment intersects 007431 but right 20 feet and straight distance b/n XY segment falls in 007430
219 should be in 470300 both segment and right 20 feet point
224 right 20 feet point should be in 252607 but both segment and right 20 feet point fall in 252608 (70 foot wide road). 
232 segment is in 2000 Tract from Esri 005100 but US Census 2000 004700 - all should be in 004700. 

I could either 1) ID the blocks that would have been selected on the first round and send over those Census variables or 2) send Tract variables for the correct (with the right 20 foot distance) tracts. 

Option 1) seems easiest at this point and would assign the intended block that was nested in the tract that has been used for analysis. 

Let me know if that’s okay or not. 

Thanks,
Danny


Danny,

I agree that #1 is the right way to go. I hadn't thought about the geographic specificity problem, but it makes complete sense. 

Thanks so much for dealing with all of this!

- mike

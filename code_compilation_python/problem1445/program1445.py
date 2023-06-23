def program1445():
    {\rtf1\ansi\ansicpg1252\cocoartf1038\cocoasubrtf360
    {\fonttbl\f0\fswiss\fcharset0 Helvetica;}
    {\colortbl;\red255\green255\blue255;}
    \margl1440\margr1440\vieww9000\viewh8400\viewkind0
    \pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\ql\qnatural\pardirnatural
    
    \f0\fs24 \cf0 a = input()\
    string = input()\
    \
    onecount = 0\
    zerocount = 0\
    \
    for thing in string:\
    	if thing == "1":\
    		onecount += 1\
    	else:\
    		zerocount += 1\
    	\
    if onecount % 2 == 0:\
    	onecount /= 2\
    else:\
    	onecount = (onecount-1)/2 + 1\
    \
    print "1" * onecount + "0" * zerocount}
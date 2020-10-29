# # Concurrency, parallelism, threading, multiprocessing. That’s a lot to grasp already. Where does async IO fit in?

# Asynchronous: language-agnostic paradigm that has implementations across
# lots of programming language

# Await/Async are two new python keywords that are used to define coroutines

# Asyncio the python package that provides a ofundation of API foundation
# and API for runnign and managing coroutines


# easy_install --upgrade pip
# #fixes many bugsys

# pip install --upgrade pip aiohttp aiofiles 
# #for pararellism libraries





# Pararellism: Performing multipl operations at the same time
# - 01
# - 02
# - 03
# - 04

# Multiprocessing: To effect pararellism, entails spreading tastks over a computers CPU
# or cores, is well suited for CPU bound tasks: tightly bound for loops and mathematical
# computations fall into this category
# -01
# -02   P  - 01
# -03	P  - 02
# -04	P  - 03 
# -05	P  - 04
# -06


# Concurrency: is a slightly broader term than parallelism. \
# It suggests that multiple tasks have the ability to run in an overlapping manner.
# Decomposability property of a program, algorithm, or problem into 
# order-independent or partially-ordered components or units.

	# Deadlock:
	# In concurrent computing, a deadlock is a state in which each
	# member of a group is waiting for another member, including itself, to take action,

		# Coffman conditions
		# Mutual exclusion: At least one resource must be held in a non-shareable mode. Otherwise, the processes would not be prevented 
		# 	from using the resource when necessary. Only one process can use the resource at any given instant of time.[6]
		# Hold and wait or resource holding: a process is currently holding at least one resource and requesting additional resources which
		# 	are being held by other processes.
		# No preemption: a resource can be released only voluntarily by the process holding it.
		# Circular wait: each process must be waiting for a resource which is being held by another process, which in turn is waiting for the first
		# 	process to release the resource. In general, there is a set of waiting processes, P = {P1, P2, …, PN}, such that P1 is waiting for a resource held by P2, P2 
		# 	is waiting for a resource held by P3 and so on until PN is waiting for a resource held by P1.[3][7]

		# Most current operating systems cannot prevent deadlocks.[9] When a deadlock occurs, different operating 
		# systems respond to them in different non-standard manners. Most approaches work by preventing one of 
		# the four Coffman conditions from occurring, especially the fourth one.[10] Major approaches are as follows.

		# In computer science, the ostrich algorithm is a strategy of ignoring potential problems on the basis that they may be exceedingly rare. 
		# It is named for the ostrich effect which is defined as "to stick one's head in the sand and pretend there is no problem
		# ". It is used when it is more cost-effective to allow the problem to occur than to attempt its prevention.

	# (There’s a saying that concurrency does not imply parallelism.)
	# -01
	# -02   P  - 01,05
	# -03	P  - 02,05
	# -04	P  - 03 
	# -05	P  - 04
	# -06

# Threading:
# Concurrent execution model whereby multiple threads take turns executing tasks. 
# One process can contain multiple threads python is werid on threading

# What’s important to know about threading is that it’s better for IO-bound tasks. 
	#While a CPU-bound task: is characterized by the computer’sc ores continually working hard from start to finish, 
	#An IO-bound job: is dominated by a lot of waiting on input/output to complete.



# ASYNCIO
# At the heart of async IO are coroutines. 
# A coroutine: is a specialized version of a Python generator function. 
# 	Let’s start with a baseline definition and then build off of it as you progress here: 
# 	A coroutine is a function that can:
# 	-	Suspend its execution before reaching return, 
#	-	Can indirectly pass control to another coroutine for some time.



# Let’s take the immersive approach and write some async IO code. 
# This short program is the Hello World of async IO but goes a long way towards illustrating its core functionality:
#!/usr/bin/env python3
# countasync.py
import time
import asyncio

def fivesec():
	asyncio.sleep(5)
	return True

async def fivecount():
	print("Five started")
	await fivesec()
	print("five ended")

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), fivecount())

if __name__ == "__main__":
    
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# time.sleep() is blocking and takes time 
#	- Incompatible with async python code
#
# asyncio.sleep() is nonblocking and takes time 
# 	- The surrounding function can temporarily cede control to another
#  	  function that’s more readily able to do something immediately



# The syntax async def introduces:
# 	- either a native coroutine or an asynchronous generator. 
#
# The expressions async with and async for are also valid, and you’ll see them later on.


# Memory

<u>Recommended:</u>

- for workstations: 8 GB minimum

- for servers: 16 GB minimum

- ECC (error correction technology)

The memory allocated to the 4D Server application depends on 4 factors:

- the amount of total memory on your machine,

- the amount of memory available,

- the operating system,

- the version of 4D Server used.

For your information, it is not possible to have a cache of 100 MB or
less. In any case, the cache is very important, so it is necessary to
reserve a sufficient amount of memory (after calculating the memory
needed for processes, etc.) for the 4D cache.

- The memory space reserved for the cache is separate from the memory
  space used by the server for the processes. In fact, increasing the
  size of the cache reduces the space reserved for the processes.

- The maximum size varies according to the number of connected users and
  the number of processes per user. However, by default, 4D uses about 1
  GB (apart from the processes), in particular to load all the system
  libraries.

- Cache management has been improved. In particular, a new mechanism
  performs the most consuming operations in the temporary memory, which
  allows to lighten the main cache. The advantage of temporary memory is
  that it is used only when needed and does not consume machine
  resources. We invite you to calculate the memory needed for 4D Server
  to function properly, and then to deduct it from the total memory
  allocated by the system to 4D. You can then deduce the maximum cache
  size you can allocate. Excessive cache size may decrease the overall
  performance of the system, or even make it unstable.

- To find out the hit rate you need to observe the variations in the
  observed cache. When you observe a decrease in the used cache, it
  means that 4D needed to delete objects in order to free up memory for
  some objects in the data engine. If the cache is purged again and
  again, this is a good analysis that indicates that the cache is too
  small. In this case, 4D needs to repeatedly purge a quarter of its
  cache in order to free up enough space for the data engine objects.

- The management of the cache should be left to 4D, only the size of the
  cache and the frequency of writing the cache are important now. We
  advise you not to use the command \"FLUSH CACHE\" for example, it is
  better to use the option \"Flush cache every 20 seconds\", which
  specifies the intervals of data saving, in order to control the
  writing of the data cache on the disk. 4D uses a built-in data cache
  system to speed up I/O operations. The fact that data changes are, at
  times, present in the data cache and not on disk is completely
  transparent to your code. For example, if you call the \"SEARCH\"
  command, the 4D engine will integrate the data present in the cache to
  perform the operation.

We advise you:

- not to check the \"Adaptive cache calculation\" option in order to set
  a fixed cache size;

- to uncheck the option \"Keep the cache in physical memory\" on the
  Mac;

- provide enough memory on the machine for the cache, the engine memory
  of 4D Server and the operating system itself;

- set the cache writing frequency to 20 seconds;

- remove calls to the \"FLUSH CACHE\" command in your code;

- deploy the 64-bit version of 4D Server (a 32-bit application cannot
  use more than 4 GB of memory, a 64-bit application has 8 TB of
  theoretical addressable space!

- determine the ideal cache value for your database in production using
  the \"4D_Info_Report\" component
  (<https://taow.4d.com/Tool-4D-Info-Report/PS.1938271.en.html>).

(Allow for free slots if the data file is going to grow rapidly in order
to add memory later on)

The database cache manager has been completely rewritten in 4D v16 and
thus improves the use of a very large cache for modern computers (with
64 or even 128 GB cache) allowing to take advantage of the low price of
memory sticks and thus allowing to store a large database entirely in
memory. It also improves situations where the cache is small but the
data file is very large by better management of priorities for data
objects to be held or released from the cache.

As a result, the database will be faster, allowing for more data and
more concurrent user access.

Finally, 4D uses a built-in data cache system to speed up I/O
operations. The fact that data changes are, at times, present in the
data cache and not on disk is completely transparent to your code. For
example, if you call the FIND command, the 4D engine will integrate the
data present in the cache to perform the operation.

It is automatically available and optimized, but can be configured or
analyzed dynamically with the following commands:

- The \"FLUSH CACHE\" command now accepts a \* parameter to empty the
  cache or a minimum number of bytes to free the cache (only for testing
  purposes)

- The \"SET CACHE SIZE\" command dynamically sets the size of the
  database cache in 64-bit versions of 4D

- \"Get cache size\" command retrieves information about cache usage in
  64-bit versions

- The \"Read cache size\" command returns the current cache size

- The \"Cache flush periodicity\" selector of the \"SET DATABASE
  PARAMETER\" command allows you to read or set the periodicity of
  writing the cache to the disk

The database data cache includes an automatic priority management
mechanism that offers a high level of efficiency and performance. This
mechanism allows to optimize the rotation of data in the cache when the
program needs space: data with lower priority is unloaded first, while
data with higher priority remains loaded.

This mechanism is fully automatic and most of the time you won't need
to worry about it. However, for special cases, it can be customized with
a set of dedicated commands, allowing you to change the priority of
objects for the whole session or just the current process. Note that
these commands should be used with care as they can affect the
performance of the database.

The cache manager selects the data to be removed from the cache when
needed using a priority system.

The three types of objects that can be loaded into the cache have
different priority:

- tables: all standard field data (numeric, dates\...), excluding blobs
  (see below). Default priority: medium

- blobs : all binary data of the fields (texts, images, objects and
  blob) stored in the data file. Default priority: low

- index: all single field indexes, including keyword indexes and
  composite indexes. Since indexes are used very frequently, they have a
  special status in the cache. Default priority: high

Default priorities generally ensure optimal performance. However, in
some specific cases you may need to customize these priorities. To do
this, you have two sets of 4D commands:

- Commands that change the cache priorities for the entire session and
  all processes: \"SET TABLE CACHE PRIORITY\", \"SET INDEX CACHE
  PRIORITY\" and \"SET BLOBS CACHE PRIORITY\". These commands must be
  called when the database is started.

- Commands that change the cache priorities for the current process
  only: \"ADJUST CACHE TABLE PRIORITY\", \"ADJUST INDEX CACHE PRIORITY\"
  and \"ADJUST BLOBS CACHE PRIORITY\". Use these commands if you want to
  temporarily change the priority of objects in the cache to improve
  performance during a temporary operation and then return to the
  original priorities.

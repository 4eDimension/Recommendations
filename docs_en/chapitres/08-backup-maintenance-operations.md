# Backup / Maintenance operations

<u>Recommended:</u>

- Schedule a daily backup of the database (structure, data and data
  index file)

- Use third-party backup software to back up the folder containing the
  4D backup files (.4BK and .4BL) to another physical location

- Use snapshot software that is compatible with the Volume Shadow Copy
  Service on Windows to back up running files (especially to back up the
  4D database \"hot\")

- Enable the 4D history file (.journal)

- Activate the automatic restitution and integration of the log when a
  data corruption is detected by 4D at the opening of the database

- Automatically restore (by programming) each new backup (.4BK) on
  another machine and verify the data with the tool integrated in 4D
  (Security and Maintenance Center / CSM)

- Program the automatic sending (by programming) of an e-mail to give
  the database administrator information on the status of the new backup
  and the result of the data verification

- Program a data file compacting operation with the CSM from time to
  time (since v13 it is possible to detect fragmentation of a 4D table
  and therefore act accordingly with the \"Read fragmentation table\"
  command)

- Close the administration window after each use

Since version v15 R4, we have significantly optimized the global
reindexing algorithm of the database. The whole process has been
redesigned, and the operation can now be performed up to twice as fast.

*Note: A global reindexing is necessary, for example, after a database
repair or when the .4dindx file has been deleted.*

As each record of each indexed table has to be loaded into memory during
the indexing, the optimization aimed at minimizing the swaps between the
cache and the disk. The operation is now performed sequentially on each
table, which reduces the need to load and unload records.

Ideally, if the cache were large enough to hold the entire data file and
indexes, the new reindexing algorithm would not provide any improvement.
However, the memory available on the server is usually not that large.
If the cache is large enough to hold at least the data and indexes of
the largest table, then the new algorithm will be up to twice as fast as
the previous one.

Making regular backups of data is important, but in the event of an
incident it is not possible to recover the data entered since the last
backup. To meet this need, 4D has a special tool: the history file. This
file ensures the permanent security of the data in the database.

In addition, 4D works permanently with a data cache located in memory.
Any modification made to the database data is temporarily stored in the
cache before being written to the hard disk. This principle speeds up
the operation of applications; in fact, memory accesses are much faster
than disk accesses. If an incident occurs in the database before the
data stored in the cache has been written to disk, you will have to
integrate the current history file in order to recover the entire
database.

If you are working in a virtual environment, use Volume Shadow Copy on
Windows Server to properly handle snapshot requests.

In addition to the 4D backup and history file, we invite you to schedule
regular maintenance operations by checking and compacting the data and
index file.

Once your backup strategy is in place, we invite you to consider the
worst case scenario (fire, theft) and therefore to make a weekly copy of
the database on an inert medium in another secure location.

For critical applications, it is also possible to set up a logical
mirror backup system, allowing an instantaneous restart in the event of
an incident on the operating database. The two machines communicate via
the network, with the operating machine regularly transmitting changes
in the database to the mirror machine via the history file.

In this way, in the event of an incident on the database in operation,
you can start again from the mirror database to resume operations very
quickly without any loss of data.

The principles implemented are as follows:

- The database is installed on the main 4D Server workstation (operating
  workstation) and an identical copy of the database is installed on the
  mirror 4D Server workstation.

- A test at the start of the application (for example, the presence of a
  specific file in a sub-folder of the 4D Server application) makes it
  possible to distinguish between each version (running and mirrored)
  and therefore to perform the appropriate operations.

- On the 4D Server workstation in operation, the history file is
  segmented at regular intervals using the \"New log file\" command.
  Since no backup is made on the main server, the database is always
  available for reading and writing.

- Each segment of the history file is sent to the mirror station, where
  it is integrated into the mirror database using the \"INTEGRATE MIRROR
  LOG FILE\" command.

The implementation of this system requires the programming of specific
code, including:

- a timer on the main server to manage the execution cycles of the \"New
  log file\" command,

- a system for transferring the history file segments between the
  operating station and the mirror station (use of 4D Internet Commands
  for transfer via ftp or email, Web Services, etc.),

- a process on the mirror station designed to supervise the arrival of
  new history file segments and to integrate them via the \"INTEGRATE
  MIRROR LOG FILE\" command,

- a communication and error management system between the main server
  and the mirror server.

*Warning: Logical mirroring is incompatible with \"standard\" backups on
the operating database because the simultaneous use of these two backup
modes leads to the desynchronization of the operating database and the
mirror database. Therefore, you must ensure that no backups, either
automatic or manual, are performed on the database in operation. On the
other hand, it is possible to backup the mirror database.*

Since version v14, it is possible to activate the current history file
on the mirror station. You can thus set up a \"mirror of mirrors\", or
serial mirror servers. This possibility is based on the command
\"INTEGRATE MIRROR LOG FILE\".

# Server monitoring

You can use the \"4D_Info_Report\" component to collect as much
information as possible :

- on the system environment, hardware, 4D

- on the database: structure, data, triggers, indexes, custom settings
  used, etc.

- in real time: memory, cache, connected users, process, etc.

This component can be used in Production without any problem: the impact
on the performance of the monitored application is negligible.

You can also use the \"Monitor\" tab of the 4D Server administration
window to display dynamic information about the database operation as
well as information about the system and the 4D Server application.

The graphical area allows you to see the evolution of several parameters
in real time:

- the processor utilization rate,

- network traffic,

- memory status.

This information can be obtained programmatically with the \"READ
ACTIVITY SUMMARY\" command. This command allows you to obtain a snapshot
of the n most time-consuming and/or most frequent operations in
progress, such as writing the cache or executing formulas.

By default, the \"READ ACTIVITY SUMMARY\" command deals with operations
performed locally (with 4D single-user, 4D Server or 4D in remote mode).
However, with 4D in remote mode, you can also get the overview of the
operations performed on the server: to do so, you just have to pass the
star (\*) as the last parameter. In this case, the data from the server
will be retrieved locally. The \* parameter is ignored when the command
is executed on 4D Server or 4D Single User.

A new command also appeared in version 4D v16 R4 (modified in v16 R5):
\"Read process activity\". It returns an instantaneous view of the
sessions of the connected users and/or of the processes executed at a
given time, including internal processes that were not accessible with
the \"PROCESS INFORMATION\" command.

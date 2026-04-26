# Processor

<u>Recommended:</u>

- for workstations: 1 CPU with 2 cores minimum

- for servers: 1 CPU with at least 4 cores (rather than 2 CPUs with 2
  cores because the cache will be shared between all cores)

- deploy your application in compiled mode in order to take advantage of
  the preemptive mode (\*) to take full advantage of the multi-core
  machines

- explicitly declare all the methods you want to start in preemptive
  mode (check the option in the properties of your methods and check
  their eligibility with the compiler)

4D takes advantage of the multiple cores available in the system (\*\*).
Indeed, the operating system distributes the \"processor time\" (total
time of all the cores) between each application and between the threads
of each application. It is then the application that defines the
priorities of each of its threads, each thread working individually.

\*: if you deploy your application in interpreted mode, all processes
will run on a single core, regardless of the number of cores available
on your machine!

\*\*: Systems that support multithreading can simulate 2 logical cores
for each core, thus doubling the processing capacity of 4D Server.

In 4D, there are cooperative threads and preemptive threads. 4D uses
them automatically (no specific software or preference) depending on the
4D code being executed.

All cooperative threads run in the main thread unlike preemptive threads
which are dispatched by the 4D server to the other threads. Indeed, when
executed in preemptive mode, a process is dedicated to a CPU
(processor). The management of the process is then delegated to the
system, which can allocate each CPU separately on a multi-core machine.

When executed in cooperative mode (the only mode available in 4D until
4D v15 R5), all processes are managed by the thread (system process) of
the parent application and share the same CPU, even on a multi-core
machine.

Therefore, in preemptive mode, the overall performance of the
application is improved, especially with multi-core machines, because
multiple threads can actually be executed simultaneously. The actual
gains, however, depend on the nature of the operations being executed.
Basically, code intended to be executed in preemptive threads cannot
call elements with external interactions such as plug-in code or
interprocess variables. Data access, however, is possible because the 4D
data server supports execution in preemptive mode.

On the other hand, since in preemptive mode each thread is independent
of the others and not managed directly by the application, specific
conditions must be met in the methods that must be executed in
preemptive mode. Moreover, the preemptive mode is only available in
certain contexts.

Notes:

- The \"Worker\" process type allows you to exchange data between any
  process, including preemptive processes.

- The \"CALL FORM\" command provides an elegant solution for calling
  interface objects from a preemptive process.

- Although designed primarily for interprocess communication needs in
  the context of preemptive processes (available in 64-bit versions
  only), the \"CALL WORKER\" and \"CALL FORM\" commands are available in
  32-bit versions and can be used with processes in cooperative mode.

It is also important to know that a non-local 4D Distant process always
communicates with two twin threads on the server: a pre-emptive thread
for DB4D requests (create, store, load, delete, sort, search, etc.) and
a cooperative thread for application requests (\"today's date(\*)\",
\"read process variable (-1;..)\", etc.). A third preemptive thread can
also be created if you execute SQL commands (when calling the \"Debut
SQL\" command).

Depending on the command executed, 4D uses this or that thread by
establishing communication on the corresponding port:

- publishing port for DB4D queries (cooperative thread)

- application port (publishing port +1) for application queries
  (preemptive thread)

- SQL port for SQL queries (preemptive thread)

In conclusion, it is strongly recommended to have a multi-core processor
even if the use of all the cores will depend on the 4D commands used in
your application, knowing that the more preemptive you are, the faster
you will be on a multi-core machine.

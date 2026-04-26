# Web

<u>Recommended:</u>

- use a 64-bit version of 4D

- use the 4D Server web server (preemptive mode is not supported by 4D
  in remote mode)

- deploy a compiled 4D application

- make sure that the base methods and the project methods related to the
  Web are confirmed thread-safe by 4D Compiler

- use a reverse proxy (e.g. Nginx) to avoid exposing the 4D server to
  the Internet

As of v16, 4D's built-in web server (64-bit only) for Windows and Mac
OS X allows you to take full advantage of multi-core by using preemptive
web processes in compiled applications. Most 4D web-related commands,
methods and database URLs are thread-safe and can be used in preemptive
mode. You can configure your web-related code, including 4D HTML tags
and web base methods, to run concurrently on as many cores as possible.

If you want to make a 4D full web application highly available, this is
the architecture we recommend:

- Front-End:

    - Set up a load balancer (e.g. Nginx) and use an elastic IP to
    redirect web requests to the VM of your choice

    - Have a maintenance page to display when production is interrupted

- Back-End:

    - Set up a VM with its system disk and 3 additional attached disks,
    including 2 SSDs (which can thus be detached and attached to another
    VM, on demand)

        - disk 1: contains the system and the applications

        - disk 2: contains the 4D application sources connected to a source
      server (e.g. Gitlab) - this facilitates integration, deployment
      and monitoring of code updates on the various servers (test,
      recipe and production)

        - disk 3: contains the database (SSD disk)

        - disk 4: contains the 4D backups and its current history file (SSD
      disk) - allows to automate the automatic restitution of the
      backups on another VM to check the data regularly and make sure
      they are healthy

    - Backup sessions to avoid losing the web contexts (stored in memory)
    of connected users, 2 solutions (of your choice) are possible for
    this:

        - Client side: Use JSON Web Token (JWT) to save sessions in the
      browser

        - Server side: Save sessions in the 4D database

When you plan to do a system or application update, here is the
procedure to follow:

- Clone the Production VM with its system disk (disk 1): this VM becomes
  the recipe VM

- Perform maintenance operations (system or application update) on this
  recipe VM

- Run your tests to make sure that these operations have no impact on
  the functioning of the 4D application

- Once the validation phase has been completed and no regression has
  been observed, clone the recipe VM with its system disk (disk 1)

- Save the web sessions and ask NGINX to display a maintenance page

- Stop the production VM and detach disks 2, 3 and 4

- Start the clone of the recipe VM, which becomes the production VM, and
  attach disks 2, 3 and 4

- Restore the web sessions and disable the maintenance page

- The production base is operational again

Of course, all these production interruption operations (lines 5 to 8)
can be automated so that the production is interrupted for only a few
seconds and that the users keep their context of use at the end.

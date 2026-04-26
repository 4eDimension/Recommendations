# Hard disk

<u>Recommended:</u>

- A disk for the operating system and the 4D Server application

- A high-performance SSD for the 4D database

- One SSD with sufficient capacity for the current history file and
  backups (.journal, .4BK and .4BL)

The advantages of having 3 separate disks:

- In case of a major incident with the system disk: no impact on data
  and backups, you reinstall the system on a new disk and reattach the 2
  SSD disks

- In case of a major incident with the disk containing the 4D database
  or in case of data corruption: restore the last backup and integrate
  the current log on the backup disk

- In case of a major incident with the backup disk: create a new
  database backup and a new history file on a new SSD disk

To improve fault tolerance, security and/or performance, a RAID system
is a very good choice:

- for the database: the best choice is RAID 10 (security and
  performance),

- for backups: the best choice is RAID 5 (price and security).

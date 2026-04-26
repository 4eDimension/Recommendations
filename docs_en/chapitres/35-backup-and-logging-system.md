# Backup and logging system

4D provides a transactional logging system by default. Every data
modification operation is recorded and can be undone. In case of
emergency, the day's work can be restored - nothing is lost. In case of
an interruption, the database is automatically checked on restart and
the missing operations (kept in memory but not stored on disk yet) are
restored, so that the database contains all the information. Even in the
case of total data corruption (disk damage, etc.), the data file is
automatically restored from the last full backup and the history file
(containing the daily work) is integrated.

The transaction log can also be useful in case of accidental (or
voluntary) deletion of records and for legal data recovery.

Standard backup is part of the 4D product, no additional license is
required, only an additional hard disk is highly recommended (to protect
against disk failure).

In 24/7 environments, 4D supports the use of cascaded and/or star-shaped
mirror systems. One production, one mirror and one secondary mirror
provide 24-hour service. An additional mirror system could be run in
another city or the cloud to protect data, even in the event of extreme
disasters.

At the same time, 4D's transactional logging system supports snapshots
of virtual machines (such as Volume Shadow Copy Service from VMWare
vSphere (ESXi Hypervisor, supported from version 16 R2).

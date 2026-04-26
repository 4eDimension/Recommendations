# Port numbers

<u>Recommended:</u> make sure that the following ports are
available and dedicated to the 4D Server application

- mandatory ports:

    - TCP 19813: client/server publishing port & application server
    (modifiable in the database properties)

    - TCP 19814: application port & database server (not modifiable:
    publishing port +1)

- optional ports:

    - TCP 19812: port for the SQL server (can be modified in the database
    properties)

    - UDP 19813: port for the broadcast (not modifiable, only used if the
    publishing port is equal to its default value: 19813)

    - TCP 19815: remote debugging port of the server (not modifiable:
    publication port +2)

    - TCP 80 and TCP 443: ports for the Web server, used for HTTP, HTTPS,
    SOAP and REST requests (modifiable in the database properties)

    - TCP 8002: port for the PHP interpreter (can be modified in the
    database properties)

    - other ports can also be used by 4D, especially by the 4D Internet
    Commands plugin

You can modify the ports used by 4D, by default. However, be aware that
some ports are used or reserved for other applications:

- 0 to 1023 (Reserved ports): These ports are assigned by the I.A.N.A.
  (Internet Assigned Numbers Authority) and on most systems can only be
  used by system (or root) processes or by programs run by users with
  advanced access privileges.

    - 20 and 21 FTP;

    - 23 TELNET;

    - 25 SMTP;

    - 37 NTP;

    - 80 and 8080 HTTP;

    - 443 HTTPS.

- 1024 to 49151 (Registered ports): These ports are registered by the
  I.A.N.A. and can be used on most systems by user processes or by
  programs run by users without special privileges (routers, specific
  applications\...)

- 49152 to 65535 (Dynamic and/or private ports): These ports are free to
  use.

People wishing to use TCP/IP commands to synchronize databases should
use port numbers higher than 49151.

For more information, please visit the I.A.N.A. website:
<http://www.iana.org>

To activate or update a licence from 4D or 4D Server application, you
must also authorise the computer to communicate with the following URLs
(port 443):

- <https://autoregistration.4d.fr/>

- <https://autoregistration.4d.com/>

- <https://motor.4d.fr/>

- <https://motor.4d.com/>

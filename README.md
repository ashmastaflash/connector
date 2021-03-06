#Halo Event Connector

The Dockerfile will drop the haloEvents.py script and all associated assets into /opt/cloudpassage/.  For the sake of convenience, it will place a copy of this README.md file into / and /root/

In this repo we have included the pdf documentation for using these scripts to pull Halo event alerts into either Sumo Logic or Splunk - however, you will just as easily be able to integrate Halo events into other popular SIEM tools, such as ArcSight, or with your Syslog infrastructure.

In addition, there are several ways you can run this script to stream event data to your desired target.

For example, let's say, you wanted to setup this script to be run from cron, emit Halo events as key-value name pairs and append them to a file on the local filesystem. And you wanted to pull only those events that were logged since Nov 10, 2012 onwards. And instead of using the script defaults where the files are expected to be in the program directory, let's say you wanted to use a different working directory /opt/cloudpassage, for example.

For that, you would do something like this:

Run crontab -e and add a line with the desired schedule, such as the following to run, say every 5 minutes

```
*/5 * * * * /opt/cloudpassage/bin/haloEvents.py --starting=2012-11-10 --auth=/opt/cloudpassage/config/myHaloKeys.auth --configdir=/opt/cloudpassage/config --kvfile=/opt/cloudpassage/logs/eventsInKVFormat >/dev/null 2>&1
```

Save your changes before you exit.

If you are extracting events from more than one (supports up to 5) Halo accounts, you can specify those in your myHaloKeys.auth file like this:

```
key_id_1|secret_1
key_id_2|secret_2
...
...
key_id_5|secret_5
```

<!---
#CPTAGS:community-supported integration archive
#TBICON:images/python_icon.png
-->

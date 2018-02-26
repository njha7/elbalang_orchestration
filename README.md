# elbalang_orchestration
Experiment data processing orchestration

## Prerequisite Setup


## Initializing RabbitMQ

## Populating Queue
```scripts/enque.py``` Enques files to be processed into target queue.
Arg | Mandatory | Purpose
--- | --- | ---
--root | Y | Root directory of files to enque
--regex | Y | Regex pattern to all files enqued must contain
--uri | Y | URI of the queue
--port | Y | Listening port of the queue
--user | Y | Username to authenticate as
--password | Y | Password to authenticate with

enque.py walks the target directory and subdirectories and enques any files that contain a match for the regex arg into target queue.

## Batch Processing
WIP
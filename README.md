# ewatch
Like watch, but only outputs (with a timestamp) when a change actually occurs.

# Usage
  
    ewatch.py [options] command

where options are:

    -n SECONDS: Check interval, default 2
    -i PATTERN: Ignore changes matching given regex

At every `-n` seconds the command's stdout and stderr is checked, and if (and only if) they differ from the last check following is written to stdout:
- an ISO 8601 GMT timestamp in square brackets
- the command's stdout
- if the command's stderr isn't empty, the string 'stderr:' followed by the command's stderr


For example to see changes in output from Slurm's `squeue` command, ignoring the changes in the elapsed job time column:

    ewatch -i "\d+:\d+" squeue

might produce something like:
```
[2020-05-01T11:09:53.691774]
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                16   compute test-001   centos  R       0:30      2 compute-[0-1]

[2020-05-01T11:12:17.466239]
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```

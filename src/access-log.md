In this example, Zon examines only the first request lines found in the logs.
Based on these lines, this test fails if:

* The percent of errors in the last two minutes of calls exceeds .1%,
* The slowest 1% of requests take longer than 50ms to satisfy,
* The median size of the response payload falls below 1,000 bytes,
* Not one successful call was seen in the last minute,
* More than 20% of calls take more than .3ms to satisfy, or
* More than 60% of the calls take more than 1ms to satisfy.

`{`  
`limits: [`  
`  max_error_ratio: 0.001,`  
`  max_lat_p99: 50,`  
`  min_byt_p50: 1000,`  
`  min_success_count: 1,`  
`  delighted_latency: 0.3,`  
`  delighted_survival_ratio: 0.2,`  
`  satisfied_latency: 1.0,`  
`  satisfied_survival_ratio: 0.6,`  
`]`  
`regexes: [req: '^/run/.*_host_monitor-.*$']`  
`routing_prefixes: '{{ val.logging_services_config.env }}.access-a.tornado-zon-test-runner'`  
`}`


Brendan says:

* This format will be replaced. (Ok, but today it's a recommended API with serious squish in its explanation.)
* This example is contrived and odd. Get a better example. (Reference example should be non-minimal, but also practical, as one might see in the wild.)

Unit-paloosa:

`max_error_count` is:

* A per-second value, [says this source](https://stash.atl.zillow.net/projects/SERVICES/repos/epa-job/browse/config/templates/zon.yaml)
* A per-minute value, [says this source](http://zoncandidate.in.zillow.net/docs/guide/verbs.html#access-log-monitor)


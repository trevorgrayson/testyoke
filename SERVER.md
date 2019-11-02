# TestYoke HTTP Service

For receiving and hosting test data. Consider using the [testyoke client](./CLIENT.md)


```HTTP
POST /projects/<project:str>/reports
Content-Type: application/xml+junit
vc-sha: "GIT, or other VC sha (optional, but recommended)"

GET /projects/<project:str>

GET /projects/<project:str>/suites/<suite:str>

GET /projects/<project:str>/suites/<suite:str>/tests/<test_name:str>

```

### Version Control SHAS

Reports on test outcomes by version control SHAs.

```HTTP
GET /projects/<project:str>/shas/<sha:str>

```

